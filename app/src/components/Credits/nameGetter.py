import json

#Opens the credits markdown file
names = open(r'app\src\components\Credits\Credits.md')
namesList = names.read().split('\n')

#Opens the output file for writing
infoFile = open(r'app\src\components\Credits\namesAndThemes.json', 'wt')

#Declares variables and files for parsing
namesAndCreators = {}
themesBuffer = open(r'server\themes.json')
themes = json.load(themesBuffer)

#Finds a match for every theme name in the credits file
#'r' is the current theme name
def credit(r):
    returnObj = {}

    for i in range(len(namesList)):
        line = namesList[i]
        lineWords = line.split()

        for e in range(len(lineWords)):
            try:
                if (r['name'].split()[0] == lineWords[e] and r['name'].split()[1] == lineWords[e + 1]):
                    returnObj =  {
                        'name': r['name'],
                        'note': line,
                        'dark': r['isDark']
                    }
            except:
                if (r['name'].split()[0] == lineWords[e]):
                    returnObj =  {
                        'name': r['name'],
                        'note': line,
                        'dark': r['isDark']
                    }

        if (returnObj == {}):
            returnObj = {
                'name': r['name'],
                'note': 'Not Found',
                'dark': r['isDark']
            }

    return returnObj

namesAndCreators['credits'] = list(map(credit, themes))

json = json.dumps(namesAndCreators, indent = 4, sort_keys = True)
infoFile.write(json)