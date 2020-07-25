# Module und Pakete
---

## Was ist ein Modul?

Eine Python-Programmdatei wird als **Modul** bezeichnet. In Python können **globale Definitionen** (z.B. Unterprogramme oder Konstanten) aus einem Modul in anderen Modulen verwendet werden. Dieser Mechanismus wird als **Importieren** von Modulen bezeichnet.

Module können aus drei unterschiedlichen Quellen stammen:

- **Standardmodule** sind bei jeder Installation von Python mit dabei. Ein typisches Beispiel ist das [`math`][1]-Modul.
- **Zusätzliche Module** können durch die Installation von Paketen hinzugefügt werden. Ein Paket stellt häufig mehrere zusätzliche Module zu Verfügung.
- **Eigene Module** können jederzeit durch das Erstellen einer Python-Datei angelegt werden.

Der Import-Mechanismus bildet somit die Grundlage für die Verwendung von Paketen sowie für die **Modularisierung** grosser Programme, also deren Aufteilung in mehrere Module.

## Module verwenden

Mit einer `import`-Anweisung wird ein Modul geladen. Dass heisst, der Programmcode des Moduls wird ausgeführt und die Namen, welche das Modul definiert, werden verfügbar gemacht. Es gibt verschiedene Varianten der `import`-Anweisung, mit welchen man steuern kann, unter welchen Namen die Definitionen des Moduls im aktuellen Programm zu Verfügung stehen.

### Einfacher Import eines Moduls

``` python
import math
math.sqrt(2)
```

Dies ist die einfachste Möglichkeit und empfohlene Möglichkeit, ein Modul zu benutzen. Hier wird das Modul als Objekt in der Variable `math` verfügbar gemacht. Die im Modul definierten Namen stehen als Attribute des Objekts zu Verfügung.

### Import eines Moduls mit Alias

Es besteht auch die Möglichkeit, den Namen der Variable zu wählen, in welcher das Modul zu Verfügung steht. Dazu wird der Anweisung `as` und der gewünschte Name angehängt:

``` python
import math as m
m.sqrt(2)
```

In diesem Fall wird das Modul als Objekt in der Variable `m` verfügbar gemacht.

### Import eines Namens aus einem Modul

Wenn nur ein Name aus einem Modul verwendet wird, bietet sich diese Anweisung an:

``` python
from math import sqrt
sqrt(2)
```

Nach dieser Anweisung steht nur die `sqrt`-Funktion aus dem `math`-Modul, zu Verfügung. Die Funktion wird direkt in der Variable `sqrt` gespeichert.

### Import eines Namens aus einem Modul mit Alias

Auch hier kann mit `as` ein Name für die Variable gewählt werden:

``` python
from math import sqrt as wurzel
wurzel(2)
```

### Import aller Namen aus einem Modul

Python bietet auch die Möglichkeit, sämtliche Namen aus einem Modul zu importieren und diese als Variablen zu Verfügung zu stellen. Diese Anweisung sollte man jedoch **auf keinen Fall verwenden**, da man keine Kontrolle darüber hat, welche Namen im eigenen Programm definiert werden.

``` python
from math import *
sqrt(2)
```

## Standardmodule

In der folgenden Tabelle sind einige wichtige Standardmodule aufgeführt:

| Modul             | Inhalt                                                                          |
|:----------------- |:------------------------------------------------------------------------------- |
| [`math`][1]       | Mathematische Funktionen für Gleitkommazahlen                                   |
| [`cmath`][2]      | Mathematische Funktionen für komplexe Gleitkommazahlen                          |
| [`fractions`][3]  | Rechnen mit rationalen Zahlen                                                   |
| [`random`][4]     | Erzeugung von Pseudo-Zufallszahlen                                              |
| [`statistics`][5] | Statistische Funktionen: Mittelwert, Median, Standardabweichung, Varianz        |
| [`turtle`][6]     | Turtlegrafik                                                                    |
| [`tkinter`][7]    | GUI-Programmierung                                                              |
| [`csv`][8]        | Lesen und Speichern von CSV-Dateien                                             |
| [`os`][9]         | Zugriff auf und Manipulation von Dateien und Verzeichnissen, Umgebungsvariablen |


[1]: https://docs.python.org/3.5/library/math.html
[2]: https://docs.python.org/3.5/library/cmath.html
[3]: https://docs.python.org/3.5/library/fractions.html
[4]: https://docs.python.org/3.5/library/random.html
[5]: https://docs.python.org/3.5/library/statistics.html
[6]: https://docs.python.org/3.5/library/turtle.html
[7]: https://docs.python.org/3/library/tkinter.html
[8]: https://docs.python.org/3.5/library/csv.html
[9]: https://docs.python.org/3.5/library/os.html
