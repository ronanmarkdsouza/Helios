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