import json

def displayCharacter(character):
    return "Character age:\n" + str(character.age) + "\n\nCharacter year born:\n" + str(character.yearBorn) + "\n\nCharacter qualities:\n" + str(json.dumps(character.qualities)) + "\n\nCharacter characteristics:\n" + str(json.dumps(character.characteristics))