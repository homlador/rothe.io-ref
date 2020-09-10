# Bilder
---

Mit `Image` werden Bilder definiert, welche auf dem Display angezeigt werden können. Die folgenden vordefinierten Bilder sind vorhanden:

|                  |                       |                        |
|:---------------- |:--------------------- |:---------------------- |
| `Image.CLOCK1`   | `Image.HEART`         | `Image.RABBIT`         |
| `Image.CLOCK2`   | `Image.HEART_SMALL`   | `Image.COW`            |
| `Image.CLOCK3`   | `Image.HAPPY`         | `Image.MUSIC_CROTCHET` |
| `Image.CLOCK4`   | `Image.SMILE`         | `Image.MUSIC_QUAVER`   |
| `Image.CLOCK5`   | `Image.SAD`           | `Image.MUSIC_QUAVERS`  |
| `Image.CLOCK6`   | `Image.CONFUSED`      | `Image.PITCHFORK`      |
| `Image.CLOCK7`   | `Image.ANGRY`         | `Image.PACMAN`         |
| `Image.CLOCK8`   | `Image.ASLEEP`        | `Image.TARGET`         |
| `Image.CLOCK9`   | `Image.SURPRISED`     | `Image.TSHIRT`         |
| `Image.CLOCK10`  | `Image.SILLY`         | `Image.ROLLERSKATE`    |
| `Image.CLOCK11`  | `Image.FABULOUS`      | `Image.DUCK`           |
| `Image.CLOCK12`  | `Image.MEH`           | `Image.HOUSE`          |
| `Image.ARROW_N`  | `Image.YES`           | `Image.TORTOISE`       |
| `Image.ARROW_NE` | `Image.NO`            | `Image.BUTTERFLY`      |
| `Image.ARROW_E`  | `Image.TRIANGLE`      | `Image.STICKFIGURE`    |
| `Image.ARROW_SE` | `Image.TRIANGLE_LEFT` | `Image.GHOST`          |
| `Image.ARROW_S`  | `Image.CHESSBOARD`    | `Image.SWORD`          |
| `Image.ARROW_SW` | `Image.DIAMOND`       | `Image.GIRAFFE`        |
| `Image.ARROW_W`  | `Image.DIAMOND_SMALL` | `Image.SKULL`          |
| `Image.ARROW_NW` | `Image.SQUARE`        | `Image.UMBRELLA`       |
| `Image.XMAS`     | `Image.SQUARE_SMALL`  | `Image.SNAKE`          |

## Eigene Bilder erstellen

~~~ python
microbit.Image(text)
~~~
erstellt ein `Image` aus der Zeichenkette `text`. Dabei besteht die Zeichenkette aus den Ziffern `0` bis `9`, welche die Helligkeit für je ein Pixel angeben. Die Ziffern werden zeilenweise von oben nach unten in der Zeichenkette angegeben. Die einzelnen Zeilen werden durch einen Doppelpunkt `:` getrennt.

Das folgende Beispiel zeigt ein X auf dem Display an:
``` python
from microbit import *

bild = Image("90009:09090:00900:09090:90009")
display.show(bild)
```

~~~ python
bild = microbit.Image(width, height)
~~~
erstellt ein `Image`, welches `width` Pixel breit und `height` Pixel hoch ist.

~~~ python
bild.width()
~~~
liefert die Breite des Bildes in Pixel zurück.

~~~ python
bild.height()
~~~
liefert die Höhe des Bildes in Pixel zurück.

## Pixel manipulieren

Mit den folgenden Anweisungen können einzelne Pixel eines Bildes manipuliert werden.

~~~ python
bild.fill(helligkeit)
~~~
setzt jedes Pixel im Bild auf die angegebene Helligkeit. Für `helligkeit` wird eine Zahl zwischen `0` (dunkel) und `9` (hell) angegeben.

~~~ python
bild.set_pixel(x, y, helligkeit)
~~~
legt die Helligkeit des Pixels an den Koordinaten `x` und `y` des Bildes fest. Für `helligkeit` wird eine Zahl zwischen `0` (dunkel) und `9` (hell) angegeben.

~~~ python
bild.get_pixel(x, y)
~~~
liefert die aktuelle Helligkeit des Pixels an den Koordinaten `x` und `y` des Bildes zurück. Der zurückgelieferte Wert liegt zwischen `0` (dunkel) und `9` (hell).

## Abgeänderte Bilder erstellen

Mit den folgenden Anweisungen können abgeänderte Kopien von Bildern erstellt werden.

~~~ python
bild.copy()
~~~
liefert eine Kopie von `bild` zurück.

~~~ python
bild.invert()
~~~
liefert eine invertierte Kopie von `bild` zurück.

~~~ python
bild.shift_left(n)
~~~
liefert eine Kopie von `bild` zurück, wobei das Bild um `n` Pixel nach links verschoben ist.

~~~ python
bild.shift_right(n)
~~~
liefert eine Kopie von `bild` zurück, wobei das Bild um `n` Pixel nach rechts verschoben ist.

~~~ python
bild.shift_up(n)
~~~
liefert eine Kopie von `bild` zurück, wobei das Bild um `n` Pixel nach oben verschoben ist.

~~~ python
bild.shift_down(n)
~~~
liefert eine Kopie von `bild` zurück, wobei das Bild um `n` Pixel nach unten verschoben ist.

~~~ python
bild.crop(x, y, w, h)
~~~
liefert eine Kopie von `bild` zurück, wobei die Kopie nur `w` Pixel breit und `h` Pixel hoch ist. Das Pixel an der Koordinate `x`, `y` wird zum Pixel oben links in der Kopie.

~~~ python
bild1 + bild2
~~~
liefert ein neues Bild zurück, wobei die Helligkeit von jedem Pixel von `bild1` und `bild2` addiert wird.

~~~ python
bild * n
~~~
liefert eine Kopie von `bild` zurück, wobei die Helligkeit von jedem Pixel mit `n` multipliziert wird.
