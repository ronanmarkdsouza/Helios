# Propulsion Para

Description:
        This function takes in multiple motor parameters like it's Wet and Dry mass, Diameter, Nozzle's mass and length, Thrust vs Time to compute 
        Motor's mass, position of center of gravity, and the Moment of Inertia using kinematics equations. The fucntion also interpolates
        the thrust generated for the given motor at every time step using the Thrust vs Time data.

Function Inputs:
        timer --> Current timestep </br>
        Length --> Length of the Motor </br>
        odia --> Outer Diameter of the motor </br>
        wetmass --> Wetmass of the motor </br>
        drymass --> Drymass of the motor </br>
        nozmass --> Nozzle mass of the motor </br>
        nozlen --> Length of the Nozzle </br>
        time --> Time data for the given motor </br>
        thrust --> Thrust data for the given motor </br>

Function Outputs:
        mass --> Mass of the entire motor (Drymass + Wetmass) </br>
        cg --> Position of Center of gravity of the motor </br>
        Ix --> Moment of Inertia along X </br>
        Iy --> Moment of Inertia along Y </br>
        currentthrust --> Thrust for the given timestep </br>


 