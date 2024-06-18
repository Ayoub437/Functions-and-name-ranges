# Hier habe ich eine Funktion mit einem Paramter.
# Der Parameter wird von dem Argument in der Konsole ersetzt.
# Jede Anweisung führt das erste Argument aus. Danach führt jede Anweisung das zweite Argument aus und so weiter...
# Man verkettet den Parameter mit dem string.
# Im Parameter wurden die Argumente gespeichert.
def example(para):  # Dieser Parameter wird nur in diesem Funktionskörper verwendbar.
    print("Eine Funktion " + para)  # Das sind die Funktionskörper.
    print("zweite Anweisung " + para)
    print("Dritte Anweisung " + para)


# Der Parameter in der ausgeführten/aufgerufenen Funktion nennt man Argument.
# Das Argument wird in der Definition hinzugefügt. Wie? In dem man den Parameter hinzufügt sieht man dann das Argument
# in der Konsole.
# Das Argument wird in dem Paramter gespeichert.
example("und erstes Beispiel.")
example(" und zweites Beispiel.")
example("und drittes Beispiel.")


# Eine weitere Funktion: Zwei Parameter.
def zweiterparameter(first_name, last_name):
    print("Mein Vorname lautet" + " " + first_name + " und Nachmname lautet " + last_name)


# Positionsbezogene Parameter:
# Das erste Argument bezieht sich auf den ersten Parameter und das zweite auf den zweiten Parameter.
zweiterparameter("Ayoub", "Ouataleb.")  # Ausführung

