###############################################################################
#   Members: Matthew Macias, Gavin Phillips, (Chris Dilley but not really)
#   Mission: Run an RPi as a gaming console that takes games in its directory
#               and executes them to the player's choice
#
###############################################################################

# Initial Import statements

import sys
from time import time, sleep
from os import listdir
import pygame


# GUI Setup
pygame.init()
buttonSel   = pygame.image.load(("buttonPressed.gif"))
buttonUnsel = pygame.image.load(("buttonUnpressed.gif"))
upArrow     = pygame.image.load(("upArrow.gif"))
background = pygame.image.load("tower.gif")

# Scans the GameFiles directory for games and stores their names
def pullGames():
    global gamesFont
    gameList = []
    gameText = []
    gamesImg = []
    print "Scanning for games..."
    # Checks each directory within GameFiles
    for game in listdir("GameFiles"):
        # Adds a name, label, and image for each game to their corrseponding lists
        gameList.append(game)
        gameText.append(gamesFont.render(game, False, (255,255,0)))
        gamesImg.append(pygame.image.load(("GameFiles/{}/IMG.gif".format(game))))
        # Scales images from imported games
        gamesImg[len(gameList)-1] = pygame.transform.scale(gamesImg[len(gameList)-1],(416,288))
        print " {}.  {} retrieved".format(len(gameList),game)
    print "All compatible games retrieved!"
    return gameList, gameText, gamesImg

def resetWindow():
    global gameDisplay, winHeight, winWidth, winTitle
    winWidth, winHeight = 800,416
    winTitle = "PiRIS Home"
    pygame.display.set_caption(winTitle)
    gameDisplay = pygame.display.set_mode((winWidth, winHeight))




def render():
    # Bottom Layer 1 - Background
    gameDisplay.blit(background, [0, 0])
    # Layer 2 - 32 x 32 px Gridlines
    for x in range(0,winWidth, 32):
        for y in range(0,winHeight, 32):
            pygame.draw.rect(gameDisplay, (150,150,150), (x, y, 33, 33), 1)
    # Layer 2 - boxes and buttons
    # Displays the selected game's image
    pygame.draw.rect(gameDisplay, (0,0,0), (316,92, 424, 296))
    gameDisplay.blit(gamesImg[sel], [320, 96])
    

    # Displays the Title Text
    gameDisplay.blit(title, (112, 16))
    




########################################################
# Main Section, establishes the GUI and loops the menu
########################################################

# Static Variable setup
gamesFont = pygame.font.SysFont("verdana",36)
# Larger font for title
titleFont = pygame.font.SysFont("verdana",48)
title  = titleFont.render("Welcome to the PiRIS", False, (255,255,0))
Running = True
isRunning = True
scrolling = 0
sel = 0
scrollAmt = 0

# Imported information when pulling games
gameList, gamesText, gamesImg = pullGames()


# Initialize the Home Screen
resetWindow()


# Menu Loop
while isRunning:
    # Ignores buttons while scrolling
    if (not scrolling):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                isRunning = 0
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    isRunning = 0
                elif (event.key == pygame.K_UP and sel > 0):
                    scrolling = -1
                elif (event.key == pygame.K_DOWN and sel < len(gameList)-1):
                    scrolling = 1
                elif (event.key == pygame.K_SPACE):
                    execfile("./GameFiles/{}/Main.py".format(gameList[sel]))

    # Scrolling active
    else:
        # Runs until one button reaches 96 pixels below or above (where the next button was)
        if(scrollAmt == 96 or scrollAmt == -96):
            scrollAmt = 0
            #print "Scroll complete"
            # increment the selected game after scrolling
            sel += scrolling
            scrolling = 0
        # Increases scrolling offset for buttons and labels
        else:
            scrollAmt += 6*scrolling

    

    # Renders lower layer objects
    render()

    # Layer 2 - Buttons
    if (sel > 0):
        gameDisplay.blit(upArrow, [32,32])
    # Displays the selected games


    # Determines how close it is to the end of the list, only renders the possible ones
    if (sel < len(gameList) - 4):
        gMax = 4
    elif (sel == len(gameList) - 3):
        gMax = 3
    elif (sel == len(gameList) - 2):
        gMax = 2
    elif (sel == len(gameList) - 1):
        gMax = 1
    # Renders a fourth game that shows only when scrolling down
    for game in range(sel, sel + gMax):
        if (game == sel):
            # every 96 pixels vertically there is a button
            # Note the scrollAmt offset
            gameDisplay.blit(buttonSel, [32, 128 + (game-sel)*96 - scrollAmt])
        else:
            gameDisplay.blit(buttonUnsel, [32, 128 + (game-sel)*96 - scrollAmt])
    # Layer 3 - Text
        # Displays game labels over buttons
        gameDisplay.blit(gamesText[game],(48, 136+(game-sel)*96 - scrollAmt))
        # Displays the Title Text - render redundant, but goes over buttons for scrolling
        gameDisplay.blit(title, (112, 16))

    # Upload rendered bits to the screen
    pygame.display.update()
    # Next frame
    sleep(0.016)

    # Remembers if a game was running previously
    if not Running:
        title  = titleFont.render("Welcome BACK to the PiRIS", False, (255,255,0))
        # Some games not default may reconfig the window
        resetWindow()
        
# Cleanup process
pygame.quit()
sys.exit()
