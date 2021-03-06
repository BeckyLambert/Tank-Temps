# main.py -- put your code here!
# Import what is necessary to create a thread
from pysense import Pysense
from SI7006A20 import SI7006A20
import machine
import _thread
from time import sleep
adc = machine.ADC()             # create an ADC object
# adc.vref_to_pin('P22')
adc.vref(1100)
apin = adc.channel(pin='P16')   # create an analog pin on P16

py = Pysense()
si = SI7006A20(py)

print("Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")

# Increment index used to scan each point from vector sensors_data
def inc(index, vector):
    if index < len(vector)-1:
        return index+1
    else:
        return 0

# Define your thread's behaviour, here it's a loop sending sensors data every 5 seconds
def send_env_data():
    while True:
        temp = get_temp()
        pybytes.send_signal(1, temp)
        sleep(5)

# Start your thread
_thread.start_new_thread(send_env_data, ())

T_MAX = 220 #F
T_MIN = -30 #F
V_MAX = 10 #V
V_MIN = 0 #V
R1 = 10 # 10 kOhm
R2 = 2 # 2 kOhm


def get_voltage():
    val = apin() #microvolts
    return val / 1000

def calculate_v_in (v_out):
    return v_out * (R1 + R2) / R2

def calculate_temp(v_in):
    return v_in * (T_MAX - T_MIN) / (V_MAX - V_MIN)

def get_temp():
    celcius = si.temperature()
    far = celcius * 9 / 5 + 32
    return far
