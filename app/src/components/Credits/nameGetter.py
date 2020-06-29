import json

#Opens the original file
names = open(r'app\src\components\Credits\Credits.md')
namesText = names.read()
namesList = namesText.split('\n')

#Opens the file and resets to a blank line
infoFile = open(r'app\src\components\Credits\namesAndThemes.json', 'wt')
infoFile.write('')
infoFile.close()
#Reopens the file to write the output
infoFile = open(r'app\src\components\Credits\namesAndThemes.json', 'at')

#Declares variables and files for parsing
namesAndCreators = {}
themeNamesBuffer = open(r'server\themes.json')
OGThemes = json.load(themeNamesBuffer)
themes = list(map(lambda x : x['name'], OGThemes))
print(themes)

def credit(variable):
    for i in range(len(namesList)):
        line = namesList[i]
        lineWords = line.split()
        print(lineWords)

        for e in range(len(lineWords)):
            if (lineWords[e] == variable):
                return {
                    "name": variable,
                    "note": line
                }

            '''
            return {
                "name": variable,
                "note": line if lineWords[e] == variable else 'Not Found'
            }
            '''

namesAndCreators['Credits'] = list(map(credit, themes))

'''
for i in range(len(namesList)):
    line = namesList[i]
    lineWords = line.split()

    for a in range(len(lineWords)):
        for e in range(len(themes)):
            if (lineWords[a] == themes[e]):

                themeObj = {
                    "name": themes[e],
                    "note": line
                }
                namesAndCreators['Credits'].append(themeObj)
'''

json = json.dumps(namesAndCreators, indent = 4, sort_keys = True)
infoFile.write(json)