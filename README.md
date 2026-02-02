# Genome Assembler

This is a very basic version of a genome assembly tool. It implements a De Bruijn graph to assembly k-mers of DNA sequences into a genome.

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
ACG
CGT
GTG
TGT
GTA
TAT
ATA
```

The only mandatory parameter is `--k-mer-file` (or simply `-f`), which receives the file listing all k-mer sequences:
```bash
assembler -f input.txt
```

Default output is in stdout:
```
Reconstructed genome:
ACGTGTATA
```

Optionally, you can specify an output file to store the final sequence.
