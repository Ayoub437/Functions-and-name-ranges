# Namensbereiche:

# Eine Funktion, die 2 Werte entgegennimmt: number1 und number2
def add(number1, number2):
    res = number1 + number2
    return res  # Diese Variable wird hier an den Aufrufer der Funktion zurückgegeben.


print(add(2, 3))  # Aufrufer der Funktion.
print(add(6, 4))


# WICHTIG: Die Parameter und Variablen einer Funktion, denen innerhalb der Funktion einen Wert zugewiesen wird, die
# befinden sich innerhalb des lokalen Namensbereichs der Funktion. Deshalb bezeichnet man diese Variablen auch als
# lokale Variablen. Diese kann man nur innerhalb einer Funktion verwenden.

# Sobald der Funktionskörper abgearbeitet wurde und die Programmausführung dann wieder an den Aufrufer der Funktion
# zurückspringt, also zurück ins Hauptprogramm, dann wird der gesamte lokale Namensbereich der Funktion zerstört.
# Er ist also nicht mehr gültig und alle dort drin definierten variablen und Parameter sind weg und existieren nicht
# mehr. Sollte man die Funktion erneut im Programm aufrufen, dann wird der lokale Namensbereich wieder neu erzeugt und
# auch die variablen, die innerhalb dieses lokalen Namensbereichs liegen, werden wieder neu angelegt und neu mit Werten
# befüllt. Sobald die Funktion dann wieder komplett abgearbeitet wurde, wird der lokale Namensbereich wieder zerstört.


# Gobaler Namensbereich - Es handelt sich um das Hauptprogramm, welches man außerhalb der Funktion festlegt.
# Der globale Namensbereich wird erzeugt, sobald das Programm ausgeführt wird. (Play button drücken) Ab Zeile 31.
def local(parameter1, parameter2):
    var = parameter1 + parameter2
    return var


# Globaler Namensbereich - ist während der kompletten Programmlaufzeit gültig.
# Also erst wenn das Programm komplett durchgelaufen ist und beendet wird, dann wird der globale Namensbereich zerstört
# und alle variablen und sonstige Referenzen werden vergessen.
# Wenn das nicht passieren würde: -> Dann würde das Programm bei einem erneutem Aufruf, alle variablen mit den selben
# Werten wie zuvor beim dem vorherigen Aufruf.
# Bei jedem Funktionsaufruf startet das Programm jedes mal wieder frisch.
test = 10  # Das ist eine globale Variable, da dieser im globalen Namensbereich liegt.
print(local(4, 9))
print(test)


# Zugriffsberechtigung zwischen den lokalen und globalen Namensbereiche:
# Ich kann von dem Standpunkt des globalen Namensbereich, nicht auf lokale variablen zugreifen.
# Jedoch kann ich vom lokalen Namensbereich auf globale variablen zugreifen.


# Eine weitere Sache - Ich kann in einer Funktion zwei variblen mit dem gleichen Bezeichner haben, wenn sie jeweils in
# unterschiedliche Namensbereiche/Namensräume liegen.
# Beispiel:
def ranges():
    global example
    example = 20
    print(example)


example = 21
print(ranges())
print(example)
