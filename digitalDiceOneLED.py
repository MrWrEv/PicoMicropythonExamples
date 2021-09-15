import random
import machine
import utime

num = random.randint(1,6)
print (num)

led=machine.Pin(15,machine.Pin.OUT)

for dice in range(num):
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)
