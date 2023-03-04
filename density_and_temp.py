"""
File:   ./density_and_temp.py

Description:
        This function takes in the altitude (m) of the rocket at a given time interval and the temperature (K) of the outside at sea level 
        to compute density and temperature at every given time step respectively using the International Standard Atmosphere model.

Function Inputes:
        y --> Altitude of the rocket at a given time step in meters
        t1 --> Temperature of the outside at sea level in kelvin
        a --> Lapse rate (-0.0065 for altitude below 10 km)

Function Outputs:
        d --> Density of the air at a given altitude
        t --> Temperature of the air at a given altitude
"""