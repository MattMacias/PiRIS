import pygame
from time import time, sleep
from Color import*
print "loading pygame"
pygame.init()
print "pygame loaded"

winWidth = 800
winHeight = 416


pygame.display.set_caption("RPG Demo")

##
bg = pygame.image.load(("./GameFiles/Anky's Adv/floor.gif"))
##


player = pygame.image.load("./GameFiles/Anky's Adv/The Ultimate Lifeform.gif")
bullet = pygame.image.load("./GameFiles/Anky's Adv/Anky Sprites/pythonblast.gif")

############################################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./GameFiles/Anky's Adv/The Ultimate Lifeform.gif")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.centerx = random.randint(1, WIDTH)
        self.rect.bottom - random.randint(1, HEIGHT)

    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def position(self):
        return [self.rect.x, self.rect.y]
###################################################
    


######################################
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):

        pygame.sprite.Sprite>__init__(self)
        self.image = pygame.image.load("./GameFiles/Anky's Adv/Anky Sprites/pythonblast.gif")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        if player.looking == "North":
            self.speedy = -100
            self.speedx = 0
        if player.looking == "South":
            self.speedy = 100
            self.speedx = 0
        if player.looking == "East":
            self.speedy = 0
            self.speedx = 100
        if player.looking == "West":
            self.speedy = 0
            self.speedx = -100

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
#########################################


gameRunning = True



while gameRunning:
    #Size is a square length/width
    size = 10
    headx = winWidth  /2 - size/2
    heady = winHeight /2 - size/2
    goingUp = 0
    goingRight = 0
    upSpeed = 3
    rightSpeed = 3
    playing = True
    looking = "North"
    arrows = pygame.key.get_pressed()[273:277]
    while playing:
        for event in pygame.event.get():
            # Exit button pressed
            if (event.type == pygame.QUIT):
                gameRunning = False
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
                elif event.key == pygame.K_ESCAPE:
                    gameRunning = False
                    playing = False
                #####################
                elif event.key == pygame.K_SPACE:
                    bullet(Bullet)
                    gameDisplay.blit(bullet, [0, 0])
                #################
                   

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
            
                
        # Movement of the player
        if (headx < winWidth-size and goingRight >0):
            headx += goingRight
        elif (headx > 0 and goingRight < 0):
            headx += goingRight
        if (heady > 0 and goingUp > 0):
            heady -= goingUp
        elif (heady < winHeight-size and goingUp < 0):
            heady -= goingUp
            
        print heady



        # Displays the background
        gameDisplay.blit(bg, [0, 0])

        # Draws placeholder gridlines
        for meridian in range(0,winWidth,32):
            gameDisplay.fill(black, rect = [meridian, 0, 1, winHeight])
        for parallel in range(0,winHeight,32):
            gameDisplay.fill(black, rect = [0,parallel, winWidth, 1])


        
        ##

        # Draw the player
        gameDisplay.blit(player, (headx, heady))
        sleep(0.016)
        pygame.display.update()
    

