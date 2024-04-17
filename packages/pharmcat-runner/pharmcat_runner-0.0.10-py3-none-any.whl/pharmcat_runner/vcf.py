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

import gzip
import shutil

import pandas as pd

from .common import *
from .utils import blockgz_compress, create_logger, log, run_command

logger = create_logger(__name__)


def index_file(func):
    def inner(*args, **kwargs):
        file = func(*args, **kwargs)
        run_command(["tabix", "-p", "vcf", file])
        return file

    return inner


@log(logger=logger)
@index_file
def annotate_id(file):
    # Need to annotate the ID field with something more informative because
    # of QC steps with PLINK. If not, can get rows that have the same affy snp
    # id and no clear way to differentiate them
    output_file = file.replace(".vcf", "_annotateid.vcf")
    run_command(
        [
            "bcftools",
            "annotate",
            "-I",
            "%ID\_%CHROM\_%POS\_%REF\_%ALT",
            "-Oz",
            "-o",
            output_file,
            file,
        ]
    )
    return output_file


@log(logger=logger)
@index_file
def sort_vcf(file, output):
    # Only one where .gz needs to be adjusted because it's the first step
    if ".gz" in output:
        sorted_file = output.replace(".vcf", "_sorted.vcf")
    else:
        sorted_file = output.replace(".vcf", "_sorted.vcf.gz")
    run_command(["bcftools", "sort", "-Oz", "-o", sorted_file, file])
    return sorted_file


@log(logger=logger)
@index_file
def fix_ugt1a1_indels(file):
    # UGT1A1 ref and alt alleles are not correct for the indels
    # Confirmed with email from Carsten 3/28/2024
    # Will be fixed in r10 release of Pscan
    output_file = file.replace(".vcf", "_ugt1a1fixed.vcf")
    output_file_nogz = output_file.replace(".gz", "")

    # Fix the indel
    with gzip.open(file, "rt") as f_in, open(output_file_nogz, "w") as f_out_nogz:
        for line in f_in:
            if "233760235" in line:
                new = "TAT\tT,TATAT"
                old = "TATAT\tT,TAT"
                line = line.replace(old, new)
            f_out_nogz.write(line)

    # Compress the output
    # Can't use python gzip to do block gzip compression
    output_file = blockgz_compress(input_file=output_file_nogz, output_file=output_file)

    return output_file


@log(logger=logger)
@index_file
def fix_chromosome_labels(file):
    fixed_file = file.replace(".vcf", "_chrfixed.vcf")
    run_command(
        [
            "bcftools",
            "annotate",
            "--rename-chr",
            CHR_CONV_PATH,
            "-Oz",
            "-o",
            fixed_file,
            file,
        ]
    )
    return fixed_file


@log(logger=logger)
@index_file
def split_multiallelic(file):
    # Needed because this can throw pharmcat off
    split_file = file.replace(".vcf", "_split.vcf")
    run_command(
        [
            "bcftools",
            "norm",
            "-m-any",
            "-c",
            "e",
            "-f",
            REFERENCE_PATH,
            "-Oz",
            "-o",
            split_file,
            file,
        ]
    )
    return split_file


@log(logger=logger)
@index_file
def filter_vcf_for_variants(file, dir_=None, positions_file=None, exclusions=None):
    # Selects only pharmcat variants
    # Including non pharmcat variants can cause issues with calling
    cleaned_file = os.path.join(dir_, "pharmcat_variants_only.vcf.gz")

    # Can't use "--regions-overlap variant" because indels don't get captured correctly
    cmd = ["bcftools", "view", "--regions-file", positions_file]
    rest = ["-Oz", "-o", cleaned_file, file]
    if exclusions:
        cmd = cmd + ["-e", exclusions]
    cmd = cmd + rest

    run_command(cmd)
    return cleaned_file


@log(logger=logger)
@index_file
def merge_vcfs(files, dir_):
    files_to_merge = os.path.join(dir_, "files_to_merge.txt")
    with open(files_to_merge, "w") as f:
        for file in files:
            f.write(file + "\n")

    merged_file = os.path.join(dir_, "merged.vcf.gz")
    run_command(
        [
            "bcftools",
            "merge",
            "--file-list",
            files_to_merge,
            "-i",
            "-",
            "-m",
            "none",
            "-Oz",
            "-o",
            merged_file,
        ]
    )
    return merged_file


@log(logger=logger)
@index_file
def filter_certain_chromosomes(file, reg=True):
    # Need to split out chromsomes that wouldn't be in reference sequence
    # Includes MT and any alternate contigs
    chrs = pd.read_table(CHR_CONV_PATH, header=None, sep=" ")[1]
    if reg:
        output_file = file.replace(".vcf", "_reg_only.vcf")
        chrs = chrs.loc[lambda x: ~x.str.contains("MT|alt", regex=True)]
    else:
        output_file = file.replace(".vcf", "_nonreg_only.vcf")
        chrs = chrs.loc[lambda x: x.str.contains("MT|alt", regex=True)]

    run_command(
        ["bcftools", "view", "-r", ",".join(chrs), "-Oz", "-o", output_file, file]
    )
    return output_file


@log(logger=logger)
@index_file
def concat_vcfs(dir_, *files):
    output_file = os.path.join(dir_, "aligned_file.vcf.gz")
    run_command(["bcftools", "concat", "-a", "-Oz", "-o", output_file] + list(files))
    return output_file


def standardize_vcfs(files, dir_):
    sorted_files = []
    for file in files:
        sorted_file = sort_vcf(file, os.path.join(dir_, os.path.basename(file)))
        sorted_files.append(sorted_file)
    merged_file = merge_vcfs(files=sorted_files, dir_=dir_)
    merged_file_ugt1a1_fixed = fix_ugt1a1_indels(file=merged_file)
    fixed_file = fix_chromosome_labels(merged_file_ugt1a1_fixed)

    reg_chr_only = filter_certain_chromosomes(file=fixed_file, reg=True)
    nonreg_chr_only = filter_certain_chromosomes(file=fixed_file, reg=False)
    split_file = split_multiallelic(file=reg_chr_only)
    alignment_fixed_file = concat_vcfs(dir_, split_file, nonreg_chr_only)
    alignment_sorted = sort_vcf(
        alignment_fixed_file, os.path.join(dir_, "alignment.vcf.gz")
    )
    annotate_id_file = annotate_id(file=alignment_sorted)

    standardized_file = os.path.join(
        os.path.dirname(annotate_id_file), "standardized.vcf.gz"
    )
    shutil.copy2(annotate_id_file, standardized_file)
    shutil.copy2(annotate_id_file + ".tbi", standardized_file + ".tbi")

    return standardized_file
