import argparse
import os
from dotenv import load_dotenv
load_dotenv()

p = argparse.ArgumentParser()

p.add_argument("-y", "--yaw", help="Initial Yaw in degrees", default=os.getenv('INIT_YAW'))
p.add_argument("-p", "--pitch", help="Initial Pitch in degrees", default=os.getenv('INIT_PITCH'))
p.add_argument("-n", "--wind-north", help="Mean wind speed in North", default=os.getenv('WIND_VEL_N'))
p.add_argument("-e", "--wind-east", help="Mean wind speed in East", default=os.getenv('WIND_VEL_E'))
p.add_argument("-t", "--turb-inten", help="Turbulance Intensity Percentage", default=os.getenv('TURB_INTEN'))
p.add_argument("-l", "--rail-length", help="Mean wind speed in North", default=os.getenv('LAUNCH_RAIL_LEN'))
p.add_argument("-a", "--air-brakes", help="Air Brakes", default=os.getenv('AIRBRAKES'))
p.add_argument("-d", "--desired-apogee", help="Desired Apogee", default=os.getenv('DESIRED'))
p.add_argument("-P", "--parachute-dia", help="Dis-reefed Parachute Diameter", default=os.getenv('PARACHUTE_DIA'))
p.add_argument("-R", "--reefed-parachute-dia", help="Reefed Parachute Diameter", default=os.getenv('REEFED_DIA'))
p.add_argument("-H", "--reefed-height", help="Height at which the parachute is dis-reefed", default=os.getenv('REEFED_HEIGHT'))
p.add_argument("-M", "--rocket-mass", help="Mass of the Rocket", default=os.getenv('ROCKET_MASS'))
p.add_argument("-C", "--rocket-cg", help="Center of Gravity of Rocket", default=os.getenv('ROCKET_CG'))
p.add_argument("-A", "--rocket-ami", help="AMI of Rocket", default=os.getenv('ROCKET_AMI'))
p.add_argument("-T", "--rocket-tmi", help="TMI of Rocket", default=os.getenv('ROCKET_TMI'))
p.add_argument("-D", "--rocket-dia", help="Diameter of the Rocket", default=os.getenv('ROCKET_DIA'))
p.add_argument("-L", "--rocket-length", help="Length of the Rocket", default=os.getenv('ROCKET_LENGTH'))
p.add_argument("-r", "--fin-root-chord", help="Root Chord of Fin", default=os.getenv('FIN_ROOT_CHORD'))
p.add_argument("-f", "--fin-tip-chord", help="Tip Chord of Fin", default=os.getenv('FIN_TIP_CHORD'))
p.add_argument("-z", "--fin-height", help="Height of Fin", default=os.getenv('FIN_HEIGHT'))
p.add_argument("-s", "--fin-sweep-length", help="Fin Sweep Length", default=os.getenv('FIN_SWEEP_LEN'))
p.add_argument("-N", "--fin-dist-nosetip", help="Distance from nosetip to leading edge of fin", default=os.getenv('FIN_DIST_NOSETIP'))

args = p.parse_args()


print(args._get_args)