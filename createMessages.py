"""
This function creates a new list of messages given any number of roles followed by their respective contents
"""
# Create Messages
def createMessages(*args):
    # Initialize list of messages
    messages = []

    # For each dictionary pair in the arguments
    for roleContent in args:

        # For each of the key value pairs in the dictionary
        for role, content in roleContent.items():

            # Structure the message
            message = {"role" : role,
                       "content" : content}
            
            # Append the message
            messages.append(message)

    # Return messages
    return messages