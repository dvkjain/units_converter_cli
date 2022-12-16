import click

from .convert_command import Code as convert

@click.group()
def cli():
    
    "units is a simple command line tool that is capable of converting units in the metric system to the imperial system, vice versa."

cli.add_command(convert.convert)
