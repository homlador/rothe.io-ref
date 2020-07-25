# Name
---

Namen sind Bezeichnungen für Programmelemente wie **Variablen** und **Funktionen**. Ein Name besteht aus einem oder mehreren Wörtern. Wenn der Name aus mehr als einem Wort besteht, werden die Wörter mit einem Unterstrich `_` verbunden. Ausserdem kann einem Namen eine Zahl angehängt werden. Hier sind einige Beispiele für Namen:

- `WIDTH`
- `q`
- `x1`
- `draw`
- `player1_score`
- `ball_speed_x`

In Python ist die Gross- und Kleinschreibung wichtig:  `width`, `WIDTH` und `Width` sind drei unterschiedliche Namen! In Python unterscheiden wir drei Varianten von Gross- und Kleinschreibung. Im Normalfall wird alles klein geschrieben. Bei Namen von Konstanten werden alle Buchstaben gross geschrieben. Bei speziellen, von Python vordefinierten Werten wird der erste Buchstabe gross geschrieben.

| Regel                      | Anwendung           | Beispiele                    |
| -------------------------- | ------------------- | ---------------------------- |
| **alles klein**            | Normallfall         | `draw`, `x`, `player1_score` |
| **alles gross**            | Konstanten          | `WIDTH`                      |
| **erster Buchstabe gross** | vordefinierte Werte | `False`, `None`              |


Dabei sollten für Variablen und Funktionen nur Kleinbuchstaben, für Konstanten nur Grossbuchstaben verwendet werden. Der Unterstrich `_` wird für bessere Lesbarkeit zwischen Wörtern eingesetzt:

### Verbotene Namen

Bestimmte Wörter haben eine spezielle Bedeutung in Python. Diese sogenannten **Schlüsselwörter** können nicht als Namen verwendet werden. Hier ist eine Übersicht aller Schlüsselwörter von Python:

|          |            |           |            |          |
|:-------- |:---------- |:--------- |:---------- |:-------- |
| `False`  | `class`    | `finally` | `is`       | `return` |
| `None`   | `continue` | `for`     | `lambda`   | `try`    |
| `True`   | `def`      | `from`    | `nonlocal` | `while`  |
| `and`    | `del`      | `global`  | `not`      | `with`   |
| `as`     | `elif`     | `if`      | `or`       | `yield`  |
| `assert` | `else`     | `import`  | `pass`     |          |
| `break`  | `except`   | `in`      | `raise`    |          |

In Python sind einige Funktionen vordefiniert. Wenn eine Variable mit dem selben Namen definiert wird, so wird die Funktion überschrieben und ist nicht mehr verfügbar. Deshalb sollten diese Namen ebenfalls nicht verwendet werden:

|               |             |              |            |                |
|:------------- |:----------- |:------------ |:---------- |:-------------- |
| `abs`         | `dict`      | `help`       | `min`      | `setattr`      |
| `all`         | `dir`       | `hex`        | `next`     | `slice`        |
| `any`         | `divmod`    | `id`         | `object`   | `sorted`       |
| `ascii`       | `enumerate` | `input`      | `oct`      | `staticmethod` |
| `bin`         | `eval`      | `int`        | `open`     | `str`          |
| `bool`        | `exec`      | `isinstance` | `ord`      | `sum`          |
| `bytearray`   | `filter`    | `issubclass` | `pow`      | `super`        |
| `bytes`       | `float`     | `iter`       | `print`    | `tuple`        |
| `callable`    | `format`    | `len`        | `property` | `type`         |
| `chr`         | `frozenset` | `list`       | `range`    | `vars`         |
| `classmethod` | `getattr`   | `locals`     | `repr`     | `zip`          |
| `compile`     | `globals`   | `map`        | `reversed` | `__import__`   |
| `complex`     | `hasattr`   | `max`        | `round`    |                |
| `delattr`     | `hash`      | `memoryview` | `set`      |                |
