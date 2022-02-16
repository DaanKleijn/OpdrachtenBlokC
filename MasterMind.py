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
        while answer != passWord:
            answerlst = []
            indexcount = 0
            tries = 0
            rightPlace = "z"
            rightButWrong = "w"
            wrong = "x"

            if answer[indexcount] == passWord[indexcount]:
                answerlst.append(rightPlace)
                indexcount += 1
            elif answer[indexcount] in passWord[indexcount]:
                answerlst.append(rightButWrong)
                indexcount += 1
            else:
                print("Your score is: ")
                print(answerlst)
                answerlst.append(wrong)
                indexcount += 1
                answer = guess()
            if answer == passWord:
                return f"Congratulations you've cracked the code!" \
                       f"It only took {tries} tries"


print(game())
