"""
Beispiel für nicht-blockierendes Warten. Die LED wird
zwei Sekunden nach dem Tastendruck eingeschaltet und sollte
nach einer Sekunde wieder ausgeschaltet werden.
"""
import machine
import utime

led = machine.Pin(5, machine.Pin.OUT)
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

old_button = False
new_button = False
alarm_on = -1
alarm_off = -1
# Alarm, um Button wieder zu aktivieren
alarm_active = -1

led.value(True)
print("start")
while True:
    # Aktuelle Zeit bestimmen
    now = utime.ticks_ms()
    new_button = button.value()
    if old_button == False and new_button == True and alarm_active < 0:
        print("button")
        alarm_on = utime.ticks_add(now, 2000)  # Zeit bis Dropmagnet reagiert
        alarm_active = utime.ticks_add(now, 5000) # Zeit bis Button wieder aktiv
    old_button = new_button

    if alarm_on != -1 and utime.ticks_diff(now, alarm_on) > 0:
        print("on")
        alarm_on = -1
        led.value(False)
        alarm_off = utime.ticks_add(now, 1000)  # Zeit bis Dropmagnet wieder ausschaltet

    if alarm_off != -1 and utime.ticks_diff(now, alarm_off) > 0:
        print("off")
        led.value(True)
        alarm_off = -1

    if alarm_active != and utime.ticks_diff(now, alarm_active) > 0:
        alarm_active = -1

print("done")
