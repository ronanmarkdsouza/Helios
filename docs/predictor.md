# Predictor

Description: This function is used to predict the apogee of the rocket using
rocket acceleration, velocity and displacement values. This function uses 
fourth order Runge-Kutta method to predict the apogee and velocity of the
rocket. It takes into account the drag while predicting the velocity and 
apogee values during the flight.

Function Input:
              - aerodata --> collection of data consisting of aerodynamic coefficients at different mach values </br>
              - accelerationx --> X-component of acceleration vector </br>
              - velocityx --> X-component of velocity vector </br>
              - displacementx --> X-component of displacement vector </br>
              - currentmass --> mass of the rocket at that interval </br>
              - refArea --> reference area of the rocket </br>
              - temp --> temperature at that time interval </br>
              - dt --> time step </br>
Function Output:
              - prediction --> predicted apogee of the rocket at that moment