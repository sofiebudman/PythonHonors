wid1 =float(input('Enter the width of the first rectangle: '))
len1 = float(input('Enter the length of the first rectangle: '))
wid2 = float(input('Enter the width of the second rectangle: '))
len2 = float(input('Enter the length of the second rectangle: '))

if((wid1*len1) > (wid2*len2)):
    print('The first rectangle has a greater area.')
elif((wid1*len1) < (wid2*len2)):
    print('The second rectangle has a greater area.')
else:
    print('The rectangles have the same area.')
