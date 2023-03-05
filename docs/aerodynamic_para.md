# Aerodynamic Para

Description: This function file handles the aerodynamic parameters related to the model rocket. 
The parameters include Drag coefficients, Normal Force coefficients, Centre of Pressure
at different angle of attacks. This includes Normal Coefficient with respect to different
pitching and yawing at different intervals of time.  

Function Inputs:
               data1 = aero_data.xlsx sheet-1 (default) </br>
               data2 = aero_data.xlsx sheet-2 (default) </br>
               mach --> velocity of the Rocket at different intervals </br>
               pitch --> pitch angle of the rocket at launch in degrees </br>
               yaw --> yaw angle of the rocket at launch in degrees </br>
               phase --> defines the phase of the rocket (boost/coasting) </br>
               flag --> airbrakes open/close counter variable </br>

Function Outputs: 
               CP --> centre of pressure at any given interval </br>
               CNP --> normal force coefficient with respect to pitch </br>
               CNY --> normal force coefficient with respect to yaw </br>
               CN_alpha --> normal force coefficient with respect to angle of attack of the rocket </br>
               CD --> drag coefficient at any time interval </br>