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
Function Output:
              - prediction --> predicted apogee of the rocket at that moment
"""