# Zeitmessung
---

Für Zeitmessung kann die MicroPython-Bibliothek `utime` verwendet werden. Dazu muss sie importiert werden:

``` python
import utime
```

## Zeit

~~~ python
zeit = utime.localtime()
~~~
liefert die aktuelle Zeit des Mikrocontrollers im Format `(jahr, monat, tag, stunde, minute, sekunde, wochentag, 0))` zurück.


## Warten

Eine übliches Problem ist das Warten, bis eine bestimmte Zeitspanne verstrichen ist. Für diese Aufgabe gibt es zwei unterschiedliche Ansätze.

### Blockierendes Warten

Der erste Ansatz nennt **blockierendes Warten** und ist sehr einfach zu programmieren.

~~~ python
utime.sleep(s)
~~~
hält die Ausführung des Programms während `s` Sekunden an.

``` python python/blink.py
```

Das führt aber dazu, dass während der Wartezeit keine anderen Anweisungen abgearbeitet werden, das Programm **blockiert**. Für ein interaktives System, welches kontinuierlich auf Ereignisse reagieren muss, kann dieser Ansatz nicht verwendet werden.

## Nicht-blockierendes Warten

Bei einem interaktiven System muss sichergestellt werden, dass die Hauptschleife des Programms nie durch längere Aktionen unterbrochen wird. Das Unterprogramm `utime.sleep()` darf also nicht verwendet werden.

Um ein **nicht-blockierendes Warten** zu programmieren, muss eine genaue Möglichkeit der Zeitmessung verwendet werden.

### Ticks

Um die verstrichene Zeit zu messen, werden sogenannte *Ticks* verwendet. Sie zeigen die verstrichene Zeit seit dem letzten Reset des Mikrocontrollers an. Sie sind aber beschränkt, d.h. die Zählung beginnt nach einem bestimmten Intervall wieder von vorne.

Aus diesem Grund dürfen *Ticks* nicht mit den normalen Operationen addiert und subtrahiert werden. Es müssen die unten vorgestellten Funktionen verwendet werden, welche die Beschränktheit der *Ticks* mit berücksichtigen.

~~~ python
utime.ticks_ms()
~~~
liefert die *Ticks* in Millisekunden zurück.

~~~ python
utime.ticks_add(ticks, delta)
~~~
addiert `delta` Millisekunden zu `ticks`. Dabei wird berücksichtigt, dass die *Ticks* ein Limit haben.

~~~ python
utime.ticks_diff(ticks1, ticks2)
~~~
bildet die Differenz zwischen `ticks1` und `ticks2`. Dabei wird berücksichtigt, dass die *Ticks* ein Limit haben.

### Prinzip «Wecker»

Mit den vorgestellten Funktionen kann ein nicht-blockierendes Warten programmiert werden, indem ein «Wecker» programmiert wird. Er besteht aus den folgenden drei Schritten:

1. **Wecker stellen:** Am Anfang der Wartezeit wird der Wecker gestellt. Dazu wird zu der aktuellen «Zeit» in *Ticks* die gewünschte Wartezeit addiert. Die resultierende Weckzeit wird in einer Variable gespeichert.

2. **Weckzeit überprüfen:** Bei jedem Durchlauf der Hauptschleife wird überprüft, ob die Weckzeit erreicht wurde. Dies ist der Fall, wenn die Differenz zwischen aktueller «Zeit» und Weckzeit grösser als Null ist.

3. **Wecker abstellen:** Wenn die Weckzeit erreicht wurde, wird die gewünscht Aktion ausgeführt. Damit die Aktion nicht immer wieder ausgeführt wird, wird der Wecker «abgestellt», indem die Weckzeit auf einen negativen Wert gestellt wird. Bei der Überprüfung muss dies berücksichtigt werden.

``` python python/delay_nonblocking.py
```

Nicht-blockierendes Warten kann auch für regelmässige wiederkehrende Aktionen verwendet werden:

``` python python/blink_nonblocking.py
```
