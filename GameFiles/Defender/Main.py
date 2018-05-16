# Initial import statements
import pygame
from time import time, sleep
from Color import*

# Rename window
pygame.display.set_caption("Handshoes and Horsegrenades")

##
bg = pygame.image.load(("./GameFiles/Defender/floor.gif"))
##

player1 = pygame.image.load("./GameFiles/Anky's Adv/test.gif")
player2 = pygame.image.load("./GameFiles/Anky's Adv/test.gif")

#Size is a square length/width
size = 10
headx = [64, winWidth - 96]
heady = [winHeight /2 - size/2, winHeight /2 - size/2]
goingUp = 0
goingRight = 0
upSpeed = 3
rightSpeed = 3
playing = True

arrows = pygame.key.get_pressed()[273:277]
playerTurn = 1
gameTurn   = 0
Running = True

while Running:
    # Iterates the current game turn every other turn
    if  playerTurn == 1:
        gameTurn += 1
    
    while playing:
        for event in pygame.event.get():
            # Exit button pressed
            if (event.type == pygame.QUIT):
                Running = False
                playing = False
            arrows = pygame.key.get_pressed()[273:277]
            # Specific key events, one time press rather than holding
            if (event.type == pygame.KEYDOWN):
                # Quits the turn and the game
                if event.key == pygame.K_ESCAPE:
                    Running = False
                    playing = False
                elif event.key == pygame.K_SPACE:
                    if playerTurn == 1:
                        playerTurn = 2
                    else:
                        gameTurn += 1
                        playerTurn = 1
            
        # Up Arrow
        if (arrows[0] == 1):
            if (goingUp < 9):
                goingUp += 1
        # Down Arrow, Up overrides if both are pressed
        elif (arrows[1] == 1):
            if (goingUp > -9):
                goingUp -= 1
        elif (goingUp < 0):
            goingUp += 1
        elif (goingUp > 0):
            goingUp -= 1
        # Right Arrow
        if (arrows[2] == 1):
            if (goingRight <9):
                goingRight += 1
        # Left Arrow, Right overrides if both are pressed
        elif (arrows[3] == 1):
            if (goingRight > -9):
                goingRight -= 1
        elif (goingRight > 0):
            goingRight -= 1
        elif (goingRight < 0):
            goingRight += 1
        print arrows, goingUp, goingRight
            
                
        # Movement of the player
        if (headx[playerTurn-1] < winWidth-size and goingRight >0):
            headx[playerTurn-1] += goingRight
        elif (headx[playerTurn-1] > 0 and goingRight < 0):
            headx[playerTurn-1] += goingRight
        if (heady[playerTurn-1] > 0 and goingUp > 0):
            heady[playerTurn-1] -= goingUp
        elif (heady[playerTurn-1] < winHeight-size and goingUp < 0):
            heady[playerTurn-1] -= goingUp
            
        print heady



        # Displays the background
        gameDisplay.fill(blue, rect = [0,0,winWidth, winHeight])

        # Draws placeholder gridlines
        for meridian in range(0,winWidth,32):
            gameDisplay.fill(black, rect = [meridian, 0, 1, winHeight])
        for parallel in range(0,winHeight,32):
            gameDisplay.fill(black, rect = [0,parallel, winWidth, 1])


        
        # Displays whose turn it is and which turn it is
        
            

        # Draw the player
        gameDisplay.blit(player1, (headx[0], heady[0]))
        gameDisplay.blit(player2, (headx[1], heady[1]))
        
        sleep(0.016)
        pygame.display.update()
    

