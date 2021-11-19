import time
from machine import PWM, Pin

# Creates Analog->Digital object and defines pin (pin_num)
adc = machine.ADC(26)
# Sets PWM up on PIN
orange = PWM(Pin(16))
orange.freq(1000)


voltageCalc = 3.3/65535

while True:
    # Reads data  from ADC u16 format
    val = adc.read_u16()
    print (val)
    
    # Not needed, unless pot won't return 0 as a value
    if val < 200:
        val = 0
    else:
        val = val
    
    # Sets PWM duty to the reading of the pot
    orange.duty_u16(val)
    
    # Turns ADC input into voltage reading from 0 -> 3.3 (depends on noise)
    newVal = adc.read_u16()*voltageCalc
    time.sleep(0.05)
