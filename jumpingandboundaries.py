import pygame as pg
#now comes the step of initalizing pygame 
pg.init() #this is how you initialize pygame

#now we have to make a window
win = pg.display.set_mode((500 , 500))#this tuple which we passed is the size of the screen we want 
pg.display.set_caption('My first game')#to give name to the window

#now we want a character move on screen so we need few attributes for that character 
screen_width = 500
screen_height = 500
x = 50 #x , y co-ordinates from where we want it 
y = 50 
height = 60 #size of rectangle
width = 40
velocity = 5 #how fast charater moves

isJump = False
jumpCount = 10

#all pygame program has a main loop that checks for mouse events collisions 
run = True
while run:
	pg.time.delay(100) #so that things dont run very fast 
	
	#drawing a character
	win.fill((0, 0, 0)) #so that after every iteration it fills background with black colour 
	pg.draw.rect(win, (255, 0, 0), (x, y, width, height))#it wont show up to get it ... rect(surface_on_which_u_want_rect , color_it_is_rgb_in_python , co-ordinates)
	pg.display.update()

	#now we start checking for events like movement of mouse , key pressing 
	for event in pg.event.get(): #so this will have list of all events and based on event we do a thing 
		if event.type == pg.QUIT : #if user exits the window
			run = False
	
	keys = pg.key.get_pressed() # a list to get actions based on key press
	#the grid is from top left 
	#now here we kind of make a boundary so that x doesnt go out of the boundary. again the rectangle remember that x and y is at top left corner so make substractions wisely
	if keys[pg.K_LEFT] and x > velocity:
		x -= velocity
	if keys[pg.K_RIGHT] and x < screen_width - width - velocity:
		x += velocity
	
	if not(isJump): #this statement will run always in begining and not work when we press space once as isJump is true 
		if keys[pg.K_UP] and y > velocity:
			y -= velocity
		if keys[pg.K_DOWN] and y < screen_height - height - velocity:
			y += velocity
		if keys[pg.K_SPACE]:
			isJump = True

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
pg.quit()#step to end code  