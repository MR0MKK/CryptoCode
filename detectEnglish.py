# Detect English module
# To use, type this code:
#   import dectectEnglish
#   detectEnglish.isEnglish(someString)
# Note: There must be a 'dictionary.txt' file in the same directory

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' tn'


# Load dictionary
def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()

# Count number of words, return a percentage from 0.0 - 1.0
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0

    count = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            count += 1
    return float(count) / len(possibleWords)    


# Remove non-letters characters in message
def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


# Main function to check if the message is English
def isEnglish(message, wordPercentage=20, letterPecentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPecentage
    return wordsMatch and lettersMatch