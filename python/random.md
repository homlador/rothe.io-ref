# Zufall
---

Mit dem Modul `random` können Zufallszahlen erzeugt oder zufällig Werte aus Listen ausgewählt werden. Mit der folgenden Anweisung wird das Modul importiert:

``` python
import random
```
## Ganze Zahlen

~~~ python
random.randrange(b)
~~~
liefert eine zufällige ganze Zahl $n$ aus dem Bereich $0 \le n < b$ zurück.

Das folgende Skript simuliert einen Münzwurf:
``` python
import random

n = random.randrange(2)
if n == 0:
    print("Kopf")
else:
    print("Zahl")
```

~~~ python
random.randrange(a, b)
~~~
liefert eine zufällige ganze Zahl $n$ aus dem Bereich $a \le n < b$ zurück.

Das folgende Skript simuliert einen Würfelwurf:

``` python
import random

wuerfel = random.randrange(1, 7)
```

## Reelle Zahlen

~~~ python
random.random()
~~~
liefert eine zufällige Zahl $x$ im Bereich $0 \le x \lt 1$ zurück.

~~~ python
random.uniform(a, b)
~~~
liefert eine **gleichverteilte** Zufallszahl $x$ im Bereich $a \le x < b$ zurück.

Das folgende Skript bestimmt einen Einheitsvektor, der in eine zufällige Richtung zeigt:
``` python
import random
import math

winkel = random.uniform(0, 2 * math.pi)
richtung = (math.cos(angle), math.sin(angle))
```

~~~ python
random.normalvariate(mu, sigma)
~~~
liefert eine **normalverteilte** Zufallszahl mit Mittelwert `mu` und Standardabweichung `sigma` zurück.

## Listen

~~~ python
random.choice(list)
~~~
wählt ein zufälliges Element aus einer Liste aus.

Hilfreich, wenn man sich nicht entscheiden kann:
``` python
import random

choices = ["Pizza", "Döner", "Pasta"]
print("Heute mittag gibt es " + random.choice(choices))
```

## Kontrollierter Zufall

Im Modul `random` werden sogenannte **Pseudozufallszahlen** erzeugt. Die erzeugten Zufälle hängen dabei von einer am Anfang bestimmten Ausgangszahl, (engl. *seed*), ab. Der *seed* wird beim Start des Programm zufällig gewählt, kann aber auch durch eine Anweisung bestimmt werden:

~~~ python
random.seed(n)
~~~
Legt die Zahl $n$ als *seed* festgelegt. Bei gleichem *seed* ergeben sich immer die gleichen Zufallszahlen.
