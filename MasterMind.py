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
    score = [0, 0]

    if answer == passWord:
        return f"Congratulations you've guessed the code in one try!!"
    else:
        tries = 0
        almostCorrect = 0
        while answer != passWord:
            tries += 1
            correct = 0

            for i in range(4):
                if answer[i] == passWord[i]:
                    correct += 1
                    score[0] = correct

                elif answer[i] != passWord[i]:
                    almostCorrect += 1

            if correct < 4 and correct != 4:
                score[-1] = almostCorrect
                print("\n")
                print(score)
                answer = guess()
                score = [0, 0]
                almostCorrect = 0

            elif correct == 0:
                print("None of the numbers in your input match.")
                answer = guess()

        if answer == passWord:
            return "You've become a Mastermind! It took you only", tries, "tries."


print(game())
