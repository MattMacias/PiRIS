# Initial import statements
import pygame
from time import time, sleep
from Color import*
from math import sin, cos, pi

# Rename window
pygame.display.set_caption("FlingFender")

# Image loading
bg = pygame.image.load(("./GameFiles/FlingFender/floor.gif"))
player1 = pygame.image.load("./GameFiles/FlingFender/test.gif")
player2 = pygame.image.load("./GameFiles/FlingFender/test.gif")
pturnFont = pygame.font.SysFont("verdana",24)
turnFont = pygame.font.SysFont("verdana",48)



class Player():
    def __init__(self, x, color):
        self.x = x
        self.fixY(self.x)
        if (color == "blue"):
            self.img = pygame.image.load("./GameFiles/FlingFender/bluetank.gif")
        elif (color == "red"):
            self.img = pygame.image.load("./GameFiles/FlingFender/redtank.gif")
        else:
            self.img = pygame.image.load("./GameFiles/FlingFender/test.gif")

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        if (x <= 0):
            self._x = 1
        elif (x >= winWidth):
            self._x = winWidth - 1
        else:
            self._x = value

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

    def render(self):
        gameDisplay.blit(self.img, (self.x - 94, self.y - 69))

    def fire(self, power, angle):
        dy = sin(180*angle/pi) * power / 100
        dx = cos(180*angle/pi) * power / 100
        while self.y > sin(self.x / 100) + 200:
            self.x += dx
            self.y += y
            dy -= 1
            render()
            print dy

    def fixY(self, x):
        self.y = sin(x/100) + 200


def render():
    # Displays the background
    gameDisplay.fill(blue, rect = [0,0,winWidth, winHeight])

    # Draws placeholder gridlines
    for meridian in range(0,winWidth,32):
        gameDisplay.fill(black, rect = [meridian, 0, 1, winHeight])
    for parallel in range(0,winHeight,32):
        gameDisplay.fill(black, rect = [0,parallel, winWidth, 1])


    
    # Displays whose turn it is and which turn it is
    turnLabel  = turnFont.render("Turn {}".format(gameTurn), False, (255,255,0))
    pturnLabel = pturnFont.render("Your move, Player {}".format(playerTurn), False, (255,255,0))
    gameDisplay.blit(turnLabel, (320, 0))
    gameDisplay.blit(pturnLabel, (272, 64))
        

    # Draw the player
    for p in range(len(player)):
            player[p].render()
    
    sleep(0.016)
    pygame.display.update()




##########################################
# Main Segment
##########################################

# Variable setup
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

player = [Player(64, "blue"), Player(winWidth - 96, "red")]


while Running:
    # Iterates the current game turn every other turn
    if  playerTurn == 1:
        gameTurn += 1
    # Resets other information
    power, angle = 0, 0
    
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
                    player[playerTurn-1].fire(power, angle)
                    if playerTurn == 1:
                        playerTurn = 2
                    else:
                        gameTurn += 1
                        playerTurn = 1
            
        # Up Arrow
        if (arrows[0] == 1 and power < 100):
            power += 1
        # Down Arrow, Up overrides if both are pressed
        elif (arrows[1] == 1 and power > 0):
            power -= 1
        elif (goingUp < 0):
            goingUp += 1
        elif (goingUp > 0):
            goingUp -= 1
        # Right Arrow
        if (arrows[2] == 1):
            angle -= 1
            if (angle < 0):
                angle = 359
        # Left Arrow, Right overrides if both are pressed
        elif (arrows[3] == 1):
            angle += 1
            if (angle > 359):
                angle = 0
        elif (goingRight > 0):
            goingRight -= 1
        elif (goingRight < 0):
            goingRight += 1
        print arrows, goingUp, goingRight, power, angle
            

            



        
        render()

        
    

