import random

kleuren = "rgbop"
vragenlst = []
wachtWoordlst = []


def inputUser():
    global vraag
    vraag = input("Voer een code van 2 in: ")
    vraag.lower()
    vragenlst.append(vraag)


def maakWachtWoord(kleuren):
    for i in range(2):
        wachtWoordlst.append(random.choice(kleuren))


def checkAntwoord():
    antwoordlst = []
    x = 0
    inputUser()
    maakWachtWoord(kleuren)
    print(wachtWoordlst, vragenlst)
    while True:
        if x == 2:
            return antwoordlst
        elif vragenlst[x] == wachtWoordlst[x]:
            antwoordlst.append("2")
            x += 1
        elif vragenlst[x] in wachtWoordlst[x]:
            antwoordlst.append("1")
            x += 1
        else:
            antwoordlst.append("0")
            x += 1

print(checkAntwoord())
