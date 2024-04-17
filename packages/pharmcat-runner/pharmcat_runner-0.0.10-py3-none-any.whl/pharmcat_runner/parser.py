# MIT License

# Copyright (c) 2024 Andrew Haddad

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os
import re
from functools import lru_cache
from io import StringIO

import numpy as np
import pandas as pd

from .common import *
from .utils import blockgz_compress, create_logger, get_files, run_command

logger = create_logger(__name__)

GENES_WITH_AS = {"CYP2C9", "DPYD", "CYP2D6"}


def get_cpic_dip_to_phen():
    dip_to_phen_data = pd.read_table(DIP_TO_PHEN_PATH, comment="#")
    dip_to_phen_data_raw = dip_to_phen_data.drop(columns="activity_score")
    dip_to_phen = {
        "VKORC1": {
            "rs9923231 reference (C)/rs9923231 reference (C)": "Variant Absent",
            "rs9923231 reference (C)/rs9923231 variant (T)": "Variant Present",
            "rs9923231 variant (T)/rs9923231 variant (T)": "Variant Present",
            "Indeterminate/Indeterminate": "Indeterminate",
        },
        "2C_CLUSTER": {
            "rs12777823 reference (G)/rs12777823 reference (G)": "Variant Absent",
            "rs12777823 reference (G)/rs12777823 variant (A)": "Variant Present",
            "rs12777823 variant (A)/rs12777823 variant (A)": "Variant Present",
            "not called": "Indeterminate",
            "Indeterminate/Indeterminate": "Indeterminate",
        },
    }
    for _, (gene, dip, phen) in dip_to_phen_data_raw.iterrows():
        try:
            dip_to_phen[gene].update({dip: phen})
        except KeyError:
            dip_to_phen[gene] = {dip: phen}
    dip_to_activity_data = dip_to_phen_data.loc[
        dip_to_phen_data["gene"].isin(GENES_WITH_AS)
    ].drop(columns="phenotype")
    dip_to_activity_score = {
        "DPYD": {
            "Indeterminate/Indeterminate": "n/a",
        },
        "CYP2C9": {
            "Indeterminate/Indeterminate": "n/a",
        },
        "CYP2D6": {"Indeterminate/Indeterminate": "n/a"},
    }
    for _, (gene, dip, activity) in dip_to_activity_data.iterrows():
        dip_to_activity_score[gene].update({dip: activity})
    return dip_to_phen, dip_to_activity_score


def get_allele_function(gene=None):
    if gene == "CYP2D6":
        file_path = CYP2D6_ALLELE_FXN_PATH
    else:
        file_path = DPYD_ALLELE_FXN_PATH
    with open(file_path) as f:
        allele_function = json.load(f)
    return allele_function


def assign_dpyd_phenotype(activity_score):
    if activity_score == "2.0":
        return "Normal Metabolizer"
    elif activity_score in {"1.5", "1.0"}:
        return "Intermediate Metabolizer"
    elif activity_score in {"0.5", "0.0"}:
        return "Poor Metabolizer"
    else:
        return "Indeterminate"


def assign_dpyd_activity_score(alleles=None, dpyd_allele_function=None):
    # Activity score is based on the two alleles with the lowest activity
    # https://pubmed.ncbi.nlm.nih.gov/29152729/
    activity_scores_alleles = [dpyd_allele_function[allele] for allele in alleles]
    return sum(sorted(activity_scores_alleles)[:2])


def adjust_dpyd_reference(genotype):
    # According to CPIC tables order should be allele/Reference
    if genotype.startswith("Reference"):
        alleles = genotype.split("/")
        return alleles[1] + "/" + alleles[0]
    return genotype


def parse_dpyd(gene_data=None, dpyd_allele_function=None, dip_to_phen=None):
    # Samples can have >2 alleles because the gene is so large and does
    # not exist as a single haplotype
    # https://pubmed.ncbi.nlm.nih.gov/29152729/
    if gene_data["diplotypes"]:
        genotypes = set()
        for diplotype_data in gene_data["diplotypes"]:
            diplotype = diplotype_data["name"]
            alleles = (
                diplotype.replace("[", "")
                .replace("]", "")
                .replace(" + ", "/")
                .split("/")
            )
            genotype = "/".join(sorted(alleles))
            genotype = adjust_dpyd_reference(genotype)
            genotypes.add(genotype)
        if len(genotypes) == 1:
            genotype = next(iter(genotypes))
            activity_score = assign_dpyd_activity_score(
                alleles=genotype.split("/"), dpyd_allele_function=dpyd_allele_function
            )
        else:
            genotype = "Indeterminate/Indeterminate"
            activity_score = "n/a"
    else:
        haplotypes = []
        for haplotype in gene_data["haplotypeMatches"]:
            haplotypes.append(haplotype["name"])
        genotype = "/".join(sorted(haplotypes))
        genotype = adjust_dpyd_reference(genotype)
        activity_score = assign_dpyd_activity_score(
            genotype.split("/"), dpyd_allele_function=dpyd_allele_function
        )
    if genotype.count("/") == 1:
        if genotype not in dip_to_phen["DPYD"]:
            first, second = genotype.split("/")
            genotype = f"{second}/{first}"
    return genotype, activity_score


def parse_2c_cluster(gene_data=None, dip_to_phen=None):
    # this "gene" doesn't exist within the normal data
    cluster_genotype_converter = {
        "G/G": "rs12777823 reference (G)/rs12777823 reference (G)",
        "G/A": "rs12777823 reference (G)/rs12777823 variant (A)",
        "A/A": "rs12777823 variant (A)/rs12777823 variant (A)",
        "./.": "Indeterminate/Indeterminate",
        None: "Indeterminate/Indeterminate",
    }
    genotype_raw = gene_data["variantsOfInterest"][0]["vcfCall"]
    genotype = cluster_genotype_converter[genotype_raw]
    phenotype = dip_to_phen["2C_CLUSTER"][genotype]
    return genotype, phenotype


@lru_cache()
def assign_cyp4f2_phenotype(genotype):
    # Phenotype/guideline is based on the variant that defines the *3
    # allele which is also contained in the new *4 allele
    # https://pubmed.ncbi.nlm.nih.gov/28198005/
    if "*3" in genotype or "*4" in genotype:
        return "Variant Present"
    return "Variant Absent"


def adjust_cyp2d6_calls(cyp2d6_cnv, genotype, cyp2d6_allele_function=None):
    phenotype = "Indeterminate"
    activity_score = "n/a"
    if cyp2d6_cnv == 3:
        allele1, allele2 = genotype.split("/")
        if allele1 == allele2:
            genotype = genotype + "xN"
            genotype_3copies = f"{allele1}/{allele2}x2"
            activity_score = assign_cyp2d6_activity(
                genotype=genotype_3copies, cyp2d6_allele_function=cyp2d6_allele_function
            )
            phenotype = assign_cyp2d6_phenotype(activity_score)
        else:
            genotype1 = f"{allele1}/{allele2}x2"
            genotype2 = f"{allele1}x2/{allele2}"
            genotype = genotype + "xN"
            activity_score1 = assign_cyp2d6_activity(
                genotype=genotype1, cyp2d6_allele_function=cyp2d6_allele_function
            )
            activity_score2 = assign_cyp2d6_activity(
                genotype=genotype2, cyp2d6_allele_function=cyp2d6_allele_function
            )
            phenotype1 = assign_cyp2d6_phenotype(activity_score1)
            phenotype2 = assign_cyp2d6_phenotype(activity_score2)
            if phenotype1 == phenotype2:
                phenotype = phenotype1
            else:
                phenotype = "Indeterminate"
            if activity_score1 == activity_score2:
                activity_score = activity_score1
            else:
                activity_score = f"{activity_score1} or {activity_score2}"
    elif cyp2d6_cnv == "CN_HybridLoss":
        genotype = "Indeterminate/Indeterminate"
    elif cyp2d6_cnv == "CN_HybridGain":
        genotype = genotype + " CN_HybridGain"
    return genotype, phenotype, activity_score


def adjust_cyp2d6_gene_deletion(cyp2d6_cnv, genotype, cyp2d6_allele_function=None):
    if cyp2d6_cnv == 0:
        genotype = "*5/*5"
        activity_score = 0
        phenotype = "Poor Metabolizer"
    elif cyp2d6_cnv == 1:
        allele1, allele2 = genotype.split("/")
        if allele1 == "*1":
            allele2_num = int(allele2.replace("*", ""))
            if allele2_num < 5:
                genotype = f"{allele2}/*5"
            else:
                genotype = f"*5/{allele2}"
            activity_score = assign_cyp2d6_activity(
                genotype=genotype, cyp2d6_allele_function=cyp2d6_allele_function
            )
            phenotype = assign_cyp2d6_phenotype(activity_score)
        else:
            genotype = "Indeterminate/Indeterminate"
            activity_score = "n/a"
            phenotype = "Indeterminate"
    return genotype, phenotype, activity_score


@lru_cache(maxsize=None)
def assign_cyp2d6_activity(genotype=None, cyp2d6_allele_function=None):
    if genotype == "Indeterminate/Indeterminate":
        return "n/a"
    elif genotype is np.nan:
        return np.nan
    total_activity = 0
    na_activity = False
    for allele in genotype.split("/"):
        copies = 1
        if "x" in allele:
            copies = int(re.findall(r"x\d", allele)[0].strip("x"))
        allele = re.findall(r"\*\d+", allele)[0]
        allele_activity = cyp2d6_allele_function[allele]
        try:
            total_activity += float(allele_activity) * copies
        except ValueError:
            na_activity = True
    if na_activity:
        return f">= {total_activity}"
    return total_activity


@lru_cache()
def assign_cyp2d6_phenotype(activity_score):
    # https://pubmed.ncbi.nlm.nih.gov/31647186/
    try:
        if activity_score == "n/a" or ">=" in activity_score:
            return "Indeterminate Metabolizer"
    except TypeError:
        # activity is already a float
        if activity_score == 0:
            return "Poor Metabolizer"
        elif activity_score >= 0.25 and activity_score <= 1:
            return "Intermediate Metabolizer"
        elif activity_score >= 1.25 and activity_score <= 2.25:
            return "Normal Metabolizer"
        elif activity_score > 2.25:
            return "Ultrarapid Metabolizer"


def determine_cyp2d6_cnv(file):
    file_gz = file + ".gz"
    file_gz = blockgz_compress(input_file=file, output_file=file_gz)
    try:
        cnv_data = run_command(
            f"bcftools view {file_gz} -H --regions-file {CYP2D6_CNV_POSITIONS_PATH} -Ov",
            capture_output=True,
            shell=True,
        )
        cnvs = (
            pd.read_table(
                StringIO(cnv_data), usecols=[4, 9], header=None, names=["ALT", "sample"]
            )
            .loc[lambda x: x["ALT"] != "C"]
            .iloc[:, -1]
            .astype(np.int64)
            .to_list()
        )
        if len(set(cnvs)) == 1:
            return cnvs[0]
        if 1 in cnvs or 0 in cnvs:
            return "CN_HybridLoss"
        else:
            return "CN_HybridGain"
    finally:
        os.remove(file_gz)


def create_frame(data):
    df = pd.DataFrame(
        data,
        columns=[
            "person_id",
            "gene",
            "genotype",
            "phenotype",
            "activity_score",
            "possible_genotype",
            "possible_phenotype",
        ],
    )
    return df


def get_genotype_phenotype(call=None, gene=None, dip_to_phen=None):
    # May need to adjust order of alleles which changes genotype

    # Weird comma for certain G6PD alleles
    call = call.replace("‚", ",")
    try:
        phenotype = dip_to_phen[gene][call]
    except KeyError:
        genotype_new = call.split("/")
        genotype_new = f"{genotype_new[1]}/{genotype_new[0]}"
        try:
            phenotype = dip_to_phen[gene][genotype_new]
            genotype = genotype_new
        except KeyError:
            genotype = call
            phenotype = "Indeterminate"
    else:
        genotype = call
    return genotype, phenotype


def _parse_pharmcat_output(
    file=None,
    vcf_dir=None,
    xy_ids=None,
    dip_to_phen=None,
    dip_to_activity_score=None,
    dpyd_allele_function=None,
    cyp2d6_allele_function=None,
):
    compiled_data = []
    with open(file) as f:
        sample_id = os.path.basename(file).split(".")[1]
        json_data = json.load(f)
        for gene_data in json_data["results"]:
            gene = gene_data["gene"]
            activity_score = np.nan
            if gene in {"CFTR", "CYP3A4", "IFNL3", "F5"}:
                # Not doing these genes
                continue
            elif gene == "CYP2C9":
                # CYP2C Cluster parsing must occur first otherwise genotype and phenotype are overwritten
                genotype, phenotype = parse_2c_cluster(
                    gene_data=gene_data, dip_to_phen=dip_to_phen
                )
                compiled_data.append(
                    [
                        sample_id,
                        "2C_CLUSTER",
                        genotype,
                        phenotype,
                        np.nan,
                        np.nan,
                        np.nan,
                    ]
                )
            if gene == "DPYD":
                genotype, activity_score = parse_dpyd(
                    gene_data=gene_data,
                    dpyd_allele_function=dpyd_allele_function,
                    dip_to_phen=dip_to_phen,
                )
                phenotype = assign_dpyd_phenotype(str(activity_score))
                possible_genotype, possible_phenotype = np.nan, np.nan
            else:
                genotypes = []
                phenotypes = []
                if xy_ids is not None:
                    if (
                        len(gene_data["diplotypes"]) == 0
                        and sample_id in xy_ids
                        and gene == "G6PD"
                    ):
                        # Assigns single Indeterminate allele for samples that are not called
                        genotypes.append("Indeterminate")
                        phenotypes.append("Indeterminate")
                for call_data in gene_data["diplotypes"]:
                    call = call_data["name"]
                    if gene == "G6PD":
                        if xy_ids is not None and sample_id in xy_ids:
                            call_split = call.split("/")
                            if call_split[0] != call_split[1]:
                                # Scenarios where a variant is not called and therefore a possible
                                # call is made that is not possible
                                # i.e A/A, A/Sierra Leone, Sierra Leone/Sierra Leone
                                # A/Sierra Leone is not possible for XY sample
                                continue
                            call = call_split[0]
                    genotype, phenotype = get_genotype_phenotype(
                        call=call, gene=gene, dip_to_phen=dip_to_phen
                    )
                    genotypes.append(genotype)
                    phenotypes.append(phenotype)
                if len(genotypes) == 1:
                    genotype = genotypes[0]
                    possible_genotype, possible_phenotype = np.nan, np.nan
                    phenotype = phenotypes[0]
                else:
                    if gene == "G6PD" and xy_ids is not None and sample_id in xy_ids:
                        genotype = "Indeterminate"
                    else:
                        genotype = "Indeterminate/Indeterminate"
                    possible_genotype = (
                        ";".join(genotypes) if len(genotypes) != 0 else np.nan
                    )
                    phenotype = "Indeterminate"
                    possible_phenotype = np.nan
                    if len(set(phenotypes)) == 1:
                        possible_phenotype = phenotypes[0]
                if gene in {"CYP2C9", "CYP2D6"}:
                    try:
                        activity_score = dip_to_activity_score[gene][genotype]
                    except KeyError:
                        activity_score = "n/a"
                if gene == "CYP4F2":
                    phenotype = assign_cyp4f2_phenotype(genotype)
                if gene == "CYP2D6":
                    if vcf_dir is None:
                        cyp2d6_cnv = 2
                    else:
                        cyp2d6_file = os.path.join(
                            vcf_dir.replace("*.vcf", ""),
                            f"No_SULT1A1_{sample_id}.CEL.vcf",
                        )

                        cyp2d6_cnv = determine_cyp2d6_cnv(file=cyp2d6_file)
                    if (
                        cyp2d6_cnv not in {0, 1, 2}
                        and genotype != "Indeterminate/Indeterminate"
                    ):
                        genotype, phenotype, activity_score = adjust_cyp2d6_calls(
                            cyp2d6_cnv=cyp2d6_cnv,
                            genotype=genotype,
                            cyp2d6_allele_function=cyp2d6_allele_function,
                        )
                    elif cyp2d6_cnv in {0, 1}:
                        genotype, phenotype, activity_score = (
                            adjust_cyp2d6_gene_deletion(
                                cyp2d6_cnv=cyp2d6_cnv,
                                genotype=genotype,
                                cyp2d6_allele_function=cyp2d6_allele_function,
                            )
                        )
            compiled_data.append(
                [
                    sample_id,
                    gene,
                    genotype,
                    phenotype,
                    activity_score,
                    possible_genotype,
                    possible_phenotype,
                ]
            )
    df = create_frame(compiled_data)
    return df


def finalize_results(results):
    call_data_pharmcat = pd.concat(results, axis=0, ignore_index=True)
    call_data_pharmcat = call_data_pharmcat.replace(
        "not called", "Indeterminate/Indeterminate"
    )
    call_data_pharmcat = call_data_pharmcat.replace("N/A", "Indeterminate")
    call_data_pharmcat.loc[:, "phenotype"] = (
        call_data_pharmcat.loc[:, "gene"] + " " + call_data_pharmcat.loc[:, "phenotype"]
    )
    call_data_pharmcat.loc[:, "possible_phenotype"] = (
        call_data_pharmcat.loc[:, "gene"]
        + " "
        + call_data_pharmcat.loc[:, "possible_phenotype"]
    )

    cond = call_data_pharmcat["gene"].isin(GENES_WITH_AS)
    call_data_pharmcat.loc[cond, "activity_score"] = (
        call_data_pharmcat.loc[cond, "gene"]
        + " Activity Score "
        + call_data_pharmcat.loc[cond, "activity_score"].astype(str)
    )
    return call_data_pharmcat


def write_pharmcat_output(call_data_pharmcat=None, dir_=None, output_dir=None):
    fname = "call_data_pharmcat.csv"
    if output_dir:
        output_path = os.path.join(output_dir, fname)
    else:
        if "*" in dir_:
            output_path = os.path.join(os.path.dirname(dir_), fname)
        else:
            output_path = os.path.join(".", fname)
    call_data_pharmcat.to_csv(output_path, index=False)


def check_sex_ids(json_files, sex_data):
    if len(json_files) != sex_data.shape[0]:
        raise ValueError(
            f"The number of json files {len(json_files)} does not match the number of samples in the sex ids file {sex_data.shape[0]}"
        )
    json_sample_ids = set()
    for json_file in json_files:
        sample_id = json_file.split(".")[1]
        json_sample_ids.add(sample_id)

    sex_ids = set(sex_data[0].astype(str))

    diff = json_sample_ids.difference(sex_ids)
    if len(diff) != 0:
        raise ValueError(f"Found {diff} sample ids in JSONs not in sex_ids file")
    diff = sex_ids.difference(json_sample_ids)
    if len(diff) != 0:
        raise ValueError(
            f"Found {diff} sample ids in sex_ids with no matching JSON file"
        )


def parse_pharmcat_output(
    pharmcat_dir=None, vcf_dir=None, sex_ids=None, output_dir=None
):
    if sex_ids is None:
        logger.warn(
            "No sex info was provided. Without this, G6PD genotypes and phenotypes can be innacurate."
        )
        xy_ids = None
    else:
        sex_data = pd.read_table(sex_ids, header=None)
    if vcf_dir is None:
        logger.warn(
            "No VCF directory was provided. Without this, CYP2D6 copy number cannot be determined including *5."
        )
    files = [file for file in get_files(dir_=pharmcat_dir) if ".json" in file]
    check_sex_ids(json_files=files, sex_data=sex_data)
    xy_ids = set(sex_data.loc[sex_data[1] == "M", 0].astype(str))

    dip_to_phen, dip_to_activity_score = get_cpic_dip_to_phen()
    dpyd_allele_function = get_allele_function(gene="DPYD")
    cyp2d6_allele_function = get_allele_function(gene="CYP2D6")
    parsed_results = []
    for file in files:
        try:
            result = _parse_pharmcat_output(
                file=file,
                vcf_dir=vcf_dir,
                xy_ids=xy_ids,
                dip_to_phen=dip_to_phen,
                dip_to_activity_score=dip_to_activity_score,
                dpyd_allele_function=dpyd_allele_function,
                cyp2d6_allele_function=cyp2d6_allele_function,
            )
            parsed_results.append(result)
            logger.info(f"Parsed results for {file}")
        except Exception as e:
            logger.exception(f"Failed to parse results for {file}")
            raise e
    call_data_pharmcat = finalize_results(parsed_results)
    write_pharmcat_output(
        call_data_pharmcat=call_data_pharmcat, dir_=pharmcat_dir, output_dir=output_dir
    )
