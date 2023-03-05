# HeliosSim


This is a 6 degree of freedom model developed by a group of enthusiastic engineers who were part of thrustMIT (MIT Manipal's Rocketry team). This model was inspired by the absence of physical testing of sounding rockets in India leading to the formation of this high-precision model. This model provides you with multiple features

## Table of Contents

- [Introduction](#introduction)
- [About the model](#about)
- [Methodology](#methodology)
- [How to install?](#install)
- [How to use this package](#package)
- [Contribution](#contributing)
- [License](#license)

## Introduction

### 
A 6 degree-of-freedom rocket model is a simulation that accurately models the motion of a rocket in flight, taking into account atmospheric conditions, turbulence, and aerodynamic parameters. It calculates the trajectory, apogee, and other parameters of the rocket at every time interval using detailed information about the motor, rocket, and aerodynamics.
This type of model is essential for predicting the behavior of rockets during flight and optimizing their performance. The model takes into account factors such as air density, wind speed, and turbulence to simulate the rocket's trajectory accurately. It also considers the rocket's weight, shape, and aerodynamic properties to predict its behavior as it flies through the air. 
In the case of the validated rocket launch at Spaceport America in New Mexico, the model accurately predicted the rocket's apogee to within 34 feet of the actual altitude reached. This level of accuracy demonstrates the effectiveness of the model and its ability to provide valuable insights into rocket performance.

## About the model
There are specific inputs required for the model to run which includes:
### Excel Data:
1) Aerodynamic Coefficients Data
2) Motor thrust vs time data
3) Rocket data (from CFD analysis or previous flight data)


### User inputs required:
1) Initial Yaw angle                            
2) Initial Pitch angle
3) Wind velocity in north direction 
4) Wind velocity in east direction           
5) Turbulance Intensity
6) Launch Rail height                        
7) Aibrakes (Y/N)   
8) Desired Apogee                           
9) Parachute diameter  
10) Reefed parachute diameter                      
11) Reefing Height  
12) Rocket mass                          
13) Rocket CG     
14) Rocket's axial moment of inertia                           
15) Rocket's transverse moment of inertia     
17) Rocket's Radius    
18) Rocket's diameter                        
19) Fin root chord    
20) Fin tip chord                        
21) Fin Height   
22) Fin sweep length                              
23) Fin's Distance from nosetip  
24) Motor Length            
25) Motor diameter   
26) Motor wet Mass                           
27) Motor dry mass 
28) Nozzle mass
29) Nozzle Length  
30) Simulation Time step       


## How to install?


## How to use this package?
Once the package is installed on the respective Python environment, one can directly run the main.py file in order to input values and run the model. The model will ask for basic inputs which includes wind speeds in east and north direction, launch pitch and yaw angles, presence/absence of airbrakes, height of the launch rail and and percentage of turbulent intensity user wants in the model. 

Users can change the input values through 2 methods.
a) Opening '.env' file and manually overridding values of necessary parameters.
b) Using CLI commands to override values. If you are unsure of what values corresponds to what parameter, simply type "HeliosSim --help" command will help the user obtain the CLI commands required
  
There are two extra  excel data the motor data can be obtained from thrust-time curve or commercial-off-the-shelf Computational fluid dynamics softwares like Ansys. By default there are example excels present within the package and the user can change the files. The model will have variable computational time depending upon the number of iterations considered through user inputs. 

## Contributing

Peformance Improvements, bug fixes, better design approaches are welcome. Please Discuss your change by raising an issue, beforehand. Advancements to the model are appreciated. 


## License
Copyright (c) thrustMIT.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE MODEL IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
