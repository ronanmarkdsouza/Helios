# Initialization

Description: This function initializes all the aerodynamic and propulsion parameters 
which has to be entered by the user. This includes initialization of all force, velocity,
moment of inertia, displacement and stability related components required in a six degree 
of freedom model. 

Function Inputs: None

Function Outputs: 
                - acceleration --> acceleration of the rocket at any time interval </br>
                - prediction --> variable to store predicted apogee at different intervals of time </br>
                - u --> X-component of the velocity vector </br>
                - v --> Y-component of the velocity vector </br>
                - w --> Z-component of the velocity vector </br>
                - p --> Yaw rate of the rocket in rad/s </br>
                - q --> Pitch rate of the rocket in rad/s </br>
                - r --> Roll rate of the rocket in rad/s </br>
                - psi --> Yaw angle of rocket in degrees </br>
                - theta --> Pitch angle of rocket in degrees </br>
                - phi --> Roll angle of rocket in degrees </br>
                - Xe --> Displacement along X-direction at any interval in meters </br>
                - Ye --> Displacement along Y-direction at any interval in meters </br>
                - Ze --> Displacement along Z-direction at any interval in meters </br>
                - timer --> time at any given time step in seconds </br>
                - velx --> Velocity along X-direction </br>
                - counter1 --> variable to track the number of iterations </br>
                - temp --> temperature at any given interval </br>
                - CP --> coefficient of pressure </br> 
                - C_roll --> coefficient for roll </br>
                - Cn_yaw --> coefficient for yaw moment </br>
                - Cn_pitch --> coefficient for pitch moment </br>
                - Cn_alpha --> coefficient for angle of attack </br>
                - Cd --> drag coefficient </br>
                - Mass --> mass of the rocket </br>
                - CG --> centre of gravity </br>
                - Ixx --> moment of inertia with respect to X-axis </br>
                - Iyy --> moment of inertia with respect to Y-axis </br>
                - Stab_Cal --> stability caliber of the rocket </br>
                - flag --> flag variable </br> 
                - phase --> variable to keep track of phase of rocket (0 for ascent and 1 for parachute) </br>
                - mphase --> determines the phase of the motors </br>
                - state --> tracks the airbrakes state (2000 when deployed and 500 when deployed) </br>
                - turb_gen --> generates turbulance constant </br>
                - drift --> range calculated from the launch pad location to the landing location </br>
                - vtrajectory --> variable for plotting rocket trajectory during ascent phase </br>