import turtle
hasKey = False
left = False
xxxright= False
straight = False
starting = True
isGameOver = False


### TURTLE
import turtle
turtle.colormode(255)
turtle.hideturtle()
turtle.speed(10)



def rect(x,y,turn):
    #90 for right
    #-90 for left
    for i in range(2):
        turtle.forward(x)
        turtle.right(turn)
        turtle.forward(y)
        turtle.right(turn)

def alternateColor(length):
    for i in range (0,length,50):
        turtle.pencolor(106,153,78)
        turtle.forward(25)
        turtle.pencolor(167,201,87)
        turtle.forward(25)

def drawInstructions():
    turtle.speed(0)
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
    sides = 0
    turtle.speed(0)
    turtle.width(6)
    turtle.fillcolor(255,255,255)
    turtle.pencolor(130,86,43)
    turtle.begin_fill()
    
    while(sides < 4):
        turtle.forward(80)
        turtle.left(90)
        sides +=1
    
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
    rect(400,270,-90)
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
    rect(80,50,-90)
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
    rect(30,30,-90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(260,-230)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    
def drawSign():
    turtle.speed(0)
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
def drawCave():
    turtle.clear()
    turtle.speed(0)
    turtle.Screen().bgcolor(166,178,179)
    turtle.penup()
    turtle.goto(0,-450)
    turtle.pendown()
    turtle.pencolor(115,107,91)
    turtle.fillcolor(115,107,91)
    turtle.begin_fill()
    turtle.circle(350)
    turtle.penup()
    turtle.goto(-333,10)
    turtle.pendown()
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
    turtle.pendown()
    turtle.fillcolor(77,72,63)
    turtle.pencolor(77,72,63)
    turtle.begin_fill()
    turtle.circle(290)
    turtle.end_fill()
    turtle.pencolor(56,53,46)
    turtle.fillcolor(56,53,46)
    turtle.begin_fill()
    turtle.circle(260)
    turtle.end_fill()
    
    

    turtle.penup()
    turtle.goto(-500,-340)
    turtle.setheading(0)
    turtle.pensize(120)
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
    #talk abt num choices made
    print('--------------------')
    print('You died, restart the program to try again.')
    quit()
### SUBCHOICE FUNCTIONS ----------------------------------------------------------------------
      
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
        print('You arrive back at the bottom of the cave and walk back to the sign where you are presented with three choices again.')
        print('--------------------')
        reset()
def caveKeepWalking():
    global right
    print('--------------------')
    shed = input('You begin to walk around the cave and arrive at an old, rusting shed. Do you go in (yes/no)? ')
    if(shed.lower() == 'yes'):
        print('--------------------')
        print('You enter the shed and it is dark, you see cobwebs on the wall. It seems that nothing there is usefull, but suddenly on the shelf you see a old, gold key.')
        grabKey = input('Do you grab the key or leave it(grab/leave it)? ')
        if(grabKey.lower() == 'grab'):
            print('--------------------')
            print('You grab the key and place it in your pocket.')
            global hasKey
            hasKey == True
            whereToNext = input('Where do you go next? Back to the 3 way sign (start), the cave (cave), or the left path(left)? ')
            if(whereToNext.lower() == 'start'):
                print('--------------------')
                reset()
            elif(whereToNext.lower() == 'cave'):
              
              
                right = True
            elif(whereToNext.lower() == 'left'):
                global left
                left = True
        elif(grabKey.lower() == 'leave it'):
            print('--------------------')
            print('You leave the key and head back to the cave.')
            
            right = True
    elif(shed.lower() == 'no'):
         print('--------------------')
         print('You leave the shed and walk back to the cave')
     
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
        global right
        right = True

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
        global right
        right = True
def buildingMailbox():
    print('You open the mailbox and see a old, yellowing peace of cardstock, on the back it says:')
    print('Hello traveler, I see you have found my note. /n This park is home to a long lost tresure, a diamond star. /n To claim this star, there is a key hidden somewhere in the park. /n Find the key, claim the star, and look out for the dangers lurking in the park.')
    # do this in turtle
    mailBoxChoice = input('Do you leave the mailbox and try another on the the path choices in hopes of finding the key(leave), enter the visitor center(enter), or look at the sign?(sign)')
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
    print('You enter the building and see a dark, ominous room.')
    buildingEnterChoice = input('Do you enter the room(enter), leave and go to the mailbox(mailbox), or leave and go to the sign(sign)? ')
    if(buildingEnterChoice.lower() == 'enter'):
        print('--------------------')
        print('At the end of the room you see a vault, it seems that you need a key to open it.')
        if(hasKey == False):
            print("You don't have the key. Go try another path to find it.")
            reset()
        else:
            print('You use your key to open the vault. Inside their is a diamond star. You grab it and leave the park.')
            print('Congratulations you won the game!')
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
        print('On the back of the sign, you see a etching that you can read. It says that "the key is in a shed near a cave".')
        lookChoice = input('Do you go to the cave (cave), go to the building(building), or go to the mailbox(mailbox)? ')
        if(lookChoice.lower() == 'cave'):
            print('--------------------')
            goRight()
        elif(lookChoice.lower() == 'building'):
            print('--------------------')
            buildingEnter()
        elif(lookChoice.lower() == 'mailbox'):
            print('--------------------')
            buildingMailBox()

    while(buildingSignChoice.lower() == 'building'):
        print('--------------------')
        buildingEnter()
    while(buildingSignChoice.lower() == 'mailbox'):
        print('--------------------')
        buildingMailbox()

### STRUCTURE OF FIRST 3 CHOICE + THEIR OUTCOMES -----------------------------------------------------       

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
    drawCave()
    caveChoice = input('Do you go in, climb to see where you are(climb), or keep walking(walk)? ')
    if(caveChoice.lower() == 'go in'):
        caveGoIn()
    elif(caveChoice.lower() == 'climb'):
        caveClimb()
    elif(caveChoice.lower() == 'walk'):
        caveKeepWalking()

def goStraight():
    print('You walk straight an arrive at an old building, it seems to be the old visitor center at the park. ')
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
    while(left == True and isGameOver ==False):
        print('--------------------')
        goLeft()
    while(right ==True and isGameOver ==False):
        print('--------------------')
        goRight()
        
    while (straight == True and isGameOver ==False):
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
print('It is a dawn and the sun has just risen. You decide to go on a hike at Pinewood park, an abandoned nature reserve near your house. Will you make it out alive, find the treasure, or die to the mysterious dangers lurking in the park?')
name = input('Welcome player. Please enter your name: ')
print(f'Hello {name}. ')
print('--------------------')

startGame()
runGame()
