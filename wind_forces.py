"""
File: ./wind_forces.py

Description:
        The function calculates the drag forces and moments exerted on the rocket due to the wind gusts that are randomly generated
        due to turbulence. The moment on the the rocket body is neglected as it is axisymmetric and only the moment on the fins
        is accounted for.
        
Function Input:
        vel --> Velocity of the wind
        cm --> Center of gravity
        den --> Density if the air at a given time interval
        rad --> Radius of the rocket
        len --> Length of the rocket
        fin --> A [5x1] Vector that holds the details of the fins in the form [Root Chord, Tip Chrod, Height, Sweep Length, Distance from Nosetip]

Function Output:
        F --> Drag force experienced by the fins due to wind gusts
        mom --> Moment due to Drag force experienced by the fins due to wind gusts
"""

import numpy as np
from scipy.interpolate import interp1d

class Cylinder:
    def __init__(self, radius, length, center_of_mass):
        self.radius = radius
        self.length = length
        self.center_of_mass = center_of_mass

class Fin:
    def __init__(self, dimensions, orientation):
        self.dimensions = dimensions
        self.orientation = orientation

def calculate_side_forces(velocity, cylinder, fluid_density, fin):
    velocity_magnitude = np.sqrt(velocity * velocity)

    cdcyl = [[-5, 5], [10, 3.33], [100, 1.334], [1000, 0.738], [10000, 0.766], [100000, 0.56], [1000000, 0.55], [10000000, 0.54], [100000000, 0.54]]
    reynolds_number = (fluid_density * velocity_magnitude**2 * cylinder.radius) / 0.0000173
    cylinder_drag_coefficient = interp1d([data[0] for data in cdcyl], [data[1] for data in cdcyl], kind='linear')(reynolds_number)
    cdplt = 1.28
    F = 0.5 * fluid_density * velocity_magnitude**2 * ((cylinder_drag_coefficient * cylinder.radius * 2 * cylinder.length) * (cdplt * (fin.dimensions[0] + fin.dimensions[1]) * fin.dimensions[2]))
    mom = 0.5 * fluid_density * velocity_magnitude**2 * cdplt * (fin.dimensions[0] + fin.dimensions[1]) * fin.dimensions[2] * (fin.orientation[1] - cylinder.center_of_mass)

    return F, mom
