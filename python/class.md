# Klassen definieren
---

## Klasse definieren

In Python beginnt die Definition einer Klasse mit `class`, gefolgt vom Namen der Klasse:

``` python
class Tasse:
    def __init__(self):
        print('Neue Tasse erzeugt.')
```

Anschliessend werden *eingerückt* die Methoden der Klasse definiert. Eine spezielle Methode ist der **Konstruktor**, welcher in Python den Namen `__init__` hat. Der Konstruktor wird jedoch nie direkt aufgerufen. Er wird automatisch beim Erzeugen eines Objektes aufgerufen.

## Objekte erzeugen

In Python wird ein Objekt erzeugt, indem eine Klasse wie eine Funktion aufgerufen wird:

``` python
a = Tasse()
b = Tasse()
```

Im obigen Beispiel werden zwei Objekte der Klasse `Tasse` erzeugt und den Variablen `a` und `b` zugewiesen. Beim Erzeugen wird jedesmal der Konstruktor aufgerufen. Es wird also zweimal «Neue Tasse erzeugt.» ausgegeben.

## Eigenschaften definieren

Ein Objekt kann Variablen besitzen. Diese werden auch als **Eigenschaften** bezeichnet. Eigenschaften können so einem Objekt zugewiesen werden:

``` python
a.volumen = 0.3
a.besitzer = 'Jenny'
b.volumen = 0.2
b.besitzer = 'Peter'
```

Besser ist allerdings, wenn Eigenschaften im Konstruktor zugewiesen werden. Hier kann mit der Variablen `self` auf das neu erzeugte Objekt zugegriffen werden:

``` python
class Tasse:
    def __init__(self, volumen, besitzer):
        self.volumen = volumen
        self.besitzer = besitzer

a = Tasse(0.3, 'Jenny')
b = Tasse(0.2, 'Peter')
```

## Eigenschaften verwenden

Auf den aktuellen Wert einer Eigenschaft greift man so zu:

``` python
print(a.volumen)
```

## Methoden aufrufen

Anstelle des direkten Zugriffs auf Eigenschaften wird häufig eine **Methode** aufgerufen:

``` python
class Tasse:
  def __init__(self, volumen, besitzer):
      self.volumen = volumen
      self.besitzer = besitzer
    def fuelle(self):
        self.inhalt = self.volumen
    def trinke(self, menge):
        self.inhalt = self.inhalt - menge

a = Tasse(0.3, 'Jenny')
a.fuelle()
a.trinke(0.05)
a.trinke(0.05)
```

## Umwandlung in Text

Mit der Methode `__str__` kann definiert werden, wie ein Objekt in einen Text umgewandelt wird.

``` python
class Tasse:
  def __init__(self, volumen, besitzer):
      self.volumen = volumen
      self.besitzer = besitzer
    def __str__(self):
        return 'Tasse von ' + self.besitzer + ' mit einem Volumen von ' + self.volumen + ' l.'

a = Person(0.3, 'Jenny')
print(a)
```
