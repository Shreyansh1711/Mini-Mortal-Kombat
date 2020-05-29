import pygame as pg
#now comes the step of initalizing pygame 
pg.init() #this is how you initialize pygame

#now we have to make a window
win = pg.display.set_mode((500 , 500))#this tuple which we passed is the size of the screen we want 
pg.display.set_caption('My first game')#to give name to the window

#now we want a character move on screen so we need few attributes for that character 
x = 50 #x , y co-ordinates from where we want it 
y = 50 
height = 60 #size of rectangle
width = 40
velocity = 5 #how fast charater moves

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
	if keys[pg.K_LEFT]:
		x -= velocity
	if keys[pg.K_RIGHT]:
		x += velocity
	if keys[pg.K_UP]:
		y -= velocity
	if keys[pg.K_DOWN]:
		y += velocity

pg.quit()#step to end code  