def createMessages(*args):
    messages = []
    for roleContent in args:
        for role, content in roleContent.items():
            message = {"role" : role,
                       "content" : content}
            messages.append(message)

    return messages