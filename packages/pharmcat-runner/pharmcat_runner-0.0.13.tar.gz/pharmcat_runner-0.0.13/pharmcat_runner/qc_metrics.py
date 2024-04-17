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

import csv
import os

import pandas as pd

from .utils import log, run_command, create_logger
from .vcf import index_file

logger = create_logger(__name__)


class QCMetrics:
    # Order matters in the QC metric operations
    # Genotype metrics -> variant metrics -> sample metrics
    # Therefore they cannot all be computed at the same time

    # Metrics are first computed using PLINK to generate the required metrics files
    # Then the data is filtered using either bcftools or PLINK
    plink_vcf_flags = [
        "--recode",
        "vcf-iid",  # Uses only sample id for header
        "bgz",
        "--output-chr",  # Outputs chromsomes with chr##
        "chrMT",
        "--real-ref-alleles",  # Needed to code the correct allele as reference
    ]

    attrs_created = ["sc_file", "hwe_file", "vc_file"]

    def __init__(
        self, file, dir_, hwe=None, variant_call_rate=None, sample_call_rate=None
    ):
        self.file = file
        self.dir_ = dir_

        self.variant_call_rate = variant_call_rate
        self.hwe = hwe
        self.sample_call_rate = sample_call_rate

    @staticmethod
    def _parse_metrics_file(file):
        compiled_data = []
        with open(file) as f:
            csv_reader = csv.reader(f, delimiter=" ")
            for line in csv_reader:
                vals = [val for val in line if len(val) != 0]
                compiled_data.append(vals)
        df = pd.DataFrame(compiled_data[1:], columns=compiled_data[0]).apply(
            pd.to_numeric, errors="ignore"
        )
        if "lmiss" in file or "hwe" in file:
            return pd.concat(
                [
                    pd.DataFrame(
                        df["SNP"].str.split("_").to_list(),
                        columns=["ID", "CHROM", "POS", "REF", "ALT"],
                    ),
                    df.iloc[:, 2:],
                ],
                axis=1,
            )
        return df.rename(columns={"IID": "SAMPLE_ID"}).drop(columns="FID")

    def genotype_qc(self):
        raise NotImplementedError("Genotype level QC has not been implemented yet.")

    def variant_qc(self):
        if self.variant_call_rate:
            self.vc_file = self.filter_on_variant_call_rate()
        if self.hwe:
            self.hwe_file = self.filter_on_hwe()

    def sample_qc(self):
        self.sc_file = self.filter_on_sample_call_rate()

    @staticmethod
    def _compute_base_qc(file, output_prefix):
        # Computes QC metrics. Need to be recomputed after each sequential metric
        run_command(
            [
                "plink",
                "--vcf",
                file,
                "--hardy",
                "midp",
                "--missing",
                "--out",
                output_prefix,
            ]
        )

    def _compute_variant_call_rate(self, file_input):
        output_prefix = os.path.join(self.dir_, "vcr")
        self._compute_base_qc(file=file_input, output_prefix=output_prefix)
        vcr = (
            self._parse_metrics_file(f"{output_prefix}.lmiss")
            .assign(VARIANT_CALL_RATE=lambda x: 1 - x["F_MISS"])
            .drop(columns="F_MISS")
        )
        vcr.to_csv(
            os.path.join(self.dir_, "variant_call_rate.tsv"), sep="\t", index=False
        )

    def _compute_hwe(self, file_input):
        output_prefix = os.path.join(self.dir_, "hwe")
        self._compute_base_qc(file=file_input, output_prefix=output_prefix)
        hwe = self._parse_metrics_file(f"{output_prefix}.hwe").drop(
            columns=["TEST", "A1", "A2"]
        )
        hwe.to_csv(os.path.join(self.dir_, "hwe.tsv"), sep="\t", index=False)

    def _compute_sample_call_rate(self, file_input):
        output_prefix = os.path.join(self.dir_, "scr")
        self._compute_base_qc(file=file_input, output_prefix=output_prefix)
        scr = (
            self._parse_metrics_file(f"{output_prefix}.imiss")
            .assign(SAMPLE_CALL_RATE=lambda x: 1 - x["F_MISS"])
            .drop(columns="F_MISS")
        )
        scr.to_csv(
            os.path.join(self.dir_, "sample_call_rate.tsv"), sep="\t", index=False
        )

    @index_file
    @log(logger=logger)
    def filter_on_variant_call_rate(self):
        file_input = self.output_file
        # Compute metrics file
        self._compute_variant_call_rate(file_input=file_input)

        # Filter on variant call rate
        vc_qc_file = os.path.join(self.dir_, "vc_qced.vcf.gz")
        run_command(
            f"bcftools view --include 'F_MISSING < {1-self.variant_call_rate}' -Oz -o {vc_qc_file} {self.file}",
            shell=True,
        )
        return vc_qc_file

    @index_file
    @log(logger=logger)
    def filter_on_hwe(self):
        # Computes HWE using mid p-value correction
        file_input = self.output_file

        # Compute metrics file
        self._compute_hwe(file_input=file_input)
        hwe_qc_file = os.path.join(self.dir_, "hwe_qced")
        run_command(
            [
                "plink",
                "--vcf",
                file_input,
                "--hwe",
                str(self.hwe),
                "midp",
                "--out",
                hwe_qc_file,
            ]
            + self.plink_vcf_flags
        )
        return f"{hwe_qc_file}.vcf.gz"

    @index_file
    @log(logger=logger)
    def filter_on_sample_call_rate(self):
        file_input = self.output_file
        self._compute_sample_call_rate(file_input=file_input)

        sc_qc_file = os.path.join(self.dir_, "sc_qced")
        run_command(
            [
                "plink",
                "--vcf",
                file_input,
                "--mind",
                str(1 - self.sample_call_rate),
                "--out",
                sc_qc_file,
            ]
            + self.plink_vcf_flags
        )
        return f"{sc_qc_file}.vcf.gz"

    @property
    def output_file(self):
        for attr in self.attrs_created:
            try:
                file = getattr(self, attr)
            except AttributeError:
                pass
            else:
                return file
        return self.file

    @property
    def files_created(self):
        files_created = []
        for file in self.attrs_created:
            try:
                attr = getattr(self, file)
            except AttributeError:
                pass
            else:
                files_created.append(attr)
        return files_created
