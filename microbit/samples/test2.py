from microbit import *
import radio

radio.on()
while True:
    radio.send('TEST')
    sleep(1000)