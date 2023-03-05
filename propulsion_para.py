"""
File: ./propulsion_para.py

Description:
        This function takes in multiple motor parameters like it's Wet and Dry mass, Diameter, Nozzle's mass and length, Thrust vs Time to compute 
        Motor's mass, position of center of gravity, and the Moment of Inertia using kinematics equations. The fucntion also interpolates
        the thrust generated for the given motor at every time step using the Thrust vs Time data.

Function Inputs:
        timer --> Current timestep
        Length --> Length of the Motor
        odia --> Outer Diameter of the motor
        wetmass --> Wetmass of the motor
        drymass --> Drymass of the motor
        nozmass --> Nozzle mass of the motor
        nozlen --> Length of the Nozzle
        time --> Time data for the given motor
        thrust --> Thrust data for the given motor

Function Outputs:
        mass --> Mass of the entire motor (Drymass + Wetmass)
        cg --> Position of Center of gravity of the motor
        Ix --> Moment of Inertia along X
        Iy --> Moment of Inertia along Y
        currentthrust --> Thrust for the given timestep
"""
from scipy.interpolate import interp1d
def propulsion_para(timer, length, odia, wetmass, drymass, nozmass, nozlen, time, thrust):
    if timer>time[-1]:
        currentthrust = 0
        mass = drymass+nozmass #total mass
        Ix1 = 0 #MI of motor grain
        Ix2 = drymass*(odia/2)**2 #MI of casing assuming it is a thin cylinder
        Ix3 = 0.5*nozmass*0.25*(odia**2)
        cg = (((mass-nozmass)*(length/2))+(nozmass*(length+(nozlen/2))))/mass
        Iy1 = 0
        Iy2 = (0.5*drymass*(odia/2)**2)+((1/12)*drymass*length**2)+(drymass*(cg-(length/2))**2)
        Iy3 = ((1/12)*nozmass*(((3/4)*(odia**2))+nozlen**2))+(nozmass*(cg-(length+(nozlen/2)))**2)
    else:
        f = interp1d(time, thrust, kind='cubic', fill_value="extrapolate")
        currentthrust = f(timer) 
        burnrate = (wetmass-drymass)/(time[-1])
        dm = burnrate*timer
        mass = (wetmass-dm)+nozmass
        Ix1 = 0.5*(mass-drymass-nozmass)*0.25*(odia**2)
        Ix2= drymass*(odia/2)**2
        Ix3= 0.5*nozmass*0.25*(odia**2)
        cg= (((drymass)*(length/2))+((mass-drymass)*((length)/2))+(nozmass*(length+(nozlen/2))))/mass
        Iy1= ((1/12)*(mass-drymass)*(((3/4)*(odia**2))+(length)**2))+((mass-drymass)*(cg-((length)/2))**2)
        Iy2= (0.5*drymass*(odia/2)**2)+((1/12)*drymass*length**2)+(drymass*(cg-(length/2))**2)
        Iy3=((1/12)*nozmass*(((3/4)*(odia**2))+nozlen**2))+(nozmass*(cg-(length+(nozlen/2)))**2)
    Ix = Ix1+Ix2+Ix3
    Iy = Iy1+Iy2+Iy3
    return mass,cg,Ix,Iy,currentthrust