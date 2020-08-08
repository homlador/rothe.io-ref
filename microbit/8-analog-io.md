# analoge Ein-/Ausgabe
---

Der micro:bit hat sechs Anschlüsse (*pins*), mit welchen analoge Ein- und Ausgabe möglich ist. Die Anschlüsse 0 bis 2 können immer verwendet werden.

| Variable | Funktion | Variable | Funktion |
| --------:|:-------- | --------:|:-------- |
|   `pin0` | Touch    |   `pin3` | Display  |
|   `pin1` | Touch    |   `pin4` | Display  |
|   `pin2` | Touch    |  `pin10` | Display  |

## Konflikt mit Display

Die Anschlüsse 3, 4 und 10 werden vom Display des micro:bit verwendet. Damit sie für die analoge Ein- oder Ausgabe verwendet werden können, muss erst das Display ausgeschaltet werden:

``` python
from microbit import *

display.off()
```

## Eingabe

~~~ python
pin.read_analog()
~~~
liest die aktuelle Spannung am Anschluss aus. Der Rückgabewert ist eine ganze Zahl, die zwischen `0` (0 V) und `1023` (3.3 V) liegt.

## Ausgabe

~~~ python
pin.write_analog(value)
~~~
gibt ein pulsweitenmoduliertes Signal auf dem Anschluss aus. Der Tastgrad wird durch `value` festgelegt. Ein Wert von `0` entspricht einem Tastgrad von 0%, ein Wert von `1023` einem Tastgrad von 100%.

~~~ python
pin.set_analog_period(period)
~~~
legt die Periodendauer `period` im Millisekunden für das pulsweitenmodulierte Signal fest. Die kleinste mögliche Wert ist `1`.

~~~ python
pin.set_analog_period_microseconds(period)
~~~
legt die Periodendauer `period` im Mikrosekunden für das pulsweitenmodulierte Signal fest. Die kleinste mögliche Wert ist `256`.
