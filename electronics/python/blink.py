"""
Lässt die eingebaute blaue Leuchtdiode auf dem Lolin blinken.
"""

import machine
import utime

BLINK_DELAY_S = 0.5

led = machine.Pin(5, machine.Pin.OUT)
while True:
    led.value(False)
    utime.sleep(BLINK_DELAY_S)
    led.value(True)
    utime.sleep(BLINK_DELAY_S)
