import pygame
import sys
import random

pygame.init()

# lists
key_timeout = {}
playerlist = []
rectangles = []
foodlist = []
walllist = []
ocupidesquers = []
unocupidesquers = []
borderw = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bordera = [0,17,34,51,68,85,102,119,136,153,170,187,204,221,238,255,272]
borders = [272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288]
borderd = [16,33,50,67,84,101,118,135,152,169,186,203,220,237,254,271,288]
white = (255, 255, 255)
red = (255, 0, 0)
width, height = 800, 800
screenwidth, screenheight = 1500, 800
go = False
class gridclass:
 def __init__(self,x,y,heightwidth,isocupied,ocuideby,color,id):
     self.x = x
     self.y = y
     self.heightwidth = heightwidth
     self.isocupied = isocupied
     self.ocuideby = ocuideby
     self.color = color
     self.id = id
     pass
class player:
    def __init__(self,pbox,lpbox,speed,score,color):
        self.pbox = pbox #box the player is in
        self.lpbox = lpbox #last box the player was in
        self.speed = speed
        self.score = score
        self.color = color
        pass
class food:
    def __init__(self,location,speedincreas,points,color):
        self.location = location
        self.speedincreas = speedincreas
        self.points = points
        self.color = color
        pass
class wall:
    def __init__(self,location,color):
        self.location = location
        self.color = color
        pass

# Set up display
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("PacTroll")
clock = pygame.time.Clock()
# Function to add cubes to the list
def cubeprinter():
    row_spacing = 5
    rect_size = 40
    io = False
    o= "AIR"
    for row in range(height // (rect_size + row_spacing)):
        for col in range(width // (rect_size + row_spacing)):
            x = 360+col * (rect_size + row_spacing) #when game is done uncoment this
            y = 20 + row * (rect_size + row_spacing)
            wh = rect_size
            c = red
            i = len(rectangles)
            newrec = gridclass(x,y,wh,io,o,c,i)
            rectangles.append(newrec)

def playerclasscrator():
    posision = 144
    lastposision = 144
    speed = 750
    score = 0
    color = (0,0,255)
    newplayer = player(posision, lastposision, speed, score, color)
    playerlist.append(newplayer)
    bordocupationupdater("PLAYER",posision)

def createfood():
    pos = randomsquer()
    color = (0,255,0)
    newfood = food(pos,10,1,color)
    foodlist.append(newfood)
    bordocupationupdater("FOOD",pos)

def createwall():
    pos = randomsquer()
    color = (128,128,128)
    newwall = wall(pos,color)
    walllist.append(newwall)
    bordocupationupdater("WALL",pos)
# code from stack overfllow link in documentastion
def getPressed(keys, key, timeout):
    global key_timeout

    if keys[key] == False:
        return False

    current_time = pygame.time.get_ticks()

    if key in key_timeout and key_timeout[key] > current_time:
        return False

    key_timeout[key] = current_time + timeout
    return True

# code from stack overfllow link in documentastion modified to fitt the game
def playermove():
    # max speed 100, lowest 750
    speed = playerlist[0].speed
    ptomove = playerlist[0].pbox
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if getPressed(keys, pygame.K_w, speed):
        if ptomove in borderw or rectangles[playerlist[0].pbox - 17].ocuideby == "WALL":
            print("hit wall")
            return
        if rectangles[playerlist[0].pbox - 17].ocuideby == "FOOD" or rectangles[playerlist[0].pbox - 17].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            playerlist[0].pbox -= 17
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYER",ptomove)
    if getPressed(keys, pygame.K_a, speed):
        if ptomove in bordera or rectangles[playerlist[0].pbox - 1].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox - 1].ocuideby == "FOOD" or rectangles[playerlist[0].pbox - 1].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            playerlist[0].pbox -= 1
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYER",ptomove)
    if getPressed(keys, pygame.K_s, speed):
        if ptomove in borders or rectangles[playerlist[0].pbox + 17].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox + 17].ocuideby == "FOOD" or rectangles[playerlist[0].pbox + 17].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            playerlist[0].pbox += 17
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYER",ptomove)
    if getPressed(keys, pygame.K_d, speed):
        if ptomove in borderd or rectangles[playerlist[0].pbox + 1].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox + 1].ocuideby == "FOOD" or rectangles[playerlist[0].pbox + 1].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            playerlist[0].pbox += 1
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYER",ptomove)

def squerdocupationchecer():
    global ocupidesquers
    global unocupidesquers
    unocupidesquers = []
    ocupidesquers = []
    for i in range(len(rectangles)):
        if rectangles[i].isocupied == True:
            ocupidesquers.append(i)
        else:
            unocupidesquers.append(i)

def bordocupationupdater(type,location):
    if type == "PLAYER":
        rectangles[location].isocupied = True
        rectangles[location].ocuideby = type
        rectangles[playerlist[0].lpbox].isocupied = False
        rectangles[playerlist[0].lpbox].ocuideby = "AIR"
    if type == "FOOD":
        rectangles[location].isocupied = True
        rectangles[location].ocuideby = type
    if type == "WALL":
        rectangles[location].isocupied = True
        rectangles[location].ocuideby = type
    if type == "AIR":
        rectangles[location].isocupied = False
        rectangles[location].ocuideby = type
    squerdocupationchecer()
    
def eatfood(location):
    global score,speed
    if rectangles[location].ocuideby != "FOOD":
        return
    if rectangles[location].ocuideby == "FOOD":
        playerlist[0].score += foodlist[0].points
        print(playerlist[0].score, playerlist[0].speed)
        if playerlist[0].speed != 100:
            playerlist[0].speed -= foodlist[0].speedincreas
        foodlist.clear()
        bordocupationupdater("PLAYER",location)
        createwall()
        createfood()
        score = font.render(f'Score: {playerlist[0].score}', True, white,)
        speed = font.render(f'Speed: {playerlist[0].speed}', True, white,)

def randomsquer():
    a = random.choice(unocupidesquers)
    return a

def bordpainter():
    for i in range(len(rectangles)):
        pygame.draw.rect(screen, rectangles[i].color, (rectangles[i].x, rectangles[i].y, rectangles[i].heightwidth, rectangles[i].heightwidth))
    
    pygame.draw.rect(screen, foodlist[0].color, (rectangles[foodlist[0].location].x, rectangles[foodlist[0].location].y, rectangles[foodlist[0].location].heightwidth, rectangles[foodlist[0].location].heightwidth))
    
    pygame.draw.rect(screen, playerlist[0].color, (rectangles[playerlist[0].pbox].x, rectangles[playerlist[0].pbox].y, rectangles[playerlist[0].pbox].heightwidth, rectangles[playerlist[0].pbox].heightwidth))
    
    if len(walllist) !=0:
     for a in range(len(walllist)):
        pygame.draw.rect(screen, walllist[a].color, (rectangles[walllist[a].location].x, rectangles[walllist[a].location].y, rectangles[walllist[a].location].heightwidth, rectangles[walllist[a].location].heightwidth))
   
# stil need to make a cheker for if the scuer is oqupied
def gameover():
    global go
    go = True
    print("game over")
    print(playerlist[0].score)
    mainmenu()
# Call the cubeprinter function to add rectangles to the list
def gamestart():
    global playerlist, rectangles, foodlist, walllist, go
    go = False
    playerlist = []
    rectangles = []
    foodlist = []
    walllist = []
    cubeprinter()
    playerclasscrator()
    createfood()
    stattextgen()

def stattextgen():
    global scoreRect, speedRect, score, speed, font
    font = pygame.font.SysFont('Corbel', 32)
    score = font.render(f'Score: {playerlist[0].score}', True, white,)
    scoreRect = score.get_rect()
    speed = font.render(f'Speed: {playerlist[0].speed}', True, white,)
    speedRect = speed.get_rect()
    speedRect.center = (100,450)
    scoreRect.center = (100,400)

def mainmenu():
    global color_light, color_dark, text
    # white color  
    tcolor = (0,255,255)
    color_light = (170,170,170)  
    color_dark = (100,100,100)   
    smallfont = pygame.font.SysFont('Corbel',35)  
    text = smallfont.render('retry' , True , tcolor) 

gamestart()
# Main game loop
def gameloop():
    while True:
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                pygame.quit() 
                quit() 
              
            #checks if a mouse is clicked  
            if ev.type == pygame.MOUSEBUTTONDOWN:  
              
            #if the mouse is clicked on the  
            # button the game is terminated  
                if screenwidth/2 <= mouse[0] <= screenwidth/2+140 and screenheight/2 <= mouse[1] <= screenheight/2+40:  
                    gamestart()
        
        # Clear the screen
        screen.fill((0, 0, 0))
        screen.blit(score, scoreRect)
        screen.blit(speed, speedRect)  
      
    # superimposing the text onto our button
        if go == True:
            mouse = pygame.mouse.get_pos() 
            if screenwidth/2-40 <= mouse[0] <= screenwidth/2+140 and screenheight/2 <= mouse[1] <= screenheight/2+40:  
                pygame.draw.rect(screen,color_light,[screenwidth/2-40,screenheight/2,100,50])  
          
            else:  
                pygame.draw.rect(screen,color_dark,[screenwidth/2-40,screenheight/2,100,50])
            screen.blit(text, (screenwidth/2-20,screenheight/2+5)) 
        else:
            bordpainter()
        playermove()
        # Draw rectangles from the list
        # Update the display
        pygame.display.flip()
gameloop()