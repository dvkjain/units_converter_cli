metric_units_distance = ["km","hm", "dam", "m", "dn", "cm", "mm"]
metric_units_mass = ["kg", "hg", "dag", "g", "dg", "cg", "mg"]
metric_units_volume = ["kl", "hl", "dal", "l", "dl", "cl", "ml"]

imperial_units_distance = ["mi", "yd", "ft", "in"]
imperial_units_mass = ["longt", "cwt", "st", "lb", "oz"]
imperial_units_volume = ["floz", "quart", "gal"]

distance_relation = metric_units_distance + imperial_units_distance
mass_relation = metric_units_mass + imperial_units_mass
volume_relation = metric_units_volume + imperial_units_volume

values_in_m = {
    
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254
}

values_in_g = {

    "ton": 1015700,
    "cwt": 50800,
    "st": 6356,
    "lb": 454,
    "oz": 28.35 
}

values_in_l = {

    "floz": 0.02841,
    "quart": 0.946353,
    "gal": 4.54609
}

values_in_in = {

    "mi": 63360,
    "yd": 86,
    "ft": 12
}

values_in_lb = {

    "longt": 2240,
    "cwt": 112,
    "st": 14,
    "oz": 0.0625
}

values_in_floz = {

    "quart": 32,
    "gal": 128
}