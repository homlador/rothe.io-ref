import machine
import scd30
import utime

scl = machine.Pin(22)
sda = machine.Pin(21)
i2c = machine.I2C(-1, scl, sda)

sensor = scd30.SCD30(i2c, 97, pause=10000)

while True:
    try:
        ready = sensor.get_status_ready() == 1
    except:
        utime.sleep_ms(10)
        print("Error")
        ready = False
    if ready:
        co2, temp, hum = sensor.read_measurement()
        print("C02=", co2, "ppm", "T=", temp, "C", "RL=", hum, "%")
        with open("log.csv", mode="a") as file:
            file.write(str(co2) + ";" + str(temp) + ";" + str(hum) + "\n")
