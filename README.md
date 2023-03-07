# HeliosSim


This is a 6 degree of freedom model developed by a group of enthusiastic engineers who were part of thrustMIT (MIT Manipal's Rocketry team). This model was inspired by the absence of physical testing of sounding rockets in India leading to the formation of this high-precision model. This model provides you with multiple features

## Table of Contents

- [Introduction](#introduction)
- [About the model](#about)
- [How to install?](#installation)
- [How to use this package](#package)
- [Contribution](#contributing)
- [License](#license)

## Introduction

### 
A 6 degree-of-freedom rocket model is a simulation that accurately models the motion of a rocket in flight, taking into account atmospheric conditions, turbulence, and aerodynamic parameters. It calculates the trajectory, apogee, and other parameters of the rocket at every time interval using detailed information about the motor, rocket, and aerodynamics.
This type of model is essential for predicting the behavior of rockets during flight and optimizing their performance. The model takes into account factors such as air density, wind speed, and turbulence to simulate the rocket's trajectory accurately. It also considers the rocket's weight, shape, and aerodynamic properties to predict its behavior as it flies through the air. 
In the case of the validated rocket launch at Spaceport America in New Mexico, the model accurately predicted the rocket's apogee to within 34 feet of the actual altitude reached. This level of accuracy demonstrates the effectiveness of the model and its ability to provide valuable insights into rocket performance.

## About
There are specific inputs required for the model to run which includes:
### Excel Data:
1) Aerodynamic Coefficients Data
2) Motor thrust vs time data

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


## Installation
Use the following to download the package from the PyPi Repository:
```
pip install helios-sim
```

## Package
## How to use this package?
Once the package has been installed on the machine and the requirements are satisfied use the following command to run the Helios Simulator:
```
helios -[options] [values]
```
The following is an example for running the code with all parameters passed through CLI:
```
helios --yaw 2 --pitch 2 --wind-north 2 --wind-east 2 --turb-inten 5 --rail-length 5.18 --air-brakes 'n' --desired 3048 --parachute-dia 3 --reefed-parachute-dia 0.8 --reefed-height 460 --rocket-mass 26.4 --rocket-cg 1.92 --rocket-ami 0.09 --rocket-tmi 17.77 --rocket-dia 0.15 --rocket-rad 0.075 --rocket-length 3.03 --fin-root-chord 0.3 --fin-tip-chord 0.2 --fin-height 0.145 --fin-sweep-length 0.179 --fin-dist-nosetip 2.6 --motor-length 0.702 --motor-odia 0.098 --motor-wetmass 8.108 --motor-drymass 3.656 --noz-mass 0.1891 --noz-length 0.057 --prop-data 'prop_data.xlsx' --aero-data 'aero_data.xlsx' --delaytracker 0 --delay 1 --time-step 0.001 -o 'helios_output.pdf'
```
The output for the simulations run is stored in a PDF file as follows: <br>
[output.pdf](helios_output.pdf)

Users can change the input values through 2 methods.
1) Opening '.env' file and manually overridding values of necessary parameters. 
2) Using CLI commands to override values. If you are unsure of what values corresponds to what parameter, simply type "HeliosSim --help" command will help the user obtain the CLI commands required
  
There are two extra  excel data the motor data can be obtained from thrust-time curve or commercial-off-the-shelf Computational fluid dynamics softwares like Ansys. By default there are example excels present within the package and the user can change the files. The model will have variable computational time depending upon the number of iterations considered through user inputs. 

## Contributing

Peformance Improvements, bug fixes, better design approaches are welcome. Please Discuss your change by raising an issue, beforehand. Advancements to the model are appreciated. 


## License
[MIT](LICENSE)
