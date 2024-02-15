from encounterEvent import encounterEvent
from makeDecision import makeDecision

from outputTest import printMessages

def years5to15(character, MODEL, messages):
    while (character.age < 16) and (character.alive):

        # Encounter Event 1
        messages = encounterEvent(character, messages, MODEL)
        if not character.alive:
            return messages

        # Make decision 1
        messages = makeDecision(character, messages, MODEL)
        if not character.alive:
            return messages
        
        # Encounter Event 2
        messages = encounterEvent(character, messages, MODEL)
        if not character.alive:
            return messages
        
        # Make decision 2
        messages = makeDecision(character, messages, MODEL)
        if not character.alive:
            return messages
        
        # Increment age
        character.age += 1
        print("\nCongratulations " + list(character.qualities.values())[0] + ", you are now " + str(character.age) + " years old!\n")

    return messages