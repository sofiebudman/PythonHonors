alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9]

telephone = input('Enter a 10 character telephone number in the format XXX-XXX-XXXX: ')
output = ' '
for i in range (10):
    if(telephone[i].isalpha()):
        output += str(nums[alphabet.index(telephone[i].upper())])

    else:
        output += telephone[i]

print(output)
