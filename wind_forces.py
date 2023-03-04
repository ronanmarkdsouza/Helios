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