import click
from .gptvision import gptvision
from .geminivision import geminivision

CONTEXT_SETTINGS = dict(
    help_option_names=[
        '-h',
        '--help'
    ]
)


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


main.add_command(gptvision)
main.add_command(geminivision)
