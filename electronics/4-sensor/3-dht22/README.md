# DHT22 Temperatursensor
---

Der DHT22 ist ein digitaler Temperatur- und Feuchtigkeitssensor.


![DHT22 Sensor ©](./dht22.svg)

* [:link: Shop][1]

## Anschluss

| Pin  | Bedeutung                   |
| ---- | --------------------------- |
| VCC  | Stromversorgung 3.3 bis 6 V |
| DATA | Datenleitung                |
| GND  | Masse                       |

## Messbereich

| Messwert     | Bereich        | Genauigkeit                     |
| ------------ | -------------- | ------------------------------- |
| Feuchtigkeit | 0 bis 100 % RH | ±2.0 % RH bei 60 % RH und 25 °C |
| Temperatur   | -40 bis 80 °C  | ±0.5 °C                         |

## MicroPython

In MicroPython kann das Modul `dht` verwendet werden, um mit dem Sensor zu kommunizieren. Ausserdem wird das Modul `machine` benötigt, um auf die Pins zuzugreifen:

``` python
import dht
import machine
```

~~~ python
sensor = dht.DHT22(machine.Pin(pin))
~~~
erzeugt ein Objekt, welches den DHT-Sensor repräsentiert. Die Datenleitung des Sensors muss mit dem Pin `pin` des Mikrocontrollers verbunden werden.

~~~ python
sensor.measure()
~~~
führt eine Messung mit dem Sensor durch. Der Sensor darf maximal alle zwei Sekunden abgefragt werden.

~~~ python
sensor.temperature()
~~~
liefert die zuletzt gemessene Temperatur in °C zurück.

~~~ python
sensor.humidity()
~~~
liefert die zuletzt gemessene relative Feuchtigkeit in Prozent zurück.

Vollständiges Beispiel:

``` python
import dht
import machine
import time

sensor = dht.DHT22(machine.Pin(5))

anzahl_messungen = 3

for messung in range(anzahl_messungen):
    sensor.measure() # eine Messung ausloesen
    tempC=sensor.temperature() # die Temperatur diser Messung
    rhum=sensor.humidity() # die relative Luftfeuchtigkeit dieseer Messung
    print("Messung Nr.", messung, "Temp (in Grad Celsius):", tempC, "rHum (in Prozent):", rhum)
    time.sleep_ms(2000) # sleep time in msec
```

[1]: https://www.play-zone.ch/de/digitaler-feuchtigkeits-und-temperatur-sensor-dht11-4659.html
