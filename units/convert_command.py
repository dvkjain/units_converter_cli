import click
from .info import conversion_factors

class Code:

    def __init__(self):
        pass

    @staticmethod
    @click.command()
    @click.argument("value")
    @click.argument("convert_from")
    @click.argument("convert_to")
    def convert(value, convert_from, convert_to):
        """
        Convert between units of distance, mass, or volume.
        """

        result = None
        try:
            value = float(value)  # Ensure value is a number
        except ValueError:
            click.echo("Invalid value: must be a number.")
            return
    
        for category, units in conversion_factors.items():

            if convert_from in units and convert_to in units:
                base_value = float(value) * units[convert_from]
                result = base_value / units[convert_to]
                break
            
        if result is not None:
            click.echo(f"{result} {convert_to}")

        else:
            click.echo(f"Invalid conversion: {convert_from} to {convert_to}")
