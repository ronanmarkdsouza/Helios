"""
File: ./rocket_sim.py

Description: This is the driver function for the simulator
"""
import pandas as pd
from initialize import rocket_params
rocketSim = rocket_params()

def rocket_sim(rocket):
    prop_data = pd.read_excel(rocket.prop_data)
    thrust = prop_data.loc[:,'thrust'].to_list()
    time = prop_data.loc[:,'time'].to_list()
    aero_data_wab = pd.read_excel(rocket.aero_data, sheet_name=0)
    aero_data_ab = pd.read_excel(rocket.aero_data, sheet_name=1)
    