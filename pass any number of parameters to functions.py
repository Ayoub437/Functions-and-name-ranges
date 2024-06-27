# Beliebig viele Parameter an Funktionen übergeben:
# Eine Aufgabe, die beliebig viele Parameter entgegennimmt und diese miteinander multipliziert.
# Dadurch das ein Stern vorangestellt ist, entspricht dieser Parameter beliebig viele Parameter. Das bedeutet, ich kann
# beliebig viele Parameter mit dieser Funktion entgegennehmen und diese werden dann in Form eines Tupels der Funktion
# bereitgestellt.

# Was passiert hier?
# Wenn ich die Funktion aufrufe, werden alle Parameter in ein Tupel gepackt.
# Dann wird die variable "sum" angelegt, wo das Endergebnis drinne stehen soll.
# Danach die For-Schleife: Hier laufe ich über den Inhalt dieses Tupels.

def multiply(*numbers):  # Der Parameter mit dem Sternchen davor soll ein Tupel darstellen.
    sum = 1  # Hier soll das Endergebnis stehen.
    for i in numbers:  # Ich iteriere jetzt über dieses Tupel drüber.
        sum *= i  # Hier wird 1 * 2 gerechnet und in sum gespeichert. Im zweiten Durchlauf 1 * 3 und so weiter.
    return sum  # Ohne return wird None als Rückgabewert zurückgegeben. Mit return wird Ergebnis zurückgegeben.


# Mit der Print-Anweisung werden alle Zahlen miteinander multipliziert.
print(multiply(2, 3, 4, 5))  # Diese Zahlen werden alle entgegengenommen und in dem Tupel verpackt.


# Gleiche Aufgabe:
# Ich möchte zusätzlich den Tupel in der Konsole sehen.

def unendlich_parameter(*variablen):
    endresult = 1
    for k in variablen:
        endresult *= k  # Die 1 wird ständig mit den Zahlen (Parametern) multipliziert und dann in Variable endresult
        # gespeichert.
    return endresult


print(unendlich_parameter(3, 6, 4, 2, 8))


# Geliche Aufgabe:
def parameter(*variable):
    print(variable)  # Hier wird der Tupel geprinted.
    endresult1 = 1
    for j in variable:
        endresult1 *= j  #
    return endresult1


print(parameter(9, 7, 5, 8, 3, 2))


# Eine neue Aufgabe: Ich kann vor dem Sternchen-notation dennoch positionsbezogene Parameter
def example(number3, age, *exa):
    print(exa)
    result = number3 * age
    for h in exa:
        result *= h
    return result


print(example(2, 7, 2, 2))
