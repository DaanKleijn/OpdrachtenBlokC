import random


def wachtWoordMaken():
    global wachtWoord
    wachtwoord = random.randrange(1000, 10000)


def guess():
    global antwoord
    antwoord = int(input("Geef 4 cijfers: "))


def spel():
    global wachtWoord
    global antwoord
    wachtWoordMaken()
    guess()
    if antwoord == wachtWoord:
        return f"Gefeliciteerd je hebt het in 1x geraden!"
    else:
        tries = 0
        while (antwoord != wachtWoord):
            tries += 1
            guesses = 0
            antwoord = str(antwoord)
            wachtWoord = str(wachtWoord)
            correctAnswer = ("W") * 4
            for i in range(4):
                if (antwoord[i] == wachtWoord[i]):
                    tries += 1

                    correctAnswer[i] = antwoord[i]
                else:
                    continue

            if (tries < 4) and (tries != 0):
                print("Not quite the number. But you did get ", tries, " digit(s) correct!")
                print("Also these numbers in your input were correct.")
                for k in correctAnswer:
                    print(k, end= '')
                print("\n")
                print("\n")
                antwoord = guess()

            elif (tries == 0):
                   antwoord = guess()

        if antwoord == wachtWoord:
            return f"Gefeliciteerd!"


print(spel())