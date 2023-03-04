"""
File: ./propulsion_para.py

Description:
        This function takes in multiple motor parameters like it's Wet and Dry mass, Diameter, Nozzle's mass and length, Thrust vs Time to compute 
        Motor's mass, position of center of gravity, and the Moment of Inertia using kinematics equations. The fucntion also interpolates
        the thrust generated for the given motor at every time step using the Thrust vs Time data.

Function Inputs:
        timer --> Current timestep
        Length --> Length of the Motor
        odia --> Outer Diameter of the motor
        wetmass --> Wetmass of the motor
        drymass --> Drymass of the motor
        nozmass --> Nozzle mass of the motor
        nozlen --> Length of the Nozzle
        time --> Time data for the given motor
        thrust --> Thrust data for the given motor

Function Outputs:
        mass --> Mass of the entire motor (Drymass + Wetmass)
        cg --> Position of Center of gravity of the motor
        Ix --> Moment of Inertia along X
        Iy --> Moment of Inertia along Y
        currentthrust --> Thrust for the given timestep
"""