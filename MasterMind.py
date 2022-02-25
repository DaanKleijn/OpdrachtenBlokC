import random
import json
with open('possibleCombinations.txt', 'r') as dataFile:
  possibleCombinations = json.loads(dataFile.read())


def whatUser():
    userInput = input("Would you like to play mastermind against a computer? y or n ")
    if "y" in userInput:
        userInput = input("Would you like to play as guesser or make the code? guess or code ")
        if "guess" in userInput:
            game()
        else:
            # userInput = ("Would you like to use the simple guess or a bit more advanced? simple or advanced ")
            # # if "simple" in userInput:
            # #     computerSimpleGuess()
            # else:
                computerRandomGuess()
    else:
        return f"Allrighty then."


def makepassword():
    passWord = []
    for i in range(4):
        passWordInput = random.randint(0, 6)
        passWord.append(passWordInput)
    print(passWord)
    print(translateColors(passWord))
    return passWord


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


# def computerSimpleGuess():
#     colors = "blue", "yellow", "red", "purple", "orange", "green"
#     passwordlst = []
#     computerAnswer = ["blue", "blue", "blue", "blue"]
#     nums = 1
#     tries = 0
#     print(colors)
#     while len(passwordlst) != 4:
#         passWord = input("What will be color " + str(nums) + "? ")
#         if passWord in colors:
#             passwordlst.append(passWord)
#             nums += 1
#
#     while computerAnswer != passwordlst:
#         computerAnswer[-1] += 1
#         print(computerAnswer)


#translates numbers to words
def translateColors(passWord):
    colors = ["blue", "yellow", "red", "purple", "orange", "green"]
    passwordslst = []
    for color in passWord:
        passwordslst.append(colors[color])
    return passwordslst

#Translates words to numbers
def translateWords(answerlst):
    colors = ["blue", "yellow", "red", "purple", "orange", "green"]
    wordlst = []
    for color in answerlst:
        wordlst.append(colors.index(color))
    return wordlst


def computerRandomGuess():

    # passwordlst = []
    # computerAnswer = []
    # nums = 1
    # tries = 0
    # while len(passwordlst) != 4:
    #     passWord = input("What will be color " + str(nums) + "? ")
    #     if passWord in colors:
    #         passwordlst.append(passWord)
    #         nums += 1
    #
    # while computerAnswer != passwordlst:
    #     for i in range(4):
    #         computerInput = random.choice(colors)
    #         computerAnswer.append(computerInput)
    #     print(computerAnswer)
    #     if computerAnswer != passwordlst:
    #         computerAnswer.clear()
    #         tries += 1
    #     print(tries)


print(whatUser())