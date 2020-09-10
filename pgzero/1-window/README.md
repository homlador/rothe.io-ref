# Fenster

## Fenster definieren

~~~ python
TITLE
~~~
legt den Fenstertitel fest.

~~~ python
WIDTH
~~~
legt die Breite des Fensters in Pixel fest.

~~~ python
HEIGHT
~~~
legt die Höhe des Fensters in Pixel fest.

``` python ./window.py
```

## Fenster verwenden

Diese Anweisungen dürfen **nur** in einem Unterprogramm verwendet werden.

~~~ python
screen.width
~~~
liefert die Breite des aktuellen Fensters in Pixel zurück.

~~~ python
screen.height
~~~
liefert die Höhe des aktuellen Fensters in Pixel zurück.

~~~ python
screen.clear()
~~~
füllt das Fenster mit der Farbe Schwarz.

~~~ python
screen.fill(farbe)
~~~
füllt das Fenster mit der angegebenen Farbe. `farbe` muss ein RGB-Tupel sein.

## Fenster schliessen

~~~ python
quit()
~~~
schliesst das Fenster.
