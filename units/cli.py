import click
from .convert_command import Code as convert

@click.group()
def cli():
    
        """
        units is a simple command line tool that is capable of converting units in the metric system to the imperial system, vice versa.
        
        Supported units:

        - Metric system:

        distance: km, hm, dam, m, dm, cm, mm

        mass: kg, hg, dag, g, dg, cg, mg

        volume: kl, hl, dal, l, dl, cl, ml

        - Imperial american system:

        distance: mi, yd, ft, in

        mass: ton, cwt, st, lb, oz

        volume: floz (fluid ounce), quart, gal
        """

cli.add_command(convert.convert)
