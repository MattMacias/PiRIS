import pygame
from time import time, sleep
from Color import*
print "loading pygame"
pygame.init()
print "pygame loaded"

winWidth = 800
winHeight = 600

gameDisplay = pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("RPG Demo")





running = True

while running:
    #Size is a square length/width
    size = 10
    headx = winWidth /2 - size/2
    heady = winHeight - 32 - size/2
    goingUp = 0
    goingRight = 0
    upSpeed = 3
    rightSpeed = 3
    playing = True
    looking = "North"
    while playing:
        for event in pygame.event.get():
            # Exit button pressed
            if (event.type == pygame.QUIT):
                running = False
                playing = False
            arrows = pygame.key.get_pressed()[273:277]

            if (event.type == pygame.KEYDOWN):
                if event.key    == pygame.K_UP:
                    looking = "North"
                elif event.key  == pygame.K_DOWN:
                    looking = "South"
                elif event.key  == pygame.K_RIGHT:
                    looking = "East"
                elif event.key  == pygame.K_LEFT:
                    looking = "West"
            
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
        print arrows, goingUp, goingRight, looking
            
                

        if (headx < 800-size and goingRight >0):
            headx += goingRight
        elif (headx > 0 and goingRight < 0):
            headx += goingRight
        if (heady < 600-size and goingUp > 0):
            heady -= goingUp
        elif (heady > 0 and goingUp < 0):
            heady -= goingUp
        
        gameDisplay.fill(white)
        for meridian in range(0,800,50):
            gameDisplay.fill(black, rect = [meridian, 0, 1, 600])
        for parallel in range(0,600,50):
            gameDisplay.fill(black, rect = [0,parallel, 800, 1])

        pygame.draw.rect(gameDisplay, green, [headx, heady, size, size])
        sleep(0.016)
        pygame.display.update()
    



pygame.quit()
quit()
