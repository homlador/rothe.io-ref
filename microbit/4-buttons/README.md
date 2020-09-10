# Tasten
---

Die beiden Tasten des micro:bit werden in Programmen durch je eine Variable dargestellt:

| Variable   | Bedeutung    |
|:---------- |:------------ |
| `button_a` | linke Taste  |
| `button_b` | rechte Taste |


~~~ python
button.is_pressed()
~~~
überprüft, ob die Taste `button` zur Zeit gedrückt wird.

``` python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.YES)
    else:
        display.show(Image.NO)
```


~~~ python
button.was_pressed()
~~~
überprüft, ob die Taste seit dem letzten Aufruf gedrückt worden ist.

``` python
from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll('Hello', wait=True)
```


~~~ python
button.get_presses()
~~~
zählt, wie oft die Taste seit dem letzten Aufruf gedrückt worden ist.

``` python
from microbit import *

while True:
    c = button_a.get_presses()
    display.scroll(str(c) + ' presses', wait=True)
```
