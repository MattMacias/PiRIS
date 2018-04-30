##########################################################
#   Members: Matthew Macias, Gavin Phillips, Chris Dilley
#
#
##########################################################
import pygame
import sys
import time
from os import listdir


# GUI Setup
pygame.init()

# Scans the GameFiles directory for games and stores their names
def pullGames():
    print "Scanning for games..."
    global gameList
    # Checks each directory within GameFiles
    for game in listdir("GameFiles"):
        # Runs the placeholder name file within it
        # It is better used to pull a game's logo rather than name\
        #   Since the name is the variable 'game' already
        execfile("./GameFiles/{}/name.py".format(game))
        print " {}.  {} retrieved".format(len(gameList),game)
    print "All compatible games retrieved"

def newWindow():
    global window, winHeight, winWidth, winTitle
    winWidth, winHeight = 800,600
    winTitle = "PiRIS Home"
    pygame.display.set_caption(winTitle)
    window = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)

def countFPS():
    global curSec, curFrame, FPS

    if curSec == time.strftime("%S"):
        curFrame += 1
    else:
        FPS = curFrame
        curFrame = 0
        curSec = time.strftime("%S")

def showFPS():
    fps_overlay = fps_font.render(str(FPS), True, (255,255,255))
    window.blit(fps_overlay, (0,0))
# GPIOSetup













# Main Section, establishes the GUI and GPIO functions
#Variable setup
fps_font = pygame.font.SysFont("verdana",12)
print fps_font
isRunning = True
curSec = 0
curFrame = 0
FPS = 0
gameList = []
pullGames()

# Init the Home Screen
newWindow()


while isRunning:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            isRunning = 0
    # Logic
    countFPS()


    # Render the next frame
    # Bottom Layer - Background
    window.fill((0,162,232))
    # Layer 1 - 32 x 32 px Gridlines
    for x in range(0,640, 32):
        for y in range(0,480, 32):
            pygame.draw.rect(window, (150,150,150), (x,y,33, 33), 1)
    showFPS()
    
    pygame.display.update()


pygame.quit()
sys.exit()
