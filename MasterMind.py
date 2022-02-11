import random


def wachtWoordMaken():
    global wachtWoord
    wachtWoord = random.randrange(1000, 10000)


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
            correct = 0
            antwoord = str(antwoord)
            wachtWoord = str(wachtWoord)
            correctlst = []

            for i in range(0, 4):
                correctlst.append("x")
                if (antwoord[i] == wachtWoord[i]):
                    correct += 1
                    correctlst.pop(i)
                    correctlst.append("w")

                else:
                    continue

            if (correct < 4) and (correct != 0):
                print("Not quite the number. But you did get ", correct, " digit(s) correct!")
                print("Also these numbers in your input were correct.")

                for k in correctlst:
                    print(k, end=' ')

                print('\n')
                print('\n')
                antwoord = int(guess())

            elif (correct == 0):
                print("None of the numbers in your input match.")
                antwoord = int(guess())

            elif tries == 10:
                return f"Geen zetten over"

        if antwoord == wachtWoord:
            print("You've become a Mastermind!")
            print("It took you only", tries, "tries.")


print(spel())
