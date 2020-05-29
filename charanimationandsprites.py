import pygame as pg
#now comes the step of initalizing pygame 
pg.init() #this is how you initialize pygame

#now we have to make a window
win = pg.display.set_mode((500 , 480))#this tuple which we passed is the size of the screen we want 
pg.display.set_caption('My first game')#to give name to the window

#now we want a character move on screen so we need few attributes for that character 
screen_width = 500
screen_height = 480
x = 50 #x , y co-ordinates from where we want it 
y = 400 
height = 64 #size of rectangle
width = 64
velocity = 5 #how fast charater moves

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0 

clock = pg.time.Clock()

#code to load images in your game we add images in a list
walkRight = [pg.image.load('R1.png'), pg.image.load('R2.png'), pg.image.load('R3.png'), pg.image.load('R4.png'), pg.image.load('R5.png'), pg.image.load('R6.png'), pg.image.load('R7.png'), pg.image.load('R8.png'), pg.image.load('R9.png')]
walkLeft = [pg.image.load('L1.png'), pg.image.load('L2.png'), pg.image.load('L3.png'), pg.image.load('L4.png'), pg.image.load('L5.png'), pg.image.load('L6.png'), pg.image.load('L7.png'), pg.image.load('L8.png'), pg.image.load('L9.png')]
bg = pg.image.load('bg.jpg')
char = pg.image.load('standing.png')
#walkRight is list which runs when image moves in right
#bg is for background
#char when char is not doing anything


#win.blit(arg1 , arg2) arg1 is the image that u want to show on screem and arg2 is at what position you want it 
def redrawGameWindow():   #this function is used to keep all the drawing part in same function 
	global walkCount
	win.blit(bg , (0,0))

	if walkCount + 1 >= 27 : #as we only have 9 pics so we start from 1st pic again 
		walkCount = 0
	if left :
		win.blit(walkLeft[walkCount//3] , (x,y)) #walkLeft[walkCount//3] to decide which image u want and // is for % and (x,y) is to tell where u want
		walkCount += 1 
	elif right :
		win.blit(walkRight[walkCount//3] , (x,y))
		walkCount += 1
	else:
		win.blit(char , (x,y))
	pg.display.update()



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
	if keys[pg.K_LEFT] and x > velocity:
		x -= velocity
		left = True #when sprite is going left 
		right = False
	elif keys[pg.K_RIGHT] and x < screen_width - width - velocity:
		x += velocity
		right = True
		left = False
	else:
		left = False
		right = False
		walkCount = 0

	if not(isJump): #this statement will run always in begining and not work when we press space once as isJump is true 
		if keys[pg.K_SPACE]:
			isJump = True
			left = False
			right = False
			walkCount = 0

	else :
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg #when value of jumpCount is >= -10 and >0 it will keep neg as 1 and it will keep decreasing y so as to move it up but 
			#as soon as jumpCount < 0 we make neg value as -1 so it comes down as we are adding to y and also we are decreasing value of jumpCount so that it goes up faster than slows down and comes down faster
			jumpCount -= 1 #and when value of jumpcount reaches -11 we come out of this loop  and run else 
		else:
			isJump = False
			jumpCount = 10
	redrawGameWindow()

pg.quit()#step to end code  