# WEMOS Lolin D32 Pro
---

Wemos Lolin ESP32 Pro ist ein Mikrocontroller-Board, welches auf dem ESP32-Mikrocontroller basiert. Das Board hat folgende Features:

- Mikro-SD-Kartenleser
- WLAN-Schnittstelle
- Ladelogik für Lithium-Akku
- I<sup>2</sup>C-Schnittstelle
- SPI-Schnittstelle

![](images/wemos-lolin-d32-pro-top.png "WEMOS Lolin D32 Pro Board")

## Pinbelegung

Am Pin 5 ist die eingebaute, blaue Leuchtdiode angeschlossen.

::: box warning
#### Pin 12 nicht benutzen
Am Pin 12 darf nichts angeschlossen werden, sonst bootet der Mikrocontroller nicht mehr.
:::

![](images/wemos-lolin-d32-pro-pinout.png "Pinbelegung des WEMOS Lolin D32 Pro Boards")

## Treiber

Damit der Mikrocontroller von Windows oder macOS aus programmiert werden kann, muss der folgende Treiber installiert werden:

* [:link: CH340 Driver][1]

## Links

* [:link: Herstellerseite][2]
* [:link: Shop][3]


[1]: https://www.wemos.cc/en/latest/ch340_driver.html
[2]: https://www.wemos.cc/en/latest/d32/d32_pro.html
[3]: https://www.bastelgarage.ch/esp8266-esp32/esp-boards/lolin-d32-pro-esp32-board-16mb-flash-8mb-psram
