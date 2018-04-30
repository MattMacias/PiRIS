##########################################################
#   Members: Matthew Macias, Gavin Phillips, Chris Dilley
#
#
##########################################################
print "Loading files"
import pygame
import sys
print "Files ready"

# GUI Setup
pygame.init()

def newWindow():
    global window, winHeight, winWidth, winTitle
    winWidth, winHeight = 800,600
    winTitle = "PiRIS Home"
    pygame.display.set_caption(winTitle)
    window = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)

def fpsCounter():
    global curSec, curFrame, FPS

    if curSec == time.strftime("%S"):
        curFrame += 1
    else:
        FPS = curFrame
        curFrame = 0
        curSec = time.strftime("%S")

# GPIOSetup













# Main Section, establishes the GUI and GPIO functions
#Variable setup
isRunning = True
curSec = 0
curFrame = 0
FPS = 0

# Init the Home Screen
newWindow()


while isRunning:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            isRunning = 0

    # Render the next frame
    window.fill((0,0,0))

    
    pygame.display.update()


pygame.quit()
sys.exit()
