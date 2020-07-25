from microbit import *

while True:
    n = compass.get_field_strength()
    display.scroll(str(n//10000), wait=True)