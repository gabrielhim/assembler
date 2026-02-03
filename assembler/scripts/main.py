import click
from assembler import __version__
from assembler.graph import select_k_mer_size, reconstruct_genome


@click.version_option(__version__)
@click.command(no_args_is_help=True, help="Assembles read sequences into a circular genome.")
@click.option("-f", "--reads-file", help="File path with all DNA sequences, one per line.")
@click.option("-o", "--output-file", required=False, help="File to write sequence to.")
def main(reads_file: str, output_file: str | None):
    with open(reads_file) as f:
        reads = [read.strip() for read in f.readlines()]

    k = select_k_mer_size(reads)
    genome = reconstruct_genome(reads, k)

    if output_file is not None:
        print(f"Writing genome to {output_file}.")
        with open(output_file, "w") as f:
            f.write(genome)
    else:
        print("Reconstructed genome:")
        print(genome)


if __name__ == "__main__":
    main()
