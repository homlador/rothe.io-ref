# Zeichenketten
---

Text als *Wert* wird in Programmiersprachen normalerweise als **Zeichenkette** (engl. *string*) bezeichnet.

## Darstellung

Um in Python einen Text als Wert zu verwenden, wird dieser Text in einfache oder doppelte Anführungszeichen gesetzt:

``` python
a = "Dies ist ein Text."
print("Hallo, wie geht's.")
```

Dabei dürfen innerhalb der Anführungszeichen keine weiteren Anführungszeichen des gleichen Typs vorkommen. Zeilenumbrüche und andere spezeielle Zeichen sind ebenfalls nicht erlaubt. Um diese Restriktion zu umgehen, können sogenannte **Escape-Sequenzen** verwendet werden. Die untenstehende Tabelle listet die wichtigsten Escape-Sequenzen auf.

| Escape-Sequenz | Zeichen | Bedeutung                   |
| -------------- | ------- | --------------------------- |
| `\\`           | `\`     | Rückstrich                  |
| `\'`           | `'`     | einfaches Anführungszeichen |
| `\"`           | `"`     | doppeltes Anführungszeichen |
| `\n`           |         | Zeilenumbruch               |

 Beispielsweise wird der Text

```
A: Hallo, wie geht's?
B: Gut, und dir?
```

so als Zeichenkette codiert:

``` python
"A: Hallo, wie geht's?\nB: Gut, und dir?"
```

## Operationen mit Zeichenketten

Zwei Zeichenketten können zusammengehängt werden, indem ein `+`-Zeichen dazwischen platziert wird:

``` python
name = "Ford"
query = "Hallo " + name + ", wie geht's?"
```

Mit dem sogenannten Index-Operator `[i]` kann auf einen Teil einer Zeichenkette zugegriffen werden. Der Operator liefert das Zeichen an der Position `i` zurück. In den Klammern muss eine ganze Zahl `i` stehen. Die Position des ersten Zeichens ist 0. Wird eine negative Zahl als Index angegeben, so wird diese Zahl erst von der Länge der Zeichenkette subtrahiert und das Ergebnis als Index verwendet.

``` python
a = "Python"

s = a[0]    # s: "P"
t = a[1]    # t: "y"
u = a[5]    # u: "n"
v = a[-6]   # v: "P"
w = a[-1]   # w: "n"
```

Im Index-Operator kann mit der Form `[a:b]` auch ein Bereich angegeben werden. In diesem Falll wird die Teilzeichenkette zurückgeliefert, welche mit dem `a`-ten Zeichen beginnt und mit dem `b-1`-ten Zeichen endet. Die Zahlen `a` und `b` können auch negativ sein oder ganz weggelassen werden. Ein fehlender Anfangsindex wird durch 0 ersetzt, ein fehlender Endindex durch die Länge der Zeichenkette.

``` python
a = "Python"

s = a[0:3]   # s: "Pyt"
t = a[2:]    # t: "thon"
u = a[:4]    # u: "Pyth"
v = a[1:-1]  # v: "ytho"
```

## Ist eine Zeichenkette in einer anderen Zeichenkette enthalten?

~~~ python
t in s
~~~
überprüft, ob `t` in `s` vorkommt.

``` python
s = "Hallo Welt"
t = "all"
if t in s:
  print("'" + t + "' ist in '" + s + "' enthalten.")
else:
  print("'" + t + "' ist nicht in '" + s + "' enthalten.")
```

~~~ python
s.find(t)
~~~
liefert die erste Position zurück, an welcher `t` in `s` vorkommt. Liefert `-1` zurück, falls `t` nicht in `s` vorkommt.

## Eingebaute Funktionen für Zeichenketten

~~~ python
len(s)
~~~
liefert die Länge der Zeichenkette `s` zurück.

~~~ python
str(x)
~~~
erzeugt eine Zeichenkette aus einem beliebigen Wert, beispielsweise einer Zahl.

``` python
name = "Ford"
say = "Der Name " + name + " besteht aus " + str(len(name)) + " Buchstaben."
```

~~~ python
chr(u)
~~~
liefert das Zeichen zurück, welches die Unicode-ID `u` hat. Das folgende Skript gibt «Preise in €» aus:
``` python
print("Preise in " + chr(8364))
```

~~~ python
ord(c)
~~~
liefert die Unicode-ID des Zeichens `c` zurück.

## Objektfunktionen für Zeichenketten

Zeichenketten-Werte stellen weitere Funktionen zu Verfügung:

~~~ python
s.count(t)
~~~
liefert Anzahl Vorkommen von `t` in `s` zurück.

~~~ python
s.endswith(t)
~~~
überprüft, ob die Zeichenkette `s` mit `t` endet.

~~~ python
s.isalpha()
~~~
überprüft, ob die Zeichenkette ausschliesslich aus Buchstaben besteht.

~~~ python
s.isdecimal()
~~~
überprüft, ob die Zeichenkette ausschliesslich aus Dezimalziffern besteht.

~~~ python
s.islower()
~~~
überprüft, ob die Zeichenkette ausschliesslich aus Kleinbuchstaben besteht.

~~~ python
s.isupper()
~~~
überprüft, ob die Zeichenkette ausschliesslich aus Grossbuchstaben besteht.

~~~ python
s.lower()
~~~
liefert eine Kopie von `s` zurück, bei welcher alle grosse durch kleine Buchstaben ersetzt werden.

~~~ python
s.replace(old, new)
~~~
ersetzt alle Vorkommen von `old` in `s` durch `new`.

~~~ python
s.upper()
~~~
liefert eine Kopie von `s` zurück, bei welcher alle kleine durch grosse Buchstaben ersetzt werden.

~~~ python
s.split(sep)
~~~
teilt die Zeichenkette `s` mit dem Trenner `sep` auf. Es wird eine Liste der Teil-Zeichenketten zurückgeliefert.

``` python
namen = "Anna,Barbara,Claire"
namenliste = namen.split(",")   # namenliste: ["Anna", "Barbara", "Claire"]
```

~~~ python
sep.join(list)
~~~
fügt die Liste von Zeichenketten `list` mit dem Trenner `sep` zusammen. Die Funktion liefert die resultierende Zeichenkette zurück.

``` python
namenliste = ["Anna", "Barbara", "Claire"]
namen = ",".join(namenliste)   # namen: "Anna,Barbara,Claire"
```
