from microbit import *

def showCount():
    display.scroll(str(count), delay=150, wait=False, loop=True)

count = 0
showCount()
while True:
    if accelerometer.was_gesture('shake'):
        count = count + 1
        showCount()
    if button_a.was_pressed():
        count = 0
        showCount()
