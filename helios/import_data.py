"""
File: ./import_data.py

Description: This function imports the aerodynamic, propulsion and rocket data which is then used to compute the flight trajectory within the driver function.
The data here is passed in the form of .xlsx files, examples for which have been provided in the repository.
    - rocket_data.xlsx
    - motor_data.xlsx
    - aero_data.xlsx
    These .xlsx files contain important information regarding the rocket, its aerodynamics and propulsion.

Function inputs:
                - rocket_data = rocket_data.xlsx (default)
                - motor_data = motor_data.xlsx (default)
                - aero_data = aero_data.xlsx (default)

Function outputs:
                - rmas --> dry mass of the rocket without the motor
                - rcg --> rocket center of gravity without the motor
                - AMI --> axial moment of inertia of the rocket without the motor
                - TMI --> transverse moment of inertia of the rocket without the motor
                - mrad --> radius of the rocket motor
                - rlen --> length of the rocket
                - np.array(fin_details) --> fin details which includes the root chord, tip chord, height, sweep length and distance from nosetip 
                - Aref --> reference area of the rocket
                - mpos --> length of the rocket
                - data1 --> aerodynamic data of the rocket without airbrakes
                - data2 --> aerodynamic data of the rocket with airbrakes
                - motor_data --> propulsion data
                - length --> length of the motor 
                - odia --> outer diameter of the rocket
                - wetmass --> mass of the motor
                - drymass --> dry mass of the rocket
                - nozmass --> mass of the nozzle
                - nozlen --> length of the nozzle
                - thrust --> motor thrust data
                - time --> motor burn time data
"""