# Operatoren definieren
---

## Arithmetische Operatoren

In Python können spezielle Methoden definiert werden, welche das Verhalten von Operationen wie `a + b` für eigene Klassen definieren. Wenn Python eine solche Operation antrifft und `a` ein Objekt ist, dann wird die Methode `a.__add__(b)` aufgerufen. Ein Beispiel:

``` python
class Tasse:
    # __init__ ...
    def __add__(self, m):
        self.inhalt = self.inhalt + m
        return self

a = Tasse('Jenny', 0.3)
a = a + 0.3
```

Die folgende Tabelle zeigt für alle arithmetischen Operationen die entsprechenden Methoden:

| Beschreibung         | Operation | Methodenaufruf      |
|:-------------------- |:--------- |:------------------- |
| Addition             | `a + b`   | `a.__add__(b)`      |
| Subtraktioon         | `a - b`   | `a.__sub__(b)`      |
| Multiplikation       | `a * b`   | `a.__mul__(b)`      |
| Division             | `a / b`   | `a.__truediv__(b)`  |
| Potenz               | `a ** b`  | `a.__pow__(b)`      |
| ganzzahlige Division | `a // b`  | `a.__floordiv__(b)` |
| Modulo               | `a % b`   | `a.__mod__(b)`      |

Vergleichsoperatoren:

| Beschreibung            | Operation | Methodenaufruf |
|:----------------------- |:--------- |:-------------- |
| gleich gross wie        | `a == b`  | `a.__eq__(b)`  |
| nicht gleich            | `a != b`  | `a.__ne__(b)`  |
| kleiner als             | `a < b`   | `a.__lt__(b)`  |
| kleiner als oder gleich | `a <= b`  | `a.__le__(b)`  |
| grösser als             | `a > b`   | `a.__gt__(b)`  |
| grösser als oder gleich | `a >= b`  | `a.__ge__(b)`  |
