# I2C
---

I<sup>2</sup>C (sprich: I-quadrat-C) ist ein serieller Datenbus, mit welchem Sensoren und andere spezialisierte Chips mit einem Mikrocontroller verbunden werden können.

Der I<sup>2</sup>C-Bus verwendet zwei Leitungen:

| Leitung | Bedeutung                          | ESP32 |
|:------- |:---------------------------------- | -----:|
| SDA     | Datenleitung (engl. *serial data*) |    21 |
| SCL     | Taktleitung (engl. *serial clock*) |    22 |


Um den I<sup>2</sup>C-Bus verwenden zu können, muss die MicroPython-Bibliothek `machine` eingebunden werden:

``` python
import machine
```

~~~ python
i2c = machine.I2C(-1, scl, sda)
~~~
erzeugt ein Objekt, welches den I<sup>2</sup>C-Bus repräsentiert. Mit `scl` wird der SCL-Pin festgelegt, mit `sda` der SDA-Pin.

Auf einem ESP32-Board hat der SCL-Pin die Nummer 22 und SDA die Nummer 21. Somit wird folgender Code benötigt, um auf diesem Board einen I<sup>2</sup>C-Bus zu benutzen:

## Vollständiges Beispiel

``` python
import machine

scl = machine.Pin(22)
sda = machine.Pin(21)
i2c = machine.I2C(-1, scl, sda)
```

## Scanner

``` python ./i2c_scanner.py
```
