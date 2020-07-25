# Spickzettel
---

::: columns 2

## Variablen und Zahlen

Einer Variable einen Wert zuweisen:
``` python
x = 2
```

Inhalt einer Variable verändern
``` python
x = x + 1
```

Grundrechenoperationen

|                      |          |
| -------------------- | --------:|
| Addition             |  `a + b` |
| Subtraktion          |  `a - b` |
| Multiplikation       |  `a * b` |
| Division             |  `a / b` |
| Potenz               | `a ** b` |
| ganzzahlige Division | `a // b` |
| Modulo               |  `a % b` |

Betrag mit `abs`:
``` python
x = abs(-5)
```

Maxiumum und Minimum mit `max` und `min`:
``` python
a = max(-10, 0, 5, 7)
b = min(-10, 0, 5, 7)
```

In Zahl umwandeln mit `int` und `float`
``` python
pi = float("3.141")
x = int(pi)
y = int("123")
```

## Unterprogramme

Unterprogramm definieren und aufrufen
``` python
def sag_hallo():
    print("Hallo")

sag_hallo()
```

Parameter übergeben
``` python
def sag_hallo(name):
    print("Hallo, " + name)

sag_hallo("Elisabeth")
```

Rückgabewerte (Funktionen)
``` python
def addiere(a, b):
    return a + b

sum = addiere(3, 5)
print(sum)
```

## Bedingungen
|                         |          |
|:----------------------- | --------:|
| kleiner als             |  `a < b` |
| kleiner als oder gleich | `a <= b` |
| grösser als             |  `a > b` |
| grösser als oder gleich | `a >= b` |
| gleich                  | `a == b` |
| nicht gleich            | `a != b` |
| sowohl – als auch       |    `and` |
| entweder – oder         |     `or` |


Bedingte Ausführung einer Anweisung
``` python
if alter >= 18:
    print("Das kannst abstimmen.")
```

Wahrheitswerte zuweisen
``` python
ist_student = True
game_over = False
```

Alternativen
``` python
if alter < 6:
    preis = 0
elif alter < 18 or ist_student:
    preis = 10
else:
    preis = 15
```

Bedingte Wiederholung
``` python
i = 0
while i < 10:
    print(i ** 2)
    i = i + 1
```

## Mathematik

Mit Modul `math`
``` python
import math
```

Pi und Eulersche Zahl
``` python
math.pi
math.e
```

natürlicher Exponent $e^x$
``` python
math.exp(x)
```

natürlicher Logarithmus $\ln(e)$
``` python
math.log(x)
```

allgemeiner Logarithmus $\log_b(e)$
``` python
math.log(x, b)
```

Winkelfunktionen, `x` in Radiant
``` python
math.sin(x)
math.cos(x)
math.tan(x)
```

Winkelfunktionen, `x` in Grad
``` python
math.sin(math.radians(x))
math.cos(math.radians(x))
math.tan(math.radians(x))
```

***
## Listen

Liste erstellen
``` python
tiere = ["Katze", "Hund", "Maus"]
```

erstes Element in der Liste
``` python
erstes_tier = tiere[0]
```

letztes Element in der Liste
``` python
letztes_tier = tiere[-1]
```

Elemente an Liste anfügen mit `append`
``` python
tiere = []
tiere.append("Katze")
tiere.append("Hund")
tiere.append("Maus")
```

Elemente zählen mit `len`
``` python
anzahl = len(tiere)
```

Liste leeren:
``` python
tiere.clear()
```

Prüfen, ob Liste Wert enthält
``` python
if "Katze" in tiere:
    print("Katze vorhanden")
```

Schleife mit allen Elementen einer Liste
``` python
for x in tiere:
    print(x)
```

## Text

``` python
print("Hallo Welt")
```

Zusammensetzen mit `+`
``` python
vorname = "Ada"
nachname = "Lovelace"
name = vorname + ' ' + nachname
```

in Liste von Wörtern zerlegen mit `split`
``` python
worte = satz.split(" ")
```

In Text umwandeln mit `str`,
``` python
alter = 23
print("Alter: " + str(alter))
```

Zeichen in Text suchen mit `find`
``` python
i = text.find("A")
if i == -1:
    print("Kein A vorhanden")
else:
    print("A an Position", i)
```

Länge ermitteln mit `len`
``` python
if len(text) > 100:
    print("Text ist zu lang.")
```

Schleife mit allen Zeichen eines Texts
``` python
for c in text:
    print(c)
```

## Dictionary

Dictionary erstellen
``` python
beine = { "Katze": 4, "Vogel": 2 }
```

Auf Werte zugreifen
``` python
n = beine["Katze"]
print("Katze hat", n, "Beine")
```

Neuen Wert hinzufügen:
``` python
beine["Fisch"] = 0
```

Alle Einträge:
```python
for tier, n in beine:
    print(tier, "hat", n, "Beine")
```

## Dateien lesen

Textdatei öffnen mit `open`
``` python
file = open(name, encoding="utf-8")
```

Datei zeilenweise lesen
``` python
for line in file:
    print(line)
```

Datei schliessen mit `close`
``` python
file.close()
```
