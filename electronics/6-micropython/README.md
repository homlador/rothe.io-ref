# MicroPython
---

MicroPython ist eine spezielle Python-Variante für Mikrocontroller.

* [:link: Offizielle Webseite von MicroPython][1]
* [:link: MicroPython-Referenz][2]
* [:link: Python-Referenz](?book=python-ref)

## Startvorgang

Wenn der Mikrocontroller eingeschaltet wird, werden nacheinander zwei Python-Skripts ausgeführt:

1. **boot.py:** Dieses Skript initialisiert MicroPython. Es sollte nicht verändert  oder gelöscht werden.
2. **main.py:** Anschliessend wird dieses Skript ausgeführt. Hier kann eigener Code platziert werden, den man gerne ausführen möchte.

### REPL

REPL (von engl. *read, evaluate, print, loop*) ist eine interaktive Python-Konsole. Sie liest eine Eingabezeile ein, führt die Zeile als Python-Befehl aus und gibt das Resultat aus.

[1]: https://micropython.org/
[2]: http://docs.micropython.org/en/latest/index.html
