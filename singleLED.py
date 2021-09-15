import machine
import utime
led_onboard = machine.Pin(15, machine.Pin.OUT)
led_onboard.value(1)
utime.sleep(2)
led_onboard.value(0)
utime.sleep(2)
