
def start():
    #addd something about fastest way to do it
    
    print('It is a dawn and the sun has just risen. You decide to go on a hike at Pinewood park, an abandoned nature reserve near your house. Will you make it out alive, find the treasure, or die to the mysterious dangers lurking in the park?')
    name = input('Welcome player. Please enter your name: ')
    print(f'Hello {name}. You begin heading up the trail. It is spooky, dark, misty, and you can barely see what is in front of you. Suddenly, you arrive at a 3-way fork in the road.')
    print('--------------------')
    pickSide()
def pickSide(): 
  
    #draw a sign in turlte
    sideChoice = input('There is an old, cracked wooden sign. You try to read where the signs point to, but it is in a different language. Do you go left, right, or forward? ')
    if (sideChoice.lower() == 'left'):
        print('--------------------')
        goLeft()
    elif(sideChoice.lower() == 'right'):
        print('--------------------')
        goRight()
    elif(sideChoice.lower() == 'forward'):
       print('--------------------')
       goForward()
def goLeft():
    print('You walk down the left path, There are many vines and roots covering the path.')
    snakeChoice = input('Suddenly, you see a large vine ahead of, but it is moving, and coming fast towards you. It is a King Cobra around 10 feet tall whose poison could kill you in a matter of minutes. Do you fight, sneak, or run? ')
    if(snakeChoice.lower() == 'fight'):
        print('--------------------')
        snakeFight()
       
    if(snakeChoice.lower() == 'sneak'):
        print('--------------------')
        snakeSneak()
        
    if(snakeChoice.lower() == 'run'):
        print('--------------------')
        snakeRun()
       
def snakeFight():
    snakeFightWeapon = input('You decide to fight the snake. Around you, you see a stick and a rock. Which one do you use to defend yourself? ')
    if(snakeFightWeapon.lower() =='stick'):
        print('--------------------')
        print('After 5 minutes of fighting, your stick snaps and the cobra bites you. You try to run and get help, but the poison quickly kills you and you die.')
        end()
    elif(snakeFightWeapon.lower() == 'rock'):
        print('--------------------')
        print('You manage to defeat the snake with your stick, but are extremely injured and tired. You take a short nap and then head back to the crossroads and try a new path.')
        pickSide()
def snakeRun():
    snakeRunChoice = input('You decide to run away from the snake. Do you keep heading deeper into the forest(forward) or go back to the intersection(go back)? ')
    if(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and arrive back at the 3-way intersection')
        pickSide()
    elif(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and it almost catches you, but you spring your way deep into the forest.')
        goStraight()
def snakeSneak():
    snakeSneakLocation = input('You crawl and the floor to avoid the snake. The snake seems to be unaware of your presence and you have the opportunity to run away. Do you keep heading into the forest(forward), or go back the crossroads(go back)?')
    if(snakeSneakLocation.lower() == 'go back'):
        print('--------------------')
        print('You successfully sneak away from the snake and arrive back at the three way crossroad')
        pickSide()
    elif(snakeSneakLocation.lower() == 'forward'):
        print('--------------------')
        print('You successfully sneak away from the snake and continue heading down the path into the unknown.')
        goStraight()
        
def goRight():
    print('You head forward and hike for 1 hour. The mist dissapates and you arrive at a large ominous cave')
    caveChoice = input('Do you go in, climb to see where you are(climb), or keep walking? ')
    if(caveChoice.lower() == 'go in'):
        caveGoIn()
    elif(caveChoice.lower() == 'climb'):
        caveClimb()
    elif(caveChoice.lower() == 'keep walking'):
#def goForward():
#def end():
start()
