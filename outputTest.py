import Character


def printCharacter(character, filename):
    out = open(filename + ".txt", "w")

    out.write("YEAR BORN  :   " + str(character.yearBorn) + "\n")

    for key, value in character.qualities.items():
        out.write(key.upper() + "   :   " + value + "\n")

    for key, value in character.characteristics.items():
        out.write(key.upper() + "   :   " + str(value) + "\n")

    out.write("AGE  :   " + str(character.age) + "\n")

    out.write("ALIVE  :  " + str(character.alive) + "\n")

    out.close()

def printMessages(messages):
    out = open("MessageLog.txt", "w")

    for message in messages:
        for key, value in message.items():
            out.write(key + ":\n")
            out.write(value + "\n\n")