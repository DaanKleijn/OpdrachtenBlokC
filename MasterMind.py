import random


def makePassWord():
    colors = "blue", "yellow", "red", "purple", "orange", "green"

    passWord = []
    for i in range (4):
        passWordInput = random.choice(colors)
        passWord.append(passWordInput)
    print(passWord)
    return passWord


def guess():
    answer = input("Guess 4 colors: ")
    return answer


def game():
    passWord = makePassWord()
    answer = guess()
    print(passWord)
    print(answer)

    if answer == passWord:
        return f"Congratulations you've guessed the code in one try!"
    else:
        tries = 0
        while (answer != passWord):
            tries += 1
            correct = 0
            correctlst = []
            rightPlace = "w"
            rightButWrong = "z"

            for i in range(4):
                correctlst.append("x")
                print(answer[i])
                if (answer[i] == passWord[i]):
                    correct += 1
                    correctlst.pop()
                    correctlst.append(rightPlace)

                else:
                    continue

            for i in range(10):
                if (correct < 4) and (correct != 0):
                    print("You got ", correct, " color(s) correct!")
                    print("Also these colors in your input were correct.")

                    for k in correctlst:
                        print(k, end=' ')
                    print('\n')
                    answer = guess()

                elif (correct == 0):
                    print("None of the colors in your input match.")
                    answer = guess()

                elif tries == 10:
                    return f"No turns left"

            if answer == passWord:
                print("You've become a Mastermind!")
                print("It took you only", tries, "tries.")


print(game())
