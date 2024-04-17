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

import filecmp
import os
import unittest
from shutil import rmtree

from pharmcat_runner import haplotype

PATH = os.path.dirname(os.path.abspath(__file__))


class TestFiles(unittest.TestCase):
    def setUp(self):
        haplotype.call_haplotypes(
            dir_=os.path.join(PATH, "test_files, *.vcf"),
            output_dir=os.path.join(PATH, "test_files", "test_output"),
        )

    def tearDown(self):
        rmtree(os.path.join(PATH, "test_files", "test_output"))

    def test_pipeline(self):
        variant_call_rate = 0.95
        sample_call_rate = 0.95
        hwe = 0.001
        f1 = os.path.join(PATH, "test_files", "something.vcf.gz")
        f2 = os.path.join(PATH, "test_files", "test_output", "something.vcf.gz")
        self.assertTrue(filecmp.cmp(f1, f2, shallow=False))

    def test_pharmcat(self):
        f1 = os.path.join(PATH, "test_files", "something.vcf.gz")
        f2 = os.path.join(PATH, "test_files", "test_output", "something.vcf.gz")
        self.assertTrue(filecmp.cmp(f1, f2, shallow=False))
