from encounterEvent import encounterEvent
from makeDecision import makeDecision

from outputTest import printMessages

def years1to5(character, MODEL, messages):
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
        print("\nCongratulations " + list(character.qualities.values())[0] + ", you are now " + str(character.age) + " years old!\n")

    return messages
