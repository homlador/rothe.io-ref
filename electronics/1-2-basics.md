# Grundlagen Elektronik
---

## Stromkreis

In einem Stromkreis fliesst Strom von einer Anode zu einer Kathode. Gemäss dem **Ohmschen Gesetz** stehen die Spannung $U$, der Widerstand $R$ und der Strom $I$ in folgendem Verhältnis zueinander:

$$U = R\cdot I$$

| Formelzeichen | Grösse     | Einheit |
|:------------- |:---------- |:------- |
| $U$           | Spannung   | Volt    |
| $R$           | Widerstand | Ohm     |
| $I$           | Strom      | Ampère  |

![](images/circuit.svg "Ein einfacher Stromkreis")

::: box warning
:warning: Die technische Stromrichtung ist der Bewegungsrichtung der Elektronen entgegengesetzt. In der Technik fliesst der Strom vom Plus- zum Minuspol.
:::

## Spannungsquelle

Die Spannungsquelle versorgt die Schaltung mit einer möglichst konstanten Spannung. Bei elektronischen Geräten ist dies meist ein Akku oder ein USB-Anschluss. In einem Schaltplan wird die Spannungsquelle durch dieses Symbol dargestellt:

![](images/voltage-source-symbol.svg)

## Masse (GND)

Der negative Pol der Spannungsquelle wird als Masse oder GND (engl. *ground*) bezeichnet. Der dient als Bezugspunkt für **Spannungsmessungen**. Ein Teil des Stromkreises, welcher direkt mit der Masse verbunden ist, hat also immer eine Spannung 0 Volt.

## Widerstand

Ein Widerstand ist ein elektronisches Bauteil, welches einen klar definierten ohmschen Widerstand in Schaltungen realisiert. In einem Schaltplan wird ein Widerstand durch folgendes Symbol dargestellt:

![](images/resistor-symbol.svg)

Der Widerstandswert in Ohm wird durch die Farbringe gekennzeichnet.
Jeder Farbe ist eine Zahl zwischen -2 und 9 zugeordnet.

![](images/resistor-color-codes.svg "Farbcodierung des Widerstandswerts")

## Leuchtdiode

Eine Leuchtdiode (engl. *light emitting diode, LED*) erzeugt Licht, wenn Strom hindurchfliesst. Der Strom kann nur in einer Richtung durch eine Diode fliessen, von **Anode** zu **Kathode**. In einem Schaltplan wird eine Leuchtdiode durch folgendes Symbol dargestellt:

![](images/led-symbol.svg)


Eine «normale» rote Leuchtdiode benötigt eine Spannung von 1.6 V und kann einen maximalen Strom von 20 mA verkraften.

![Leuchtdiode](images/led.png)


## Vorwiderstand

Um den Strom klein zu halten, muss eine Schaltung mit einer Leuchtdiode durch einen Widerstand ergänzt werden.

![Stromkreis mit Leuchtdiode und Vorwiderstand](images/circuit-led.svg)

 Der benötigte Widerstand berechnet sich so:

$$R_V = \frac{U_V}{I} = \frac{U - U_L}{I}$$

| Formelzeichen | Bedeutung                     |
|:------------- |:----------------------------- |
| $R_V$         | Widerstand                    |
| $U_V$         | Spannung über dem Widerstand  |
| $I$           | Strom                         |
| $U$           | Gesamtspannung                |
| $U_L$         | Spannung über der Leuchtdiode |

::: task Aufgabe – Einfache Schaltung mit Leuchtdiode
1. Berechne den benötigten Vorwiderstand für eine rote Leuchtdiode (20 mA, 1.6 V) bei einer 3.3&nbsp;V- sowie bei einer 5&nbsp;V-Spannungsquelle.
2. Vergleiche Deine Lösung mit der Musterlösung.
3. Bringe eine Leuchtdiode zum Leuchten, indem Du den obenstehenden Schaltkreis realisierst.
---

Der Vorwiderstand muss bei 3.3 V mindestens 77 Ohm betragen.

Bei 5 V muss der Vorwiderstand mindestens 170 Ohm betragen.
:::
