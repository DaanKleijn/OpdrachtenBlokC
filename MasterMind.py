import random
import json

def getData():
    with open('possibleCombinations.txt', 'r') as dataFile:
        possibleCombinations = json.loads(dataFile.read())
    return possibleCombinations


def whatUser():
    userInput = input("Would you like to play mastermind against a computer? y or n ")
    if "y" in userInput:
        userInput = input("Would you like to play as guesser or make the code? guess or code ")
        print("\n")
        if "guess" in userInput:
            game()
        else:
            userInput = ("Would you like to use the simple guess or a bit more advanced? simple or advanced ")
            if "simple" in userInput:
                computerSimpleStrat()
            else:
                computerProStrat()

    else:
        return f"Allrighty then."


def makepassword():
    passWord = []
    for i in range(4):
        passWordInput = random.randint(0, 5)
        passWord.append(passWordInput)
    print(passWord)
    print(translateColors(passWord))
    return passWord


def makeAIPassword():
    colors = "blue", "yellow", "red", "purple", "orange", "green"
    count = 1
    passWord = []
    print("These are the possible colors: " + str(colors))
    for i in range(4):
        answerInput = input("Guess color " + str(count) + ": ")
        passWord.append(answerInput)
        count += 1
    print("Your code is:" + str(passWord))
    wordlst = translateWords(passWord)
    return wordlst


def guess():
    answerlst = []
    nums = 1
    for i in range(4):
        answerInput = input("Guess color " + str(nums) + ": ")
        answerlst.append(answerInput)
        nums += 1
    answerlst = translateWords(answerlst)
    return answerlst


def game():
    passWord = makepassword()
    answer = guess()
    while answer != passWord:
        score = [0, 0]
        restAnswer = []
        restPassword = []

        if answer == passWord:
            return f"Congratulations you've guessed the code in one try!!"
        else:
            tries = 0
            almostCorrect = 0
            correct = 0

            for i in range(0, 4):
                if answer[i] == passWord[i]:
                    correct += 1
                    score[0] = correct
                else:
                    restAnswer.append(answer[i])
                    restPassword.append(passWord[i])

            for i in range(len(restAnswer)):
                if restAnswer[i] in restPassword:
                    almostCorrect += 1
                    score[-1] = almostCorrect
                    restPassword.remove(restAnswer[i])

            if correct < 4:
                print("\n")
                print(score)
                answer = guess()
                print(answer)

        if correct == 4:
            print("You've cracked the code! It took you only", tries, "tries.")


# translates numbers to words
def translateColors(passWord):
    colors = ["blue", "yellow", "red", "purple", "orange", "green"]
    passwordlst = []
    for numbers in passWord:
        passwordlst.append(colors[numbers])
    return passwordlst


# Translates words to numbers
def translateWords(answerlst):
    colors = ["blue", "yellow", "red", "purple", "orange", "green"]
    wordlst = []
    for color in answerlst:
        wordlst.append(colors.index(color))
    return wordlst


def computerSimpleStrat():
    password = makeAIPassword()
    tries = 0
    computerAnswerlst = []
    while computerAnswerlst != password:
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    for n in range(6):
                        computerAnswerlst = [k, l, m, n]
                        tries += 1
                        print("try:", tries)
                        if computerAnswerlst == password:
                            return f"Congratulations your code: {password} took {tries} tries"


def computerProStrat():


print(whatUser())
