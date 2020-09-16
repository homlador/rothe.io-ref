import machine
import ds3231
import utime

# Zugriff auf I2C-Bus
scl = machine.Pin(22)
sda = machine.Pin(21)
i2c = machine.I2C(-1, scl, sda)

# Zugriff auf Echtzeituhr
uhr = ds3231.DS3231(i2c)

zeit = (2020, 4, 29, 3, 11, 58, 30)
uhr.set_time(zeit)

WOCHENTAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

# Zeit aus der Echtzeituhr auslesen
while True:
    zeit = uhr.get_time()
    datum = WOCHENTAGE[zeit[3] - 1] + ", "
    datum = datum + str(zeit[2]) + "." + str(zeit[1]) + "." + str(zeit[0])
    uhrzeit = str(zeit[4]) + ":" + str(zeit[5]) + ":" + str(zeit[6])
    print(datum, uhrzeit)
    utime.sleep(1)
