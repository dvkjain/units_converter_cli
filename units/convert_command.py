import click
from units.info import *

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
        Can convert distance, mass and volume units within the metric and imperial system. These are the supported units:
        """

        if convert_from in distance_relation and convert_to in distance_relation:

            Code.convert_distance(value, convert_from, convert_to)
        
        if convert_from in mass_relation and convert_to in mass_relation:

            Code.convert_mass (value, convert_from, convert_to)

        if convert_from in volume_relation and convert_to in volume_relation:

            Code.convert_volume (value, convert_from, convert_to)

    @staticmethod
    def convert_distance(value, convert_from, convert_to):
        
        if convert_from in metric_units_distance:

            if convert_to in imperial_units_distance:

                num = metric_units_distance.index(convert_from) - metric_units_distance.index("m")
                to_m = float(value) * (10**num)
                result = to_m * values_in_m[convert_to]
            
            elif convert_to in metric_units_distance:

                num = metric_units_distance.index(convert_from) - metric_units_distance.index(convert_to)
                result = float(value) * (10**num)
        
        elif convert_from in imperial_units_distance:

            if convert_to in metric_units_distance:

                to_m = float(value) * values_in_m[convert_from]
                
                if convert_to != "m":

                    num = -1*(metric_units_distance.index("m") - metric_units_distance.index(convert_to))
                    result = to_m * (10**num)
                
                else:

                    result = to_m
            
            elif convert_to in imperial_units_distance:

                if convert_from != "in":

                    result = float(value) * values_in_in[convert_from]
                
                elif convert_from == "in":

                    result = float(value)/values_in_in[convert_to]

        click.echo (f"{result} {convert_to}")

    @staticmethod
    def convert_mass(value, convert_from, convert_to):
        
        if convert_from in metric_units_mass:

            if convert_to in imperial_units_mass:

                num = metric_units_mass.index(convert_from) - metric_units_mass.index("g")
                to_g = float(value) * (10**num)
                result = to_g * values_in_g[convert_to]
            
            else:

                num = metric_units_mass.index(convert_from) - metric_units_mass.index(convert_to)
                result = float(value) * (10**num)
        
        elif convert_from in imperial_units_mass:

            if convert_to in metric_units_mass:

                to_g = float(value) * values_in_g[convert_from]
                
                if convert_to != "g":

                    num = -1*(metric_units_mass.index("g") - metric_units_mass.index(convert_to))
                    result = to_g * (10**num)
                
                else:

                    result = to_g

            elif convert_to in imperial_units_mass:

                if convert_from != "lb":

                    result = float(value) * values_in_lb[convert_from]
                
                elif convert_from == "lb":

                    result = float(value)/values_in_lb[convert_to]

        click.echo (f"{result} {convert_to}")

    @staticmethod
    def convert_volume(value, convert_from, convert_to):
        
        if convert_from in metric_units_volume:

            if convert_to in imperial_units_volume:

                num = metric_units_volume.index(convert_from) - metric_units_volume.index("l")
                to_l = float(value) * (10**num)
                result = to_l * values_in_l[convert_to]
            
            elif convert_to in metric_units_volume:

                num = metric_units_volume.index(convert_from) - metric_units_volume.index(convert_to)
                result = float(value) * (10**num)
        
        elif convert_from in imperial_units_volume:

            if convert_to in metric_units_volume:

                to_l = float(value) * values_in_l[convert_from]
                
                if convert_to != "l":

                    num = -1*(metric_units_volume.index("l") - metric_units_volume.index(convert_to))
                    result = to_l * (10**num)
                
                else:

                    result = to_l
            
            elif convert_to in imperial_units_volume:

                if convert_from != "floz":

                    result = float(value) * values_in_floz[convert_from]
                
                elif convert_from == "floz":

                    result = float(value)/values_in_floz[convert_to]

        click.echo (f"{result} {convert_to}")