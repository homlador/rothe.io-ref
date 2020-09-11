# MicroPython - Digitale Ein- und Ausgabe
---

Um I/O-Pins ansprechen zu können, muss die MicroPython-Bibliothek `machine` eingebunden werden:

``` python
import machine
```

~~~ python
pin = machine.Pin(id, mode, pull)
~~~
erzeugt ein Objekt, welche den Pin mit der angegebenen `id` repräsentiert. Mit `mode` wird der Betriebsmodus des Pins festgelegt, mit `pull` der interne Pull-Widerstand.

Für `mode` können folgende Werte angegeben werden:

| `mode`                   | Bedeutung                                              |
|:------------------------ |:------------------------------------------------------ |
| `machine.Pin.IN`         | Der Pin wird für die Einlesen verwendet.               |
| `machine.Pin.OUT`        | Der Pin wird für die Ausgabe verwendet.                |
| `machine.Pin.OPEN_DRAIN` | Der Pin wird für die Open-Collector-Ausgabe verwendet. |

Für `pull` können folgende Werte angegeben werden:

| `pull`                  | Bedeutung                                     |
|:----------------------- |:--------------------------------------------- |
| `None`                  | Es wird kein Pull-Widerstand konfiguriert.    |
| `machine.Pin.PULL_UP`   | Es wird ein Pullup-Widerstand konfiguriert.   |
| `machine.Pin.PULL_DOWN` | Es wird ein Pulldown-Widerstand konfiguriert. |

Beispielsweise wird mit folgender Anweisung der Pin 5 für die Ausgabe konfiguriert:
``` python
led = machine.Pin(5, machine.Pin.OUT)
```

~~~ python
pin.value()
~~~
liefert den aktuellen Wert des Eingabe-Pins `pin` zurück.

~~~ python
pin.value(val)
~~~
schaltet den Ausgabe-Pin `pin` ein oder aus. Wenn `val` den Wert `True` hat, wird der Pin eingeschaltet, wenn er den Wert `False` hat wird er eingeschaltet.

## Beispiel

Das folgende Beispiel lässt eine Leuchtdiode blinken:

``` python ./blink.py
```
