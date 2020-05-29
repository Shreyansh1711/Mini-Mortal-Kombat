import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


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
    sk.draw(win)
    for bullet in bullets:
        bullet.draw(win) 
    
    pygame.display.update()


#mainloop
sk = player(200, 410, 64,64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets: #this is step 2 
        if bullet.x < 500 and bullet.x > 0: #to see whether the first bullet in list has is within window or not 
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #to remove the bullet which is at win 
 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if sk.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5: #so that we can only fire 5 bullets at a time
            bullets.append(projectile(round(sk.x + sk.width //2), round(sk.y + sk.height//2), 6, (0,0,0), facing)) # to add bullet to list this is step 1

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