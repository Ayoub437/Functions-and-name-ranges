# Das Schlüsselwort Parameter: Schlüsselwortbezogene Argumente/ Schlüsselwort-Argumente

# Define a function.
def keywordparameter(first_name, last_name, age, academic_title=""):
    if academic_title != "":
        academic_title += " "
    print("Es gibt ein Schlüsselwort namens Parameter.")
    print("Mein Name lautet " + academic_title + first_name + " " + last_name + " and I am " + age + " years old.")
    print("He is " + age + " years old.")


# Schlüsselwortbezogene Argumente/ Schlüsselwort-Argumente: Hier kann ich angeben in welchem Parameter die
# entsprechenden Argumente geladen werden sollen. Das bedeutet ich kann die Argumente in eine beliebige Reihenfolge
# übergeben.
keywordparameter(first_name="Ayoub", last_name="Ouataleb", age="26")


# Man kann auch die zwei Arten, Argumente zu übergeben, vermischen: Also ich kann ein Teil der Argumente beim Aufruf
# positionsbezogen und den anderen Teil als Schlüsselwort-Argument übergeben.
# WICHTIG: Alle Argumente, die ich positionsbezogen übergeben möchte, müssen im Funktionsaufruf am Anfang stehen.
keywordparameter("Thomas", "Gotschalk", "23", academic_title="Dr.")
