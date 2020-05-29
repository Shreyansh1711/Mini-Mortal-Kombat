import pygame as pg
#now comes the step of initalizing pygame 
pg.init() #this is how you initialize pygame

#now we have to make a window
win = pg.display.set_mode((500 , 480))#this tuple which we passed is the size of the screen we want 
pg.display.set_caption('My first game')#to give name to the window
screen_width = 500
screen_height = 480


clock = pg.time.Clock()
#code to load images in your game we add images in a list
walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'), pg.image.load('R9.png')]
walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'), pg.image.load('L9.png')]
bg = pg.image.load('bg.jpg')
char = pg.image.load('standing.png')
#walkRight is list which runs when image moves in right
#bg is for background
#char when char is not doing anything

#the reason we did object oriented is that it will help us to keep code smaller and simpler when we have more characters
class player(object) : 
	def __init__(self , x , y , width , height) :
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.velocity = 5
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False 
		self.walkCount = 0

	def draw(self,win) : 
		if self.walkCount + 1 >= 27 : #as we only have 9 pics so we start from 1st pic again 
			self.walkCount = 0
		if self.left :
			win.blit(walkLeft[self.walkCount//3] , (self.x , self.y)) #walkLeft[walkCount//3] to decide which image u want and // is for % and (x,y) is to tell where u want
			self.walkCount += 1 
		elif self.right :
			win.blit(walkRight[self.walkCount//3] , (self.x , self.y))
			self.walkCount += 1
		else:
			win.blit(char , (self.x , self.y))
		 

		


#win.blit(arg1 , arg2) arg1 is the image that u want to show on screem and arg2 is at what position you want it 
def redrawGameWindow():   #this function is used to keep all the drawing part in same function 
	win.blit(bg , (0,0))
	sk.draw(win)
	pg.display.update()


sk = player(40 , 410 , 64 , 64)
#all pygame program has a main loop that checks for mouse events collisions 
run = True
while run:
	clock.tick(27) #this will keep the fps 27
	
	#now we start checking for events like movement of mouse , key pressing 
	for event in pg.event.get(): #so this will have list of all events and based on event we do a thing 
		if event.type == pg.QUIT : #if user exits the window
			run = False
	
	keys = pg.key.get_pressed() # a list to get actions based on key press
	#the grid is from top left 
	#now here we kind of make a boundary so that x doesnt go out of the boundary. again the rectangle remember that x and y is at top left corner so make substractions wisely
	if keys[pg.K_LEFT] and sk.x > sk.velocity:
		sk.x -= sk.velocity
		sk.left = True #when sprite is going left 
		sk.right = False
	elif keys[pg.K_RIGHT] and sk.x < screen_width - sk.width - sk.velocity:
		sk.x += sk.velocity
		sk.right = True
		sk.left = False
	else:
		sk.left = False
		sk.right = False
		sk.walkCount = 0

	if not(sk.isJump): #this statement will run always in begining and not work when we press space once as isJump is true 
		if keys[pg.K_SPACE]:
			sk.isJump = True
			sk.left = False
			sk.right = False
			sk.walkCount = 0

	else :
		if sk.jumpCount >= -10:
			neg = 1
			if sk.jumpCount < 0:
				neg = -1
			sk.y -= (sk.jumpCount ** 2) * 0.5 * neg #when value of jumpCount is >= -10 and >0 it will keep neg as 1 and it will keep decreasing y so as to move it up but 
			#as soon as jumpCount < 0 we make neg value as -1 so it comes down as we are adding to y and also we are decreasing value of jumpCount so that it goes up faster than slows down and comes down faster
			sk.jumpCount -= 1 #and when value of jumpcount reaches -11 we come out of this loop  and run else 
		else:
			sk.isJump = False
			sk.jumpCount = 10
	redrawGameWindow()

pg.quit()#step to end code  