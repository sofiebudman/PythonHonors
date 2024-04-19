import turtle
hasKey = False
sideChoice = 'none'
isGameOver = False


### TURTLE
import turtle
turtle.colormode(255)
turtle.hideturtle()



def alternateColor(length):
    for i in range (0,length,50):
        turtle.pencolor(106,153,78)
        turtle.forward(25)
        turtle.pencolor(167,201,87)
        turtle.forward(25)

def drawInstructions():
    
    turtle.penup()
    turtle.goto(-200,60)
    turtle.pendown()
    turtle.write("Welcome to the choose your own adventure game!", font = ('Arial', 15,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("1. Navigate through many different paths of the park and try to collect the treasure" ,font = ('Arial', 12,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("2. The game is best played with the turtle window and terminal window side by side",font = ('Arial', 12,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("3. Enjoy!",font = ('Arial', 12,'normal'))
    

def drawPath():
    turtle.pencolor(255,255,255)

    turtle.Screen().bgcolor(40,54,24)
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.speed(10)
    
    turtle.fillcolor(234,208,168)
    turtle.pencolor(47,14,7)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-500,-350)
    turtle.pendown()
    turtle.left(35)
    turtle.forward(600)
    turtle.left(60)
    turtle.forward(500)
    turtle.right(120)
    turtle.forward(150)
    turtle.right(60)
    turtle.forward(380)

    turtle.left(120)
    turtle.forward(500)
    turtle.right(120)
    turtle.forward(150)
    turtle.right(60)
    turtle.forward(380)
    turtle.left(120)
    turtle.forward(500)
    turtle.right(120)
    turtle.forward(150)
    turtle.right(60)
    turtle.forward(500)
    turtle.left(60)
    turtle.forward(700)
    turtle.right(60)
    turtle.forward(200)
    turtle.end_fill()


def drawSign():
    
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    
    #pole
  
    turtle.fillcolor(169,146,125)

    turtle.goto(60,-100)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(180)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(105)
    turtle.pendown()

    #sign shape
    turtle.fillcolor(231,188,145)
    turtle.pencolor(47,14,7)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(90)
    turtle.end_fill()
    #words
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(15)
    turtle.pendown()
    turtle.write('^ %$d*@!~')
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.write('> ,O.\|**(-')
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.write('< !`C#^$*/{')

def drawSnake():
    turtle.clear()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.Screen().bgcolor(161,139,95)
  
    #SNAKE BODY
    turtle.penup()
    turtle.goto(-150,-90)
    turtle.width(40)
    turtle.pendown()
    alternateColor(300)
    turtle.left(90)
    alternateColor(50)
    turtle.left(90)
    alternateColor(250)
    turtle.right(90)
    alternateColor(50)
    turtle.right(90)
    alternateColor(200)
    turtle.left(90)
    alternateColor(50)
    turtle.left(90)
    alternateColor(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(40)
    turtle.pendown()
    #SNAKE HEAD
    turtle.width(1)
    turtle.pencolor(173,193,120)
    turtle.fillcolor(173,193,120)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    #SNAKE EYES
    turtle.pencolor(255,255,255)
    turtle.fillcolor(0,0,0)
    turtle.width(4)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.right(180)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    turtle.right(180)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    #TURTLE MOUTH
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(12)
    turtle.width(1)
    turtle.pencolor(138,0,63)
    turtle.fillcolor(186,0,84)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(150)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.left(150)
    turtle.forward(30)
    turtle.end_fill()
    

def drawStartScreen():
    turtle.clear()
    drawPath()
    drawSign()



###FUNCTIONS ----------------------------------------------------------------------

def reset():
    global sideChoice
    sideChoice = 'none'
    startGame()
def gameOver():
    global gameOver
    gameOver = True
    #talk abt num choices made
    print('--------------------')
    print('You died, restart the program to try again.')
    quit()
      
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
        reset()
def caveClimb():
    print('You decide to climb the cave. The cave is very tall and your arms are getting tired.')
    caveClimbChoice = input('Do you keep climbing the cave(up), or head down(down)? ')
    if(caveClimbChoice.lower()== 'up'):
        print('You keep climbing up the cave, and the top seems unreachable. After 10 minutes of climbing your arms tire out, you miss an arm grip and fall.')
        gameOver()
    elif(caveClimbChoice.lower()== 'down'):
        print('You arrive back at the bottom of the cave and walk back to the sign where you are presented with three choices again.')
        reset()
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
  
         #gloabl = rigt

def snakeFight():
    snakeFightWeapon = input('You decide to fight the snake. Around you, you see a stick and a rock. Which one do you use to defend yourself? ')
    if(snakeFightWeapon.lower() =='stick'):
        print('--------------------')
        print('After 5 minutes of fighting, your stick snaps and the cobra bites you. You try to run and get help, but the poison quickly kills you and you die.')
        gameOver()
        
    elif(snakeFightWeapon.lower() == 'rock'):
        print('--------------------')
        print('You manage to defeat the snake with your stick, but are extremely injured and tired. You take a short nap and then head back to the crossroads and try a new path.')
        reset()
def snakeRun():
    snakeRunChoice = input('You decide to run away from the snake. Do you keep heading deeper into the forest(forward) or go back to the intersection(go back)? ')
    if(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and arrive back at the 3-way intersection')
        reset()
    elif(snakeRunChoice.lower == 'go back'):
        print('--------------------')
        print('You run away from the snake and it almost catches you, but you spring your way deep into the forest.')
        #global lebel = forward

def snakeSneak():
    snakeSneakLocation = input('You crawl and the floor to avoid the snake. The snake seems to be unaware of your presence and you have the opportunity to run away. Do you keep heading into the forest(yes/no)?')
    if(snakeSneakLocation.lower() == 'no'):
        print('--------------------')
        print('You successfully sneak away from the snake and arrive back at the three way crossroad')
        print('--------------------')
        reset()
    elif(snakeSneakLocation.lower() == 'yes'):
        print('--------------------')
        print('You successfully sneak away from the snake and continue heading down the path into the unknown.')
        #global level, levle = forward
def buildingMailbox():
    print('You open the mailbox and see a old, yellowing peace of cardstock, on the back it says:')
    print('Hello traveler, I see you have found my note. /n This park is home to a long lost tresure, a diamond star. /n To claim this star, there is a key hidden somewhere in the park. /n Find the key, claim the star, and look out for the dangers lurking in the park.')
    # do this in turtle
    mailBoxChoice = input('Do you leave the mailbox and try another on the the path choices in hopes of finding the key(leave), enter the visitor center(enter), or look at the sign?(sign)')
    if(mailBoxChoice.lower() == 'leave'):
        print("You leave the building to look for the key in another one of the park's paths. I wonder, will you have to come back to this center later?")
        reset()

    elif(mailBoxChoice.lower() == 'enter'):
        buildingEnter()
    elif(mailBoxChoice.lower() == 'sign'):
        buildingSign()
def buildingEnter():
    print('You enter the building and see a dark, ominous room.')
    buildingEnterChoice = input('Do you enter the room(enter), leave an go to the mailbox(mailbox), or leave and go to the sign(sign)? ')
    if(buildingEnterChoice.lower() == 'enter'):
        print('At the end of the room you see a vault, it seems that you need a key to open it.')
        if(hasKey == False):
            print("You don't have the key. Go try anothe path to find it.")
            reset()
        else:
            print('You use your key to open the vault. Inside their is a diamond star. You grab it and leave the park.')
            print('Congratulations you won the game!')
    elif(buildingEnterChoice.lower() == 'mailbox'):
        buildingMailbox()
    elif(buildingEnterChoice.lower() == 'sign'):
        buildingSign()
    
def buildingSign():

    
        

def goLeft():
    print('You walk down the left path, There are many vines and roots covering the path.')
    drawSnake()
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

def goStraight():
    print('You walk straight an arrive at an old building, it seems to be the old visitor center at the park. ')
    buildingChoice = input('In front of the building there is a sign and a mailbox. Do you enter the building(enter), read the sign(read), or open the mailbox(mailbox).  ')
    if(buildingChoice.lower()== 'enter'):
        buildingEnter()
    elif(buildingChoice.lower() == 'sign'):
        buildingSign()
    elif(buildingChoice.lower() =='mailbox'):
        buildingMailbox()
#def goForward():
   
    
    
### START GAME ----------------------------------------------------------------------------------------------------------------------------
def startGame():
    
    print('You begin heading up the trail. It is spooky, dark, misty, and you can barely see what is in front of you. Suddenly, you arrive at a 3-way fork in the road.')

    drawStartScreen()
    
    #draw 
    global sideChoice
    sideChoice = input('There is an old, cracked wooden sign. You try to read where the signs point to, but it is in a different language. Do you go left, right, or forward? ')

drawInstructions()   
print('It is a dawn and the sun has just risen. You decide to go on a hike at Pinewood park, an abandoned nature reserve near your house. Will you make it out alive, find the treasure, or die to the mysterious dangers lurking in the park?')
name = input('Welcome player. Please enter your name: ')
print(f'Hello {name}. ')
print('--------------------')

startGame()

###RUNGAME --------------------------------------------------------------------------------------------------------------------------
while(sideChoice.lower() == 'left' and isGameOver ==False):
    print('--------------------')
    goLeft()
    
   
    
 
while(sideChoice.lower() == 'right' and isGameOver ==False):
    print('--------------------')
    goRight()
        
while (sideChoice.lower() == 'forward' and isGameOver ==False):
    print('--------------------')
    goStraight()


       

#RIGHT SIDE + OPTIONS
#change








