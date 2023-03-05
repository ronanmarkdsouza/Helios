"""
File:  ./turbulence_generator.py

Description:
        This function generates random gusts of wind who's magnitudes are centered around the mean of user inputed wind
        velocities which is then weighted using turbulence intensity. It also adds pink noise around the mean velocity to generate 
        turbulence.
        
Function Input:
        n --> Counter Variable
        a --> Turbuelnce generated due to gusts of wind
        U --> Mean air speed
        I --> Turbulence Intensity
        dt --> time step 

Function Output:
        u --> Velocity of the wind with noise
        a --> Turbulence generated due to gusts of wind
"""
import numpy as np

def turbulence_generator(n,a,U,I,dt):
        
        Standard_deviation = U*I*0.01
        
        if n==0:
                a[0,1] = np.random.normal()
        
        elif n==1:
                a[1,0] = (2-(5/6))*(a[0,0]/2)
                a[1,1] = np.random.normal() - (a[2,1]*a[1,2])
                a[1,2] = a[0,2] + dt
        