# Kommentar
---

Kommentare sind Teile eines Programms, welche nicht ausgeführt werden. Sie dienen als zusätzliche Erläuterung des Programms für Menschen. Kommentare können auch genutzt werden, um einzelne Anweisungen kurzzeitig zu deaktivieren.

In Python gibt es zwei Möglichkeiten, Kommentare zu schreiben:

## Einzeiliger Kommentar

Ein einzeiliger Kommentar wird mit einem Hashtag-Zeichen `#` eingeleitet. Alles, was auf der gleichen Zeile folgt, wird als Kommentar interpretiert. So kann zu einer Zeile eine Anmerkung geschrieben werden:

``` python
print("Hallo Welt") # gibt einen Text aus
```

Man kann damit auch Befehle **auskommentieren**, damit sie nicht ausgeführt werden. Das ist hilfreich, wenn man Fehler im Programm suchen will:

``` python
# print("Hallo Welt")
```

## Mehrzeiliger Kommentar

Ein mehrzeiliger Kommentar wird mit drei doppelten Anführungszeichen `"""` eingeleitet. Da er über das Ende der Zeile hinausgeht, muss auch sein Ende gekennzeichnet sein. Dies macht man mit weiteren drei doppelten Anführungszeichen.

Wir verwenden immer den folgenden dreizeiligen Kommentar zu Beginn jeder Python-Datei. So können wir später auf einen Blick erkennen, wer wann was programmiert hat.

``` python
"""
Gibt den Text "Hallo Welt" aus.
Autor: Stefan Rothe (ros)
Datum: 20.11.2019
"""

print("Hallo Welt")
```
