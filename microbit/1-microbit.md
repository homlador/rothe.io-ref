# micro:bit
---

~~~ python
reset()
~~~
Mit dieser Anweisung kann der micro:bit neu gestartet werden. Dies hat den gleichen Effekt wie die Reset-Taste zu drücken.

``` python
from microbit import *

reset()
```

~~~ python
sleep(n)
~~~

Diese Anweisung lässt das Programm `n` Millisekunden warten. Während dieser Zeit werden keine anderen Anweisungen ausgeführt, der micro:bit reagiert nicht auf Ereignisse.

``` python
from microbit import *

sleep(1000)
display.scroll("Hallo")
```

~~~ python
running_time()
~~~

Diese Anweisung liefert die Anzahl Millisekunden zurück, welche seit dem Einschalten oder dem letzten Neustart verstrichen sind.

``` python
from microbit import *

sleep(1000)
display.scroll("Seit " + str(running_time() // 1000) + " Sekunden in Betrieb.")
```

~~~ python
temperature()
~~~

Diese Funktion liefert die aktuelle Temperatur des micro:bit in Grad Celsius zurück.

``` python
display.scroll("Temperatur ist " + str(temperature()) "C.")
```
