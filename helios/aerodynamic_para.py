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
import numpy as np
from scipy.interpolate import interp1d

def aerodynamic_para(data1, data2, mach, pitch, yaw, phase, flag):
    m = np.arange(0,1.99,0.01)
    cd_poweron = np.zeros((199,3,2))
    cn = np.zeros((199,3))
    cd_poweroff = np.zeros((199,3,2))
    cn_alpha = np.zeros((199,1))
    cp = np.zeros((199,1))
    angle=[0,2,4]
    mach = np.abs(mach)
    pitch = np.abs(pitch)
    yaw = np.abs(yaw)
    
#NO Airbrakes
    cd_poweron[:,0,0] = data1.iloc[0:199,4]
    cd_poweron[:,1,0] = data1.iloc[2500:2699,4]
    cd_poweron[:,2,0] = data1.iloc[5000:5199,4]
    cd_poweroff[:,0,0] = data1.iloc[0:199,3]
    cd_poweroff[:,1,0] = data1.iloc[2500:2699,3]
    cd_poweroff[:,2,0] = data1.iloc[5000:5199,3]

    cn[:,0] = data1.iloc[0:199,8]
    cn[:,1] = data1.iloc[2500:2699,8]
    cn[:,2] = data1.iloc[5000:5199,8]

    cn_alpha[:,0] = data1.iloc[0:199,11]
    cp[:,0] = data1.iloc[0:199,12]
   
#Airbrakes
    cd_poweron[:,0,1] = data2.iloc[0:199,4]
    cd_poweron[:,1,1] = data2.iloc[2500:2699,4]
    cd_poweron[:,2,1] = data2.iloc[5000:5199,4]
    cd_poweroff[:,0,1] = data2.iloc[0:199,3]
    cd_poweroff[:,1,1] = data2.iloc[2500:2699,3]
    cd_poweroff[:,2,1] = data2.iloc[5000:5199,3]

    cd_poweron = np.transpose(cd_poweron)
    cn = np.transpose(cn)
    cp = np.transpose(cp)
    cd_poweroff = np.transpose(cd_poweroff)
    cn_alpha = np.transpose(cn_alpha)
    
    if phase == 1:
        f_cd0 = interp1d(m,cd_poweron[0,0,:])
        cd0 = f_cd0(mach)
        f_cd2 = interp1d(m,cd_poweron[0,1,:])
        cd2 = f_cd2(mach)
        f_cd4 = interp1d(m,cd_poweron[0,2,:])
        cd4 = f_cd4(mach)
        coeffs_cd = np.array([cd0, cd2, cd4])
        p1 = np.polyfit(angle,coeffs_cd,2)

        CD=(p1[0] * (pitch**2+ yaw**2)) + (p1[1]*np.sqrt(pitch**2 + yaw**2)) + p1[2]

        cn0=0
        f_cn2 = interp1d(m,cn[1,:])
        cn2 = f_cd0(mach)
        f_cn4 = interp1d(m,cn[2,:])
        cn4 = f_cd2(mach)
        coeffs_cn = np.array([cn0, cn2, cn4])
        p2 = np.polyfit(angle,coeffs_cn,2)

        CNP=(p2[0]*pitch**2) +( p2[1]*pitch) + p1[2]
        CNY=(p2[0]*yaw**2) + (p2[1]*yaw) + p1[2]

        f_cp = interp1d(m,cp)
        CP = f_cp(mach)

    elif phase == 0:
        if flag == 0:
            f_cd0 = interp1d(m,cd_poweroff[0,0,:])
            cd0 = f_cd0(mach)
            f_cd2 = interp1d(m,cd_poweroff[0,1,:])
            cd2 = f_cd2(mach)
            f_cd4 = interp1d(m,cd_poweroff[0,2,:])
            cd4 = f_cd4(mach)
            coeffs_cd = np.array([cd0, cd2, cd4])
            p1 = np.polyfit(angle,coeffs_cd,2)

            CD=(p1[0] * (pitch**2+ yaw**2)) + (p1[1]*np.sqrt(pitch**2 + yaw**2)) + p1[2]

            cn0=0
            f_cn2 = interp1d(m,cn[1,:])
            cn2 = f_cd0(mach)
            f_cn4 = interp1d(m,cn[2,:])
            cn4 = f_cd2(mach)
            coeffs_cn = np.array([cn0, cn2, cn4])
            p2 = np.polyfit(angle,coeffs_cn,2)

            CNP=(p2[0]*pitch**2) +( p2[1]*pitch) + p1[2]
            CNY=(p2[0]*yaw**2) + (p2[1]*yaw) + p1[2]

            f_cp = interp1d(m,cp)
            CP = f_cp(mach)

        elif flag == 1:
            f_cd0 = interp1d(m,cd_poweroff[1,0,:])
            cd0 = f_cd0(mach)
            f_cd2 = interp1d(m,cd_poweroff[1,1,:])
            cd2 = f_cd2(mach)
            f_cd4 = interp1d(m,cd_poweroff[1,2,:])
            cd4 = f_cd4(mach)
            coeffs_cd = np.array([cd0, cd2, cd4])
            p1 = np.polyfit(angle,coeffs_cd,2)

            CD=(p1[0] * (pitch**2+ yaw**2)) + (p1[1]*np.sqrt(pitch**2 + yaw**2)) + p1[2]

            cn0=0
            f_cn2 = interp1d(m,cn[1,:])
            cn2 = f_cd0(mach)
            f_cn4 = interp1d(m,cn[2,:])
            cn4 = f_cd2(mach)
            coeffs_cn = np.array([cn0, cn2, cn4])
            p2 = np.polyfit(angle,coeffs_cn,2)

            CNP=(p2[0]*pitch**2) +( p2[1]*pitch) + p1[2]
            CNY=(p2[0]*yaw**2) + (p2[1]*yaw) + p1[2]

            f_cp = interp1d(m,cp)
            CP = f_cp(mach)
    
    f_CN_alpha = interp1d(m,cn_alpha)
    CN_alpha = f_CN_alpha(mach)
    CP = CP/39.37 
    
    return CP, CNP, CNY, CN_alpha, CD
    
    