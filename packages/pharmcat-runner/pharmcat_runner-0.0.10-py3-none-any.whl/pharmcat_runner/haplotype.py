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

import glob
import os
import shutil
from datetime import datetime
from tempfile import TemporaryDirectory

from .common import *
from .qc_metrics import QCMetrics
from .utils import (
    check_python_verison,
    create_logger,
    get_files,
    maybe_create_dir,
    run_command,
)
from .vcf import filter_vcf_for_variants, standardize_vcfs

logger = create_logger(__name__, stream=True)


def _copy_outputs(dir_, glob_pattern, tempdir):
    maybe_create_dir(dir_)
    for file in glob.glob(os.path.join(tempdir, glob_pattern)):
        shutil.copy2(file, dir_)


def move_outputs(vcf_input=None, tempdir=None, output_dir=None):
    # VCF used in PharmCAT
    shutil.copy2(vcf_input, output_dir)
    # Log file
    shutil.copy2(os.path.join(tempdir, "pharmcat_runner.log"), output_dir)

    data_to_copy = {
        "pharmcat_output": "*.json",  # PharmCAT jsons
        "pharmcat_warnings": "*warnings*",  # PharmCAT warnings
        "qc_metrics": "*.tsv",  # QC metrics
    }
    for dir_, glob_pattern in data_to_copy.items():
        dir_ = os.path.join(output_dir, dir_)
        _copy_outputs(dir_=dir_, glob_pattern=glob_pattern, tempdir=tempdir)


def get_python_path():
    if not check_python_verison():
        return os.path.join(BIN_DIR, "python", "bin", "python3.9")
    return "python3"


def run_pharmcat(vcf_input, tempdir):
    preprocessor_path = os.path.join(BIN_DIR, "preprocessor")
    python_path = get_python_path()
    pharmcat_pipeline_path = os.path.join(preprocessor_path, "pharmcat_pipeline")
    num_threads = os.cpu_count() - 1 if os.cpu_count() != 1 else 1
    run_command(
        f"cd {preprocessor_path} && {python_path} -m pipenv run python {pharmcat_pipeline_path} {vcf_input} --missing-to-ref -o {tempdir} -matcher --research-mode cyp2d6 -cp {num_threads}",
        shell=True,
    )


def get_pharmcat_positions(tempdir=None):
    # Multiallelic variants mess up indels
    # Need to split these up so that they are captured correctly

    pharmcat_variants_orig_file = os.path.join(
        BIN_DIR, "preprocessor", "pharmcat_positions.vcf"
    )
    pharmcat_variants_split_file = os.path.join(tempdir, "pharmcat_positions_split.vcf")
    pharmcat_positions_file = os.path.join(tempdir, "pharmcat_positions.tsv.gz")

    # Splits multiallelic and left normalizes pharmcat variants
    run_command(
        f"bcftools norm -m -both -c e -f {REFERENCE_PATH} {pharmcat_variants_orig_file} > {pharmcat_variants_split_file} && bcftools query -f'%CHROM\t%POS\t%REF,%ALT\n' {pharmcat_variants_split_file} | bgzip -c > {pharmcat_positions_file} && tabix -s1 -b2 -e2 {pharmcat_positions_file}",
        shell=True,
    )

    return pharmcat_positions_file


def write_manifest(
    output_dir=None,
    num_files=None,
    vcf_input=None,
    variant_call_rate=None,
    sample_call_rate=None,
    hwe=None,
):
    for file in os.listdir(BIN_DIR):
        if "jdk" in file:
            jdk_version = file.replace("jdk-", "")
    user = os.path.basename(os.path.expanduser("~"))
    today = datetime.today().strftime("%B %d, %Y")
    bcftools_version = (
        run_command(["bcftools", "--version"], capture_output=True)
        .split("\n")[0]
        .split(" ")[-1]
        .strip()
    )
    num_samples = run_command(
        f"bcftools query -l {vcf_input} | wc -l", capture_output=True, shell=True
    ).strip()
    plink_version = run_command(["plink", "--version"], capture_output=True).split()[1]
    with open(os.path.join(BIN_DIR, "preprocessor", "preprocessor", "common.py")) as f:
        for line in f:
            if "PHARMCAT_VERSION" in line:
                pharmcat_version = line.split("= ")[-1].strip().strip("'")
    with open(os.path.join(output_dir, "manifest.txt"), "w") as f:
        f.write(MANIFEST_HEADER + "\n")
        f.write(f"User: {user}\n")
        f.write(f"Date: {today}\n")
        f.write(f"PharmCAT version: {pharmcat_version}\n")
        f.write(f"Python version: {sys.version.split()[0]}\n")
        f.write(f"JDK version: {jdk_version}\n")
        f.write(f"Bcftools version: {bcftools_version}\n")
        f.write(f"PLINK version: {plink_version}\n")
        f.write(f"Number of input VCF files: {num_files}\n")
        f.write(f"Number of samples: {num_samples}\n")
        f.write(f"Variant call rate cutoff: {variant_call_rate}\n")
        f.write(f"Sample call rate cutoff: {sample_call_rate}\n")
        f.write(f"Hardy Weinburg Equilibrium cutoff: {hwe}\n")
        f.write(f"VCF input to PharmCAT: {os.path.basename(vcf_input)}\n")


def _get_files(dir_):
    files = get_files(dir_)
    clean_files = []
    for file in files:
        if file.endswith(".vcf") or file.endswith(".vcf.gz"):
            clean_files.append(file)
    return clean_files


def move_all_files(files):
    debug_dir = os.path.join(os.getcwd(), "debug")
    maybe_create_dir(debug_dir, strict=True)
    for file in files:
        shutil.copy2(file, debug_dir)


def check_warnings(dir_):
    num_warnings = len(os.listdir(dir_))
    if num_warnings != 0:
        logger.warn(
            f"PharmCAT returned {num_warnings} warnings when running. Review warnings at {dir_}"
        )


def run_qc(
    file=None, dir_=None, hwe=None, variant_call_rate=None, sample_call_rate=None
):
    qc_metrics = QCMetrics(
        file=file,
        dir_=dir_,
        hwe=hwe,
        variant_call_rate=variant_call_rate,
        sample_call_rate=sample_call_rate,
    )
    if variant_call_rate or hwe:
        qc_metrics.variant_qc()
    if sample_call_rate:
        qc_metrics.sample_qc()
    return qc_metrics


def call_haplotypes(
    dir_=None,
    hwe=None,
    variant_call_rate=None,
    sample_call_rate=None,
    output_dir=None,
    debug=False,
):
    with TemporaryDirectory() as tempdir:
        try:
            pharmcat_positions_file = get_pharmcat_positions(tempdir=tempdir)

            files = _get_files(dir_)
            print("Prepping files for PharmCAT...")
            vcf_standardized = standardize_vcfs(files=files, dir_=tempdir)
            pharmcat_variants_only_file = filter_vcf_for_variants(
                file=vcf_standardized,
                dir_=tempdir,
                positions_file=pharmcat_positions_file,
                exclusions='POS==42126599 || ID=="AX-165885131_chrX_154532990_CGGT_C"',
            )

            if any([hwe, variant_call_rate, sample_call_rate]):
                print("Running pre-PharmCAT QC...")
                qc_metrics = run_qc(
                    file=pharmcat_variants_only_file,
                    dir_=tempdir,
                    hwe=hwe,
                    variant_call_rate=variant_call_rate,
                    sample_call_rate=sample_call_rate,
                )
            try:
                vcf_input = qc_metrics.output_file
            except NameError:
                vcf_input = pharmcat_variants_only_file
            print("Running PharmCAT...")
            if output_dir is None:
                output_dir = os.path.join(os.getcwd(), "results")
            else:
                if not output_dir.startswith("/"):
                    output_dir = os.path.join(os.getcwd(), output_dir)
            maybe_create_dir(output_dir)
            run_pharmcat(vcf_input=vcf_input, tempdir=tempdir)
            move_outputs(vcf_input=vcf_input, tempdir=tempdir, output_dir=output_dir)
            check_warnings(dir_=os.path.join(output_dir, "pharmcat_warnings"))
            write_manifest(
                output_dir=output_dir,
                num_files=len(files),
                vcf_input=vcf_input,
                variant_call_rate=variant_call_rate,
                sample_call_rate=sample_call_rate,
                hwe=hwe,
            )
            print("Succesfully ran PharmCAT.")
        finally:
            if debug:
                debug_files = glob.glob(os.path.join(tempdir, "*"))
                move_all_files(debug_files)
