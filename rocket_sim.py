"""
File: ./rocket_sim.py

Description: This is the driver function for the simulator
"""
import math
import pandas as pd
import numpy as np
from initialize import rocket_params
from density_and_temp import density_and_temp
from propulsion_para import propulsion_para
from aerodynamic_para import aerodynamic_para
from predictor import predictor
from turbulance_generator import turbulence_generator
from wind_forces import wind_forces

rocketSim = rocket_params()


def rocket_sim(rocket):
    prop_data = pd.read_excel(rocket.prop_data)
    thrust = prop_data.loc[:,'thrust'].to_list()
    time = prop_data.loc[:,'time'].to_list()
    aero_data_wab = pd.read_excel(rocket.aero_data, sheet_name=0)
    aero_data_ab = pd.read_excel(rocket.aero_data, sheet_name=1)
    Aref = math.pi*(rocket.rocket_dia**2)/4
    fin_details = [rocket.fin_root_chord,rocket.fin_tip_chord,rocket.fin_height,rocket.fin_sweep_len,rocket.fin_dist_nosetip]
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

        if rocketSim.timer[counter] > time[-1]:
            rocketSim.mphase = 0
        if rocketSim.phase == 0:
            rocketSim.CP[counter], rocketSim.Cn_pitch[counter], rocketSim.Cn_yaw[counter], rocketSim.Cn_alpha[counter], rocketSim.Cd[counter] = aerodynamic_para(aero_data_wab,
                                                                                                                                                                 aero_data_ab,
                                                                                                                                                                 mach_no,
                                                                                                                                                                 rocketSim.psi[counter],
                                                                                                                                                                 rocketSim.theta[counter],
                                                                                                                                                                 rocketSim.mphase,
                                                                                                                                                                 rocketSim.flag)
        momentarm = rocketSim.CP[counter]-rocketSim.CG[counter] 
        rocketSim.Stab_Cal[counter] = momentarm/(rocket.rocket_dia)

        if rocketSim.timer[counter] > time[-1]:
            if rocketSim.flag == 0:
                rocketSim.prediction[counter] = predictor(aero_data_wab, 
                                                          rocketSim.acceleration[counter], 
                                                          rocketSim.u[counter],
                                                          rocketSim.Xe[counter],
                                                          rocketSim.Mass[counter],
                                                          Aref,
                                                          mytemperature,
                                                          rocket.time_step)
                
            elif rocketSim.flag == 1:
                rocketSim.prediction[counter] = predictor(aero_data_ab, 
                                                          rocketSim.acceleration[counter], 
                                                          rocketSim.u[counter],
                                                          rocketSim.Xe[counter],
                                                          rocketSim.Mass[counter],
                                                          Aref,
                                                          mytemperature,
                                                          rocket.time_step)
            
            if rocketSim.prediction[counter] > rocket.desired:
                if rocketSim.timer[counter] - rocket.delaytracker >= rocket.delay:
                    rocketSim.flag = 1
                    rocket.delaytracker = rocketSim.timer[counter]
            
            elif rocketSim.prediction[counter] < rocket.desired:
                if rocketSim.timer[counter] - rocket.delaytracker >= rocket.delay:
                    rocketSim.flag = 0
                    rocket.delaytracker = rocketSim.timer[counter]
        
        else:
            rocketSim.prediction[counter] = 0
        
        if rocketSim.flag == 1:
            rocketSim.state[counter] = 2000
        
        else:
            rocketSim.state[counter] = 500
        
        if rocketSim.timer[counter] < 10 or rocketSim.u[counter] >= 0:
            sidey, turbgen = turbulence_generator(counter,turbgen,rocket.wind_vel_n,rocket.turb_inten,rocket.time_step)
            sidez, turbgen = turbulence_generator(counter,turbgen,rocket.wind_vel_e,rocket.turb_inten,rocket.time_step)
        
            Fy, Mz = wind_forces(sidey,rocketSim.CG[counter],mydensity,rocket.rocket_rad,rocket.rocket_length,fin_details)
            Fz, My = wind_forces(sidez,rocketSim.CG[counter],mydensity,rocket.rocket_rad,rocket.rocket_length,fin_details)

            Fy = Fy*np.sign(sidey)*cpsi
            Fz = Fz*np.sign(sidez)*ctheta
            My = My*np.sign(sidez)*ctheta
            Mz = -Mz*np.sign(sidey)*cpsi
            
            if rocketSim.Xe[counter] > rocket.launch_rail_len:
                CNY = -(rocketSim.Cn_yaw[counter]*np.sign(rocketSim.psi[counter]))-(rocketSim.Cd[counter]*spsi)-(rocketSim.Cn_alpha[counter]*math.atan((rocketSim.q[counter]*momentarm)/rocketSim.u[counter]))
                CNP= -(rocketSim.Cn_pitch[counter]*np.sign(rocketSim.theta[counter]))-(rocketSim.Cd[counter]*stheta)-(rocketSim.Cn_alpha[counter]*math.atan((rocketSim.p[counter]*momentarm)/rocketSim.u[counter]))
                rocketSim.C_roll[counter]= -2*math.pi*math.atan((1.5*rocket.rocket_rad*rocketSim.r[counter])/rocketSim.u[counter])*np.sign(rocketSim.r[counter])
                
            else:
                CNY = 0
                CNP = 0
                rocketSim.C_roll[counter] = 0
                My = 0
                Mz = 0
                Fy = 0
                Fz = 0
            
            drag = 0.5*rocketSim.Cd[counter]*rocketSim.u[counter]*rocketSim.u[counter]*mydensity*Aref
            Yaw = (0.5*CNY*mydensity*rocketSim.u[counter]*rocketSim.u[counter]*Aref*momentarm) + Mz
            Pitch = (0.5*CNP*mydensity*rocketSim.u[counter]*rocketSim.u[counter]*Aref*momentarm) + My
            Roll = rocketSim.C_roll[counter]*mydensity*rocketSim.u[counter]*rocketSim.u[counter]*(fin_details[2]*(fin_details[0]+fin_details[1]))*(1.5*rocket.rocket_rad)
            
            rocketSim.vtrajectory[counter,0]=rocketSim.Xe[counter]
            rocketSim.vtrajectory[counter,1]=rocketSim.Ye[counter]
            rocketSim.vtrajectory[counter,2]=rocketSim.Ze[counter]
        
        else:
            pdia = rocket.reefed_dia
            if rocketSim.Xe[counter]<rocket.reefed_height:
                pdia = rocket.parachute_dia
                drag = (0.5*1.2*math.pi*(pdia)*(pdia)/4)*mydensity*rocketSim.u[counter]*rocketSim.u[counter]*np.sign(rocketSim.u[counter])
                Fy = (0.5*0.1*mydensity*(sidey**2)*(math.pi*(pdia)*(pdia)/4)*np.sign(sidey))-(0.5*0.1*mydensity*(rocketSim.v[counter]**2)*(math.pi*(pdia)*(pdia)/4)*np.sign(rocketSim.v[counter]))
                Fz = (0.5*0.1*mydensity*(sidez**2)*(math.pi*(pdia)*(pdia)/4)*np.sign(sidez))-(0.5*0.1*mydensity*(rocketSim.w[counter]**2)*(math.pi*(pdia)*(pdia)/4)*np.sign(rocketSim.w[counter]))
                Yaw = 0
                Pitch = 0
                Roll = 0
                rocketSim.phi[counter] = 0
                rocketSim.psi[counter] = 0
                rocketSim.theta[counter] = 0
                rocketSim.phase = 1
                rocketSim.flag = 0
    

