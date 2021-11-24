import machine
import time

#Needs to be connected to 
button = machine.Pin(16,machine.Pin.OUT,machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("pressed")
        
    time.sleep(0.5)
