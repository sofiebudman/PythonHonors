import turtle
hasKey = False
sideChoice = 'none'
###FUNCTIONS ----------------------------------------------------------------------

def reset(location):
    global sideChoice
    sideChoice = level
    if (level == 'none'):
        
        startGame()
def gameOver():
    #talk abt num choices made
    print('--------------------')
    print('You died, restart the program to try again.')
      
def caveGoIn():
    print('You enter the cave. It is dark and hard to see anything. Suddenly, a bear is approaching you.')
    caveGoInChoice = input('Do you try to fight, run, or hide from the bear? ')
    if(caveGoInChoice.lower() == 'fight'):
        print('--------------------')
        print('You try to fight the bear, but is is much stronger then you. You die.')
        gameOver()
        
    elif(caveGoInChoice.lower() == ' run'):
        print('--------------------')
        print('You try to run from the bear, but it is much faster than you. You die')
        gameOver()
        
    elif(caveGoInChoice.lower()== 'hide'):
        print('--------------------')
        print('You hide from the bear and it goes back to sleep. You exit the cave and walk back to the intersection.')
        reset('none')
def caveClimb():
    print('You decide to climb the cave. The cave is very tall and your arms are getting tired.')
    caveClimbChoice = input('Do you keep climbing the cave(up), or head down(down)? ')
    if(caveClimbChoice.lower()== 'up'):
        print('You keep climbing up the cave, and the top seems unreachable. After 10 minutes of climbing your arms tire out, you miss an arm grip and fall.')
        gameOver()
    elif(caveClimbChoice.lower()== 'down'):
        print('You arrive back at the bottom of the cave and walk back to the sign where you are presented with three choices again.')
        reset('none')
def caveKeepWalking():
    shed = input('You begin to walk around the cave and arrive at an old, rusting shed. Do you go in (yes/no)? ')
    if(shed.lower() == 'yes'):
        print('You enter the shed and it is dark, you see cobwebs on the wall. It seems that nothing there is usefull, but suddenly on the shelf you see a old, gold key.')
        grabKey = input('Do you grab the key or leave it(grab/leave it)? ')
        if(grabKey.lower() == 'grab'):
            print('You grab the key and place it in your pocket')
            hasKey == True
        elif(grabKey.lower() == 'leave it'):
            print('You leave the key and head back to the cave.')
            goRight()
    elif(shed.lower() == 'no'):
         print('You leave the shed and walk back to the cave')
         reset('right')

def snakeFight():
    snakeFightWeapon = input('You decide to fight the snake. Around you, you see a stick and a rock. Which one do you use to defend yourself? ')
    if(snakeFightWeapon.lower() =='stick'):
        print('--------------------')
        print('After 5 minutes of fighting, your stick snaps and the cobra bites you. You try to run and get help, but the poison quickly kills you and you die.')
        gameOver()
        
    elif(snakeFightWeapon.lower() == 'rock'):
        print('--------------------')
        print('You manage to defeat the snake with your stick, but are extremely injured and tired. You take a short nap and then head back to the crossroads and try a new path.')
        reset('none')
def snakeRun():
    snakeRunChoice = input('You decide to run away from the snake. Do you keep heading deeper into the forest(forward) or go back to the intersection(go back)? ')
    if(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and arrive back at the 3-way intersection')
        reset('none')
    elif(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and it almost catches you, but you spring your way deep into the forest.')
        reset('forward')
    snakeSneakLocation = input('You crawl and the floor to avoid the snake. The snake seems to be unaware of your presence and you have the opportunity to run away. Do you keep heading into the forest(yes/no)?')
    if(snakeSneakLocation.lower() == 'no'):
        print('--------------------')
        print('You successfully sneak away from the snake and arrive back at the three way crossroad')
        reset('none')
    elif(snakeSneakLocation.lower() == 'yes'):
        print('--------------------')
        print('You successfully sneak away from the snake and continue heading down the path into the unknown.')
        reset('forward')

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
def goRight():
    print('You head forward and hike for 1 hour. The mist dissapates and you arrive at a large ominous cave')
    caveChoice = input('Do you go in, climb to see where you are(climb), or keep walking? ')
    if(caveChoice.lower() == 'go in'):
        caveGoIn()
    elif(caveChoice.lower() == 'climb'):
        caveClimb()
    elif(caveChoice.lower() == 'keep walking'):
        caveKeepWalking()
    
### START GAME ----------------------------------------------------------------------------------------------------------------------------
def startGame():
    

    print('You begin heading up the trail. It is spooky, dark, misty, and you can barely see what is in front of you. Suddenly, you arrive at a 3-way fork in the road.')
    #draw 
    global sideChoice
    sideChoice = input('There is an old, cracked wooden sign. You try to read where the signs point to, but it is in a different language. Do you go left, right, or forward? ')


print('It is a dawn and the sun has just risen. You decide to go on a hike at Pinewood park, an abandoned nature reserve near your house. Will you make it out alive, find the treasure, or die to the mysterious dangers lurking in the park?')
name = input('Welcome player. Please enter your name: ')
print(f'Hello {name}. ')
print('--------------------')

startGame()

###RUNGAME --------------------------------------------------------------------------------------------------------------------------
while(sideChoice.lower() == 'left'):
    #print('--------------------')
    goLeft()
    
 
while(sideChoice.lower() == 'right'):
    print('--------------------')
    goRight()
        
while (sideChoice.lower() == 'forward'):
    print('--------------------')
    goForward()


       

#RIGHT SIDE + OPTIONS
#change







