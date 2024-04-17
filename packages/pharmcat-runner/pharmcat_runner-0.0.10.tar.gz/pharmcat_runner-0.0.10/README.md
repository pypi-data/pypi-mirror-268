# PharmCAT Runner

The PharmCAT Runner tool provides a simplified pipeline for installing, running, and parsing PharmCAT outputs.

## Dependencies
1. bcftools/tabix/bgzip - 1.18+
2. PLINK - Required for Hardy Weinburg and sample call rate QC methods
3. Python 3.9+ - Optional but highly recommended

## Installation

Installation can be acheived using pip or any other package manager of your choosing. It is highly recommended that installation is done with Python 3.9+. Some conda environments can conflict with installation of a new verison.
```sh
pip install pharmcat_runner 
```

## Usage
```sh
# Install PharmCAT and all required dependencies. If an installation already exists, must pass --overwrite to update
python3 -m pharmcat_runner install

# Run optional QC steps followed by PharmCAT
python3 -m pharmcat_runner haplotype --files "data/*.vcf" --hwe 0.001 --variant_call_rate 0.95 --sample_call_rate 0.95

# Parse PharmCAT output
# VCFs are required for accurate reporting of CYP2D6
# Sex ids are required for accurate reporting of G6PD
# Warnings are reported if either of these are not supplied
python3 -m pharmcat_runner parser --files "results/pharmcat_output/*.json" --vcfs "data/*.vcf" --sex_ids sex_ids.txt
```

## sex_ids file
This file is required for accurate reporting of G6PD genotypes and phenotypes. This should be a tab delimited file without a header. The two columns should be sample id and predicted sex (M-Male, F-Female, O-Other). The sample ids in this file must match the sample ids in the pharmcat output
|   |   |
|---|---|
|1234 | M |
|5678 | F |
|1357 | O |

## Bugs and desired features
Please report any bugs and/or desired features to either the github issues page or to andrew.haddad@pitt.edu