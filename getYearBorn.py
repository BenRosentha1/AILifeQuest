from prompts import yearBornPrompt, yearBornAgainPrompt
from buildSpeech import buildSpeech
from playsound import playsound

'''
This function prompts the user for what year they want their character to be born and returns it as an int.
'''
# Get year born
def getYearBorn():
    # Prompt user
    speech = buildSpeech(yearBornPrompt[0:92] + "?")
    print(yearBornPrompt)
    playsound(speech)
    
    # Collect response
    yearBorn = input()

    # Verify response
    while not yearBorn.isdecimal() or (int(yearBorn) > 4000 or int(yearBorn) < 0):
        
        # Re-prompt
        print(yearBornAgainPrompt)
        
        # Re-collect response
        yearBorn = input()
    
    # Return as int
    return int(yearBorn)