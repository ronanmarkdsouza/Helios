"""
File: ./wind_forces.py

Description:
        The function calculates the drag forces and moments exerted on the rocket due to the wind gusts that are randomly generated
        due to turbulence. The moment on the the rocket body is neglected as it is axisymmetric and only the moment on the fins
        is accounted for.
        
Function Input:
        vel --> Velocity of the wind
        cm --> Center of gravity
        den --> Density if the air at a given time interval
        rad --> Radius of the rocket
        len --> Length of the rocket
        fin --> A [5x1] Vector that holds the details of the fins in the form [Root Chord, Tip Chrod, Height, Sweep Length, Distance from Nosetip]

Function Output:
        F --> Drag force experienced by the fins due to wind gusts
        mom --> Moment due to Drag force experienced by the fins due to wind gusts
"""

import numpy as np
from scipy.interpolate import interp1d

def side_forces1(vel,cm,den,rad,len,fin):
    vel = np.sqrt(vel*vel)   
    cdcyl=[[-5,5],[10 ,3.33],[100 ,1.334],[1000 ,0.738],[10000 ,0.766],[100000 ,0.56],[1000000 ,0.55],[10000000, 0.54],[100000000 ,0.54]]
    cdcyl_1 = []
    cdcyl_2 = []
    for i in cdcyl:
        cdcyl_1.append(i[0])
        cdcyl_2.append(i[1])
    cdplt=1.28;  
    ryno=(1.225*vel**2*rad)/(0.0000173);    
    f = interp1d(cdcyl_1,cdcyl_2, kind = 'linear')
    cn = f(ryno)
    F = 0.5* den* vel**2*((cn*rad*2*len)*(cdplt*(fin[0]+fin[1])*fin[2]))
    mom = 0.5*den*vel**2*cdplt*(fin[0]+fin[1])*fin[2]*(fin[4]-cm)
    return F,mom