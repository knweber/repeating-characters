import click

@click.command()
@click.help_option('--help', '-h')

def count_occurrences(filename):
