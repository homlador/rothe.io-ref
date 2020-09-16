# Echtzeituhr DS3231
---

![Echtzeituhr DS3231 ©](./ds3231.png)

* [:link: Shop][1]

## Anschluss

| Pin | Bedeutung                   | ESP32 |
| --- | --------------------------- | -----:|
| VCC | Stromversorgung             |    3V |
| GND | Masse                       |   GND |
| SCL | I<sup>2</sup>C Taktleitung  |    22 |
| SDA | I<sup>2</sup>C Datenleitung |    21 |

## MicroPython

Um die Echtzeituhr verwenden zu können muss der folgende Treiber für MicroPython auf dem Mikrocontroller installiert werden:

* [:download: DS3231-Treiber für MicroPython](./ds3231.py)

[1]: https://www.bastelgarage.ch/rtc-ds3231-zeitmodul-mit-at24c32-eeprom-speicher-32k

Der Treiber muss im Python-Programm importiert werden:

``` python
import ds3231
```
Nun kann die Echtzeituhr wie folgt verwendet werden:

~~~ python
uhr = ds3231.DS3231(i2c)
~~~
erstellt ein Objekt, um mit der Echtzeituhr zu kommunizieren.

~~~ python
zeit = uhr.get_time()
~~~
liest die aktuelle Zeit aus im Format `(jahr, monat, tag, wochentag, stunde, minute, sekunde)`.

~~~ python
uhr.set_time(zeit)
~~~
setzt die Zeit der Echtzeituhr im Format `(jahr, monat, tag, wochentag, stunde, minute, sekunde)`.

Die Wochentage sind wie folgt definiert:

| Zahl | Wochentag  |
| ---- | ---------- |
| 1    | Montag     |
| 2    | Dienstag   |
| 3    | Mittwoch   |
| 4    | Donnerstag |
| 5    | Freitag    |
| 6    | Samstag    |
| 7    | Sonntag    |

## Vollständiges Beispiel

``` python ./ds3231_sample.py
```
