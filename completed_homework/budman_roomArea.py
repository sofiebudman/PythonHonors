a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
d = int(input("Enter side D: "))
e = int(input("Enter side E: "))

area = (a*b) + ((d-b-e)*(a-c)) + (((a-c)*e)/2)
print('Room Area: ' +str( area))
