# Wahrheitswerte
---

Eine Aussage wie «Die Sonne scheint» ist entweder **wahr** oder **falsch**. In der Sprache der Logik und Mathematik sagt man, dass der Aussage ein **Wahrheitswert** zugeordnet wird.

In der Informatik spricht man auch von **booleschen Werten** (engl. *Boolean values* nach dem Mathematiker George Boole). Das Rechnen mit boolschen Werten spielt in der Informatik eine zentrale Rolle beim Design von Computerchips sowie bei der Codierung von Informationen.

In Python heissen die zwei Wahrheitswerte
- `True` (wahr) und
- `False` (falsch).

Beim Programmieren werden Wahrheitswerte vor allem für die Steuerung des Programmflusses eingesetzt. Wahrheitswerte entstehen
- durch den **Vergleich** von Werten, z.B. «Der Wert der Variable `x` ist grösser als 5»,
- durch die **Kombination** von Wahrheitswerten, z.B. «die Taste «W» ist gedrückt **und** `vx` ist kleiner als 10» oder
- indem ein anderer Wert, zB. eine Zahl von Python automatisch als Wahrheitswert interpretiert wird.

## Vergleiche

In Python können Werte auf folgende Arten verglichen werden:

| Vergleich               | Mathematisch | Python   |
|:----------------------- |:------------ |:-------- |
| kleiner als             | $a < b$      | `a < b`  |
| kleiner als oder gleich | $a \leq b$   | `a <= b` |
| grösser als             | $a > b$      | `a > b`  |
| grösser als oder gleich | $a \geq b$   | `a >= b` |
| gleich                  | $a = b$      | `a == b` |
| nicht gleich            | $a \neq b$   | `a != b` |

::: box warning
#### :warning: Gleichheit und Zuweisung
Die Gleichheit wird durch zwei aufeinanderfolgende Gleichheitszeichen `==` dargestellt. Ein einzelnes Gleichheitszeichen `=` wird für die Zuweisung eines Werts an eine Variable verwendet.
:::

Die folgende Anweisung bestimmt den Wahrheitswert der Aussage «Der Wert der Variable `x` ist grösser als 5» und speichert den Wahrheitswert in der Variable `q`.

``` python
q = x > 5
```

::: box warning
#### :warning: Gleichheit bei Gleitkommazahlen

Beim Vergleichen von Gleitkommazahlen ist zu beachten, dass sich diese nicht wie rationale Zahlen verhalten. Beispielsweise ist die Summe von `0.1` und `0.2` nicht gleich `0.3`. Deshalb sollten Gleitkommazahlen nie auf (Un-)Gleichheit getestet werden. Anstelle von $a = b$ überprüft man, ob $|a - b|$ sehr klein ist:

``` python
q = 0.1 + 0.2 == 0.3               # t: False
r = abs(0.1 + 0.2 - 0.3) < 1e-10   # u: True
```
:::

Mit diesen Operationen kann auch Text verglichen werden. Dabei werden die Zeichen beider Texte von links nach rechts verglichen. Für den Vergleich einzelner Zeichen wird deren Position in Unicode verwendet.

``` python
q = "Lovelace" > "Babbage"   # q: True
r = "A" == "a"               # r: False
s = "iu" < "äuä"             # s: True
t = "Simon" < "Simone"       # t: True
```

## Operationen mit Wahrheitswerten

Wahrheitswerte können mit **boolschen Operationen** verknüpft werden. Python kennt die boolschen Operationen «Und», «Oder» und «Nicht».

| Operation | Fachbegriff | Mathematisch | Python    |
|:--------- |:----------- |:------------ |:--------- |
| Oder      | Disjunktion | $q\lor r$    | `q or r`  |
| Und       | Konjunktion | $q\land r$   | `q and r` |
| Nicht     | Negation    | $\lnot q$    | `not q`   |

### Und

Der Ausdruck `q and r` ist genau dann `True`, wenn beide Werte `True` sind.

|   `q`   |   `r`   | `q and r` |
|:-------:|:-------:|:---------:|
| `False` | `False` |  `False`  |
| `False` | `True`  |  `False`  |
| `True`  | `False` |  `False`  |
| `True`  | `True`  |  `True`   |

### Oder

Der Ausdruck `q or r` ist genau dann `True`, wenn mindestens einer der Werte `True` ist.

|   `q`   |   `r`   | `q or r` |
|:-------:|:-------:|:--------:|
| `False` | `False` | `False`  |
| `False` | `True`  |  `True`  |
| `True`  | `False` |  `True`  |
| `True`  | `True`  |  `True`  |

### Nicht

Der Ausdruck `not q` ist genau dann `True`, wenn `q` den Wert `False` hat.

|   `q`   | `not q` |
|:-------:|:-------:|
| `False` | `True`  |
| `True`  | `False` |

## Automatische Wahrheitswerte

Python ordnet jedem beliebigen Wert automatisch ein Wahrheitswert zu. Dabei erhalten die folgenden Werte den Wahrheitswert <code class="python">False</code>:

- `None`
- `False`
- Die Zahl Null von jedem Zahlentyp, beispielsweise `0` (Typ `int`), `0.0` (Typ `float`), `0j` (Typ `complex`)
- Eine leere Sequenz, beispielsweise die leere Zeichenkette `""`, das leere Tupel `()` oder die leere Liste `[]`.
- Eine leere Menge `{}`.

Allen anderen Werten wird der Wahrheitswert `True` zugeordnet.
