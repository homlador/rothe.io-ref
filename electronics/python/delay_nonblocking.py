"""
Beispiel für nicht-blockierendes Warten. Die LED wird
eine Sekunde nach dem Tastendruck eingeschaltet.
"""

import machine
import utime

DELAY_MS = 1000
led = machine.Pin(5, machine.Pin.OUT)
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

led.value(False)
old_button = False
new_button = False
alarm = -1

while True:
    # Aktuelle Zeit bestimmen
    now = utime.ticks_ms()
    new_button = button.value()
    # Überprüfen, ob die Taste gedrückt wurde
    if old_button == False and new_button == True:
        # Weckzeit stellen
        alarm = utime.ticks_add(now, DELAY)
    old_button = new_button
    # Überprüfen, ob der Alarm eingeschaltet
    # und die Weckzeit erreicht worden ist
    if alarm != -1 and utime.ticks_diff(now, alarm) > 0:
        # LED einschalten
        led.value(True)
        # Alarm ausschalten
        alarm = -1
