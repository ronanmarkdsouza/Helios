"""
File: ./aerodynamic_para.py

Description: This function file handles the aerodynamic parameters related to the model rocket. 
The parameters include Drag coefficients, Normal Force coefficients, Centre of Pressure
at different angle of attacks. This includes Normal Coefficient with respect to different
pitching and yawing at different intervals of time.  

Function Inputs:
               data1 = aero_data.xlsx sheet-1 (default)
               data2 = aero_data.xlsx sheet-2 (default)
               mach --> velocity of the Rocket at different intervals
               pitch --> pitch angle of the rocket at launch in degrees 
               yaw --> yaw angle of the rocket at launch in degrees
               phase --> defines the phase of the rocket (boost/coasting)
               flag --> airbrakes open/close counter variable
Function Outputs: 
               CP --> centre of pressure at any given interval
               CNP --> normal force coefficient with respect to pitch
               CNY --> normal force coefficient with respect to yaw
               CN_alpha --> normal force coefficient with respect to angle of attack of the rocket
               CD --> drag coefficient at any time interval
"""