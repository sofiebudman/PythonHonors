#turtle import
import turtle
#flags
hasKey = False
left = False
right= False
straight = False
starting = True
isGameOver = False
hasKilledSnake = False

turtle.screensize(1000,800)

### TURTLE
import turtle
turtle.colormode(255)
turtle.hideturtle()
turtle.speed(10)

#turtle shape functions to make drawing more convient + reduce lines of the program
def parallellogram(x,y,xturn,yturn):
    #this function is used to make drawing other turtle object easier. It is similar to the rect function we used in cmucs academy
    #90 for right turn
    #-90 for left turn
    for i in range(2):
        #first use of for loop loop
        turtle.forward(x)
        turtle.right(xturn)
        turtle.forward(y)
        turtle.right(yturn)

def square(x,turn):
    sides = 0
    while (sides < 4):
        turtle.forward(x)
        turtle.right(turn)
        sides +=1

def circle(radius,fillcolor,pencolor):
    turtle.fillcolor(fillcolor)
    turtle.pencolor(pencolor)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def alternateColor(length):
    #used to alternate the color of snake depending on a desired length
    for i in range (0,length,50):
        #2nd for loop, used to alternate the snake color every 50 pixels
        turtle.pencolor(106,153,78)
        turtle.forward(25)
        turtle.pencolor(167,201,87)
        turtle.forward(25)

def drawInstructions():
    #this function draws the initial instructions for the game
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-250,40)
    turtle.pendown()
    turtle.write('The Treasure of Pinewood Park : \n A Chose Your Own Adventure Game', font = ('Courier New', 30, 'bold'))
    turtle.penup()
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.write("Welcome to this choose your own adventure game!", font = ('Courier New', 15,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("1. Navigate through many different paths of the park and try to collect the treasure." ,font = ('Courier New', 12,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("2. The game is best played with the turtle window and terminal window side by side.",font = ('Courier New', 12,'normal'))
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()
    turtle.write("3. Enjoy!",font = ('Courier New', 12,'normal'))
    
def drawLoseScreen():
    turtle.Screen().bgcolor(0,0,0)
    turtle.pencolor(255,255,255)
    turtle.clear()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,200)
    turtle.pendown()
    turtle.write('You Lose!', font = ('Courier New', 30, 'bold'), align = 'center')
    turtle.penup()
def drawWinScreen():
    turtle.Screen().bgcolor(0,0,0)
    turtle.pencolor(255,255,255)
    turtle.clear()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,200)
    turtle.pendown()
    turtle.write('You Win!', font = ('Courier New', 30, 'bold'), align = 'center')
def drawPath():
    #this function draws the three intersecting paths where the player is directed to make the first choice
    turtle.Screen().bgcolor(40,54,24)
    turtle.penup()
    turtle.pencolor(255,255,255)
    turtle.goto(0,0)
    turtle.pendown()
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
    
def drawWindow():
    #this function is used to draw the window of the building
    turtle.speed(0)
    turtle.width(6)
    turtle.fillcolor(255,255,255)
    turtle.pencolor(130,86,43)
    turtle.begin_fill()
    square(80,-90)
    turtle.end_fill()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(80)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(80)   
def drawBuilding():
    turtle.clear()
    turtle.speed(0)
    turtle.Screen().bgcolor(161,213,237)
    turtle.penup()
    turtle.goto(-500,-350)
    turtle.pencolor(64,107,69)
    turtle.width(100)
    turtle.pendown()
    turtle.forward(1000)
    turtle.penup()
    turtle.width(1)
    turtle.goto(-230,-300)
    turtle.fillcolor(130,86,43)
    turtle.pencolor(130,86,43)
    turtle.pendown()
    turtle.begin_fill()
    parallellogram(400,270,-90,-90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-280,-30)
    turtle.setheading(0)
    turtle.pencolor(163,28,28)
    turtle.fillcolor(163,28,28)
    turtle.width(7)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(500)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(402)
    turtle.left(60)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-190,-140)
    turtle.setheading(0)
    turtle.pendown()
    drawWindow()
    turtle.penup()
    turtle.goto(50,-140)
    turtle.pendown()
    drawWindow()
    turtle.penup()
    turtle.goto(-65,-298)
    turtle.pencolor()
    turtle.fillcolor()
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(70)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(120)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor(231,188,145)
    turtle.fillcolor(231,188,145)
    turtle.goto(-320,-300)
    turtle.setheading(90)
    turtle.width(10)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.goto(-380,-300)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.goto(-390,-287)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    parallellogram(80,50,-90,-90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(260,-300)
    turtle.setheading(90)
    turtle.pencolor(138,90,68)
    turtle.fillcolor(138,90,68)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.fillcolor(128,14,19)
    turtle.pencolor(128,14,19)
    turtle.width(1)
    turtle.goto(245,-250)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    square(30,-90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(260,-230)
    turtle.setheading(0)
    circle(15,(128,14,19),(128,14,19))

    
def drawSign():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
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
    turtle.write('> ,O./|**(-')
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.write('< !`C#^$*/{')

def drawSnake(): 
    turtle.clear()
    turtle.speed(10)
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.Screen().bgcolor(161,139,95)
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
    circle(50,(173,193,120),(173,193,120))
    #SNAKE EYES
    
    turtle.width(4)
    turtle.penup()
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20)
    circle(10,(0,0,0),(255,255,255))
    turtle.right(180)
    turtle.penup()
    turtle.forward(40)
    turtle.setheading(180)
    circle(10,(0,0,0),(255,255,255))
    #SNAKE MOUTH
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
def drawCave():
    turtle.clear()
    turtle.speed(0)
    turtle.Screen().bgcolor(166,178,179)
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(0,-450)
    circle(350,(115,107,91),(115,107,91))
    turtle.penup()
    turtle.goto(-333,10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(260)
    turtle.forward(390)
    turtle.right(260)
    turtle.forward(800)
    turtle.right(260)
    turtle.forward(280)
    turtle.left(80)
    turtle.forward(708)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0,-420)
    turtle.setheading(0)
    circle(290,(77,72,63),(77,72,63))
    circle(260,(56,53,46),(56,53,46))
    turtle.penup()
    turtle.goto(-500,-400)
    turtle.setheading(0)
    turtle.pensize(240)
    turtle.pendown()
    turtle.pencolor(19,97,40)
    turtle.forward(1000)

def drawStartScreen():
    turtle.width(1)
    turtle.clear()
    turtle.speed(0)
    drawPath()
    drawSign()

###GENERAL FUNCTIONS ----------------------------------------------------------------------

def reset():
    global starting
  
    global left
    global right
    global straight
   
    left = False
    right= False
    straight = True
    startGame()
    runGame()
def gameOver():
    global gameOver
    gameOver = True
    global left
    global right
    global straight
    left = False
    right = False
    straight = False
    #talk abt num choices made
    print('--------------------')
    print('You died, restart the program to try again.')
    drawLoseScreen()

### SUBCHOICE FUNCTIONS ----------------------------------------------------------------------
      
def caveGoIn():
    print('You enter the cave. It is dark and hard to see anything. Suddenly, a bear is coming at you.')
    caveGoInChoice = input('Do you try to fight, run, or hide from the bear? ')
    if(caveGoInChoice.lower() == 'fight'):
        print('--------------------')
        print('You try to fight the bear, but is is much stronger then you. You die.')
        gameOver()
        
    elif(caveGoInChoice.lower() == 'run'):
        print('--------------------')
        print('You try to run from the bear, but it is much faster than you. You die')
        gameOver()
        
    elif(caveGoInChoice.lower()== 'hide'):
        print('--------------------')
        print('You hide from the bear and it goes back to sleep. You exit the cave.')
        caveKeepWalking()
def caveClimb():
    print('--------------------')
    print('You decide to climb the cave. The cave is very tall and your arms are getting tired.')
    caveClimbChoice = input('Do you keep climbing the cave(up), or head down(down)? ')
    if(caveClimbChoice.lower()== 'up'):
        print('--------------------')
        print('You keep climbing up the cave, and the top seems unreachable. After 10 minutes of climbing your arms tire out, you miss an arm grip and fall.')
        gameOver()
    elif(caveClimbChoice.lower()== 'down'):
        print('--------------------')
        print('You arrive back at the bottom of the cave and are able to chose a new option.')
        print('--------------------')
        goRight()
def caveKeepWalking():
    global right
    print('--------------------')
    shed = input('You begin to walk around the cave and arrive at an old, rusting shed. Do you go in (yes/no)? ')
    if(shed.lower() == 'yes'):
        print('--------------------')
        print('You enter the shed and it is dark, you see cobwebs on the wall. It seems that nothing there is useful, but suddenly on the shelf you see a old, gold key.')
        grabKey = input('Do you grab the key or leave it(grab/leave it)? ')
        if(grabKey.lower() == 'grab'):
            print('--------------------')
            print('You grab the key and place it in your pocket.')
            global hasKey
            hasKey = True
            whereToNext = input('Where do you go next? Back to the 3 way sign (start), the cave (cave), or the left path(left)? ')
            if(whereToNext.lower() == 'start'):
                print('--------------------')
                reset()
            elif(whereToNext.lower() == 'cave'):
              
              
                right = True
            
            elif(whereToNext.lower() == 'left'):
                global left
                left = True
                right = False


        elif(grabKey.lower() == 'leave it'):
            print('--------------------')
            print('You leave the key and head back to the cave.')
            
            right = True

    elif(shed.lower() == 'no'):
         print('--------------------')
         print('You leave the shed and walk back to the cave.')
     
         right = True

def snakeFight():
    snakeFightWeapon = input('You decide to fight the snake. Around you, you see a stick and a rock. Which one do you use to defend yourself? ')
    if(snakeFightWeapon.lower() =='stick'):
        print('--------------------')
        print('After 5 minutes of fighting, your stick snaps and the cobra bites you. You try to run and get help, but the poison quickly kills you and you die.')
        gameOver()
        
    elif(snakeFightWeapon.lower() == 'rock'):
        print('--------------------')
        print('You manage to defeat the snake with your stick, but are extremely injured and tired. You take a short nap and then head back to the crossroads and try a new path.')
        global hasKilledSnake
        hasKilledSnake = True
        print('--------------------')
        reset()
def snakeRun():
    snakeRunChoice = input('You decide to run away from the snake. Do you run at average speed to avoid tiring out (average) or full speed to make sure you escape(full)? ')
    if(snakeRunChoice.lower() == 'average'):
        print('--------------------')
        print('You run at average speed in hopes of saving energy, but the snake catches up to you.')
        gameOver()
    elif(snakeRunChoice.lower() == 'full'):
        print('--------------------')
        print('You run away from the snake at full speed and it almost catches you, but you escape into the forest.')
        global right
        right = True
        global left
        left = False

def snakeSneak():
    snakeSneakLocation = input('You crawl on the floor to avoid the snake. The snake seems to be unaware of your presence and you have the opportunity to run away. Do you keep heading into the forest(yes/no)?')
    if(snakeSneakLocation.lower() == 'no'):
        print('--------------------')
        print('You successfully sneak away from the snake and arrive back at the three way crossroad')
        print('--------------------')
        reset()
    elif(snakeSneakLocation.lower() == 'yes'):
        print('--------------------')
        print('You successfully sneak away from the snake and continue heading down the path into the unknown.')
        global right
        right = True
        global left
        left = False
def buildingMailbox():
    print('You open the mailbox and see a old, yellowing piece of paper. On the back it says:')
    print('~~~~~~~~~~~~~~~~~~\n Hello traveler, I see you have found my note.\n This park is home to a long lost treasure, a diamond star.\n To claim this star, there is a key hidden in the park.\n Find the key, claim the star, and look out for the dangers lurking in the park.\n~~~~~~~~~~~~~~~~~~')
    mailBoxChoice = input('Do you leave the mailbox and try another another path choice in hopes of finding the key(leave), enter the visitor center(enter), or look at the sign?(sign)? ')
    if(mailBoxChoice.lower() == 'leave'):
        print('--------------------')
        print("You leave the building to look for the key in another one of the park's paths. I wonder, will you have to come back to this center later?")
        reset()

    elif(mailBoxChoice.lower() == 'enter'):
        print('--------------------')
        buildingEnter()
    elif(mailBoxChoice.lower() == 'sign'):
        print('--------------------')
        buildingSign()
def buildingEnter():
    print('You enter the building and see a dark, foreboding room.')
    buildingEnterChoice = input('Do you enter the room(enter), leave and go to the mailbox(mailbox), or leave and go to the sign(sign)? ')
    if(buildingEnterChoice.lower() == 'enter'):
        print('--------------------')
        print('At the end of the room you see a vault.')
        roomChoice = input('Do you try to open the vault(yes/no)? ')
        if(roomChoice.lower() == 'yes'):

            if(hasKey == False):
                print('--------------------')
                print("To open the vault you need a key. You don't have the key. Go try another path to find it.")
                reset()
            else:
                print('--------------------')
                print('You use your key to open the vault. Inside their is a diamond star. You grab it and leave the park.')
                print('Congratulations you won the game!')
                drawWinScreen()
                global win
               
                global straight
                straight = False
        elif(roomChoice.lower() == 'no'):
            print('--------------------')
            roomNextChoice = input('You decide not to try opening the box. Where do you go next? The mailbox(mailbox) or sign(sign)? ')
            if(roomNextChoice.lower() == 'mailbox'):
                print('--------------------')
                buildingMailbox()
            elif(roomNextChoice.lower() == 'sign'):
                print('--------------------')
                buildingSign()

    elif(buildingEnterChoice.lower() == 'mailbox'):
        print('--------------------')
        buildingMailbox()
    elif(buildingEnterChoice.lower() == 'sign'):
        print('--------------------')
        buildingSign()
    
def buildingSign():
    print('You approach the sign, but it is worn down and in another language.')
    buildingSignChoice = input('Do you try to use the symbols to understand the signs meaning(decode), look around the sign(look), go to the building(building), or go to the mailbox(mailbox)? ')
    while(buildingSignChoice.lower() == 'decode'):
        print('--------------------')
        print('While trying to understand the meaning of the sign, you see 3 symbols you understand. One looks like a tree, the other looks like a stone, and the last looks like a skull. I wonder what these mean.')
        buildingSignChoice = input('Do you look around the sign(look), go to the building(building), or go to the mailbox(mailbox).')
    while(buildingSignChoice.lower() == 'look'):
        print('--------------------')
        print('On the back of the sign, you see an etching that you can read. It says that "the key is in a shed near a cave."')
        lookChoice = input('Do you go to the cave (cave), go to the building(building), or go to the mailbox(mailbox)? ')
        if(lookChoice.lower() == 'cave'):
            print('--------------------')
            goRight()
        elif(lookChoice.lower() == 'building'):
            print('--------------------')
            buildingEnter()
        elif(lookChoice.lower() == 'mailbox'):
            print('--------------------')
            buildingMailbox()

    while(buildingSignChoice.lower() == 'building'):
        print('--------------------')
        buildingEnter()
    while(buildingSignChoice.lower() == 'mailbox'):
        print('--------------------')
        buildingMailbox()

### STRUCTURE OF FIRST 3 CHOICE  -----------------------------------------------------       

def goLeft():
    print('You walk down the left path. There are many vines and roots covering the path.')
    if(hasKilledSnake == False):
        drawSnake()
        snakeChoice = input('Suddenly, you see a large vine ahead of you, but it is moving, and coming fast towards you. It is a King Cobra, around 10 feet tall whose poison could kill you in a matter of minutes. Do you fight, sneak, or run? ')
    
        if(snakeChoice.lower() == 'fight'):
            print('--------------------')
            snakeFight()
       
        if(snakeChoice.lower() == 'sneak'):
            print('--------------------')
            snakeSneak()
        
        if(snakeChoice.lower() == 'run'):
            print('--------------------')
            snakeRun()
    else:
        global left
        global right
        turtle.clear()
        turtle.Screen().bgcolor(161,139,95)
        print('You have already defeated the snake, try going to another path or continuing into the forest. ')
        nextMove = input('Do you go to the middle path (middle), continue into the forest(forest), or right path (right)? ')
        if(nextMove.lower() == 'middle'):
            global straight
            straight = True

            left = False
        elif(nextMove.lower() == 'right'):
            global right
            right = True
            left = False

        elif(nextMove.lower() == 'middle'):
            print('You continue walking through the forest for an hour.')

            right = True
            left = False
def goRight():
    print('After hiking you arrive at a large, ominous cave.')
    drawCave()
    caveChoice = input('Do you go in(go in), climb to see where you are(climb), or keep walking(walk)? ')
    if(caveChoice.lower() == 'go in'):
        print('--------------------')
        caveGoIn()
    elif(caveChoice.lower() == 'climb'):
        print('--------------------')
        caveClimb()
    elif(caveChoice.lower() == 'walk'):
        caveKeepWalking()

def goStraight():
    print('You walk straight and arrive at an old building. It seems to be the old visitor center at the park. ')
    drawBuilding()
    buildingChoice = input('In front of the building there is a sign and a mailbox. Do you enter the building(enter), read the sign(sign), or open the mailbox(mailbox).  ')
    if(buildingChoice.lower()== 'enter'):
        print('--------------------')
        buildingEnter()
    elif(buildingChoice.lower() == 'sign'):
        print('--------------------')
        buildingSign()
    elif(buildingChoice.lower() =='mailbox'):
        print('--------------------')
        buildingMailbox()
### RUN GAME ------------------------------------------------------------------------------------------------------------------
def runGame():
    while(left == True):
        print('--------------------')
        goLeft()
    while(right ==True ):
        print('--------------------')
        goRight()
        
    while (straight == True):
        print('--------------------')
        goStraight()

        
    
### START GAME ----------------------------------------------------------------------------------------------------------------------------
def startGame():
    
    print('You begin heading up the trail. It is spooky, dark, misty, and you can barely see what is in front of you. Suddenly, you arrive at a 3-way fork in the road.')

    drawStartScreen()
    
    global left
    global right
    global straight
  
    choice = input('There is an old, cracked wooden sign. You try to read where the signs point to, but it is in a different language. Do you go left, right, or forward? ')
    if(choice.lower() == 'left'):
        left = True
    elif(choice.lower() == 'right'):
        right = True
    elif(choice.lower() == 'forward'):
        straight = True
drawInstructions()   
print('It is a dawn and the sun has just risen. You decide to go on a hike at Pinewood Park, an abandoned nature reserve near your house. Will you make it out alive, find the treasure, or die to the mysterious dangers lurking in the park?')
name = input('Welcome player. Please enter your name: ')
print(f'Hello {name}. ')
print('--------------------')

startGame()

while(isGameOver == False):
    runGame()


 