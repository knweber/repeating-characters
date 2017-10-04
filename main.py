# import click
#
# @click.command()
# @click.help_option('--help', '-h')
#
# def count_occurrences(file):
#
# if __filename__ == "__main__":
#     count_occurrences()
#
# def main():
#     print('yooooooo')
import click

@click.command()
@click.argument('file')
def cli(file):
    click.echo("Whaddup?")
    click.echo('You entered {0}'.format(file))
