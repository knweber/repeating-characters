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

# @click.group(chain=True, invoke_without_command=True)
@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def cli(input, output):
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)
