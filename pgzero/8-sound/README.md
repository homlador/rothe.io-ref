# Musik und Soundeffekte
---

## Soundeffekte

Soundeffekte müssen im Format `WAV` oder `OGG` im Unterordner `sound` abgespeichert werden.

~~~ python
sounds.name.play()
~~~
spielt den Soundeffekt mit dem Name `name` ab.

Um beispielsweise den Soundeffekt `extraleben.wav` abzuspielen, schreibt man:
``` python
sounds.extraleben.play()
```

## Musik

Musikdateien müssen im Format `MP3` oder `OGG` im Unterordner `music` abgelegt werden. Um die Datei `hintergrundmusik.mp3` abzuspielen, schreibt man:

``` python
music.play("hintergrundmusik")
```

~~~ python
music.play(name)
~~~
spielt die Musikdatei mit dem Namen `name` ab. Das Abspielen wird endlos wiederholt.

~~~ python
music.play_once(name)
~~~
spielt die Musikdatei mit dem Namen `name` ab. Die Musikdatei wird nur einmal abgespielt.

~~~ python
music.queue(name)
~~~
fügt die Musikdatei mit dem Namen `name` in die Abspielliste ein.

~~~ python
music.stop()
~~~
stoppt das Abspielen der Musik.

~~~ python
music.pause()
~~~
pausiert das Abspielen der Musik.

~~~ python
music.unpause()
~~~
nimmt das Abspielen der Musik nach einer Pause wieder auf.

~~~ python
music.is_playing()
~~~
überprüft, ob zur Zeit Musik abgespielt wird.
