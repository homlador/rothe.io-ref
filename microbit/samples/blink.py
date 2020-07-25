"""
Lässt eine Leuchtdiode am Anschluss 1 im Sekundentakt blinken.
"""
from microbit import *

def update():
    pin1.write_digital(True)
    sleep(500)
    pin1.write_digital(False)
    sleep(500)

while True:
    update()
