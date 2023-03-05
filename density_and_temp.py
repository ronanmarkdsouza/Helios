"""
File:   ./density_and_temp.py

Description:
        This function takes in the altitude (m) of the rocket at a given time interval and the temperature (K) of the outside at sea level 
        to compute density and temperature at every given time step respectively using the International Standard Atmosphere model.

Function Inputes:
        altitude --> Altitude of the rocket at a given time step in meters
        temperature_outside --> Temperature of the outside at sea level in kelvin
        a --> Lapse rate (-0.0065 for altitude below 10 km)

Function Outputs:
        density --> Density of the air at a given altitude
        temperature --> Temperature of the air at a given altitude
"""

def density_and_temp(altitude,temperature_outside):
        a = -0.0065
        temperature = temperature_outside + (a * altitude)
        density = 1.23 * ((temperature/temperature_outside)**((-9.81/(a*287))-1))
        
        return density, temperature