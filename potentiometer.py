#https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led <- this helped!

import machine
import time

# Creates Analog->Digital object and defines pin (pin_num)
adc = machine.ADC(26)
while True:
    # Reads data afrom ADC u16 format
    val = adc.read_u16()
    print (val)
    time.sleep(0.2)
