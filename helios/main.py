import argparse
import os
from dotenv import load_dotenv
from .rocket_sim import rocket_sim
from .output_pdf import output_pdf
load_dotenv()

def main():
    p = argparse.ArgumentParser()

    p.add_argument("--yaw", help="Initial Yaw in degrees", default=os.getenv('INIT_YAW'), type=float)
    p.add_argument("--pitch", help="Initial Pitch in degrees", default=os.getenv('INIT_PITCH'), type=float)
    p.add_argument("--wind-north", help="Mean wind speed in North", default=os.getenv('WIND_VEL_N'), type=float)
    p.add_argument("--wind-east", help="Mean wind speed in East", default=os.getenv('WIND_VEL_E'), type=float)
    p.add_argument("--turb-inten", help="Turbulance Intensity Percentage", default=os.getenv('TURB_INTEN'), type=float)
    p.add_argument("--rail-length", help="Mean wind speed in North", default=os.getenv('LAUNCH_RAIL_LEN'), type=float)
    p.add_argument("--air-brakes", help="Air Brakes", default=os.getenv('AIRBRAKES'))
    p.add_argument("--desired-apogee", help="Desired Apogee", default=os.getenv('DESIRED'), type=float)
    p.add_argument("--parachute-dia", help="Dis-reefed Parachute Diameter", default=os.getenv('PARACHUTE_DIA'), type=float)
    p.add_argument("--reefed-parachute-dia", help="Reefed Parachute Diameter", default=os.getenv('REEFED_DIA'), type=float)
    p.add_argument("--reefed-height", help="Height at which the parachute is dis-reefed", default=os.getenv('REEFED_HEIGHT'), type=float)
    p.add_argument("--rocket-mass", help="Mass of the Rocket", default=os.getenv('ROCKET_MASS'), type=float)
    p.add_argument("--rocket-cg", help="Center of Gravity of Rocket", default=os.getenv('ROCKET_CG'), type=float)
    p.add_argument("--rocket-ami", help="AMI of Rocket", default=os.getenv('ROCKET_AMI'), type=float)
    p.add_argument("--rocket-tmi", help="TMI of Rocket", default=os.getenv('ROCKET_TMI'), type=float)
    p.add_argument("--rocket-dia", help="Diameter of the Rocket", default=os.getenv('ROCKET_DIA'), type=float)
    p.add_argument("--rocket-rad", help="Radius of the Rocket", default=os.getenv('ROCKET_RAD'), type=float)
    p.add_argument("--rocket-length", help="Length of the Rocket", default=os.getenv('ROCKET_LENGTH'), type=float)
    p.add_argument("--fin-root-chord", help="Root Chord of Fin", default=os.getenv('FIN_ROOT_CHORD'), type=float)
    p.add_argument("--fin-tip-chord", help="Tip Chord of Fin", default=os.getenv('FIN_TIP_CHORD'), type=float)
    p.add_argument("--fin-height", help="Height of Fin", default=os.getenv('FIN_HEIGHT'), type=float)
    p.add_argument("--fin-sweep-length", help="Fin Sweep Length", default=os.getenv('FIN_SWEEP_LEN'), type=float)
    p.add_argument("--fin-dist-nosetip", help="Distance from nosetip to leading edge of fin", default=os.getenv('FIN_DIST_NOSETIP'), type=float)
    p.add_argument("--motor-length", help="Length of the motor", default=os.getenv('MOTOR_LENGTH'), type=float)
    p.add_argument("--motor-odia", help="Outer Diameter of the motor", default=os.getenv('MOTOR_ODIA'), type=float)
    p.add_argument("--motor-wetmass", help="Wetmass of the motor", default=os.getenv('MOTOR_WETMASS'), type=float)
    p.add_argument("--motor-drymass", help="Drymass of the motor", default=os.getenv('MOTOR_DRYMASS'), type=float)
    p.add_argument("--noz-mass", help="Nozzle Mass", default=os.getenv('NOZ_MASS'), type=float)
    p.add_argument("--noz-length", help="Nozzle Length", default=os.getenv('NOZ_LENGTH'), type=float)
    p.add_argument("--prop-data", help="Path to Propulsion Data", default=os.getenv('PROP_DATA'))
    p.add_argument("--aero-data", help="Path to Aerodynamics Data", default=os.getenv('AERO_DATA'))
    p.add_argument("--delaytracker", help="Keeps track of mechanical delay of airbrakes in seconds", default=os.getenv('DELAY_TRACKER'), type=float)
    p.add_argument("--delay", help="Keeps track of electrical delay of airbrakes in seconds", default=os.getenv('DELAY'), type=float)
    p.add_argument("--time-step", help="Time step for each computation", default=os.getenv('TIME_STEP'), type=float)
    p.add_argument("-o","--output", help="Name of the output file", default=os.getenv('OUTPUT'))

    args = p.parse_args()

    vtrajectory, acceleration, velocity, drift_dist, timer, stability_cal, Xe, Ye, Ze, motor_time, motor_thrust = rocket_sim(args)
    output_pdf(args.output,vtrajectory, acceleration, velocity, drift_dist, timer, stability_cal, Xe, Ye, Ze, motor_time, motor_thrust, args)

