#hitboxes are commonly used in pygame . they are box around character and whenever two boxes are over one another we say char are colliding
#try that hit box fits the character well and try to play around with measurements so as to get perfect hitbox
import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

#bulletSound = pygame.mixer.Sound('bullet.wav')
#hitSound = pygame.mixer.Sound('hit.mp3')
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score = 0


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [self.x , self.end]
        self.hitbox = (self.x + 17 , self.y + 2 , 31 , 57) 
        self.count = 0
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move() #to draw we need to first move
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3] , (self.x , self.y))    
                self.walkCount +=1

            else :
                win.blit(self.walkLeft[self.walkCount // 3] , (self.x , self.y))    
                self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        self.hitbox = (self.x + 17 , self.y + 2 , 31 , 57) 
        pygame.draw.rect(win , (255 , 0 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 , 10))
        pygame.draw.rect(win , (0 , 128 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 - (5 * (10 - self.health)), 10))
        #pygame.draw.rect(win , (255 , 0 , 0) , self.hitbox , 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible= False
        self.count += 1
        print('hit ',self.count)

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17 , self.y + 11 , 29 , 52) #wheneverthere are four things inside () we consider it as rectangle with (x , y , width , height)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17 , self.y + 11 , 29 , 52)
        #pygame.draw.rect(win , (255 , 0 , 0) , self.hitbox , 2)


    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0 
        font1 = pygame.font.SysFont('comicsans' , 100)
        text = font1.render('u lost 5 points' , 1 , (255 , 0 , 0))
        win.blit(text , (250 - (text.get_width() / 2) , 200))
        pygame.display.update()
        i = 0
        while(i < 300):
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    i = 301
                    pygame.quit()
            
#so we make a class for the bullets thrown 
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing #it will have value 1 for right and -1 for left 
        self.vel = 8 * facing #to decide the velocity of bullet 
        

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)



def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score :' + str(score) , 1 , (0 , 0 , 0)) #rendering new text so it is ready to be placed on screen or make a surface which can be put on screen render(textuwannadisplay , 1->compulsory , color)
    win.blit(text , (390 ,10))
    sk.draw(win)
    sp.draw(win)
    for bullet in bullets:
        bullet.draw(win) 
    
    pygame.display.update()


#mainloop

sk = player(200, 410, 64,64)
sp = enemy(100, 410, 64, 64 , 400)
shootLoop = 0
bullets = []
run = True

font = pygame.font.SysFont('comicsans' , 30 , True , True)  # (font , size , Bold , Italics)

while run:
    clock.tick(27)

    if sk.hitbox[1] < sp.hitbox[1] + sp.hitbox[3] and sk.hitbox[1] + sk.hitbox[3] >sp.hitbox[1]:
        if sk.hitbox[0] + sk.hitbox[2] > sp.hitbox[0] and sk.hitbox[0] < sp.hitbox[0] + sp.hitbox[2]:
            sk.hit()
            score -= 5 
            
    if shootLoop >= 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets: #this is step 2 
        if bullet.y - bullet.radius < sp.hitbox[1] + sp.hitbox[3] and bullet.y + bullet.radius >sp.hitbox[1]:
            if bullet.x + bullet.radius > sp.hitbox[0] and bullet.x -bullet.radius < sp.hitbox[0] + sp.hitbox[2]:
                score += 1 
                #hitSound.play()
                sp.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0: #to see whether the first bullet in list has is within window or not 
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #to remove the bullet which is at win 
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        #bulletSound.play()
        if sk.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5: #so that we can only fire 5 bullets at a time
            bullets.append(projectile(round(sk.x + sk.width //2), round(sk.y + sk.height//2), 6, (0,0,0), facing)) # to add bullet to list this is step 1
        shootLoop = 1
        

    if keys[pygame.K_LEFT] and sk.x > sk.vel:
        sk.x -= sk.vel
        sk.left = True
        sk.right = False
        sk.standing = False
    elif keys[pygame.K_RIGHT] and sk.x < 500 - sk.width - sk.vel:
        sk.x += sk.vel
        sk.right = True
        sk.left = False
        sk.standing = False
    else:
        sk.standing = True
        sk.walkCount = 0
    
    if not(sk.isJump):
        if keys[pygame.K_UP]:
            sk.isJump = True
            sk.right = False
            sk.left = False
            sk.walkCount = 0
    else:
        if sk.jumpCount >= -10:
            neg = 1
            if sk.jumpCount < 0:
                neg = -1
            sk.y -= (sk.jumpCount ** 2) * 0.5 * neg
            sk.jumpCount -= 1
        else:
            sk.isJump = False
            sk.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()