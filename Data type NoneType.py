# Funktionen mit Rückgabewerten definieren und der Basis-Datentyp NoneType:

# In der Regel definiert man Funktionen, die bestimmte Aufgaben für mich übernehmen und mir das Ergebnis in mein
# Hauptprogramm zurückgeben, damit ich im Hauptprogramm dann mit diesem Ergebnis in irgendeine Art und Weise
# weiterarbeiten kann. Und dafür ist der Rückgabewert von Funktionen da.
# Jede Funktion besitzt ein Rückgabewert. Immer wenn ich eine Funktion aufrufe und diese dann komplett abgearbeitet
# wurde, wird mir in das Hauptprogramm von wo aus ich die Funktion aufgerufen habe, ein Wert zurückgegeben.

# Wie finde ich diesen Rückgabewert? Ich muss um den Funktionsaufruf drum herum eine print-Anweisung hinschreiben.
# Selbst innerhalb eines Funktionskörpers kann man den Rückgabewert printen.
# Definition einer Funktion:
def rueckgabewert():
    print(type(print("Jede Funktion hat einen Rückgabewert.")))


# Wie finde ich diesen Rückgabewert? Ich muss um den Funktionsaufruf drum herum eine print-Anweisung hinschreiben.
# Jetzt wird in der Konsole zuerst die Funktion mit den dazugehörigen Funktionskörper ausgeführt
# Danach wird an der Stelle, an dem die Funktion ausgeführt wurde, ein Rückgabewert zurückgegeben.
# Dieser Wert wird in der Konsole ausgegeben durch die print-Anweisung.
# Der Datentyp dieses Rückgabewertes der Funktion heißt NoneType. Konsole: None
# Wann wird None verwendet? Wenn man aktuell keinen sinvollen anderen Wert hat, den man benutzen kann.
# Der Wert "None" steht für die Abwesenheit eines Wertes.
print(rueckgabewert())  # Konsole: Der Wert heißt hier None.


# Wenn ich mir bewusst einen Wert zurückgeben lassen möchte, verwendet man einen Schlüsselwort namens "return".
# Sobald dieses return innerhalb einer Funktion aufgerufen wird, wird die Funktion sofort beendet und der entsprechend
# nach "return" folgende Wert wird daraufhin zurückgegeben. Also der Wert in return wird an den Aufrufer der Funktion
# returned. In dieser Funktion möchte ich 2 Zahlen übergeben. Dann soll Sie mir das Maximum ermitteln. Also die Zahl die
# größer ist, soll Sie mir in der Konsole zurückgeben.
# Beispiel
def maximum(a, b):
    if a < b:
        return b
    else:
        return a


result = maximum(5, 3)
print(result)
