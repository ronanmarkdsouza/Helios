"""
File: ./rocket_sim.py

Description: This is the driver function for the simulator
"""
import math
import pandas as pd
from initialize import rocket_params
from density_and_temp import density_and_temp
from propulsion_para import propulsion_para
rocketSim = rocket_params()

def rocket_sim(rocket):
    prop_data = pd.read_excel(rocket.prop_data)
    thrust = prop_data.loc[:,'thrust'].to_list()
    time = prop_data.loc[:,'time'].to_list()
    aero_data_wab = pd.read_excel(rocket.aero_data, sheet_name=0)
    aero_data_ab = pd.read_excel(rocket.aero_data, sheet_name=1)
    
    counter = 1
    while rocketSim.Xe[counter] >= 0 or rocketSim.timer[counter]<time[-1]:
        sphi = math.sin(rocketSim.phi[counter])
        stheta = math.sin(rocketSim.theta[counter])
        spsi = math.sin(rocketSim.psi[counter])
        cphi = math.cos(rocketSim.phi[counter])
        ctheta = math.cos(rocketSim.theta[counter])
        cpsi = math.cos(rocketSim.psi[counter])

        mydensity, mytemperature = density_and_temp(rocketSim.Xe[counter], rocketSim.temperature)
        v_sound = math.sqrt(1.4*287*mytemperature)
        mach_no = rocketSim.u[counter]/v_sound

        mmass, mcg, mIx, mIy, mythrust = propulsion_para(rocketSim.timer[counter], 
                                                         rocket.motor_length, 
                                                         rocket.motor_odia, 
                                                         rocket.motor_wetmass,
                                                         rocket.motor_drymass,
                                                         rocket.noz_mass,
                                                         rocket.noz_length,
                                                         thrust, 
                                                         time
                                                         )
        rocketSim.Mass[counter] = rocket.rocket_mass + mmass
        rocketSim.CG[counter] = ((rocket.rocket_mass*rocket.rocket_cg)+(mmass*(rocket.rocket_length-(rocket.motor_length+rocket.noz_length)+mcg)))/rocketSim.Mass[counter]
        rocketSim.Ixx[counter] = rocket.rocket_ami + mIx
        rocketSim.Iyy[counter] = rocket.rocket_tmi + (rocket.rocket_mass*(rocketSim.CG[counter]-(rocket.rocket_cg))**2)+(mIy)+(mmass*(rocketSim.CG[counter]-(rocket.rocket_length-rocket.motor_length+mcg))**2)
        