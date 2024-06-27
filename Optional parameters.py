# Optionale Parameter:
# Aufgabe: Einige haben einen Dr. Titel und möchten mit diesem angesprochen werden.
# Aus dem Grund benutze ich den optionalen Parameter. Wie? In dem ich einen dritten Parameter angebe.
# Ich muss dem optionalen Parameter einen default Wert zuweisen, um ihn als optionalen Parameter zu kennzeichnen.
# Das mache ich durch den Zuweisungsoperator und den entsprechenden default Wert.
#  academic_title="" -> Dieser Default Wert ist leer.
# Selbst durch den optionalen Parameter wird alles ganz normal geprinted.
def greeting(first_name, last_name, academic_title=""):
    if academic_title != "":
        academic_title += " "
    print("Hallo " + academic_title + first_name + " " + last_name)
    print("Schön das du da bist!")


# Der leere default Wert wird durch das dritte Argument ersetzt.
# Damit ich eine Leerzeile in der Konsole zwischen dem ersten und dem optionalen Parameter habe, kann ich zwei Lösungen
# anstreben.
# Variante 1: Dem optionalen Parameter (drittes Argument) eine Leertaste hinzufügen.
# Problem ist aber: Derjenige der das Programm schreibt bzw. die Funktion aufruft muss wissen, dass er im dritten
# Argument eine Leertaste mit übergeben muss, damit das ganze sauber ausgegeben wird.
# Und wenn derjenige, der die Funktion aufruft so ganz spezielle Sachen wissen muss, ist es nie gut. Denn in der Regel
# wird es vorkommen, dass er es natürlich vergessen wird.
# Variante 2 - bessere Lösung: In der Funktion regeln. Wie? Durch das if-Konstrukt.
# Dort oben hänge ich eine Leertaste.  ->   if academic_title != "": academic_title += " "
greeting("Max", "Mustermann", "Dr.")


# WICHTIG: Wann brauche ich dieses Konzept?
# Wenn ich eine Funktion habe, die für einen Wert zum Großteil einen default Wert verwendet, der aber bei Bedarf
# auch durch den Aufruf modifiziert (= in einer oder mehreren Einzelheiten anders umgestalten) werden kann.
# Genauso wie im oberen Beispiel.

# WICHTIG: Der optionale Parameter muss in der Parameter-Liste hinten stehen muss. Mehrere optionale Parameter sind
# auch möglich. Sie müssen also in der Funktionsdefinition nach den positionsbezogenen Parametern stehen.
# Denn nur so ist gewährleistet, dass die positionsbezogenen Parametern, also die die man auch zwingend mit übergeben
# muss, noch eindeutig zugewiesen werden können.


# Eine Funktion, die 3 Zahlen entgegennimmt und diese dann miteinander multipliziert.
# Hier werden nur die ersten zwei Parameter miteinander multipliziert. Der dritte Parameter aber nicht, da er die Zahl
# 1 beträgt.
def multiply(number1, number2, number3=1):
    return number1 * number2 * number3


print(multiply(3, 2))

