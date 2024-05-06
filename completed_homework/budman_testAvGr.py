def determine_grade(score):
    if(score>=90 and score <= 100):
        return 'A'
    elif(score>=80):
        return 'B'
    elif(score>=70):
        return 'C'
    elif(score>=60):
        return 'D'
    else:
        return 'F'
def main():
    test1 = int(input('Enter score 1: '))
    test2 = int(input('Enter score 2: '))
    test3 = int(input('Enter score 3: '))
    test4 = int(input('Enter score 4: '))
    test5 = int(input('Enter score 5: '))
    print()
    scores = [test1,test2,test3,test4,test5]
    print('     Numeric Grade     Letter Grade  ')
    print()
    for i in range(5):
        print(f'score {i+1}: {scores[i]:>10} {determine_grade(scores[i]):^20}')
    print()
    print(f'Average Score: {sum(scores)/5:.2f}')
main()
    

