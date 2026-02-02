import click
from assembler import __version__
from assembler.graph import reconstruct_genome


@click.version_option(__version__)
@click.command(help="Assembles k-mer sequences into a genome.")
@click.option("-f", "--k-mers-file", help="File path with all k-mers, one per line.")
@click.option("-o", "--output-file", required=False, help="File to write sequence to.")
def main(k_mers_file: str, output_file: str | None):
    with open(k_mers_file) as f:
        k_mers = [k_mer.strip() for k_mer in f.readlines()]

    genome = reconstruct_genome(k_mers)

    if output_file is not None:
        print(f"Writing genome to {output_file}.")
        with open(output_file, "w") as f:
            f.write(genome)
    else:
        print("Reconstructed genome:")
        print(genome)


if __name__ == "__main__":
    main()
