import machine
import scd30
import utime

scl = machine.Pin(22)
sda = machine.Pin(21)

i2c = machine.I2C(-1, scl, sda)

sensor = scd30.EasySCD30(i2c)

utime.sleep_ms(500)

err_count = 0
while True:
    sensor.read()
    if sensor.ready:
        print("C02=", sensor.co2, "ppm", "T=", sensor.temperature, "C", "RL=", sensor.humidity, "%")

