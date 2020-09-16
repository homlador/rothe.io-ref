import machine
import scd30
import utime

#scl = machine.Pin(22)
#sda = machine.Pin(21)

scl = machine.Pin(5)
sda = machine.Pin(4)
i2c = machine.I2C(-1, scl, sda)

try:
    sensor = scd30.SCD30(i2c, 97)
except scd30.SCD30.NotFoundException:
    print("Sensor not found")


utime.sleep_ms(500)
sensor.set_measurement_interval(2)
utime.sleep_ms(500)
sensor.start_continous_measurement()
utime.sleep_ms(500)
sensor.soft_reset()
utime.sleep_ms(500)

print("firmware version =", sensor.get_firmware_version())
print("measurement interval =", sensor.get_measurement_interval())
print("automatic recalibration =", sensor.get_automatic_recalibration())
utime.sleep_ms(500)

err_count = 0
while True:
    try:
        ready = sensor.get_status_ready() == 1
    except:
        err_count += 1
        ready = False
        print("Error " + str(err_count))
    if ready:
        co2, temp, hum = sensor.read_measurement()
        print("C02=", co2, "ppm", "T=", temp, "C", "RL=", hum, "%")

