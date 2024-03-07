from prompts import yearBornPrompt, yearBornAgainPrompt

'''
This function prompts the user for what year they want their character to be born and returns it as an int.
'''
# Get year born
def getYearBorn():
    # Prompt user
    print(yearBornPrompt)
    
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