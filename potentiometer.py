#https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led <- this helped!

import machine
import time

#Creates a new analog -> digital instance
ldr = machine.ADC(26)

while True:
    # Reads data from ADC u16 format
    lightReading = ldr.read_u16()
    print (lightReading)
    time.sleep(0.2)
