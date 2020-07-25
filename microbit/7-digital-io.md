# digitale Ein-/Ausgabe
---

::: box warning
Die Anschlüsse 5 und 11 sind fix mit den Tasten A und B verbunden. Sie dürfen nur verwendet werden, um eine externe Taste anzuschliessen.
:::

Der micro:bit hat 17 Anschlüsse (*pins*), mit welchen analoge Ein- und Ausgabe möglich ist:

| Variable | Typ     | zusätzliche Funktion |
|:-------- | ------- | --------------------:|
| `pin0`   | Touch   |          Touch-Taste |
| `pin1`   | Touch   |          Touch-Taste |
| `pin2`   | Touch   |          Touch-Taste |
| `pin3`   | Analog  |              Display |
| `pin4`   | Analog  |              Display |
| `pin6`   | Digital |              Display |
| `pin7`   | Digital |              Display |
| `pin8`   | Digital |                      |
| `pin9`   | Digital |              Display |
| `pin10`  | Analog  |              Display |
| `pin12`  | Digital |                      |
| `pin13`  | Digital |             SPI MOSI |
| `pin14`  | Digital |             SPI MISO |
| `pin15`  | Digital |              SPI SCK |
| `pin16`  | Digital |                      |
| `pin19`  | Digital |              I2C SCL |
| `pin20`  | Digital |              I2C SDA |

## Voraussetzung

Die Anschlüsse 3, 4, 6, 7, 9 und 10 werden vom Display des micro:bit verwendet. Damit sie für die analoge Ein- oder Ausgabe verwendet werden können, muss erst das Display ausgeschaltet werden:

``` python
from microbit import *

display.off()
```

## Eingabe

~~~ python
pin.read_digital()
~~~
überprüft, welche Spannung am Anschluss anliegt. Liefert `0` zurück, wenn keine Spannung anliegt und `1`, wenn eine hohe Spannung anliegt.

## Ausgabe

~~~ python
pin.write_digital(value)
~~~
schaltet den Anschluss ein oder aus. Der Anschluss wird eingeschaltet, wenn `value` den Wert `1` hat und ausgeschaltet, wenn `value` den Wert `0` hat.

``` python samples/blink.py
```

## Touch-Tasten

Die Anschlüsse 0, 1 und 2 können als Touch-Taste verwendet werden. Bei diesen Anschlüssen steht zusätzlich folgender Befehl zu Verfügung:

~~~ python
pin.is_touched()
~~~
liefert `True` zurück, falls der Anschluss zur Zeit berührt wird. Ansonsten wird `False` zurückgeliefert.
