# Textdateien
---

## Datei öffnen und schliessen

~~~ python
with open(filename, mode="r", encoding="utf-8") as file:
~~~
öffnet die Textdatei mit dem Dateinamen `filename` und führt die folgenden, eingerückten Anweisungen mit dem Datei-Objekt `file` aus. Mit `mode=` wird festgelegt, wie auf die Textdatei zugegriffen werden soll:

| Mode | Bedeutung                                                               |
|:---- |:----------------------------------------------------------------------- |
| `r`  | Datei wird gelesen (Standardeinstellung)                                |
| `w`  | Datei wird neu erstellt oder überschrieben                              |
| `x`  | Datei wird neu erstellt, eine bestehende Datei aber nicht überschrieben |
| `a`  | Daten werden an die Datei angehängt                                     |
| `b`  | Zugriff auf eine binäre Datei                                           |

Mit `encoding=` wird die Zeichencodierung der Textdatei angegeben. Diese Angabe sollte unbedingt vorhanden sein, da das Standardverhalten je nach Betriebssystem unterschiedlich ist.

## Datei lesen

~~~ python
file.read()
~~~
liest den ganzen Inhalt einer geöffneten Datei und liefert ihn zurück.
``` python
with open("test.txt", encoding="utf-8") as file:
    content = file.read()
```

~~~ python
for line in file:
~~~
liest eine Textdatei zeilenweise.
``` python
with open("test.txt", encoding="utf-8") as file:
    for line in file:
        print(line)
```

## Datei schreiben

~~~ python
file.write(text)
~~~
schreibt `text` in die geöffnete Datei `file`.

``` python
with open("test.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello\nWorld")
```
