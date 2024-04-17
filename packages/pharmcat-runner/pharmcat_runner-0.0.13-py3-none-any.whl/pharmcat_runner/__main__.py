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

import argparse
import os
import sys

from .haplotype import call_haplotypes
from .install import install
from .parser import parse_pharmcat_output
from .utils import (
    validate_directory,
    validate_environment,
    validate_plink,
    validate_file,
)


def call_install(args):
    if "linux" not in sys.platform.lower():
        raise OSError("Only linux systems are supported at this time.")
    install(overwrite=args.overwrite)


def call_haplotype(args):
    validate_environment()
    validate_directory(args.files, file_ext=".vcf")
    if args.hwe or args.sample_call_rate:
        validate_plink()
    call_haplotypes(
        dir_=args.files,
        hwe=args.hwe,
        variant_call_rate=args.variant_call_rate,
        sample_call_rate=args.sample_call_rate,
        output_dir=args.output,
        debug=args.debug,
    )


def call_parser(args):
    validate_directory(args.files, file_ext=".json")
    if args.sex_ids:
        validate_file(args.sex_ids)
    if args.vcfs:
        validate_directory(args.vcfs, file_ext=".vcf")
    parse_pharmcat_output(
        pharmcat_dir=args.files,
        vcf_dir=args.vcfs,
        sex_ids=args.sex_ids,
        output_dir=args.output,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Runs PharmCAT pipeline using Pharmacoscan input data",
    )
    subparsers = parser.add_subparsers(required=True)

    # Install
    subparser_install = subparsers.add_parser(
        "install", help="Install PharmCAT pipeline"
    )
    subparser_install.set_defaults(func=call_install)
    subparser_install.add_argument(
        "--overwrite",
        help="Overwrite existing pharmcat installation",
        action="store_true",
        default=False,
    )

    # Haplotype
    subparser_haplotype = subparsers.add_parser(
        "haplotype", help="Call haplotypes using PharmCAT"
    )
    subparser_haplotype.set_defaults(func=call_haplotype)
    subparser_haplotype.add_argument(
        "--files",
        help="Directory of VCF file inputs. Supports with and without glob patterns.",
        type=str,
        required=True,
    )
    subparser_haplotype.add_argument(
        "--hwe",
        type=float,
        help="Cutoff for Hardy-Weinburg Equilibrium. PLINK must be installed and callable to run this QC method.",
    )
    subparser_haplotype.add_argument(
        "--variant_call_rate", type=float, help="Variant call rate cutoff"
    )
    subparser_haplotype.add_argument(
        "--sample_call_rate", type=float, help="Sample call rate cutoff"
    )
    subparser_haplotype.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Run haplotyping in debug mode.",
    )
    subparser_haplotype.add_argument(
        "--output",
        help="Output directory. Default is results within the working directory.",
        type=str,
        default=os.path.join(os.getcwd(), "results"),
    )

    # Parser
    subparser_pharmcat_parser = subparsers.add_parser(
        "parser", help="Parse PharmCAT output"
    )
    subparser_pharmcat_parser.set_defaults(func=call_parser)
    subparser_pharmcat_parser.add_argument(
        "--files",
        help="Directory of PharmCAT JSON files. Supports with and without glob patterns.",
        required=True,
        type=str,
    )
    subparser_pharmcat_parser.add_argument(
        "--sex_ids",
        help="Path to file to with genetically imputed sex for each sample. Required to accurately call G6PD",
        type=str,
    )
    subparser_pharmcat_parser.add_argument(
        "--vcfs",
        help="Path to VCFs. Required for accurate CYP2D6 haplotyping.",
        type=str,
    )
    subparser_pharmcat_parser.add_argument(
        "--output",
        help="Directory to save pharmcat parsed output",
        type=str,
        default="results",
    )
    args = parser.parse_args()
    args.func(args)
