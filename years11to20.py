from encounterEvent import encounterEvent
from makeDecision import makeDecision

"""
This function takes the user through the years 11 to 20 of the characters life.  Each year the character will encounter 2 events 2 corresponding decisions.
"""
# Years 11 to 20
def years11to20(character, MODEL, messages):

    # While the character is alive and younger than 21
    while (character.age < 21) and (character.alive):

        # The character has two events and decisions in each year
        for i in range(2):
            # Encounter Event
            messages = encounterEvent(character, messages, MODEL)

            # Check is the character lived through the event
            if not character.alive:
                
                # If the character died end the game
                return messages

            # Make decision
            messages = makeDecision(character, messages, MODEL)
            
            # Check is the character lived through the event
            if not character.alive:
                
                # If the character died end the game
                return messages
        
            # Clean up messages
            messages = messages[2 : len(messages) - 1]

        # Increment age
        character.age += 1
        print("Congratulations " + list(character.qualities.values())[0] + ", you are now " + str(character.age) + " years old!\n")

    # Return messages
    return messages