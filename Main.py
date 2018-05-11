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
        print " {}.  {} retrieved".format(len(gameList),game)
    print "All compatible games retrieved"
    return gameList, gameText, gamesImg

def newWindow():
    global gameDisplay, winHeight, winWidth, winTitle
    winWidth, winHeight = 800,416
    winTitle = "PiRIS Home"
    pygame.display.set_caption(winTitle)
    gameDisplay = pygame.display.set_mode((winWidth, winHeight))


# GPIOSetup













# Main Section, establishes the GUI and GPIO functions
#Variable setup
gamesFont = pygame.font.SysFont("verdana",36)
titleFont = pygame.font.SysFont("verdana",48)
title  = titleFont.render("Welcome to the PiRIS", False, (255,255,0))
isRunning = True

gameList, gamesText, gamesImg = pullGames()

sel = 0

# Init the Home Screen
newWindow()


while isRunning:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            isRunning = 0
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                isRunning = 0
            elif (event.key == pygame.K_UP and sel > 0):
                sel -= 1
            elif (event.key == pygame.K_DOWN and sel < len(gameList)-1):
                sel += 1
            elif (event.key == pygame.K_SPACE):
                execfile("./GameFiles/{}/Main.py".format(gameList[game]))
                

    

    # Render the next frame
    # Bottom Layer - Background
    gameDisplay.fill((128,0,0))
    # Layer 1 - 32 x 32 px Gridlines
    for x in range(0,winWidth, 32):
        for y in range(0,winHeight, 32):
            pygame.draw.rect(gameDisplay, (150,150,150), (x, y, 33, 33), 1)

    # Displays the Title Text
    gameDisplay.blit(title, (144, 16))

    # Displays the selected game's image
    pygame.draw.rect(gameDisplay, (0,0,0), (316,92, 424, 296))
    gameDisplay.blit(gamesImg[sel], [320, 96])
    
    # Displays the selected games
    for game in range(len(gameList)):
        if (game == sel):
            gameDisplay.blit(buttonSel, [32, 96 + game*128])
        else:
            gameDisplay.blit(buttonUnsel, [32, 96 + game*128])
        gameDisplay.blit(gamesText[game],(48, 120+game*128))
    
    pygame.display.update()
    sleep(0.016)

pygame.quit()
sys.exit()
