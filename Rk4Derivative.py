"""
File: ./Rk4Derivative.py

Description: This function is used to calculate derivatives of velocity components
and respective pitch, roll and yaw rates of the rocket. 

Function input:
             - thrust --> thrust of the rocket at that interval
             - drag -->  drag force experienced by the rocket at that time interval
             - sidey --> side forces along Y-axis
             - sidez --> side forces along Z-axis
             - mass --> mass of the rocket
             - u --> X-component of the velocity vector
             - v --> Y-component of the velocity vector
             - w --> Z-component of the velocity vector
             - p --> Yaw rate of the rocket in rad/s
             - q --> Pitch rate of the rocket in rad/s
             - r --> Roll rate of the rocket in rad/s
             - cphi --> cosine of the yaw angle
             - cpsi --> cosine of the roll angle
             - ctheta --> cosine of the pitch angle
             - sphi --> sine of the yaw angle
             - spsi --> sine of the roll angle
             - stheta --> sine of the pitch angle
             - ymoment --> yaw moment
             - pmoment --> pitch moment
             - rmoment --> roll moment
             - Ixx --> moment of inertia with respect to X-axis
             - Iyy --> moment of inertia with respect to Y-axis
             - Izz --> moment of inertia with respect to Z-axis

Function Output:
             - udot --> derivative of the velocity component along X-axis
             - vdot --> derivative of the velocity component along Y-axis
             - wdot --> derivative of the velocity component along Z-axis
             - rdot --> derivative of roll
             - qdot --> derivative of pitch
             - pdot --> derivative of yaw
             - phidot --> yaw rate
             - thetadot --> pitch rate
             - psidot --> roll rate
             - xedot --> derivative of displacement along X-axis
             - yedot --> derivative of displacement along Y-axis
             - zedot --> derivative of displacement along Z-axis
"""