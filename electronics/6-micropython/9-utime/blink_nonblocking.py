"""
Lässt die eingebaute blaue Leuchtdiode auf dem Lolin blinken.
Diese Variante blockiert nicht, in der Schleife können andere Aufgaben
bearbeitet werden.
"""

import machine
import utime

BLINK_DELAY_MS = 500
led = machine.Pin(5, machine.Pin.OUT)
led.value(False)

on_alarm = 0
off_alarm = -1

while True:
    now = utime.ticks_ms()
    if on_alarm != -1 and utime.ticks_diff(now, on_alarm) > 0:
        led.value(True)
        on_alarm = -1
        off_alarm = utime.ticks_add(now, BLINK_DELAY_MS)

    if off_alarm != -1 and utime.ticks_diff(now, off_alarm) > 0:
        led.value(False)
        off_alarm = -1
        on_alarm = utime.ticks_add(now, BLINK_DELAY_MS)
