from microbit import *

while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        display.show(Image.HEART)
    else:
        pin0.write_digital(0)
        display.clear()
    if pin1.read_digital() == 1:
        display.show(Image.HEART)
    else:
        display.clear()