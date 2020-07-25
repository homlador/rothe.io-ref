# Turtle-Grafik
---

Mit dem Standardmodul `turtle` können Turtle-Grafiken gezeichnet werden. Dazu muss das Modul ins Pythonskript eingebunden werden:

``` python
import turtle
```

## Bewegung

~~~ python
turtle.forward(n)
~~~
bewegt die Turtle um `n` Pixel nach vorne.

``` python
import turtle

turtle.forward(100)
```

~~~ python
turtle.left(w)
~~~
dreht die Turtle um `w` Grad nach links.

``` python
import turtle

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
```

~~~ python
turtle.right(w)
~~~
dreht die Turtle um `w` Grad nach rechts.

~~~ python
turtle.goto(x, y)
~~~
bewegt die Turtle zu den Koordinaten (`x`, `y`).

``` python
import turtle

turtle.goto(100, 20)
```

## Richtung

~~~ python
turtle.setheading(w)
~~~
dreht die Turtle so, dass sie in Richtung `w` blickt. Die Winkel sind so festgelegt:

| Richtung | Winkel |
| -------- | ------:|
| Osten    |      0 |
| Norden   |     90 |
| Westen   |    180 |
| Süden    |    270 |

~~~ python
w = turtle.heading()
~~~
weist der Variable `w` die aktuelle Richtung der Turtle zu.

~~~ python
w = turtle.towards(andere_turtle)
~~~
weist der Variable `w` die Richtung zu, in welche die Turtle gehen muss, um zu `andere_turtle` zu kommen.

~~~ python
w = turtle.towards(x, y)
~~~
weist der Variable `w` die Richtung zu, in welche die Turtle gehen muss, um zum Punkt mit den Koordinaten (`x`, `y`) zu kommen.


## Stift

~~~ python
turtle.pendown()
~~~
senkt den Stift der Turtle. Nachfolgende Bewegungen hinterlassen eine Spur.

~~~ python
turtle.penup()
~~~
hebt den Stift der Turtle. Nachfolgende Bewegungen hinterlassen keine Spur.

``` python
import turtle

turtle.penup()
turtle.forard(100)
turtle.pendown()
turtle.forard(100)
```

~~~ python
turtle.pensize(n)
~~~
legt die Dicke der Spur für nachfolgende Bewegungen auf `n` Pixel fest.

~~~ python
turtle.pencolor(r, g, b)
~~~
legt die Farbe der Spur für nachfolgende Bewegungen fest. Dabei sind `r`, `g` und `b` die Rot-, Grün- und Blauanteile der Farbe und müssen zwischen 0 und 1 liegen.

``` python
import turtle

turtle.color(0.5, 0.5, 0)
turtle.pensize(3)
turtle.forard(100)
```

## Füllen

~~~ python
turtle.begin_fill()
~~~
beginnt das Zeichnen einer ausgefüllten Figur.

~~~ python
turtle.end_fill()
~~~
beendet das Zeichnen einer ausgefüllten Figur.

~~~ python
turtle.fillcolor(r, g, b)
~~~
legt die Füllfarbe fest. Dabei sind `r`, `g` und `b` die Rot-, Grün- und Blauanteile der Farbe und müssen zwischen 0 und 1 liegen.

## Geschwindigkeit

~~~ python
turtle.speed(s)
~~~
legt die Geschwindigkeit der Turtle auf `s` fest. Für `s` kann entweder eine Zahl zwischen `0` und `10` oder einer der folgenden Werte angegeben werden:

| Wert        | Geschwindigkeit        | Zahl |
|:----------- | ---------------------- | ----:|
| `"fastest"` | so schnell wie möglich |    0 |
| `"fast"`    | schnell                |   10 |
| `"normal"`  | normal                 |    6 |
| `"slow"`    | langsam                |    3 |
| `"slowest"` | sehr langsam           |    1 |

## Text

~~~ python
turtle.write(text, font=(schrift, groesse))
~~~
gibt den Text `text` an der aktuellen Position der Turtle aus. Mit `schrift` wird die Schriftart und mit `groesse` die Schriftgrösse festgelegt.

``` python
import turtle

turtle.write("Hello World", font=("sans", 16))
```
