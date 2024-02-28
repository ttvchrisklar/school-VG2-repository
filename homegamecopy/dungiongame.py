import pygame
import random

pygame.init()
# lists
nextavalebelpress = 0
wallplacelist = []
key_timeout = {}
playerlist = []
rectangles = []
foodlist = []
walllist = []
unocupidesquers = []
portallist = []
borderwallpos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 85, 128, 171, 214, 257, 300, 343, 386, 429, 472, 515, 558, 601, 644, 687, 730, 773, 816, 859, 902, 945, 988, 1031, 1117, 1116, 1115, 1114, 1113, 1112, 1111, 1110, 1109, 1108, 1107, 1106, 1105, 1104, 1103, 1102, 1101, 1100, 1099, 1098, 1097, 1096, 1095, 1094, 1093, 1092, 1091, 1090, 1089, 1088, 1087, 1086, 1085, 1084, 1083, 1082, 1081, 1080, 1079, 1078, 1077, 1076, 1075, 1074, 1032, 989, 946, 903, 860, 817, 774, 731, 688, 645, 602, 559, 516, 473, 430, 387, 344, 301, 258, 215, 172, 129, 86, 43]
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
width, height = 1300, 800
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
class wall:
    def __init__(self,location,color):
        self.location = location
        self.color = color
        pass
class oregenerator:
    def __init__(self,location,color,oretype,genspeed,direction):
        self.location = location
        self.color = color
        self.oretype = oretype
        self.genspeed = genspeed
        self.direction = direction
        pass
# Set up display
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("PacTroll")
clock = pygame.time.Clock()
# Function to add cubes to the list
def cubeprinter():
    row_spacing = 5
    rect_size = 25
    io = False
    o= "AIR"
    for row in range(height // (rect_size + row_spacing)):
        for col in range(width // (rect_size + row_spacing)):
            x = 200+col * (rect_size + row_spacing) #when game is done uncoment this
            y = 10 + row * (rect_size + row_spacing)
            wh = rect_size
            c = black
            i = len(rectangles)
            newrec = gridclass(x,y,wh,io,o,c,i)
            rectangles.append(newrec)
    bordpaternmaker()

def playerclasscrator():
    posision = 144
    lastposision = 144
    speed = 250
    score = 0
    color = (0,0,255)
    newplayer = player(posision, lastposision, speed, score, color)
    playerlist.append(newplayer)
    bordocupationupdater("PLAYER",posision)

def createwall(pos):
    if pos < 0 or pos >= len(rectangles):
        print("Error: Invalid position for wall creation")
        print(pos)
        return
    
    color = (64, 64, 64)
    newwall = wall(rectangles[pos], color)  # Pass rectangles[pos] instead of pos
    walllist.append(newwall)
    bordocupationupdater("WALL", pos)

def createbuilding():
    print()

def makeborderwalls(borderwalls):
    for i in range(len(borderwalls)):
        createwall(borderwalls[i])
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
def keydetection():
    # max speed 100, lowest 750
    speed, ptomove, keys = playerlist[0].speed, playerlist[0].pbox, pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    if getPressed(keys, pygame.K_u, speed):
        bordpaternmaker()
    if getPressed(keys,pygame.K_r,speed) and go == True:
        gamestart()
    if getPressed(keys, pygame.K_w, speed):
        if rectangles[playerlist[0].pbox - 43].ocuideby == "WALL":
            print("hit wall")
            # gameover()
            return
        if rectangles[playerlist[0].pbox - 43].ocuideby == "AIR":           
            bordocupationupdater("AIR",ptomove)
            playerlist[0].pbox -= 43
            ptomove = playerlist[0].pbox
            bordocupationupdater("PLAYER",ptomove)
    
    if getPressed(keys, pygame.K_a, speed):
        if rectangles[playerlist[0].pbox - 1].ocuideby == "WALL":
            print("hit wall")
            # gameover()
            return
        if rectangles[playerlist[0].pbox - 1].ocuideby == "AIR":            
            bordocupationupdater("AIR",ptomove)
            playerlist[0].pbox -= 1
            ptomove = playerlist[0].pbox
            bordocupationupdater("PLAYER",ptomove)
    
    if getPressed(keys, pygame.K_s, speed):
        if rectangles[playerlist[0].pbox + 43].ocuideby == "WALL":
            print("hit wall")
            # gameover()
            return
        if rectangles[playerlist[0].pbox + 43].ocuideby == "AIR":            
            bordocupationupdater("AIR",ptomove)
            playerlist[0].pbox += 43
            ptomove = playerlist[0].pbox
            bordocupationupdater("PLAYER",ptomove)
    
    if getPressed(keys, pygame.K_d, speed):
        if rectangles[playerlist[0].pbox + 1].ocuideby == "WALL":
            print("hit wall")
            return
        if rectangles[playerlist[0].pbox + 1].ocuideby == "AIR":            
            bordocupationupdater("AIR",ptomove)
            playerlist[0].pbox += 1
            ptomove = playerlist[0].pbox
            bordocupationupdater("PLAYER",ptomove)

def squerdocupationchecer():
    global unocupidesquers
    unocupidesquers = []
    for i in range(len(rectangles)):
        if rectangles[i].ocuideby == "AIR":
            unocupidesquers.append(i)

def bordocupationupdater(type,location):
    rectangles[int(location)].isocupied = True
    rectangles[int(location)].ocuideby = type
    squerdocupationchecer()

def randomsquer():
    if not unocupidesquers:
        print("Error: No unoccupied squares available")
        return -1  # or any other value indicating error
    else:
        return random.choice(unocupidesquers)

def mouseclickchecer():
    global nextavalebelpress
    mouse = pygame.mouse.get_pos()
    canpres = True
    if ev.type == pygame.MOUSEBUTTONDOWN and canpres == True and ((nextavalebelpress <= pygame.time.get_ticks() and nextavalebelpress != 0)):
        for i in range(len(rectangles)):
            if rectangles[i].x <= mouse[0] <= rectangles[i].x+25 and rectangles[i].y <= mouse[1] <= rectangles[i].y+25 and rectangles[i].ocuideby == "AIR":
                rectangles[i].color = (random.randint(25,230),random.randint(25,230),random.randint(25,230))
                canpres = False
                nextavalebelpress= pygame.time.get_ticks()+100
                return
            

def bordpaternmaker():
    for i in range(len(rectangles)):
        if i % 2 != 0:
            rectangles[i].color = (255,255,255)
        else:
            rectangles[i].color = (0,0,0)
def bordpainter():
    seconderywallcolor = (150,150,150)
    for i in range(len(rectangles)):
        pygame.draw.rect(screen, rectangles[i].color, (rectangles[i].x, rectangles[i].y, rectangles[i].heightwidth, rectangles[i].heightwidth))  
    
    pygame.draw.rect(screen, playerlist[0].color, (rectangles[playerlist[0].pbox].x, rectangles[playerlist[0].pbox].y, rectangles[playerlist[0].pbox].heightwidth, rectangles[playerlist[0].pbox].heightwidth))

    for wall in walllist:
        wall_pos = wall.location.id  # Access the id attribute of the gridclass object
        pygame.draw.rect(screen, wall.color, (rectangles[wall_pos].x, rectangles[wall_pos].y, rectangles[wall_pos].heightwidth, rectangles[wall_pos].heightwidth))
        pygame.draw.rect(screen, seconderywallcolor, (rectangles[wall_pos].x, rectangles[wall_pos].y, rectangles[wall_pos].heightwidth, rectangles[wall_pos].heightwidth),3)

# stil need to make a cheker for if the scuer is oqupied
def gameover():
    global go
    go = True
    print("game over")
    print(playerlist[0].score)
    mainmenu()
# Call the cubeprinter function to add rectangles to the list
def gamestart():
    global playerlist, rectangles, portallist, walllist, go
    go = False
    playerlist = []
    rectangles = []
    portallist = []
    walllist = []
    cubeprinter()
    squerdocupationchecer()
    makeborderwalls(borderwallpos)
    playerclasscrator()
    squerdocupationchecer()
    stattextgen()

def stattextgen():
    global scoreRect, speedRect, score, speed, font, font1, gameovertext, gameovertextRect
    font = pygame.font.SysFont('Corbel', 25)
    font1 = pygame.font.SysFont('Corbel', 50)
    score = font.render(f'Score: {playerlist[0].score}', True, white)
    scoreRect = score.get_rect()
    scoreRect.center = (90,400)
    speed = font.render(f'Speed: {playerlist[0].speed}', True, white)
    speedRect = speed.get_rect()
    speedRect.center = (90,450)
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
        global ev, mouse
        for ev in pygame.event.get():  
          
            if ev.type == pygame.QUIT:  
                pygame.quit() 
                quit()  
        # Clear the screen
        screen.fill((30, 30, 30))
        # superimposing the text onto our button
        if go == True:
            mouse = pygame.mouse.get_pos()
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if screenwidth/2 <= mouse[0] <= screenwidth/2+140 and screenheight/2 <= mouse[1] <= screenheight/2+40:  
                    gamestart()
            screen.blit(text, (screenwidth/2-20,screenheight/2+5)) 
            screen.blit(gameovertext, gameovertextRect)
            screen.blit(score, (screenwidth/2-35,screenheight/2-25))
            keydetection()
        else:
            mouseclickchecer()
            keydetection()
            bordpainter()
            screen.blit(score, scoreRect)
            screen.blit(speed, speedRect)
        # Draw rectangles from the list
        # Update the display
        pygame.display.flip()
gameloop()