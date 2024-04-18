"""Read a ROOT file and print the file structure

:Usage:

 .. code-block:: bash

    inspect_rootfile <file>

A YAML layout of all the branches and leaves in a ROOT file

 .. code-block:: bash

    inspect_rootfile <file> --format=yaml --output-file=test.yml

A JSON layout of all the branches and leaves and their respective sizes

 .. code-block:: bash

    inspect_rootfile <file> --deep --format=json --output-file=test.json
"""
# import uproot
import click


@click.command(help=__doc__)
@click.argument('input_file')
@click.option('-o', '--output-file', type=click.Path())
@click.option('--format', default='plain', type=click.Choice(['json', 'plain', 'yaml']))
@click.option('--deep', is_flag=True)
def cli(input_file, output_file, format, deep):
    click.echo(input_file, output_file, format, deep)
