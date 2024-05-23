alphabet = [' ', ',','.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse_list = [' ', '--..--', '.-.-.-','..--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']
word = input('Enter a word to be converted to morse code: ')
output = ''
for i in range(len(word)):

    character = word[i]
    if(character.isalpha()):
        character = character.lower() 
    output += morse_list[alphabet.index(character)]
    
    
    
    output += ' '


print(f'{word} in morse code is {output}')
