import pygame
import random
from time import time, sleep
from Color import*
print "loading pygame"
pygame.init()
print "pygame loaded"

winWidth = 800
winHeight = 416

WIDTH = 800
HEIGHT = 416


pygame.display.set_caption("RPG Demo")

##
bg = pygame.image.load(("./GameFiles/Anky's Adv/floor.gif"))
##


font_name = pygame.font.match_font("arial")
def drawText(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


############################################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./GameFiles/Anky's Adv/The Ultimate Lifeform.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        

    def shoot(self):
        blast = Blast(self.rect.centerx, self.rect.top)
        all_sprites.add(blast)
        blasts.add(blast)


#########################################
class Bug(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./GameFiles/Anky's Adv/Anky Sprites/bug.gif")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

######################################
class Blast(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./GameFiles/Anky's Adv/Anky Sprites/pythonblast.gif")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        
#########################################

all_sprites = pygame.sprite.Group()
bugs = pygame.sprite.Group()
blasts = pygame.sprite.Group()
Anky = Player()
all_sprites.add(Anky)

for i in range(8):
    b = Bug()
    all_sprites.add(b)
    bugs.add(b)
score = 0




gameRunning = True

while gameRunning:
    
    #Size is a square length/width
    #size = 10
    #headx = winWidth  /2 - size/2
    #heady = winHeight /2 - size/2
    #goingUp = 0
    #goingRight = 0
    #upSpeed = 3
    #rightSpeed = 3
    playing = True
    #looking = "North"
    arrows = pygame.key.get_pressed()[273:277]
    while playing:
        for event in pygame.event.get():
            # Exit button pressed
            if (event.type == pygame.QUIT):
                gameRunning = False
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Anky.shoot()
                elif event.key == pygame.K_ESCAPE:
                    gameRunning = False
                    playing = False
            arrows = pygame.key.get_pressed()[273:277]

##            if (event.type == pygame.KEYDOWN):
##                if event.key    == pygame.K_UP:
##                    looking = "North"
##                elif event.key  == pygame.K_DOWN:
##                    looking = "South"
##                elif event.key  == pygame.K_RIGHT:
##                    looking = "East"
##                elif event.key  == pygame.K_LEFT:
##                    looking = "West"
            ##elif event.ty == pygame.K_ESCAPE:
               # gameRunning = False
##                    playing = False

        all_sprites.update()

    # check if blast hits a bug
        hits = pygame.sprite.groupcollide(bugs, blasts, True, True)
        for hit in hits:
            score += 1 
            b = Bug()
            all_sprites.add(b)
            bugs.add(b)

    # check if bug bites Anky
        hits = pygame.sprite.spritecollide(Anky, bugs, False)
        if hits:
            gameRunning = False

##        # Up Arrow
##        if (arrows[0] == 1):
##            if (goingUp < 9):
##                goingUp += 1
##        # Down Arrow, Up overrides if both are pressed
##        elif (arrows[1] == 1):
##            if (goingUp > -9):
##                goingUp -= 1
##        elif (goingUp < 0):
##            goingUp += 1
##        elif (goingUp > 0):
##            goingUp -= 1
##        # Right Arrow
##        if (arrows[2] == 1):
##            if (goingRight <9):
##                goingRight += 1
##        # Left Arrow, Right overrides if both are pressed
##        elif (arrows[3] == 1):
##            if (goingRight > -9):
##                goingRight -= 1
##        elif (goingRight > 0):
##            goingRight -= 1
##        elif (goingRight < 0):
##            goingRight += 1
##        print arrows, goingUp, goingRight, looking
            
                
        # Movement of the player
        #if (headx < winWidth-size and goingRight >0):
           # headx += goingRight
        #elif (headx > 0 and goingRight < 0):
            #headx += goingRight
        ##if (heady > 0 and goingUp > 0):
           # heady -= goingUp
        #elif (heady < winHeight-size and goingUp < 0):
           # heady -= goingUp
            
        #print heady



        # Displays the background
        gameDisplay.blit(bg, [0, 0])

        # Draws placeholder gridlines
        for meridian in range(0,winWidth,32):
            gameDisplay.fill(black, rect = [meridian, 0, 1, winHeight])
        for parallel in range(0,winHeight,32):
            gameDisplay.fill(black, rect = [0,parallel, winWidth, 1])


        #all_sprites.update()

        all_sprites.draw(gameDisplay)
        drawText(gameDisplay, str(score), 18, WIDTH/2, 30)
        pygame.display.flip()
        
        ##

        # Draw the player
       # gameDisplay.blit(player, (headx, heady))
        sleep(0.016)
        pygame.display.update()
    

