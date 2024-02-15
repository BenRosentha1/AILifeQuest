def parseForOptions(response):
    options = []
    while len(response) > 0:
        sIndex = response.find(')') + 2
        eIndex = response.find('.', sIndex) + 1
        options.append(response[sIndex : eIndex])
        response = response[eIndex :]

    return options