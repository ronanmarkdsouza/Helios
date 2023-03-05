"""
File: ./predictor.py

Description: This function is used to predict the apogee of the rocket using
rocket acceleration, velocity and displacement values. This function uses 
fourth order Runge-Kutta method to predict the apogee and velocity of the
rocket. It takes into account the drag while predicting the velocity and 
apogee values during the flight.

Function Input:
              - aerodata --> collection of data consisting of aerodynamic coefficients at different mach values
              - accelerationx --> X-component of acceleration vector
              - velocityx --> X-component of velocity vector
              - displacementx --> X-component of displacement vector
              - currentmass --> mass of the rocket at that interval
              - refArea --> reference area of the rocket
              - temp --> temperature at that time interval
              - dt --> time step
Function Output:
              - prediction --> predicted apogee of the rocket at that moment
"""
import numpy as np
from scipy.interpolate import interp1d

def predictor(aerodata,accelerationx,velocityx,displacementx,currentmass,refArea,temp,dt):

    accel = np.zeros(100)
    vel = np.zeros(100)
    disp = np.zeros(100)
    timer = np.zeros(100)
    counter = 0

    accel[0] = -accelerationx
    vel[0] = velocityx
    disp[0]= displacementx

    cd_data = aerodata.iloc[1:200, 2]
    mach_data = aerodata.iloc[1:200, 0]
    a = -0.0065

    while vel[counter]>0:
        mytemp = temp+(a*disp[counter])
        mydensity = 1.23*((mytemp/temp)**((-9.81/(a*287))-1))
        mach = vel[counter]/np.sqrt(1.4*287*mytemp)
        f = interp1d(mach_data, cd_data, kind='cubic')
        Cd = f(mach)
        def F(t,y,v):
            return v
        def G(t, y, v):
            return -((0.5 * Cd * mydensity * v * abs(v) * refArea) / currentmass) - 9.81
        
        k1 = F(timer[counter], disp[counter], vel[counter])
        L1 = G(timer[counter],disp[counter],vel[counter])
        k2 = F((timer[counter]+0.5*dt),(disp[counter]+0.5*dt*k1),(vel[counter]+0.5*dt*L1))
        L2 = G((timer[counter]+0.5*dt),(disp[counter]+0.5*dt*k1),(vel[counter]+0.5*dt*L1))
        k3 = F((timer[counter]+0.5*dt),(disp[counter]+0.5*dt*k2),(vel[counter]+0.5*dt*L2))
        L3 = G((timer[counter]+0.5*dt),(disp[counter]+0.5*dt*k2),(vel[counter]+0.5*dt*L2))
        k4 = F((timer[counter]+dt),(disp[counter]+k3*dt),(vel[counter]+L3*dt))
        L4 = G((timer[counter]+dt),(disp[counter]+k3*dt),(vel[counter]+L3*dt))


        disp[counter+1] = disp[counter] + dt*(1/6)*(k1 + 2*k2 + 2*k3 +  k4)
        vel[counter+1] = vel[counter] + dt*(1/6)*(L1 + 2*L2 + 2*L3 + L4)
        accel[counter+1] = G(timer[counter],disp[counter+1],vel[counter+1])
        timer[counter+1] = timer[counter] + dt
        counter = counter + 1
    
    prediction = np.max(disp)
    return prediction