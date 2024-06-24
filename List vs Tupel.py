# Hauptunterschied zwischen Tupel und Listen:
# Listen sind veränderliche Dastenstruktur.
# Tupel sind unveränderliche Datenstrukturen.
# Werte eines Tupels können im Vergleich zu Listen also nicht mehr im nachhinein modifiziert werden.


list1 = [1, 3, 4, 8]
list1[1] = 10
print(list1)

print("Hier kommen jetzt die tupel...")
# Jetzt kommt ein Tupel: runde Klammern.
tupel1 = (1, 3, 4, 8)
print(tupel1)

# Hier kann ich mir auch ein bestimmtes Element aus der Tupel ausgeben lassen.
print(tupel1[1])  # Man kann also lesend auf die einzelnen Elemente eines Tupels zugreifen.

# WICHTIG: Tupel haben im Vergleich zu Listen einen Performance-Vorteil. Der Code von Tupel kann schneller ausgeführt
# werden, als der von Listen.
# Mit einer Liste kann man wesentlich flexibler arbeiten, da die Werte nachträglich verändert werden können.
# Diese Flexibilität kostet natürlich performance, da im Hintergrund etwas dafür getan werden muss.
# Da man sowas bei Tupeln nicht hat, sind diese auch performance-technisch schneller als Listen.

# Bei Tupeln gibt es einen Sonderfall:
# Wenn ich ein Tupel mit nur einem Wert habe, wird dieser von Python nicht als Tupel aufgefasst. tupel2 = (7)
# Beispiel: -> Es wird von Python als ein integer gewertet. Nebenbei kann man auch im Terminal beobachten, dass der Wert
# nicht mit runden klammern versehen ist, welches bei einem Tupel immer dazugehört.
# Damit Python meinen Tupel als solches auch wertet, kann ich neben dem Wert einen Komma hinschreiben. tupel2 = (7,)
# Beispiel:
tupel2 = (7,)
print(tupel2)

# Unpackaging/Entpacken:
# Es gibt einen Weg, wie ich die Werte eines Tupels verändern kann -> Ich kann einzelne Werte aus dem Tupel rausziehen,
# in dem ich lesend darauf zugreife und in jeweils einzelne Variablen speichere.
# Nun kann ich mit diesen Variablen weiterarbeiten.
person1 = ("Max", "Mustermann", 28)

# Eine Methode, in der man die einzelnen Werte entpacken kann.
# first_name = person1[0]
# last_name = person1[1]
# age = person1[2]

# Die schnellere und elegantere Methode:
first_name, last_name, age = person1  # Die Elemente des oberen Tupels werden auf diese 3 Variablen verteilt.

print(first_name, last_name, age)  # Hier habe ich alle Werte in eine Zeile Code.
print(first_name)
print(last_name)
print(age)

# WICHTIG: Wieso braucht man Tupeln? Und vorallem wieso im Kontext von Funktionen?
# Mithilfe von Tupeln kann ich von einer Funktion mehrere Rückgabewerte zurückgeben lassen.
# Das Schlüsselwort return kann ich in einer Funktion aufrufen, um einen Wert zurückzugeben und die Funktion ist danach
# sofort beendet. -> Mehr dazu in der Datei namens "Data type NoneType".
# Das ist unpraktisch, wenn ich mehr als nur einen Wert zurückgeben lassen möchte. Mithilfe von Tupeln funktioniert das
# zurückgeben mehrerer Werte. Ich packe also alle Werte die ich zurückgeben lassen möchte in einem Tupel und dann
# returne ich nur dieses eine Tupel.
# Das zurückgegebene Tupel kann ich im Funktionsaufruf direkt wieder entpacken/modifizieren.

# Mit return kann man nur einen Wert zurückgeben, weshalb ich einen Tupel benutze. Ein Tupel wird als ein Wert gesehen.


def generate_passwort(name, age):
    # Aus übergebenen Namen und dem Alter mehrere Passwort Kombinationen generieren.
    return ("Passwort1", "Passwort2", "Passwort3")  #Tupel


# Die Funktion arbeitet wie folgt: Basierend auf die übergebenen Parametern, werden 3 Passwort Kombinationen erzeugt,
# die geeignet sind. Die werden dann in Form eines Tupels zurückgegeben.
# Mithilfe von unpackaging/entpacken kann ich die oberen 3 Passwörter auf 3 Variablen aufsplitten:
passwort1, passwort2, passwort3 = generate_passwort("Jonas", 20)
print(passwort2)  # unpackaging
print(generate_passwort("ayoub", 22))  # Ausführung aller Werte des Tupels.
