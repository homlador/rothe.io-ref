# Joystick
---

![](images/joystick.png)

* [:link: Shop][1]

[1]: https://www.bastelgarage.ch/5-weg-mikro-joystick-breakout

## Anschluss


## MicroPython

Die Anschlüsse des Joysticks werden als digitale Eingänge angesteuert.

### Dauerreaktion auf Tastendruck

``` python
import machine

while True:
    up_current = up_pin.value()
    if up_pin.value():
        # do something
```


### Einmalige Reaktion auf Tastendruck

``` python
import machine
up_pin = machine.Pin(34, machine.Pin.IN)

up_current = False
up_last = False

while True:
    up_current = up_pin.value()
    if up_current and not up_last:
        # do something
    up_last = up_current
```
