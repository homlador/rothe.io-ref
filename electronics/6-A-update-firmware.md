# Firmware-Update
---

Gehe folgendermassen vor, um die neueste Version von MicroPython auf einem ESP32-Mikrocontroller zu installieren:

1. Neueste Version von MicroPython herunterladen:

* [:link: MicroPython Downloads][1]

2. esptool installieren:

   ```
   pip3 install esptool
   ```

3. Port bestimmen:


4. Update starten:

   ```
   esptool.py --chip esp32 --port [Port] write_flash -z 0x1000 [Datei]
   ```

   Dabei muss **[Port]** durch den in Schritt 3 bestimmten Port ersetzt werden und **[Datei]** durch den Namen der in Schritt 1 heruntergeladenen Datei.

[1]: https://micropython.org/download#esp32
