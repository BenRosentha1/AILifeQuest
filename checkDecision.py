"""
This function checks to see if the users input was a selection of one of the choices or a selection of a pre-written decision
"""
# Check decision
def checkDecision(options, decision):
    # If the decision is only one character
    if len(decision) == 1:
        # Check what character and assign associated response
        match decision.upper():
            case 'A':
                decision = list(options.values())[0]
            case 'B':
                decision = list(options.values())[1]
            case 'C':
                decision = list(options.values())[2]
            case 'D':
                decision = list(options.values())[3]
    
    # Return the new decision
    return decision