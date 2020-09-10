# Firmware-Update
---

## Firmware-Version überprüfen

Um die Firmware-Version zu überprüfen, muss der micro:bit via USB mit einem Computer verbunden werden. Am Computer meldet sich der micro:bit als Laufwerk mit dem Namen _MICROBIT_ an. Es enthält die Datei _DETAILS.TXT_, die so aussieht:

```
# DAPLink Firmware - see https://mbed.com/daplink Unique ID: 9900000031634e4500624014000000320000000097969901
HIC ID: 97969901
Auto Reset: 1
Automation allowed: 0
Overflow detection: 0
Daplink Mode: Interface
Interface Version: 0250
Git SHA: 682d8303e37355532402b8d93c4f240a3cec02a9
Local Mods: 0
USB Interfaces: MSD, CDC, HID, WebUSB
Interface CRC: 0x3f2b7e12
Remount count: 0URL: https://microbit.org/device/?id=9900&v=0250
```

Der Eintrag _Interface Version_ bezeichnet die Versionsnummer der Firmware.

## Firmware herunterladen

Die neueste Firmware kann direkt hier herunterladen werden:

* [:download: micro:bit-Firmware Version 253](./0253_kl26z_microbit_0x8000.hex)

Die offizielle Download-Seite für die micro:bit-Firmware ist hier:

* [:link: micro:bit Firmware](https://microbit.org/get-started/user-guide/firmware/)

## Firmware installieren

Um die Firmware zu aktualisieren, muss der micro:bit im *maintenance mode* am Computer angeschlossen werden. Dazu drückt man die _Reset_-Taste, währen man den micro:bit per USB am Computer anschliessen. Im *maintenance mode* erscheint der micro:bit als Laufwerk mit dem Namen _MAINTENANCE_.

Die Firmaware wird installiert, indem die entsprechende Datei in das _MAINTENANCE_-Laufwerk kopiert wird.
