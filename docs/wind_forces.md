# Wind Force

Description:
        The function calculates the drag forces and moments exerted on the rocket due to the wind gusts that are randomly generated due to turbulence. The moment on the the rocket body is neglected as it is axisymmetric and only the moment on the fins is accounted for.
        
Function Input:
        vel --> Velocity of the wind </br>
        cm --> Center of gravity </br>
        den --> Density if the air at a given time interval </br>
        rad --> Radius of the rocket </br>
        len --> Length of the rocket </br>
        fin --> A [5x1] Vector that holds the details of the fins in the form [Root Chord, Tip Chrod, Height, Sweep Length, Distance from Nosetip] </br>

Function Output:
        F --> Drag force experienced by the fins due to wind gusts </br>
        mom --> Moment due to Drag force experienced by the fins due to wind gusts </br>