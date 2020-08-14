# Mathematik
---

Das Modul `math` stellt verschiedene mathematische Funktionen zu Verfügung. Es wird mit der folgenden Anweisung importiert:

``` python
import math
```

### Zahlentheorie

~~~ python
math.factorial(n)
~~~
berechnet die Fakultät von `n`.

~~~ python
math.gcd(a, b)
~~~
berechnet den grössten gemeinsamen Teiler von `a` und `b`.

### Potenzen und Logarithmen

~~~ python
math.exp(x)
~~~
berechnet $e^x$.

~~~ python
math.expm1(x)
~~~
berechnet $e^x-1$. Für kleine Werte von `x` ist die Berechnung von `math.exp(x) - 1`  ungenau. Deshalb sollte in diesem Fall die Funktion `math.expm1(x)` eingesetzt werden.

~~~ python
math.log(x, b)
~~~
berechnet $\log_b{x}$. Wenn die Basis weggelassen wird, wird der natürliche Logarithmus von `x` berechnet.

~~~ python
math.log1p(x)
~~~
berechnet $\log_e (x + 1)$. Im Gegensatz zu `math.log(x + 1)` liefert diese Funktion genauere Werte Resultate für Werte nahe bei Null.

~~~ python
math.log10(x)
~~~
berechnet $\log_{10}{x}$ mit grösserer Genauigkeit als `math.log(x, 10)`

~~~ python
math.sqrt(x)
~~~
berechnet die Quadratwurzel von x.

~~~ python
math.hypot(x, y)
~~~
berechnet die Länge der Hypotenuse des rechtwinkligen Dreiecks mit den Katheten `x` und `y`. Die Funktion liefert also $\sqrt{x^2+y^2}$ zurück.

### Winkelfunktionen

**Achtung:** Die Winkelfunktionen rechnen in der Einheit **Radiant**.

~~~ python
math.sin(x)
~~~
liefert den Sinus von `x` zurück.

~~~ python
math.cos(x)
~~~
liefert den Cosinus von `x` zurück.

~~~ python
math.tan(x)
~~~
liefert den Tangens von `x` zurück.

~~~ python
math.asin(x)
~~~
liefert den Sinus von `x` zurück.

~~~ python
math.acos(x)
~~~
liefert den Cosinus von `x` zurück.

~~~ python
math.atan(x)
~~~
liefert den Tangens von `x` zurück.

~~~ python
math.degrees(x)
~~~
konvertiert den Winkel `x` von Radiant nach Grad.

~~~ python
math.radians(x)
~~~
konvertiert den Winkel `x` von Grad nach Radiant.

### Konstanten

~~~ python
math.pi
~~~
ist die Kreiszahl Pi.

~~~ python
math.e
~~~
ist die Eulersche Zahl.
