
##########################################################
#   Members: Matthew Macias, Gavin Phillips, Chris Dilley
#
#
##########################################################

import sys
from time import time, sleep
from os import listdir
import pygame


# GUI Setup
pygame.init()
buttonSel   = pygame.image.load(("buttonPressed.gif"))
buttonUnsel = pygame.image.load(("buttonUnpressed.gif"))
upArrow     = pygame.image.load(("upArrow.gif"))

# Scans the GameFiles directory for games and stores their names
def pullGames():
    global gamesFont
    gameList = []
    gameText = []
    gamesImg = []
    print "Scanning for games..."
    # Checks each directory within GameFiles
    for game in listdir("GameFiles"):
        # Runs the placeholder name file within it
        # It is better used to pull a game's logo rather than name\
        #   Since the name is the variable 'game' already
        gameList.append(game)
        gameText.append(gamesFont.render(game, False, (255,255,0)))
        gamesImg.append(pygame.image.load(("GameFiles/{}/IMG.gif".format(game))))
        gamesImg[len(gameList)-1] = pygame.transform.scale(gamesImg[len(gameList)-1],(416,288))
        print " {}.  {} retrieved".format(len(gameList),game)
    print "All compatible games retrieved"
    return gameList, gameText, gamesImg

def resetWindow():
    global gameDisplay, winHeight, winWidth, winTitle
    winWidth, winHeight = 800,416
    winTitle = "PiRIS Home"
    pygame.display.set_caption(winTitle)
    gameDisplay = pygame.display.set_mode((winWidth, winHeight))

def scroll(direction):
    render()
    

    pygame.display.update()

###
background = pygame.image.load("tower.gif")
###

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
    
# GPIOSetup













# Main Section, establishes the GUI and GPIO functions
#Variable setup
gamesFont = pygame.font.SysFont("verdana",36)
titleFont = pygame.font.SysFont("verdana",48)
title  = titleFont.render("Welcome to the PiRIS", False, (255,255,0))
Running = True
isRunning = True
scrolling = 0



gameList, gamesText, gamesImg = pullGames()
sel = 0


# Init the Home Screen
resetWindow()



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
                    sel -= 1
                    scroll("up")
                elif (event.key == pygame.K_DOWN and sel < len(gameList)-1):
                    sel += 1
                    scroll("down")
                elif (event.key == pygame.K_SPACE):
                    execfile("./GameFiles/{}/Main.py".format(gameList[sel]))
                

    

    # Render the next frame


    # Renders lower layer objects
    render()

    # Layer 2 - Buttons
    if (sel > 0):
        gameDisplay.blit(upArrow, [32,32])
    # Displays the selected games
    if (sel < len(gameList) - 2):
        gMax = 3
    elif (sel == len(gameList) - 2):
        gMax = 2
    elif (sel == len(gameList) - 1):
        gMax = 1
    for game in range(sel, sel + gMax):
        if (game == sel):
            gameDisplay.blit(buttonSel, [32, 128 + (game-sel)*96])
        else:
            gameDisplay.blit(buttonUnsel, [32, 128 + (game-sel)*96])
    # Layer 3 - Text
        # Displays game names over buttons
        gameDisplay.blit(gamesText[game],(48, 136+(game-sel)*96))
    
    pygame.display.update()
    sleep(0.016)
    if not Running:
        title  = titleFont.render("Welcome BACK to the PiRIS", False, (255,255,0))
        resetWindow()
        

pygame.quit()
sys.exit()
