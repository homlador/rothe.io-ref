import machine
import neopixel

pin = machine.Pin(4, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 3, timing=1)

np[0] = (255, 0, 0)
np[1] = (0, 255, 0)
np[2] = (0, 0, 255)

np.write()
