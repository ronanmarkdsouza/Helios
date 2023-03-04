import argparse
import os
from dotenv import load_dotenv
load_dotenv()

p = argparse.ArgumentParser()

p.add_argument("--yaw", help="Initial Yaw in degrees", default=os.getenv('INIT_YAW'))
p.add_argument("--pitch", help="Initial Pitch in degrees", default=os.getenv('INIT_PITCH'))
p.add_argument("--wind-north", help="Mean wind speed in North", default=os.getenv('WIND_VEL_N'))
p.add_argument("--wind-east", help="Mean wind speed in East", default=os.getenv('WIND_VEL_E'))
p.add_argument("--turb-inten", help="Turbulance Intensity Percentage", default=os.getenv('TURB_INTEN'))
p.add_argument("--rail-length", help="Mean wind speed in North", default=os.getenv('LAUNCH_RAIL_LEN'))
p.add_argument("--air-brakes", help="Air Brakes", default=os.getenv('AIRBRAKES'))
p.add_argument("--desired-apogee", help="Desired Apogee", default=os.getenv('DESIRED'))
p.add_argument("--parachute-dia", help="Dis-reefed Parachute Diameter", default=os.getenv('PARACHUTE_DIA'))
p.add_argument("--reefed-parachute-dia", help="Reefed Parachute Diameter", default=os.getenv('REEFED_DIA'))
p.add_argument("--reefed-height", help="Height at which the parachute is dis-reefed", default=os.getenv('REEFED_HEIGHT'))
p.add_argument("--rocket-mass", help="Mass of the Rocket", default=os.getenv('ROCKET_MASS'))
p.add_argument("--rocket-cg", help="Center of Gravity of Rocket", default=os.getenv('ROCKET_CG'))
p.add_argument("--rocket-ami", help="AMI of Rocket", default=os.getenv('ROCKET_AMI'))
p.add_argument("--rocket-tmi", help="TMI of Rocket", default=os.getenv('ROCKET_TMI'))
p.add_argument("--rocket-dia", help="Diameter of the Rocket", default=os.getenv('ROCKET_DIA'))
p.add_argument("--rocket-length", help="Length of the Rocket", default=os.getenv('ROCKET_LENGTH'))
p.add_argument("--fin-root-chord", help="Root Chord of Fin", default=os.getenv('FIN_ROOT_CHORD'))
p.add_argument("--fin-tip-chord", help="Tip Chord of Fin", default=os.getenv('FIN_TIP_CHORD'))
p.add_argument("--fin-height", help="Height of Fin", default=os.getenv('FIN_HEIGHT'))
p.add_argument("--fin-sweep-length", help="Fin Sweep Length", default=os.getenv('FIN_SWEEP_LEN'))
p.add_argument("--fin-dist-nosetip", help="Distance from nosetip to leading edge of fin", default=os.getenv('FIN_DIST_NOSETIP'))
p.add_argument("--motor-length", help="Length of the motor", default=os.getenv('MOTOR_LENGTH'))
p.add_argument("--motor-odia", help="Outer Diameter of the motor", default=os.getenv('MOTOR_ODIA'))
p.add_argument("--motor-wetmass", help="Wetmass of the motor", default=os.getenv('MOTOR_WETMASS'))
p.add_argument("--motor-drymass", help="Drymass of the motor", default=os.getenv('MOTOR_DRYMASS'))
p.add_argument("--noz-mass", help="Nozzle Mass", default=os.getenv('NOZ_MASS'))
p.add_argument("--noz-length", help="Nozzle Length", default=os.getenv('NOZ_LENGTH'))
p.add_argument("--prop-data", help="Path to Propulsion Data", default=os.getenv('PROP_DATA'))
p.add_argument("--aero-data", help="Path to Aerodynamics Data", default=os.getenv('AERO_DATA'))



args = p.parse_args()