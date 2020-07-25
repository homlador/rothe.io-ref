# Magnetometer
---

Der micro:bit enthält ein Magnetometer oder Kompass, welches die magnetische Feldstärke misst. Vor dem Gebrauch sollte der Kompass kalibriert werden, sonst sind die Messungen möglicherweise falsch.

micro:bit misst die magnetische Flussdichte in milliardstel Tesla (nT). Einige typische Werte sind in folgender Tabelle zusammengefasst:

| Beispiel                               | magnetische Flussdichte |
|:-------------------------------------- | -----------------------:|
| Erdmagnetfeld Minimum[^1]              |               20'000 nT |
| Erdmagnetfeld Maximum[^1]              |               60'000 nT |
| Grenzwert für 50 Hz-Haushaltsstrom[^2] |              100'000 nT |
| 1 cm Abstand von einem 100 A-Strom[^2] |            2'000'000 nT |
| handelsüblicher Hufeisenmagnet[^2]     |          100'000'000 nT |

~~~ python
compass.calibrate()
~~~
startet den Kalibrierungsprozess. Auf dem Display wird eine Nachricht angezeigt. Anschliessend muss der micro:bit gedreht werden, um einen Kreis auf dem Display zu zeichnen.

~~~ python
compass.is_calibrated()
~~~
überprüft, ob der Kompass erfolgreich kalibriert worden ist.

~~~ python
compass.clear_calibration()
~~~
löscht die Kalibrierung des Kompasses.

~~~ python
compass.get_x()
~~~
liefert die gemessene Magnetfeldstärke in nT in Richtung der x-Achse zurück.

~~~ python
compass.get_y()
~~~
liefert die gemessene Magnetfeldstärke in nT in Richtung der y-Achse zurück.

~~~ python
compass.get_z()
~~~
liefert die gemessene Magnetfeldstärke in nT in Richtung der z-Achse zurück.

~~~ python
compass.heading()
~~~
liefert die aktuelle Himmelsrichtung in Grad zurück. `0` bedeutet Norden, `90` Osten, `180` Süden und `270` Westen.

~~~ python
compass.get_field_strength()
~~~
liefert den Betrag der gemessenen magnetischen Flussdichte in nT zurück.

[^1]: Wikipedia: [Erdmagnetfeld](https://de.wikipedia.org/wiki/Erdmagnetfeld)
[^2]: Wikipedia: [Tesla (Einheit)](https://de.wikipedia.org/wiki/Tesla_(Einheit))
