# Analoge Eingabe
---

Mit einem Analog-Digital-Umsetzer (engl. *ADC, analog-to-digital converter*) kann die vorhandene Spannung an einem Anschluss in eine ganze Zahl umgewandelt werden.

Auf dem Lolin D32 stehen dazu die Anschlüsse 32, 33 und 34 zu Verfügung.

Wie üblich muss zuerst die Bibliothek `machine` eingebunden werden:
``` python
import machine
```

Der gewünschte Anschluss wird mit `machine.Pin` festgelegt:
``` python
pin = machine.Pin(32)
```

Nun kann mit `machine.ADC` ein Analog-Digital-Umsetzer für diesen Anschluss definiert werden:

``` python
adc = machine.ADC(pin)
```

Der Analog-Digital-Umsetzer gibt es zwei Konfigurationsmöglichkeiten. Einerseits kann der Spannungsbereich festgelegt werden, andererseits der Wertebereich.

~~~ python
adc.atten(attenuation)
~~~
legt den Spannungsbereich für den Analog-Digital-Umsetzer fest. Für `attenuation` kann eine der folgenden Konstanten eingesetzt werden:

| Konstante                | Spannungsbereich |
|:------------------------ | ----------------:|
| `machine.ADC.ATTN_0DB`   |        0 bis 1 V |
| `machine.ADC.ATTN_2_5DB` |     0 bis 1.34 V |
| `machine.ADC.ATTN_6DB`   |        0 bis 2 V |
| `machine.ADC.ATTN_11DB`  |      0 bis 3.6 V |

~~~ python
adc.width(width)
~~~
legt den Wertebereich für den Analog-Digital-Umsetzer fest. Für `width` kann eine der folgenden Konstanten eingesetzt werden:

| Konstante                 | Wertebereich |
|:------------------------- | ------------:|
| `machine.ADC.WIDTH_9BIT`  |    0 bis 511 |
| `machine.ADC.WIDTH_10BIT` |   0 bis 1023 |
| `machine.ADC.WIDTH_11BIT` |   0 bis 2047 |
| `machine.ADC.WIDTH_12BIT` |   0 bis 4095 |

~~~ python
adc.read()
~~~
liest die aktuelle Spannung am Anschluss und liefert einen entsprechenden Wert zurück.

## Beispiel
``` python
import machine
import utime

pin = machine.Pin(32)
adc = machine.ADC(pin)
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_12BIT)
while True:
    value = adc.read()
    print(value)
    utime.sleep(0.1)
```
