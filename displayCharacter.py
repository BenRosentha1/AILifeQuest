import json

"""
This function unrolls the characters profile into a string
"""
# Display character
def displayCharacter(character):
    prompt = f"""Character age: {str(character.age)}
    Character year born: {str(character.yearBorn)}
    Character qualities:
    {str(json.dumps(character.qualities))}
    Character characteristics:
    {str(json.dumps(character.characteristics))}"""
    return prompt