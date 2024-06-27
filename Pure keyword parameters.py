# Hier printe ich mehrmals, jedoch wird dies in der Konsole auf der gleichen Zeile stehen. (Ohne Zeilenumbruch)
# Bei dem Parameter "end" spricht man von einem reinen Schlüsselwort-Parameter, weil man den nur mit einem Schlüsselwort
# bezogenen Argument befüllen kann.
print("Eine Zeile ohne Zeilenumbruch", end=" ")
print("und hier geht es weiter.")

# Ein weiteres Schlüsselwort namens "sep". Er steht für Separator und trennt oder verbindet Argumente.
# Beispiel:
print("Hello", "World", "My", "Name", sep="-")  # Dieses Zeichen "-" wird zwischen den Argumenten sein.

print("Hello", "World", "My", "Name", sep="")  # Hier wird alles zusammengeschrieben, ohne Leertaste.


# Die Schlüsselwortbezogenen Parameter kann ich auch in einer Funktioon in Kombination mit positionsbezogenen Parameter
# und der Sternchen Notation (beliebig viele Parameter an eine Funktion, z.b.) hinzufügen.
# Die Schlüsselwortbezogenen Parameter müssen aber nach dem Sternchen Notation folgen und nicht davor.
# Beispiel:
def unendlich_schluesselwort(name, age, *variable, school):
    print("Ich heiße " + name + " und bin " + age + " Jahre alt")
    print("Meine ehemalige Schule heißt " + school)
    print(variable)  # Hier printe ich den Tupel.
    sum = 1
    for loop in variable:
        sum *= loop
    return sum, name, variable  # gebe ich den Rückgabewert zurück: Ein Tupel und ein weiterer Tupel innerhalb des
    # Tupels, in dem die 3 Zahlen gespeichert sind.


print(unendlich_schluesselwort("Max", "20", 22, 55, 66, school="Rackow-Schule"))

