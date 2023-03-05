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
from Rk4Derivative import Rk4Derivative
from Rk4Utils import Rk4Utils
rocketSim = rocket_params()


def rocket_sim(rocket):
    counter = 1
    prop_data = pd.read_excel(rocket.prop_data)
    thrust = prop_data.loc[:,'thrust'].to_list()
    time = prop_data.loc[:,'time'].to_list()
    aero_data_wab = pd.read_excel(rocket.aero_data, sheet_name=0)
    aero_data_ab = pd.read_excel(rocket.aero_data, sheet_name=1)
    Aref = math.pi*(rocket.rocket_dia**2)/4
    fin_details = [rocket.fin_root_chord,rocket.fin_tip_chord,rocket.fin_height,rocket.fin_sweep_length,rocket.fin_dist_nosetip]
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
                                                         time, 
                                                         thrust
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
                                                          mytemperature)
                
            elif rocketSim.flag == 1:
                rocketSim.prediction[counter] = predictor(aero_data_ab, 
                                                          rocketSim.acceleration[counter], 
                                                          rocketSim.u[counter],
                                                          rocketSim.Xe[counter],
                                                          rocketSim.Mass[counter],
                                                          Aref,
                                                          mytemperature)
            
            if rocketSim.prediction[counter] > rocket.desired_apogee:
                if rocketSim.timer[counter] - rocket.delaytracker >= rocket.delay:
                    rocketSim.flag = 1
                    rocket.delaytracker = rocketSim.timer[counter]
            
            elif rocketSim.prediction[counter] < rocket.desired_apogee:
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
            sidey, rocketSim.turb_gen = turbulence_generator(counter,rocketSim.turb_gen,rocket.wind_north,rocket.turb_inten,rocket.time_step)
            sidez, rocketSim.turb_gen = turbulence_generator(counter,rocketSim.turb_gen,rocket.wind_east,rocket.turb_inten,rocket.time_step)
        
            Fy, Mz = wind_forces(sidey,rocketSim.CG[counter],mydensity,rocket.rocket_rad,rocket.rocket_length,fin_details)
            Fz, My = wind_forces(sidez,rocketSim.CG[counter],mydensity,rocket.rocket_rad,rocket.rocket_length,fin_details)

            Fy = Fy*np.sign(sidey)*cpsi
            Fz = Fz*np.sign(sidez)*ctheta
            My = My*np.sign(sidez)*ctheta
            Mz = -Mz*np.sign(sidey)*cpsi
            
            if rocketSim.Xe[counter] > rocket.rail_length:
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
            pdia = rocket.reefed_parachute_dia
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

        Rk1 = Rk4Utils(Rk4Derivative(mythrust,
                                     drag,
                                     Fy,
                                     Fz,
                                     rocketSim.Mass[counter],
                                     rocketSim.u[counter],
                                     rocketSim.v[counter],
                                     rocketSim.w[counter],
                                     rocketSim.p[counter],
                                     rocketSim.q[counter],
                                     rocketSim.r[counter],
                                     cphi,cpsi,ctheta,sphi,spsi,stheta,
                                     Yaw,Pitch,Roll,
                                     rocketSim.Ixx[counter],
                                     rocketSim.Iyy[counter],rocketSim.Iyy[counter]))
        Rk2 = Rk4Utils(Rk4Derivative(mythrust,
                                     drag,
                                     Fy,
                                     Fz,
                                     rocketSim.Mass[counter],
                                     rocketSim.u[counter] + Rk1.udot*(rocket.time_step/2),
                                     rocketSim.v[counter] + Rk1.vdot*(rocket.time_step/2),
                                     rocketSim.w[counter] + Rk1.wdot*(rocket.time_step/2),
                                     rocketSim.p[counter] + Rk1.pdot*(rocket.time_step/2),
                                     rocketSim.q[counter] + Rk1.qdot*(rocket.time_step/2),
                                     rocketSim.r[counter] + Rk1.rdot*(rocket.time_step/2),
                                     cphi,cpsi,ctheta,sphi,spsi,stheta,
                                     Yaw,Pitch,Roll,
                                     rocketSim.Ixx[counter],
                                     rocketSim.Iyy[counter],rocketSim.Iyy[counter]))
        
        Rk3 = Rk4Utils(Rk4Derivative(mythrust,
                                     drag,
                                     Fy,
                                     Fz,
                                     rocketSim.Mass[counter],
                                     rocketSim.u[counter] + Rk2.udot*(rocket.time_step/2),
                                     rocketSim.v[counter] + Rk2.vdot*(rocket.time_step/2),
                                     rocketSim.w[counter] + Rk2.wdot*(rocket.time_step/2),
                                     rocketSim.p[counter] + Rk2.pdot*(rocket.time_step/2),
                                     rocketSim.q[counter] + Rk2.qdot*(rocket.time_step/2),
                                     rocketSim.r[counter] + Rk2.rdot*(rocket.time_step/2),
                                     cphi,cpsi,ctheta,sphi,spsi,stheta,
                                     Yaw,Pitch,Roll,
                                     rocketSim.Ixx[counter],
                                     rocketSim.Iyy[counter],rocketSim.Iyy[counter]))
        
        Rk4 = Rk4Utils(Rk4Derivative(mythrust,
                                     drag,
                                     Fy,
                                     Fz,
                                     rocketSim.Mass[counter],
                                     rocketSim.u[counter] + Rk3.udot*(rocket.time_step/2),
                                     rocketSim.v[counter] + Rk3.vdot*(rocket.time_step/2),
                                     rocketSim.w[counter] + Rk3.wdot*(rocket.time_step/2),
                                     rocketSim.p[counter] + Rk3.pdot*(rocket.time_step/2),
                                     rocketSim.q[counter] + Rk3.qdot*(rocket.time_step/2),
                                     rocketSim.r[counter] + Rk3.rdot*(rocket.time_step/2),
                                     cphi,cpsi,ctheta,sphi,spsi,stheta,
                                     Yaw,Pitch,Roll,
                                     rocketSim.Ixx[counter],
                                     rocketSim.Iyy[counter],rocketSim.Iyy[counter]))
        
        rocketSim.u[counter+1] = rocketSim.u[counter] + (1/6)*(Rk1.udot + 2*Rk2.udot + 2*Rk3.udot + Rk4.udot)*rocket.time_step
        rocketSim.acceleration[counter+1] =  (1/6)*(Rk1.udot + 2*Rk2.udot + 2*Rk3.udot + Rk4.udot)
        rocketSim.v[counter+1] = rocketSim.v[counter] + (1/6)*(Rk1.vdot + 2*Rk2.vdot + 2*Rk3.vdot + Rk4.vdot)*rocket.time_step
        rocketSim.w[counter+1] = rocketSim.w[counter] + (1/6)*(Rk1.wdot + 2*Rk2.wdot + 2*Rk3.wdot + Rk4.wdot)*rocket.time_step
        rocketSim.r[counter+1] = rocketSim.r[counter] + (1/6)*(Rk1.rdot + 2*Rk2.rdot + 2*Rk3.rdot + Rk4.rdot)*rocket.time_step
        rocketSim.q[counter+1] = rocketSim.q[counter] + (1/6)*(Rk1.qdot + 2*Rk2.qdot + 2*Rk3.qdot + Rk4.qdot)*rocket.time_step
        rocketSim.p[counter+1] = rocketSim.p[counter] + (1/6)*(Rk1.pdot + 2*Rk2.pdot + 2*Rk3.pdot + Rk4.pdot)*rocket.time_step
        rocketSim.phi[counter+1] = rocketSim.phi[counter] + (1/6)*(Rk1.phidot + 2*Rk2.phidot + 2*Rk3.phidot + Rk4.phidot)*rocket.time_step
        rocketSim.theta[counter+1] = rocketSim.theta[counter] + (1/6)*(Rk1.thetadot + 2*Rk2.thetadot + 2*Rk3.thetadot + Rk4.thetadot)*rocket.time_step
        rocketSim.psi[counter+1] = rocketSim.psi[counter] + (1/6)*(Rk1.psidot + 2*Rk2.psidot + 2*Rk3.psidot + Rk4.psidot)*rocket.time_step
        rocketSim.Xe[counter+1] = rocketSim.Xe[counter] + (1/6)*(Rk1.xedot + 2*Rk2.xedot + 2*Rk3.xedot + Rk4.xedot)*rocket.time_step
        rocketSim.Ye[counter+1] = rocketSim.Ye[counter] + (1/6)*(Rk1.yedot + 2*Rk2.yedot + 2*Rk3.yedot + Rk4.yedot)*rocket.time_step
        rocketSim.Ze[counter+1] = rocketSim.Ze[counter] + (1/6)*(Rk1.zedot + 2*Rk2.zedot + 2*Rk3.zedot + Rk4.zedot)*rocket.time_step
        rocketSim.velx[counter+1] = (1/6)*(Rk1.xedot + 2*Rk2.xedot + 2*Rk3.xedot + Rk4.xedot)
        rocketSim.timer[counter+1] = rocketSim.timer[counter] + rocket.time_step
        counter = counter + 1
        rocketSim.drift[counter] = np.sqrt((rocketSim.Ye[counter]**2)+(rocketSim.Ze[counter]**2))

        if rocketSim.phase == 0 and rocketSim.Xe[counter]<0:
            rocketSim.Xe[counter] = 0
            rocketSim.u[counter] = 0

    rocketSim.prediction[counter] = 0
    rocketSim.state[counter] = 500
    return rocketSim.vtrajectory, rocketSim.acceleration, rocketSim.velx, rocketSim.drift, rocketSim.timer, rocketSim.Stab_Cal, rocketSim.Xe, rocketSim.Ye,rocketSim.Ze, time, thrust