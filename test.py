import argparse
import os
from dotenv import load_dotenv
load_dotenv()

p = argparse.ArgumentParser()

p.add_argument("-w", "--wind-speed", help="wind speed", default=5)
p.add_argument("-a", "--ashwin", help="fuck ashwin", default='yes')
p.add_argument("-m", "--rocket-mass", help="Rocket Mass", default=os.getenv('ROCKET_MASS'))
args = p.parse_args()

print(args.wind_speed)
print(args.ashwin)
print(args.rocket_mass)