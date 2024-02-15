from prompts import yearBornPrompt, yearBornAgainPrompt

def getYearBorn():
    print(yearBornPrompt)
    yearBorn = input()
    while not yearBorn.isdecimal() or (int(yearBorn) > 4000 or int(yearBorn) < 0):
        print(yearBornAgainPrompt)
        yearBorn = input()
    yearBorn = int(yearBorn)
    return yearBorn