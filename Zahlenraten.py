from random import randint

# Generiere eine Zufallszahl zwischen 1 und 100
randomNumber = randint(1, 100)
attempts = 0
maxAttempts = 5  # Maximale Anzahl von Versuchen

while attempts < maxAttempts:
    userInput = input("Rate die Zahl (zwischen 1 und 100): ")
    
    if userInput.isdigit():
        userInput = int(userInput)
        if 1 <= userInput <= 100:
            attempts += 1  # Inkrementiere die Anzahl der Versuche
            if userInput < randomNumber:
                print("Zu niedrig! Versuch es erneut.")
            elif userInput > randomNumber:
                print("Zu hoch! Versuch es erneut.")
            else:
                print("Herzlichen Glückwunsch! Du hast die richtige Zahl erraten.")
                break  # Beende die Schleife, wenn die richtige Zahl geraten wurde
        else:
            print("Bitte gib eine Zahl zwischen 1 und 100 ein.")
    else:
        print("Bitte gib eine gültige Zahl ein.")

if attempts == maxAttempts:
    print(f"Du hast {maxAttempts} Versuche aufgebraucht. Die zufällige Zahl war {randomNumber}.")
