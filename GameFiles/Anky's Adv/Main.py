import random
from Color import*



WIDTH = 800
HEIGHT = 416


pygame.display.set_caption("Anky's Adventure")

##
bg = pygame.image.load(("./GameFiles/Anky's Adv/background.gif"))
##


font_name = pygame.font.match_font("arial")
def drawText(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
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

def show_go_screen():
    gameDisplay.blit(bg, [0, 0])
    drawText(gameDisplay, "Anky's Adventure", 64, WIDTH / 2, HEIGHT / 4)
    drawText(gameDisplay, "Arrow keys move, Space to fire your python blast", 22,
              WIDTH / 2, HEIGHT / 2)
    drawText(gameDisplay, "The bugs are coming, get ready!", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


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
    show_go_screen()
    sleep(3.5)

    playing = True
   
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


        all_sprites.update()

    # check if blast hits a bug
        hits = pygame.sprite.groupcollide(bugs, blasts, True, True)
        for hit in hits:
            score += 1 
            b = Bug()
            all_sprites.add(b)
            bugs.add(b)

    # check if bug bites Anky
        hits = pygame.sprite.spritecollide(Anky, bugs, True)
        if hits:
            score -= 1
            b = Bug()
            all_sprites.add(b)
            bugs.add(b)



        # Displays the background
        gameDisplay.blit(bg, [0, 0])




    

        all_sprites.draw(gameDisplay)
        drawText(gameDisplay, str(score), 18, WIDTH/2, 30)
        pygame.display.flip()
        
 


        sleep(0.016)
        pygame.display.update()
    

