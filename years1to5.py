from encounterEvent import encounterEvent
from makeDecision import makeDecision

"""
This function takes the user through the first five years of the characters life
"""

def years1to5(character, MODEL, messages):
    # While the character is alive and younger than six
    while (character.age < 6) and (character.alive):

        # Encounter Event
        messages = encounterEvent(character, messages, MODEL)
        if not character.alive:
            return messages

        # Make decision
        messages = makeDecision(character, messages, MODEL)
        if not character.alive:
            return messages

        # Increment age
        character.age += 1

        # Prompt user with age progression
        name = list(character.qualities.values())[0]
        print("\Happy Birthday!  " + name + ", you are now " + str(character.age) + " years old!\n")

    return messages
