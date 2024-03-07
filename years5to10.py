from encounterEvent import encounterEvent
from makeDecision import makeDecision

"""
This function takes the user through the years 5 to 10 of the characters life.
"""
# Years 5 to 10
def years5to10(character, MODEL, messages):
    
    # While the character is alive and younger than six
    while (character.age < 6) and (character.alive):

        # Encounter Event
        messages = encounterEvent(character, messages, MODEL)
        
        # Check is the character lived through the event
        if not character.alive:
            
            # If the character died end the game
            return messages

        # Make decision
        messages = makeDecision(character, messages, MODEL)

        # Increment age
        character.age += 1

        # Prompt user with age progression
        name = list(character.qualities.values())[0]
        print(f"Happy Birthday!  {name}, you are now {str(character.age)} years old!\n")

    # Return messages
    return messages
