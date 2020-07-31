# :reference: micro:bit
---

![micro:bit](images/microbit-red-heart.png)


## Python auf dem micro:bit

Um auf Hardware des micro:bit zugreifen zu können, muss erst das Modul `microbit` in das Python-Skript importiert werden. Dies geschieht mit der Anweisung

``` python
from microbit import *
```

Nach dieser Anweisung stehen im Skript die folgenden Objekte zu Verfügung. Sie repräsentieren je ein Teil der Hardware des micro:bit.

| Objekt          | Bedeutung                    | zusätzliche Funktion |
|:--------------- |:---------------------------- | --------------------:|
| `accelerometer` | [Beschleunigungssensor][11]  |                      |
| `button_a`      | [linke Taste][12]            |                      |
| `button_b`      | [rechte Taste][12]           |                      |
| `compass`       | [Magnetometer (Kompass)][13] |                      |
| `display`       | [5x5 LED-Matrix][14]         |                      |
| `pin0`          | [Anschluss 0][15]            |          Touch-Taste |
| `pin1`          | [Anschluss 1][15]            |          Touch-Taste |
| `pin2`          | [Anschluss 2][15]            |          Touch-Taste |
| `pin3`          | [analoger Pin 3][16]         |              Display |
| `pin4`          | [analoger Pin 4][16]         |              Display |
| `pin6`          | [Anschluss 6][15]            |              Display |
| `pin7`          | [Anschluss 7][15]            |              Display |
| `pin8`          | [Anschluss 8][15]            |                      |
| `pin9`          | [Anschluss 9][15]            |              Display |
| `pin10`         | [analoger Pin 10][15]        |              Display |
| `pin12`         | [Anschluss 12][15]           |                      |
| `pin13`         | [Anschluss 13][15]           |             SPI MOSI |
| `pin14`         | [Anschluss 14][15]           |             SPI MISO |
| `pin15`         | [Anschluss 15][15]           |              SPI SCK |
| `pin16`         | [Anschluss 16][15]           |                      |
| `pin19`         | [Anschluss 19][15]           |              I2C SCL |
| `pin20`         | [Anschluss 20][15]           |              I2C SDA |
| `radio`         | [Funk][17]                   |                      |

## Links

* [:link: BCC micro:bit Dokumentation][1]
* [:link: 101 Computing: Projektideen][2]

[1]: https://microbit-micropython.readthedocs.io/en/latest/
[2]: https://www.101computing.net/category/bbc-microbit/

[11]: ?page=5-accelerometer
[12]: ?page=4-buttons
[13]: ?page=6-compass
[14]: ?page=2-display
[15]: ?page=7-digital-io
[16]: ?page=8-analog-io
[17]: ?page=9-radio
