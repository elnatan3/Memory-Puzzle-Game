from Card_Class import *
from button import *
import time
import random
from graphics2 import *
'''
Assistance- Button Class produced by Dr.Stonedahl
'''

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


def titlePageWindow():
    '''creates the welcome page window and asks the user to press Enter to continue.'''
    #Creates new window and adds text
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    bgImage = Image(Point(300,300), "memoryGame.gif")
    bgImage.draw(window)
    titleOfGameText = Text(Point(300, 250), f"Welcome to... \n Memory Card Game!")
    titleOfGameText.setSize(25)
    titleOfGameText.setTextColor("purple")
    titleOfGameText.setStyle("bold")
    titleOfGameText.draw(window)
    directionToContinueText = Text(Point(300, 400), f"Press Enter to Continue")
    directionToContinueText.setStyle("bold italic")
    directionToContinueText.setTextColor("red")
    directionToContinueText.setSize(15)
    directionToContinueText.draw(window)
    
    #button to continue     
    keyPressed = window.getKey()
    while keyPressed != 'Return':
        keyPressed = window.getKey()
    window.close()
    
    
def setUpInstructions():
    ''' creates the window that tells the users how to play the game
        and asks the user to enter the label type of their choice that will asked of them later in the game.
        this function returns the window'''

    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('pink')
    
    #provides an overview for the game.
    titleText = Text(Point(300,50), "How this game Works?")
    titleText.setSize(18)
    titleText.setTextColor("dark blue")
    titleText.setStyle("bold")
    titleText.draw(window)
    
    #provides direction on how to play game
    directionsText = Text(Point(300, 200), f"Different shapes and colors with labels will appear on the grid.\n"
                                                                    "You'll be asked to match the label \n"
                                                                    " with the shape and color that contains it.\n\n"
                                                                    "This game has four levels. Each level is more challenging\n than the previous."
                                                                    " Each level will most likely ask the player \n to match a new label."
                                                                    " When the correct card is matched,\n"
                                                                    "the scores will be updated accordingly\n\n")
    directionsText.draw(window)
    
    
    #provides hint
    hintText = Text(Point(300,300), "Hint: the position of the cards do not change through each level.")
    hintText.setTextColor("green")
    hintText.draw(window)
    
    
    #creates text for the user to enter label 
    prompt = Text(Point(200,400),"Choose a label type (letter or number)?")
    prompt.setTextColor("purple")
    prompt.setStyle("bold italic")
    prompt.draw(window)
    
    return window

    
def getLabel(window):
    '''creates the submit button and checks the if the appropriate label is typed
        then returns the label.'''
    #Asks the user to enter a label
    chooseLabel = Entry(Point(450,400),7)
    chooseLabel.draw(window)
    
    #creates submit button
    submit = Button(Point(300, 490), 100, 30, f"Submit")
    submit.activate()
    submit.draw(window)
    
    #waits until user has clicked on the button 
    click = window.getMouse()
    while not submit.isClicked(click):
        click = window.getMouse()
        
    #checks whether the label entered is valid.
    labelResponse = chooseLabel.getText()
    labelResponse = labelResponse.lower()
    while labelResponse != "letter" and labelResponse != "number":
        error = Text(Point(200, 450), "ENTER APPROPRIATE LABEL!")
        error.setTextColor("red")
        error.setStyle("bold italic")
        error.draw(window)
        time.sleep(1)
        error.undraw()
        
        #waits until user has clicked on the button then checks the text in the entry
        click = window.getMouse()
        while not submit.isClicked(click):
            click = window.getMouse()
            
        labelResponse = chooseLabel.getText()
        labelResponse = labelResponse.lower()
        
    return labelResponse
    
    
def drawGridForShapes():
    ''' returns the window for the grids'''
    #creates the window and returns it
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    window.setCoords(0,600,600,0)
    
    #horizontal lines
    Line(Point(0,200),Point(600,200)).draw(window)
    Line(Point(0,400),Point(600,400)).draw(window)
    
    #vertical lines
    Line(Point(200,0),Point(200,600)).draw(window)
    Line(Point(400,0),Point(400,600)).draw(window)
    return window
    
    
def drawEachCard(window,labelResponse):
    ''' reads through label file and randomly creates the shape, one color, and one label for each card
        then draws it in the grid window'''
    #creates list of lists for the grid and a list for each object(shape, color, label).
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    shapeList = ['Triangle', 'Square', 'Circle']
    colorList = ['red', 'green', 'yellow', 'blue', 'pink', 'grey', 'orange', 'purple', 'white']
    labelList = []
    
    #Based on what the user entered for the label, opens a txt file, retrieves the data, and adds it to the label list. 
    if labelResponse == "letter":
        fileName = open("letter.txt","r")
        for letter in fileName:
            labelList.append(letter.strip())
    else:
        fileName = open("num.txt","r")
        for number in fileName:
            labelList.append(number.strip())
            
    #randomly chooses a shape, color, and label, and draws it in the grid.
            
    y = 100
    for row in range(len(grid)):
        x = 100
        for col in range(len(grid[row])):
    
            randomShape = random.choice(shapeList)
            randomColor = random.choice(colorList)
            randomLabel = random.choice(labelList)
            
            #removes duplicates
            colorList.remove(randomColor)
            labelList.remove(randomLabel)
            
            grid[row][col] = Card(Point(x,y), randomShape, randomColor, randomLabel)
            grid[row][col].draw(window)
            
            x += 200
        y += 200    
    time.sleep(7)
    
    window.close()
    
    return grid
        
            
def displayQuestion(grid):
    ''' creates the questions window, submit button, and then randomly chooses a label to ask the user
        then calls the userGuess function, passes the parameters and returns it'''
    #creates a new window
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("yellow")
    
    #creates text to draws in the window.
    directions = Text(Point(300, 100), f"Now its Time To Guess\n"
                                        "which shape and color has this label")
    directions.setTextColor("red")
    directions.setSize(20)
    directions.draw(window)
    labelText = Text(Point(200, 400), "LABEL IS ...")
    labelText.draw(window)
    time.sleep(1)
    
    # randomly chooses a label from the grid.
    card = random.choice((random.choice(grid)))
    labelOfCard = card.getLabel().getText()
    label = Text(Point(400, 400), labelOfCard)
    label.setSize(36)
    label.draw(window)
    
    #creates text and entry object to prompt the user to enter shape and color.
    kindOfShape = Text(Point(120, 200), "What Kind of Shape is it?")
    kindOfColor = Text(Point(120, 300), "What Kind of Color is it?")
    kindOfShape.draw(window)
    kindOfColor.draw(window)
    entryForShape = Entry(Point(300, 200), 10)
    entryForColor = Entry(Point(300, 300), 10)
    entryForShape.draw(window)
    entryForColor.draw(window)
    
    #creates the submit button and activates it.
    submit = Button(Point(400, 250), 100, 30, "Submit")
    submit.activate()
    submit.draw(window)
    
    #calls the getUserGuess function and returns it.
    userGuess = getUserGuess(window, entryForShape, entryForColor, card, submit)
    return userGuess

            
def getUserGuess(window, entryForShape, entryForColor, card, submit):
    ''' gets the user guess, and calls the checkUserGuess function
        then passes the parameters and returns it'''
    #checks until mouse is clicked.
    click = window.getMouse()
    while not submit.isClicked(click):
        click = window.getMouse()
        
    #returns the string of text in each entry box.
    shapeEntered = entryForShape.getText()
    shapeEntered = shapeEntered.title()
    colorEntered = entryForColor.getText()
    colorEntered = colorEntered.lower()
    
    #calls the ckeckUserGuess functions and returns it.
    userGuessIsCorrect = checkUserGuess(shapeEntered, colorEntered, card)
    
    window.close()
    return userGuessIsCorrect
    
          
def checkUserGuess(shapeEntered, colorEntered, card):
    ''' gets the user guess, correct answers and compares them, then return text according
        to user response'''
    #return the shape and color of the color from the Card Class.
    correctShape = card.getShape()
    correctColor = card.getColor()
    
    displayCorrectCard(card)
         
    #compares the attributes of the card with what the user has the entered and returns specific values.
    if shapeEntered == correctShape and colorEntered == correctColor:
        return 'both'
    elif shapeEntered == correctShape:
        return 'shape'
    elif colorEntered == correctColor:
        return 'color'
    else:
        return 'neither'
    
    
def displayCorrectCard(card):
    ''' creates a window that displays a rotating shape and color of the correct card'''
    #creates new window
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("black")
    
    #returns the correct card shape and color
    correctCardShape = card.getShape()
    correctCardColor = card.getColor()
    cardLabel = card.getLabel().getText()
    
    #displays text for correct shape and color
    shapeAndColorText = Text(Point(300,300), "This is the correct shape and color\n"
                             f"for the label ({cardLabel})") 
    shapeAndColorText.setTextColor('white')
    shapeAndColorText.setSize(13)
    shapeAndColorText.draw(window)
    
    #draws the correct shape and color
    if correctCardShape == 'Triangle':
        polygon = Polygon(Point(100,50),Point(150,150), Point(50,150))
        polygon.setFill(f'{correctCardColor}')
        polygon.draw(window)
    
    #orbits the shape and color
        for i in range(80):
            polygon.orbitAround(5,Point(300,300))
            time.sleep(0.06)
            
    elif correctCardShape == 'Square':
        square = Rectangle(Point(50,50),Point(150,150))
        square.setFill(f'{correctCardColor}')
        square.draw(window)
        
        #orbits the shape and color
        for i in range(80):
            square.orbitAround(5,Point(300,300))
            time.sleep(0.06)
    
    elif correctCardShape == 'Circle':
        circle = Circle(Point(100,100),60)
        circle.setFill(f'{correctCardColor}')
        circle.draw(window)
        
        #orbits the shape and color
        for i in range(80):
            circle.orbitAround(5,Point(300,300))
            time.sleep(0.06)
    window.close()
    

def resultsScreen(userGuessIsCorrect, score):
    ''' gets the text called from checkUserGuess and then creates a window based on userguess
        then adds the score and return the score'''

    #displays background and text based on whether the user has entered the correct values then adds to the score and return it.
    if userGuessIsCorrect == 'both':
        window = GraphWin("Results Pending...", WINDOW_WIDTH, WINDOW_HEIGHT)
        bgImage = Image(Point(300,300), "Excellent.gif")
        bgImage.draw(window)
        text = Text(Point(300,500),"You have found both the Shape and Color of this label. \n"
                                    "+5 score \n")
        text.setStyle('bold')
        text.draw(window)
        score += 5
    elif userGuessIsCorrect == 'shape':
        window = GraphWin("Results Pending...", WINDOW_WIDTH, WINDOW_HEIGHT)
        bgImage = Image(Point(300,300), "goodJob.gif")
        bgImage.draw(window)
        text = Text(Point(300,500),f"You have found the shape of this label. \n"
                                    "+2 score \n"
                                    "BUT, you have not found the color.")
        text.setStyle('bold')
        text.draw(window)
        score += 2
    elif userGuessIsCorrect == 'color':
        window = GraphWin("Results Pending...", WINDOW_WIDTH, WINDOW_HEIGHT)
        bgImage = Image(Point(300,300), "goodJob.gif")
        bgImage.draw(window)
        text = Text(Point(300,500),f"You have found the color of this label. \n"
                                    "+3 score \n"
                                    "BUT, you have not found the shape.")
        text.setStyle('bold')
        text.draw(window)
        score += 3
    elif userGuessIsCorrect == 'neither':
        window = GraphWin("Results Pending...", WINDOW_WIDTH, WINDOW_HEIGHT)
        bgImage = Image(Point(300,300), "Nicetry.gif")
        bgImage.draw(window)
        text = Text(Point(300,500),f"But, you have not found neither shape or color of this label.\n"
                                    "+0 score")
        text.setStyle('bold')
        text.draw(window)
        score += 0
        
    time.sleep(4)
    window.close()
        
    return score    
           
    
def getLevel(levelNum):
    ''' creates a window and button for the levels'''
    #creates a new window
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("ivory")
    bgImage = Image(Point(300,300), "level.gif")
    bgImage.draw(window)
    
    #creates button for the labels
    level = Button(Point(300, 300), 200, 30, f"{levelNum}")
    level.activate()
    level.draw(window)
    
    #waits until user has clicked on the button then closes the window
    click = window.getMouse()
    while not level.isClicked(click):
        click = window.getMouse()
    window.close()       
            
        
def calculateEachScore(scoreList):
    ''' returns the window that displays a row and column of results for each level.'''
    #creates a new window and returns it
    window = GraphWin("Memory Card Game", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("yellow")
    
    #creates the text to be displayed on the window
    levels = Text(Point(100,50), "Levels")
    levels.setStyle('bold italic')
    levels.draw(window)
    scores = Text(Point(200,50), "Scores")
    scores.setStyle('bold italic')
    scores.draw(window)
    levelOne = Text(Point(100,100), "Level 1")
    levelOne.draw(window)
    levelTwo = Text(Point(100,150), "Level 2")
    levelTwo.draw(window)
    levelThree = Text(Point(100,200), "Level 3")
    levelThree.draw(window)
    levelFour = Text(Point(100,250), "Level 4")
    levelFour.draw(window)
    
    #gets the values from the score list and aligns it with the appropriate label.
    scoreForLevelOne = scoreList[0]
    displayLevelOneScore = Text(Point(200,100), f"{scoreForLevelOne}")
    displayLevelOneScore.draw(window)
    scoreForLevelTwo = scoreList[1]
    displayLevelTwoScore = Text(Point(200,150), f"{scoreForLevelTwo}")
    displayLevelTwoScore.draw(window)
    scoreForLevelThree = scoreList[2]
    displayLevelThreeScore = Text(Point(200,200), f"{scoreForLevelThree}")
    displayLevelThreeScore.draw(window)
    scoreForLevelFour = scoreList[3]
    displayLevelFourScore = Text(Point(200,250), f"{scoreForLevelFour}")
    displayLevelFourScore.draw(window)

    return window


def calculateTotalScore(window, scoreList):
    ''' calculates the total score from the score list and draws it in the window'''
    #adds the scores in the score list.
    theSum = 0
    for i in range(len(scoreList)):
        theSum = theSum + scoreList[i]
        
    #creates text to be displayed on the window.
    totalScoreText = Text(Point(100, 350), "Total Score")
    totalScoreText.setStyle('bold')
    totalScoreText.draw(window)
    
    #displays the total score aligned with the text.
    totalScoreValue = Text(Point(200,350), f"{theSum}") 
    totalScoreValue.setStyle('bold')
    totalScoreValue.draw(window)
    
    return theSum
    
    
def displayRecordScore(displayScoreWindow, totalScore, recordScore):
    ''' while play again is true, it displays the record score of the player based on total score'''
    #calculates record and displays it on the screen
    recordText = Text(Point(400, 100), "Recent record:")
    recordText.draw(displayScoreWindow)
    recordScore['largestScore'] = recordScore.get('largestScore',0)
    if totalScore > recordScore['largestScore']:
        recordScore['largestScore'] = totalScore
        recordScore = Text(Point(500, 100), f"{totalScore}")
        recordScore.draw(displayScoreWindow)
    else:
        recordScore = Text(Point(500, 100), f"{recordScore['largestScore']}")
        recordScore.draw(displayScoreWindow)
        
    
def playAgainOrNot(window):
    ''' creates the play again and quit button, draw it on the window, and return True or False
        based on what the user clicked'''
    #creates play again and quit button.
    playAgain = Button(Point(200, 450), 100, 30, "Play Again")
    playAgain.activate()
    playAgain.draw(window)
    quitGame = Button(Point(500, 450), 100, 30, "Quit")
    quitGame.activate()
    quitGame.draw(window)
        
    #checks until play again or quit button is clicked
    click = window.getMouse()
    while not(playAgain.isClicked(click) or quitGame.isClicked(click)):
        click = window.getMouse()
    if playAgain.isClicked(click):
        window.close()
        return True
    if quitGame.isClicked(click):
        window.close()
        return False
    
    
def main():
    titlePageWindow()
    window = setUpInstructions()
    recordScore = {}
    playAgain = True
    #checks until play again is false
    while playAgain:
        #returns the label response of the user
        labelResponse = getLabel(window)
        
        #creates the button for level one
        getLevel("Level 1")
        
        #returns the game Window
        gameWindow = drawGridForShapes()
        
        #returns the grid for the objects
        grid = drawEachCard(gameWindow,labelResponse)
        
        # returns the values for the user's guesses 
        userGuessIsCorrect = displayQuestion(grid)
        
        #creates a score list 
        scoreList = []
        score = 0
        
        #returns the score for label one and appends it into the score list.
        levelOneScore = resultsScreen(userGuessIsCorrect, score)
        scoreList.append(levelOneScore)
        
        
        #creates button for level two and waits untils its clicked
        getLevel("Level 2")
        
        #returns the game Window
        gameWindow = drawGridForShapes()
        
        #creates the object and displays it in the game window
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                polygon = grid[row][col]
                polygon.draw(gameWindow)
                time.sleep(1.5)        
        gameWindow.close()
        
        #returns the values for the user's guesses 
        userGuessIsCorrect = displayQuestion(grid)
        
        #returns the score for label two and appends it into the score list.
        levelTwoScore = resultsScreen(userGuessIsCorrect, score)
        scoreList.append(levelTwoScore)
        
        #creates button for level three and waits untils its clicked
        getLevel("Level 3")
        
        #returns the game Window
        gameWindow = drawGridForShapes()
        
        #creates the object in each row, pauses for one second, then pauses for 3 seconds before closing the window.
        for rowObjects in range(len(grid)):
            for colObjects in range(len(grid[row])):
                grid[rowObjects][colObjects].draw(gameWindow)
            time.sleep(2)
        time.sleep(1.5)    
        gameWindow.close()
        
        #returns the values for the user's guesses 
        userGuessIsCorrect = displayQuestion(grid)
        
        #returns the score for label three and appends it into the score list.
        levelThreeScore = resultsScreen(userGuessIsCorrect, score)
        scoreList.append(levelThreeScore)
        
        #creates button for level four and waits untils its clicked.
        getLevel("Level 4")
        
        #returns the game Window
        gameWindow = drawGridForShapes()
        
        # creates the shapes and colors of each labels in the grid and makes them disappear after one second
        for rowObjects in range(len(grid)):
            for colObjects in range(len(grid[row])):
                grid[rowObjects][colObjects].draw(gameWindow)
                time.sleep(1.5)
                grid[rowObjects][colObjects].undraw()
        gameWindow.close()
        
        #returns the values for the user's guesses 
        userGuessIsCorrect = displayQuestion(grid)
        
        #returns the score for label four and appends it into the score list.
        levelFourScore = resultsScreen(userGuessIsCorrect, score)
        scoreList.append(levelFourScore)
        
        #returns window created by calculateEachScore function
        displayScoreWindow = calculateEachScore(scoreList)
        
        #Calculates the total score and displays it in the window created by calculateEachScore function
        totalScore = calculateTotalScore(displayScoreWindow, scoreList)
        
        #compares the record score with the total score then display the recent record score on the window
        displayRecordScore(displayScoreWindow, totalScore, recordScore)
        
        #return 'True' if the user clicked on play again button and 'False' otherwise
        playAgain = playAgainOrNot(displayScoreWindow)
        
        
        
     
             
main()    

