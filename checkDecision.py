"""
This function checks to see if the users input was a selection of one of the choices or a selection of a pre-written decision
"""
def checkDecision(options, decision):
    if len(characterDecision) == 1:
        match characterDecision:
            case 'A':
                characterDecision = options[0]
            case 'B':
                characterDecision = options[1]
            case 'C':
                characterDecision = options[2]
            case 'D':
                characterDecision = options[3]
    
    return characterDecision