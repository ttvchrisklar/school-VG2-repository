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
unocupidesquers = []
borderw = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bordera = [0,17,34,51,68,85,102,119,136,153,170,187,204,221,238,255,272]
borders = [272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288]
borderd = [16,33,50,67,84,101,118,135,152,169,186,203,220,237,254,271,288]
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
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
    def __init__(self,location,speedincreas,color):
        self.location = location
        self.speedincreas = speedincreas
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
            c = black
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
    bordocupationupdater("PLAYERMOVTO",posision)

def createfood(pos):
    color = (0,200,0)
    newfood = food(pos,10,color)
    foodlist.append(newfood)
    bordocupationupdater("FOOD",pos)

def createwall():
    pos = randomsquer()
    color = (64,64,64)
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
    if keys[pygame.K_r] and go == True:
        gamestart()
    if getPressed(keys, pygame.K_w, speed):
        if ptomove in borderw or rectangles[playerlist[0].pbox - 17].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox - 17].ocuideby == "FOOD" or rectangles[playerlist[0].pbox - 17].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            bordocupationupdater("PLAYERMOVFROM",ptomove)
            playerlist[0].pbox -= 17
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYERMOVTO",ptomove)
    if getPressed(keys, pygame.K_a, speed):
        if ptomove in bordera or rectangles[playerlist[0].pbox - 1].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox - 1].ocuideby == "FOOD" or rectangles[playerlist[0].pbox - 1].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            bordocupationupdater("PLAYERMOVFROM",ptomove)
            playerlist[0].pbox -= 1
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYERMOVTO",ptomove)
    if getPressed(keys, pygame.K_s, speed):
        if ptomove in borders or rectangles[playerlist[0].pbox + 17].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox + 17].ocuideby == "FOOD" or rectangles[playerlist[0].pbox + 17].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            bordocupationupdater("PLAYERMOVFROM",ptomove)
            playerlist[0].pbox += 17
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYERMOVTO",ptomove)
    if getPressed(keys, pygame.K_d, speed):
        if ptomove in borderd or rectangles[playerlist[0].pbox + 1].ocuideby == "WALL":
            print("hit wall")
            gameover()
            return
        if rectangles[playerlist[0].pbox + 1].ocuideby == "FOOD" or rectangles[playerlist[0].pbox + 1].ocuideby == "AIR":
            playerlist[0].lpbox = playerlist[0].pbox
            bordocupationupdater("PLAYERMOVFROM",ptomove)
            playerlist[0].pbox += 1
            ptomove = playerlist[0].pbox
            eatfood(ptomove)
            bordocupationupdater("PLAYERMOVTO",ptomove)

def squerdocupationchecer():
    global unocupidesquers
    unocupidesquers = []
    for i in range(len(rectangles)):
        if rectangles[i].isocupied == False:
            unocupidesquers.append(i)

def bordocupationupdater(type,location):
    if type == "PLAYERMOVTO":
        rectangles[location].isocupied = True
        rectangles[location].ocuideby = type
    if type == "PLAYERMOVFROM":
        rectangles[location].isocupied = False
        rectangles[location].ocuideby = "AIR"
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
        for i in range(len(foodlist)):
            for a in range(len(rectangles)):
                if rectangles[a].id == foodlist[i].location and playerlist[0].pbox == foodlist[i].location:
                    pos = i
                    break
        playerlist[0].score += 1
        if playerlist[0].speed != 100:
            playerlist[0].speed -= foodlist[pos].speedincreas
        foodlist.pop(pos)
        bordocupationupdater("PLAYER",location)
        createwall()
        createfood(randomsquer())
        score = font.render(f'Score: {playerlist[0].score}', True, white,)
        speed = font.render(f'Speed: {playerlist[0].speed}', True, white,)

def randomsquer():
    a = random.choice(unocupidesquers)
    return a

def bordpainter():
    seconderywallcolor = (150,150,150)
    seconderyfoodcolor = (0,100,0)
    for i in range(len(rectangles)):
        if i/2 == int(i/2):
            pygame.draw.rect(screen, rectangles[i].color, (rectangles[i].x, rectangles[i].y, rectangles[i].heightwidth, rectangles[i].heightwidth))
        else:    
            pygame.draw.rect(screen, white, (rectangles[i].x, rectangles[i].y, rectangles[i].heightwidth, rectangles[i].heightwidth))  
    
    for c in range(len(foodlist)):
        pygame.draw.rect(screen, foodlist[c].color, (rectangles[foodlist[c].location].x, rectangles[foodlist[c].location].y, rectangles[foodlist[c].location].heightwidth, rectangles[foodlist[c].location].heightwidth))
        pygame.draw.rect(screen, seconderyfoodcolor, (rectangles[foodlist[c].location].x, rectangles[foodlist[c].location].y, rectangles[foodlist[c].location].heightwidth, rectangles[foodlist[c].location].heightwidth),3)
    
    pygame.draw.rect(screen, playerlist[0].color, (rectangles[playerlist[0].pbox].x, rectangles[playerlist[0].pbox].y, rectangles[playerlist[0].pbox].heightwidth, rectangles[playerlist[0].pbox].heightwidth))
    if len(walllist) !=0:
     for a in range(len(walllist)):
        pygame.draw.rect(screen, walllist[a].color, (rectangles[walllist[a].location].x, rectangles[walllist[a].location].y, rectangles[walllist[a].location].heightwidth, rectangles[walllist[a].location].heightwidth))
        pygame.draw.rect(screen, seconderywallcolor, (rectangles[walllist[a].location].x, rectangles[walllist[a].location].y, rectangles[walllist[a].location].heightwidth, rectangles[walllist[a].location].heightwidth),3)
   
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
    squerdocupationchecer()
    createfood(randomsquer())
    createfood(randomsquer())
    createfood(randomsquer())
    stattextgen()

def stattextgen():
    global scoreRect, speedRect, score, speed, font, font1, gameovertext, gameovertextRect
    font = pygame.font.SysFont('Corbel', 32)
    font1 = pygame.font.SysFont('Corbel', 50)
    score = font.render(f'Score: {playerlist[0].score}', True, white)
    scoreRect = score.get_rect()
    scoreRect.center = (100,400)
    speed = font.render(f'Speed: {playerlist[0].speed}', True, white)
    speedRect = speed.get_rect()
    speedRect.center = (100,450)
    gameovertext = font1.render(f'Game Over', True, red)
    gameovertextRect = speed.get_rect()
    gameovertextRect.center = (screenwidth/2-30, screenheight/2-60)

def mainmenu():
    global color_light, color_dark, text
    # white color  
    color_light = (170,170,170)  
    color_dark = (100,100,100)   
    smallfont = pygame.font.SysFont('Corbel',35)  
    text = smallfont.render('retry' , True , white) 

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
        screen.fill((30, 30, 30))
          
      
    # superimposing the text onto our button
        if go == True:
            mouse = pygame.mouse.get_pos() 
            screen.blit(text, (screenwidth/2-20,screenheight/2+5)) 
            screen.blit(gameovertext, gameovertextRect)
            screen.blit(score, (screenwidth/2-35,screenheight/2-25))
        else:
            pygame.time.delay(100)
            bordpainter()
            screen.blit(score, scoreRect)
            screen.blit(speed, speedRect)
        playermove()
        # Draw rectangles from the list
        # Update the display
        pygame.display.flip()
gameloop()