import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

prop_data = pd.read_excel('prop_data.xlsx')
thrust = prop_data.loc[:,'thrust'].to_list()
time = prop_data.loc[:,'time'].to_list()

fig, ax = plt.subplots(5,2)
ax[0][0].plot(time, thrust)
ax[0][0].set_title("Thrust-Time Curve")
ax[0][0].set_xlabel("Time")
ax[0][0].set_ylabel("Thrust")
ax[0][1].plot(time, thrust)
ax[1][0].plot(time, thrust)
ax[1][1].plot(time, thrust)
ax[2][0].plot(time, thrust)
ax[2][1].plot(time, thrust)
ax[3][0].plot(time, thrust)
ax[3][1].plot(time, thrust)
ax[4][0].plot(time, thrust)
ax[4][1].plot(time, thrust)


plt.show()