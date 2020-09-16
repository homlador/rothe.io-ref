# SPI
---

Der Serial Peripheral Interface (SPI) ist ein serieller Datenbus, mit welchem Displays, Sensoren und andere spezialisierte Chips mit einem Mikrocontroller verbunden werden können.

![](./spi.svg "Einfacher SPI-Bus")

Der SPI-Bus verwendet folgende drei Leitungen:

| Leitung | Bedeutung                                             | ESP32 1 | ESP32 2 |
|:------- |:----------------------------------------------------- | -------:| -------:|
| SCK     | Taktleitung (engl. *serial clock*)                    |      14 |      18 |
| MOSI    | ausgehende Datenleitung (engl. *master out slave in*) |      13 |      23 |
| MISO    | eingehende Datenleitung (engl. *master in slave out*) |      12 |      19 |

ESP32-Mikrocontroller verfügen über zwei SPI-Busse mit den IDs 1 und 2. Die verwendeten Pins sind in der Tabelle oben ersichtlich.

Jedes angeschlossene Gerät muss zusätzlich über eine Auswahlleitung (engl. *chip select*) angebunden werden. Über diese Leitung aktiviert der Mikrocontroller die Kommunikation mit diesem Gerät.

Um den SPI-Bus verwenden zu können, muss die MicroPython-Bibliothek `machine` eingebunden werden:

``` python
import machine
```

~~~ python
spi = machine.SPI(id, sck=sck, mosi=mosi, miso=miso)
~~~
erzeugt ein Objekt, welches den SPI-Bus repräsentiert. `sck`, `mosi` und `miso` sind die entsprechenden Pins und müssen unbedingt angegeben werden.

## Vollständige Beispiele

Der SPI-Bus 1 wird so initialisiert:
``` python
import machine

sck = machine.Pin(14)
mosi = machine.Pin(13)
miso = machine.Pin(12)
spi = machine.SPI(1, sck=sck, mosi=mosi, miso=miso)
```

Der SPI-Bus 2 wird so initialisiert:
``` python
import machine

sck = machine.Pin(18)
mosi = machine.Pin(23)
miso = machine.Pin(19)
spi = machine.SPI(2, sck=sck, mosi=mosi, miso=miso)
```
