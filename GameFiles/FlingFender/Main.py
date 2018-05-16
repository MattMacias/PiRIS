# Initial import statements
import pygame
from time import time, sleep
from Color import*
from math import sin, cos, pi, sqrt

# Rename window
pygame.display.set_caption("FlingFender")

# Image loading
bg = pygame.image.load(("./GameFiles/FlingFender/bg.png"))
player1 = pygame.image.load("./GameFiles/FlingFender/test.gif")
player2 = pygame.image.load("./GameFiles/FlingFender/test.gif")
pturnFont = pygame.font.SysFont("verdana",24)
turnFont = pygame.font.SysFont("verdana",48)



class Player():
    def __init__(self, x, color):
        self.x = x
        self.fixY(self.x)
        self.health = 1000
        self.score = 0
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
        # Renders off the aesthetically center of the image
        gameDisplay.blit(self.img, (self.x - 135, self.y - 69))

    def fire(self, power, angle):
        dy = sin(pi*angle/180) * power / 3
        dx = cos(pi*angle/180) * power / 3
        while self.y <= 416 - (50*sin(self.x / 100) + 276):
            self.x += dx
            self.y -= dy
            dy -= 1
            render()
            # Wallbouncing
            if ((self.x + 77) > 800):
                dx = -abs(dx)
            elif (self.x < 0):
                dx = abs(dx)
        self.fixY(self.x)
        impact = sqrt(dx**2 + dy **2)
        return impact

    def fixY(self, x):
        self.y = 416 - (50*sin(x/100.0) + 276)


def render():
    # Displays the background
    gameDisplay.blit(bg, (0,0))

##    # Draws placeholder gridlines
##    for meridian in range(0,winWidth,32):
##        gameDisplay.fill(black, rect = [meridian, 0, 1, winHeight])
##    for parallel in range(0,winHeight,32):
##        gameDisplay.fill(black, rect = [0,parallel, winWidth, 1])


    
    # Displays whose turn it is and which turn it is
    turnLabel  = turnFont.render("Turn {}".format(gameTurn), False, (255,255,0))
    pturnLabel = pturnFont.render("Your move, Player {}".format(playerTurn), False, (255,255,0))
    gameDisplay.blit(turnLabel, (320, 0))
    gameDisplay.blit(pturnLabel, (272, 64))

    # Display player scores, angle, and power
    p1Score = pturnFont.render("Player 1 score: %0.2f" % player[0].score, False, (255,255,0))
    p2Score = pturnFont.render("Player 2 score: %0.2f" % player[1].score, False, (255,255,0))
    gameDisplay.blit(p1Score, (32,288))
    gameDisplay.blit(p2Score, (32,336))
    powLabel = pturnFont.render("Power: {}".format(power), False, (255,255,0))
    angLabel = pturnFont.render("Angle: {}".format(angle), False, (255,0,0))
    gameDisplay.blit(powLabel, (640, 288))
    gameDisplay.blit(angLabel, (640, 336))
        

    # Draw the player
    for p in range(len(player)):
            player[p].render()

    # Output to the screen
    pygame.display.update()
    sleep(0.016)




##########################################
# Main Segment
##########################################

# Variable setup
Running = True
playerTurn = 1
gameTurn   = 1
power, angle = 0, 0
arrows = pygame.key.get_pressed()[273:277]
player = [Player(64, "blue"), Player(winWidth - 96, "red")]


# Loading screen with how to play
gameDisplay.blit(bg, (0,0))
tFont = pygame.font.SysFont("verdana",60)
dFont = pygame.font.SysFont("verdana",30)
titleLabel  = tFont.render("Welcome to FlingFenders!", False, (255,255,0))
descLabel1  = dFont.render("Use arrow keys to adjust angle and power", False, (255,255,0))
descLabel2  = dFont.render("Use space to fire...YOURSELF!", False, (255,255,0))
gameDisplay.blit(titleLabel, (16, 100))
gameDisplay.blit(descLabel1, (68, 190))
gameDisplay.blit(descLabel2, (160, 240))
pygame.display.update()

waiting = True
# Waits for spacebar event to begin the game
while waiting:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                waiting = False
            elif (event.key == pygame.K_ESCAPE):
                waiting = False
                Running = False

while Running:
    for event in pygame.event.get():
        # Exit button pressed
        if (event.type == pygame.QUIT):
            Running = False
        arrows = pygame.key.get_pressed()[273:277]
        # Specific key events, one time press rather than holding
        if (event.type == pygame.KEYDOWN):
            # Quits the turn and the game
            if event.key == pygame.K_ESCAPE:
                Running = False
            elif event.key == pygame.K_SPACE:
                # Fires the player according to player input
                impact = player[playerTurn-1].fire(power, angle)
                # Calculate how hard the other player is knocked around by
                dist = sqrt((player[0].x - player[1].x)**2 + (player[0].y - player[1].y)**2)
                knockback = impact / dist * 300
                # Add knockback to player's score
                player[playerTurn - 1].score += knockback
                # Knock the other player around, using knockback as power
                if (player[not (playerTurn - 1)].x < player[playerTurn - 1].x): 
                    player[not (playerTurn - 1)].fire(knockback, 110)
                else:
                    player[not (playerTurn - 1)].fire(knockback, 70)
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
    # Right Arrow
    if (arrows[2] == 1):
        angle -= 3
        if (angle < 0):
            angle = 0
    # Left Arrow, Right overrides if both are pressed
    elif (arrows[3] == 1):
        angle += 3
        if (angle > 180):
            angle = 180
   

    # Render all changes
    render()

    


