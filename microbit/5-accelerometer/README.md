# Beschleunigungssensor
---

Der micro:bit enthält einen Beschleunigungssensor, wie er auch in den meisten Smartphones verbaut ist. Damit kann einerseits die Beschleunigung in Richtung der drei Achsen gemessen werden. Andererseits verwendet der micro:bit den Beschleunigungssensor, um folgende Gesten zu erkennen:

| Geste         | Bedeutung                                       |
|:------------- |:----------------------------------------------- |
| `'up'`        | Die Seite mit dem USB-Stecker zeigt nach oben.  |
| `'down'`      | Die Seite mit dem USB-Stecker zeigt nach unten. |
| `'left'`      | Die linke Seite zeigt nach unten.               |
| `'right'`     | Die rechte Seite zeigt nach unten.              |
| `'face up'`   | Das Display zeigt nach oben.                    |
| `'face down'` | Das Disaply zeigt nach unten.                   |
| `'freefall'`  | Der micro:bit fällt.                            |
| `'3g'`        | Die Beschleunigung beträgt mindestens 3g.       |
| `'6g'`        | Die Beschleunigung beträgt mindestens 6g.       |
| `'8g'`        | Die Beschleunigung beträgt mindestens 8g.       |
| `'shake'`     | Der micro:bit wird geschüttelt.                 |

micro:bit misst die Beschleunigung in tausendstel g-Kraft. Ein g entspricht 9.81 Newton. Ein gemessener Wert von 1 entspricht somit 0.00981 Newton.

~~~ python
accelerometer.get_x()
~~~
liefert die aktuelle Beschleunigung in tausendstel g-Kraft in Richtung der x-Achse zurück.

~~~ python
accelerometer.get_y()
~~~
liefert die aktuelle Beschleunigung in tausendstel g-Kraft in Richtung der y-Achse zurück.

~~~ python
accelerometer.get_z()
~~~
liefert die aktuelle Beschleunigung in tausendstel g-Kraft in Richtung der z-Achse zurück.

~~~ python
accelerometer.get_values()
~~~
liefert die aktuelle Beschleunigung als Vektor zurück.

~~~ python
accelerometer.current_gesture()
~~~
liefert die neueste Geste des micro:bit zurück.


``` python
from microbit import *

while True:
    print(accelerometer.current_gesture())
```

~~~ python
accelerometer.is_gesture(name)
~~~
überprüft, ob die für `name` angegebene Geste zur Zeit aktiv ist.

~~~ python
accelerometer.was_gesture(name)
~~~
überprüft, ob die für `name` angegebene Geste seit dem letzten Aufruf der Funktion aktiv war.

~~~ python
accelerometer.get_gestures()
~~~
liefert eine Liste aller Gesten zurück, die seit dem letzten Aufruf der Funktion aktiv waren.

## Beispiel 1

``` python ./accelerometer_test.py
```

## Beispiel 2 - Schrittzähler

``` python ./pedometer.py
```
