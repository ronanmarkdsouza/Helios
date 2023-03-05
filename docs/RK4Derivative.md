# RK4Derivative

Description: This function is used to calculate derivatives of velocity components
and respective pitch, roll and yaw rates of the rocket. 

Function input:
             - thrust --> thrust of the rocket at that interval </br>
             - drag -->  drag force experienced by the rocket at that time interval </br>
             - sidey --> side forces along Y-axis </br>
             - sidez --> side forces along Z-axis </br>
             - mass --> mass of the rocket </br>
             - u --> X-component of the velocity vector </br>
             - v --> Y-component of the velocity vector </br>
             - w --> Z-component of the velocity vector </br>
             - p --> Yaw rate of the rocket in rad/s </br>
             - q --> Pitch rate of the rocket in rad/s </br>
             - r --> Roll rate of the rocket in rad/s </br>
             - cphi --> cosine of the yaw angle </br>
             - cpsi --> cosine of the roll angle </br>
             - ctheta --> cosine of the pitch angle </br>
             - sphi --> sine of the yaw angle </br>
             - spsi --> sine of the roll angle </br>
             - stheta --> sine of the pitch angle </br>
             - ymoment --> yaw moment </br>
             - pmoment --> pitch moment </br>
             - rmoment --> roll moment </br>
             - Ixx --> moment of inertia with respect to X-axis </br>
             - Iyy --> moment of inertia with respect to Y-axis </br>
             - Izz --> moment of inertia with respect to Z-axis </br>

Function Output:
             - udot --> derivative of the velocity component along X-axis </br>
             - vdot --> derivative of the velocity component along Y-axis </br>
             - wdot --> derivative of the velocity component along Z-axis </br>
             - rdot --> derivative of roll </br>
             - qdot --> derivative of pitch </br>
             - pdot --> derivative of yaw </br>
             - phidot --> yaw rate </br>
             - thetadot --> pitch rate </br>
             - psidot --> roll rate </br>
             - xedot --> derivative of displacement along X-axis </br>
             - yedot --> derivative of displacement along Y-axis </br>
             - zedot --> derivative of displacement along Z-axis </br>