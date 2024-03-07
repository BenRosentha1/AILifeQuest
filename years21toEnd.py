from encounterEvent import encounterEvent
from makeDecision import makeDecision

"""
This function takes the user through the years 21 to the end of the characters life.  Each year the character will encounter 3 events 3 corresponding decisions.
"""
# Years 21 to end of game when the character dies
def years21toEnd(character, MODEL, messages):
    
    # While the character is alive
    while character.alive:
        
        # The character has three events and decisions in each year
        for i in range(3):
            
            # Encounter event
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