import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
from datetime import date
import time

def output_pdf(file_name,vtrajectory, acceleration, velocity, drift_dist, timer, stability_cal, Xe, Ye, Ze, motor_time, motor_thrust, rocket):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 16)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    ch = 8
    class PDF(FPDF):
        def __init__(self):
            super().__init__()
        def header(self):
            self.set_font('Arial', '', 12)
            self.cell(0, 8, 'Flight Simulation Report by Helios', 0, 1, 'C')
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', '', 12)
            self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')
    
    launch_details = pd.DataFrame(
          {'features' : ['Initial Yaw', 
                          'Initial Pitch', 
                          'Mean Wind Speed - North', 
                          'Mean Wind Speed - East',
                          'Turbulance Intensity',
                          'Launch Rail Length'],
           'values' : [rocket.yaw, 
                          rocket.pitch, 
                          rocket.wind_north, 
                          rocket.wind_east,
                          rocket.turb_inten,
                          rocket.rail_length]
          })
    
    Rocket_details = pd.DataFrame(
          {'features' : ['Rocket Mass', 
                          'Rocket CG', 
                          'Rocket Axial Moment of Inertia', 
                          'Rocket Transverse Moment of Inertia',
                          'Rocket Diameter',
                          'Rocket Radius',
                          'Rocket Length'],
           'values' : [rocket.rocket_mass, 
                          rocket.rocket_cg, 
                          rocket.rocket_ami, 
                          rocket.rocket_tmi,
                          rocket.rocket_dia,
                          rocket.rocket_rad,
                          rocket.rocket_length]
          })
    
    Fin_details = pd.DataFrame(
          {'features' : ['Fin Root Chord', 
                          'Fin Tip Chord', 
                          'Fin height', 
                          'Fin Sweep Length',
                          'Fin Distance from Nosetip'],
           'values' : [rocket.fin_root_chord, 
                          rocket.fin_tip_chord, 
                          rocket.fin_height, 
                          rocket.fin_sweep_length,
                          rocket.fin_dist_nosetip,]
          })
    Parachute_details = pd.DataFrame(
          {'features' : ['Parachute Diameter', 
                          'Reefed Parachute Diameter', 
                          'Reefed Height'],
           'values' : [rocket.parachute_dia, 
                          rocket.reefed_parachute_dia, 
                          rocket.reefed_height]
          })
    
    Motor_details = pd.DataFrame(
          {'features' : ['Motor Length', 
                          'Motor Diameter', 
                          'Motor Wet Mass', 
                          'Motor Dry Mass',
                          'Nozzle Mass',
                          'Nozzle Length'],
           'values' : [rocket.motor_length, 
                          rocket.motor_odia, 
                          rocket.motor_wetmass,
                          rocket.motor_drymass,
                          rocket.noz_mass,
                          rocket.noz_length]
          })
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(w=0, h=20, txt="Helios Simulation Report", ln=1)
    pdf.set_font('Arial', '', 16)
    pdf.cell(w=30, h=ch, txt=str(date.today()), ln=1)
    pdf.cell(w=30, h=ch, txt=str(current_time), ln=2)
    pdf.ln(ch)
    pdf.multi_cell(w=0, h=5, txt="User required ")
    pdf.ln(ch)
    pdf.multi_cell(w=0, h=5, txt="Launch Details")

    for i in range(0, len(launch_details)):
        pdf.cell(w=80, h=8, 
                txt=launch_details['features'].iloc[i], 
                border=1, ln=0, align='C')
        pdf.cell(w=80, h=8, 
                txt=launch_details['values'].iloc[i].astype(str), 
                border=1, ln=1, align='C')
    pdf.ln(ch)

    pdf.multi_cell(w=0, h=5, txt="Fin Details")
    for i in range(0, len(Fin_details)):
        pdf.cell(w=80, h=8, 
                txt=Fin_details['features'].iloc[i], 
                border=1, ln=0, align='C')
        pdf.cell(w=80, h=8, 
                txt=Fin_details['values'].iloc[i].astype(str), 
                border=1, ln=1, align='C')
    pdf.ln(ch)

    pdf.multi_cell(w=0, h=5, txt="Parachute Details")
    for i in range(0, len(Parachute_details)):
        pdf.cell(w=80, h=8, 
                txt=Parachute_details['features'].iloc[i], 
                border=1, ln=0, align='C')
        pdf.cell(w=80, h=8, 
                txt=Parachute_details['values'].iloc[i].astype(str), 
                border=1, ln=1, align='C')
    pdf.ln(ch)
        
    pdf.multi_cell(w=0, h=5, txt="Motor Details")
    for i in range(0, len(Motor_details)):
        pdf.cell(w=80, h=8, 
                txt=Motor_details['features'].iloc[i], 
                border=1, ln=0, align='C')
        pdf.cell(w=80, h=8, 
                txt=Motor_details['values'].iloc[i].astype(str), 
                border=1, ln=1, align='C')
    pdf.ln(ch)
    pdf.multi_cell(w=0, h=5, txt="Results of the Simulation")
    
    plt.plot(motor_time, motor_thrust)
    plt.xlabel('Time')
    plt.ylabel('Thrust')
    plt.title('Thrust-Time Curve')
    plt.savefig('./plots/thrust_time.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")
    
    plt.plot(timer, stability_cal)
    plt.xlabel('Time')
    plt.ylabel('Stability Caliber')
    plt.title('Stability Caliber-Time Curve')
    plt.savefig('./plots/stabcal_time.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")
    
    plt.plot(timer, velocity)
    plt.xlabel('Time')
    plt.ylabel('Velocity')
    plt.title('Velocity-Time Curve')
    plt.savefig('./plots/vel_time.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")

    plt.plot(timer, acceleration)
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.title('Acceleration-Time Curve')
    plt.savefig('./plots/accel_time.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")
    
    plt.plot(timer, Xe)
    plt.xlabel('Time')
    plt.ylabel('Altitude')
    plt.title('Altitude-Time Curve')
    plt.savefig('./plots/alt_time.png', 
           transparent=False,  
           facecolor='white', 
           bbox_inches="tight")

    pdf.image('./plots/thrust_time.png', 
          x = 10, y = None, w = 100, h = 0, type = 'PNG')
    
    pdf.image('./plots/stabcal_time.png', 
      x = 10, y = None, w = 100, h = 0, type = 'PNG')

    pdf.image('./plots/vel_time.png', 
      x = 10, y = None, w = 100, h = 0, type = 'PNG')

    pdf.image('./plots/accel_time.png', 
      x = 10, y = None, w = 100, h = 0, type = 'PNG')

    pdf.image('./plots/alt_time.png', 
      x = 10, y = None, w = 100, h = 0, type = 'PNG')

    pdf.output(file_name)