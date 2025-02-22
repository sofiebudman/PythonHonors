vowelList = ['a','e','i','o','u']

def vowels(string):
    numVowels = 0
    for i in range(len(string)):
        if(string[i].lower() in vowelList):
            numVowels +=1
    return numVowels

def consonants(string):
    numConsonants = 0
    for i in range(len(string)):
        if(string[i].isalpha and not string[i].lower() in vowelList):
            numConsonants +=1
    return numConsonants
userInput = input('Enter a string: ')
print(f'{userInput} has {vowels(userInput)} vowels and {consonants(userInput)} consonants.')



    
