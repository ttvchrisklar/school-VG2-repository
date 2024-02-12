import pygame
import sys
# lists
playerlist = []
rectangles = []
borderw = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bordera = [0,17,34,51,68,85,102,119,136,153,170,187,204,221,238,255,272]
borders = [272,273,274,275,276,278,279,280,281,282,283,284,285,286,287,288]
borderd = [16,33,50,67,84,101,118,135,152,169,186,203,220,237,254,271,288]
class gridclass:
 def __init__(self,x,y,height,width,isocupied,ocuideby,color,id):
     self.x = x
     self.y = y
     self.height = height
     self.width = width
     self.isocupied = isocupied
     self.ocuideby = ocuideby
     self.color = color
     self.id = id
     pass
class player:
    def __init__(self,pbox,speed,score,color):
        self.pbox = pbox
        self.speed = speed
        self.score = score
        self.color = color
        pass
# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 800
screenwidth, screenheight = 1500, 800
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("TrolPac")
clock = pygame.time.Clock()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Function to add cubes to the list
def cubeprinter():
    row_spacing = 5
    rect_size = 40
    io = False
    o= "AIR"
    for row in range(height // (rect_size + row_spacing)):
        for col in range(width // (rect_size + row_spacing)):
            x = 360+col * (rect_size + row_spacing)
            y = 20+row * (rect_size + row_spacing)
            h = rect_size
            w = rect_size
            c = red
            i = len(rectangles)
            newrec = gridclass(x,y,h,w,io,o,c,i)
            rectangles.append(newrec)
            print(rectangles[i].id)

def playerclasscrator():
    posision = 144
    speed = 500
    score = 0
    color = (0,0,255)
    newplayer = player(posision,speed,score,color)
    playerlist.append(newplayer)

# code from stack overfllow link in documentastion
key_timeout = {}
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
    speed = 500
    ptomove = playerlist[0].pbox
    keys = pygame.key.get_pressed()
    if getPressed(keys, pygame.K_w, speed) and ptomove not in borderw:
        playerlist[0].pbox -= 17
        print("up",playerlist[0].pbox)
    if getPressed(keys, pygame.K_a, speed) and ptomove not in bordera:
        playerlist[0].pbox -= 1
        print("left",playerlist[0].pbox)
    if getPressed(keys, pygame.K_s, speed) and ptomove not in borders:
        playerlist[0].pbox += 17
        print("down",playerlist[0].pbox)
    if getPressed(keys, pygame.K_d, speed) and ptomove not in borderd:
        playerlist[0].pbox += 1
        print("right",playerlist[0].pbox)
    
# stil need to make a cheker for if the scuer is oqupied
# Call the cubeprinter function to add rectangles to the list
cubeprinter()
playerclasscrator()
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Clear the screen
    screen.fill((0, 0, 0))
    newcolor = (0,255,0)
    othercolor = (255,0,0)
    playermove()
    # Draw rectangles from the list
    for i in range(len(rectangles)):
        pygame.draw.rect(screen, rectangles[i].color, (rectangles[i].x, rectangles[i].y, rectangles[i].width, rectangles[i].height), 2)
        if rectangles[i].id/2 == int(rectangles[i].id/2):
            pygame.draw.rect(screen, newcolor, (rectangles[i].x+2, rectangles[i].y+2, rectangles[i].width-4, rectangles[i].height-4))
        else:
            pygame.draw.rect(screen, othercolor, (rectangles[i].x+2, rectangles[i].y+2, rectangles[i].width-4, rectangles[i].height-4))
    for i in range(len(rectangles)):
        if rectangles[i].id == playerlist[0].pbox:
            pygame.draw.rect(screen, playerlist[0].color, (rectangles[i].x+2, rectangles[i].y+2, rectangles[i].width-4, rectangles[i].height-4))
    # Update the display
    pygame.display.flip()
