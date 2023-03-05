"""
File: ./initialize.py

Description: This function initializes all the aerodynamic and propulsion parameters 
which has to be entered by the user. This includes initialization of all force, velocity,
moment of inertia, displacement and stability related components required in a six degree 
of freedom model. 

Function Inputs: None

Function Outputs: 
                - acceleration --> acceleration of the rocket at any time interval
                - prediction --> variable to store predicted apogee at different intervals of tim-
                - u --> X-component of the velocity vector
                - v --> Y-component of the velocity vector
                - w --> Z-component of the velocity vector
                - p --> Yaw rate of the rocket in rad/s
                - q --> Pitch rate of the rocket in rad/s
                - r --> Roll rate of the rocket in rad/s
                - psi --> Yaw angle of rocket in degrees
                - theta --> Pitch angle of rocket in degrees
                - phi --> Roll angle of rocket in degrees
                - Xe --> Displacement along X-direction at any interval in meters
                - Ye --> Displacement along Y-direction at any interval in meters
                - Ze --> Displacement along Z-direction at any interval in meters
                - timer --> time at any given time step in seconds
                - velx --> Velocity along X-direction
                - dt --> time step between each iteration in seconds (default = 0.01s)
                - counter1 --> variable to track the number of iterations
                - temp --> temperature at any given interval
                - CP --> coefficient of pressure 
                - C_roll --> coefficient for roll
                - Cn_yaw --> coefficient for yaw moment
                - Cn_pitch --> coefficient for pitch moment
                - Cn_alpha --> coefficient for angle of attack
                - Cd --> drag coefficient
                - Mass --> mass of the rocket
                - CG --> centre of gravity
                - Ixx --> moment of inertia with respect to X-axis
                - Iyy --> moment of inertia with respect to Y-axis
                - Stab_Cal --> stability caliber of the rocket
                - flag --> flag variable 
                - phase --> variable to keep track of phase of rocket (0 for ascent and 1 for parachute)
                - mphase --> determines the phase of the motors
                - state --> tracks the airbrakes state (2000 when deployed and 500 when deployed)
                - delay --> delay due to electrical constraints in airbrakes
                - delaytracker --> delay due to mechanical constraints in airbrakes
                - turb_gen --> generates turbulance constant
                - drift --> range calculated from the launch pad location to the landing location
                - vtrajectory --> variable for plotting rocket trajectory during ascent phase
"""
import numpy as np
from main import mrad as rad
class rocket_params:
    acceleration = np.zeros(300000)
    prediction = np.zeros(300000)
    u = np.zeros(300000)
    v = np.zeros(300000)
    w = np.zeros(300000)
    p = np.zeros(300000)
    q = np.zeros(300000)
    r = np.zeros(300000)
    psi = np.zeros(300000)
    theta = np.zeros(300000)
    phi = np.zeros(300000)
    Xe = np.zeros(300000)
    Ye = np.zeros(300000)
    Ze = np.zeros(300000)
    timer = np.zeros(300000)
    velx = np.zeros(300000)
    temperature = 300
    CP = np.zeros(300000)
    C_roll = np.zeros(300000)
    Cn_yaw = np.zeros(300000)
    Cn_pitch = np.zeros(300000)
    Cn_alpha = np.zeros(300000)
    Cd = np.zeros(300000)
    Mass = np.zeros(300000)
    CG = np.zeros(300000)
    Ixx = np.zeros(300000)
    Iyy = np.zeros(300000)
    Stab_Cal = np.zeros(300000)
    flag= 0
    phase = 0
    mphase = 1
    state = np.zeros(300000)
    turb_gen = np.zeros((4,4))
    turb_gen[0,0] = 1
    turb_gen[0,3] = 1.5
    drift = np.zeros(300000)
    vtrajectory = np.zeros((300000, 3))
    Aref = np.pi*(rad**2)