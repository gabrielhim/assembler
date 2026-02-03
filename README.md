# Circular Genome Assembler

This is a very basic version of a genome assembly tool. It implements De Bruijn graphs to assemble DNA reads into a circular genome, such as plasmids or virus genomes.

The aim of this tool is to study bioinformatics implementations in Python. It assumes error-free sequences and perfect read coverage.

## Usage

Install the tool by following these steps:
```bash
git clone https://github.com/gabrielhim/assembler.git
cd assembler
pip install .
```

Alternatively, you can install it directly from GitHub:
```bash
pip install git+https://github.com/gabrielhim/assembler.git
```

Create a test input:
```
GCCTATGC
ATGCAAGT
AGTCTAAG
CAAGTCTA
CTAAGCCT
GCAAGTCT
```

The only mandatory parameter is `--reads-file` (or simply `-f`), which receives the file listing all input sequences:
```bash
assembler -f input.txt
```

Default output is in stdout:
```
Reconstructed genome:
AAGCCTATGCAAGTCTAAGC
```

Optionally, you can specify an output file to store the final sequence.
