# digitale Ein-/Ausgabe
---

::: warning
Die Anschlüsse 5 und 11 sind fix mit den Tasten A und B verbunden. Sie dürfen nur verwendet werden, um eine externe Taste anzuschliessen.
:::

Der micro:bit hat 17 Anschlüsse (*pins*), mit welchen digitale Ein- und Ausgabe möglich ist. Die Anschlüsse 0 bis 2, 8, 12 und 16 können immer verwendet werden. Die Anschlüsse 13 bis 15 sind für den SPI-Bus vorgesehen. 19 und 20 sind für den I2C-Bus reserviert. Diese Anschlüsse können verwendet werden, wenn nicht gleichzeitig der entsprechende Bus benötigt wird.

| Variable | Funktion    | Variable | Funktion | Variable | Funktion |
| --------:|:----------- | --------:|:-------- | --------:|:-------- |
|   `pin0` | Touch-Taste |  `pin13` | SPI MOSI |   `pin3` | Display  |
|   `pin1` | Touch-Taste |  `pin14` | SPI MISO |   `pin4` | Display  |
|   `pin2` | Touch-Taste |  `pin15` | SPI SCK  |   `pin6` | Display  |
|   `pin8` |             |  `pin19` | I2C SCL  |   `pin7` | Display  |
|  `pin12` |             |  `pin20` | I2C SDA  |   `pin9` | Display  |
|  `pin16` |             |          |          |  `pin10` | Display  |

## Konflikt mit Display

Die Anschlüsse 3, 4, 6, 7, 9 und 10 werden vom Display des micro:bit verwendet. Damit sie für die digitale Ein- oder Ausgabe verwendet werden können, muss erst das Display ausgeschaltet werden:

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

``` python ./blink.py
```

## Touch-Tasten

Die Anschlüsse 0, 1 und 2 können als Touch-Taste verwendet werden. Bei diesen Anschlüssen steht zusätzlich folgender Befehl zu Verfügung:

~~~ python
pin.is_touched()
~~~
liefert `True` zurück, falls der Anschluss zur Zeit berührt wird. Ansonsten wird `False` zurückgeliefert.
