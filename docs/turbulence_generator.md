# Turbulence Generator

# Turbulence Generator

Description:
        This function generates random gusts of wind who's magnitudes are centered around the mean of user inputed wind
        velocities which is then weighted using turbulence intensity. It also adds pink noise around the mean velocity to generate 
        turbulence.
        
Function Input:
        n --> Counter Variable </br>
        a --> Turbuelnce generated due to gusts of wind </br>
        U --> Mean air speed </br>
        I --> Turbulence Intensity </br>
        dt --> time step </br> 

Function Output:
        u --> Velocity of the wind with noise </br>
        a --> Turbulence generated due to gusts of wind </br>