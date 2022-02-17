import random


def makepassword():
    colors = "blue", "yellow", "red", "purple", "orange", "green"

    passWord = []
    for i in range(4):
        passWordInput = random.choice(colors)
        passWord.append(passWordInput)
    print(passWord)
    return passWord


def guess():
    answerlst = []
    nums = 1
    for i in range(4):
        answerInput = input("Guess color " + str(nums) + ": ")
        answerlst.append(answerInput)
        nums += 1
    return answerlst


def game():
    passWord = makepassword()
    answer = guess()

    if answer == passWord:
        return f"Congratulations you've guessed the code in one try!!"
    else:
        tries = 0
        while answer != passWord:

            tries += 1
            correct = 0
            correctlst = ['X'] * 4

            for i in range(4):

                if answer[i] == passWord[i]:
                    correct += 1
                    correctlst[i] = answer[i]

            if correct < 4 and correct != 4:
                print("Not quite the number. But you did get ", correct, " colors correct!")
                print("Also these colors in your input were correct.")

                right = "z"
                rightButWrong = "w"
                for right in correctlst:
                    print(right, end=' ')
                print('\n')
                print('\n')
                answer = guess()

            elif correct == 0:
                print("None of the numbers in your input match.")
                answer = guess()

        if answer == passWord:
            return "You've become a Mastermind!" \
                   "It took you only", tries, "tries."


print(game())
