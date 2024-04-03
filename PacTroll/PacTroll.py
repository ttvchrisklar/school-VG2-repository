import pygame
import random

pygame.init()
# lists
row_spacing = 5
rect_size = 40
# path is not permement if you want to use cmd you need to edit the path to whats under just your own path
txt_dock = "C:/Users/chris/Desktop/skole/programfag/coding/school-VG2-repository/PacTroll/gamescore.txt"
game_mode = "STANDERD"
last_eaten_food_posision = ""
dir = 0
key_timeout = {}
player_list = []
rectangles = []
food_list = []
wall_list = []
unocupide_squers = []
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
width, height = 1360, 790
screen_width, screen_height = 1500, 800
go = False
class gridclass:
 def __init__(self,x,y,height_width,is_ocupied,ocuide_by,color,id):
     self.x = x
     self.y = y
     self.height_width = height_width
     self.is_ocupied = is_ocupied
     self.ocuide_by = ocuide_by
     self.color = color
     self.id = id
     self.is_viseble = True
     pass
class player:
    def __init__(self,location,last_location,speed,score,color):
        self.location = location #box the player is in
        self.last_location = last_location #last box the player was in
        self.speed = speed
        self.score = score
        self.color = color
        pass
class food:
    def __init__(self,location,speed_increas,color):
        self.location = location
        self.speed_increas = speed_increas
        self.color = color
        self.is_viseble = True
        pass
class wall:
    def __init__(self,location,color):
        self.location = location
        self.color = color
        self.is_viseble = True
        pass

# Set up display
# screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PacTroll")
clock = pygame.time.Clock()

def change_gamode():
    global game_mode
    speed = player_list[0].speed
    keys = pygame.key.get_pressed()
    if getPressed(keys, pygame.K_1, speed):
        game_mode = "STANDERD"
        return
    if getPressed(keys, pygame.K_2, speed):
        game_mode = "LOWVIS"
        print("gamode changed")
        return
    if getPressed(keys, pygame.K_3, speed):
        game_mode = "OTHER"
        return

# Function to add cubes to the list
def cube_printer():
    io = False
    o= "AIR"
    for row in range(height // (rect_size + row_spacing)):
        for col in range(width // (rect_size + row_spacing)):
            x = 140+col * (rect_size + row_spacing)
            y = 10 + row * (rect_size + row_spacing)
            new_rec = gridclass(x,y,rect_size,io,o,(100,100,100),len(rectangles))
            rectangles.append(new_rec)

def finde_senter():
    midel = len(rectangles)//2
    return midel

def player_class_crator():
    posision = finde_senter()
    new_player = player(posision, posision, 750, 0, (0,0,255))
    player_list.append(new_player)
    bord_ocupation_updater("PLAYERMOVTO",posision)

def create_food(pos):
    new_food = food(pos,10,(255,0,0))
    food_list.append(new_food)
    bord_ocupation_updater("FOOD",pos)

def create_wall(pos):
    new_wall = wall(pos,(64,64,64))
    wall_list.append(new_wall)
    bord_ocupation_updater("WALL",pos)

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
def player_move():
    global dir, grid_width
    # max speed 100, lowest 750
    speed = player_list[0].speed
    p_to_move = player_list[0].location
    keys = pygame.key.get_pressed()
    grid_width = len(rectangles) // (height // (rect_size + row_spacing))
    
    if keys[pygame.K_g]:
        game_over()
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()
    
    if getPressed(keys, pygame.K_r, speed) and go == False:
        dir += 90
        if dir == 360:
            dir = 0
        return
    
    if keys[pygame.K_r] and go == True:
        game_start()
    
    
    if getPressed(keys, pygame.K_q, speed):
        dir = 0
        if rectangles[player_list[0].location].y == rectangles[0].y or rectangles[player_list[0].location - grid_width+1].ocuide_by == "WALL":
            game_over()
            return
        
        if rectangles[player_list[0].location - grid_width+1].ocuide_by == "FOOD" or rectangles[player_list[0].location - grid_width+1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location -= grid_width+1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_w, speed):
        dir = 0
        if rectangles[player_list[0].location].y == rectangles[0].y or rectangles[player_list[0].location - grid_width].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location - grid_width].ocuide_by == "FOOD" or rectangles[player_list[0].location - grid_width].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location -= grid_width
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_e, speed):
        dir = 0
        if rectangles[player_list[0].location].y == rectangles[0].y or rectangles[player_list[0].location - grid_width-1].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location - grid_width-1].ocuide_by == "FOOD" or rectangles[player_list[0].location - grid_width-1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location -= grid_width - 1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_a, speed):
        dir = 270
        if rectangles[player_list[0].location].x == rectangles[0].x or rectangles[player_list[0].location - 1].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location - 1].ocuide_by == "FOOD" or rectangles[player_list[0].location - 1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location -= 1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_s, speed):
        dir = 180
        if rectangles[player_list[0].location].y == rectangles[-1].y or rectangles[player_list[0].location + grid_width].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location + grid_width].ocuide_by == "FOOD" or rectangles[player_list[0].location + grid_width].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location += grid_width
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_d, speed):
        dir = 90
        if rectangles[player_list[0].location].x == rectangles[-1].x or rectangles[player_list[0].location + 1].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location + 1].ocuide_by == "FOOD" or rectangles[player_list[0].location + 1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location += 1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_z, speed):
        dir = 180
        if rectangles[player_list[0].location].y == rectangles[-1].y or rectangles[player_list[0].location + grid_width - 1].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location + grid_width - 1].ocuide_by == "FOOD" or rectangles[player_list[0].location + grid_width - 1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location += grid_width - 1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)
    
    if getPressed(keys, pygame.K_x, speed):
        dir = 180
        if rectangles[player_list[0].location].y == rectangles[-1].y or rectangles[player_list[0].location + grid_width + 1].ocuide_by == "WALL":
            game_over()
            return
        if rectangles[player_list[0].location + grid_width + 1].ocuide_by == "FOOD" or rectangles[player_list[0].location + grid_width + 1].ocuide_by == "AIR":
            player_list[0].last_location = player_list[0].location
            bord_ocupation_updater("AIR",p_to_move)
            player_list[0].location += grid_width + 1
            p_to_move = player_list[0].location
            food_to_wall_convertor()
            eat_food(p_to_move)
            bord_ocupation_updater("PLAYERMOVTO",p_to_move)

def squer_ocupation_checer():
    global unocupide_squers
    unocupide_squers = []
    for rec in rectangles:
        if rec.ocuide_by == "AIR":
            unocupide_squers.append(rec.id)

def bord_ocupation_updater(type,location):
    rectangles[location].is_ocupied = True
    rectangles[location].ocuide_by = type
    squer_ocupation_checer()
    
def eat_food(location):
    global score,speed,last_eaten_food_posision
    if rectangles[location].ocuide_by != "FOOD":
        return
    for i in range(len(food_list)):
        for a in range(len(rectangles)):
            if rectangles[a].id == food_list[i].location and player_list[0].location == food_list[i].location:
                pos = i
                break
    player_list[0].score += 1
    if player_list[0].speed != 100:
        player_list[0].speed -= food_list[pos].speed_increas
    last_eaten_food_posision = food_list[pos].location
    food_list.pop(pos)
    bord_ocupation_updater("PLAYER",location)
    create_food(random_squer())
    score = font.render(f'Score: {player_list[0].score}', True, white,)
    speed = font.render(f'Speed: {player_list[0].speed}', True, white,)

def random_squer():
    a = random.choice(unocupide_squers)
    return a

def food_to_wall_convertor():
    global last_eaten_food_posision
    if player_list[0].score == 0:
        return
    last_eaten_food_posision = int(last_eaten_food_posision)
    if rectangles[last_eaten_food_posision].ocuide_by == "AIR":
        create_wall(last_eaten_food_posision)

def draw_player_face():
    # paints the eye on the troll
    eye_frame_hight,eye_frame_width = rectangles[player_list[0].location].height_width - 26,rectangles[player_list[0].location].height_width - 26
    eye_ball_hight,eye_ball_width = rectangles[player_list[0].location].height_width - 33, rectangles[player_list[0].location].height_width - 33
    match dir:
        case 0:
            set_face(rectangles[player_list[0].location].x + 13, rectangles[player_list[0].location].y + 0, eye_frame_hight, eye_frame_width, rectangles[player_list[0].location].x + 16, rectangles[player_list[0].location].y + 3, eye_ball_hight, eye_ball_width)
        case 270:
            set_face(rectangles[player_list[0].location].x, rectangles[player_list[0].location].y + 13, eye_frame_hight, eye_frame_width, rectangles[player_list[0].location].x + 3, rectangles[player_list[0].location].y + 16, eye_ball_hight, eye_ball_width)
        case 180:
            set_face(rectangles[player_list[0].location].x+13, rectangles[player_list[0].location].y+25, eye_frame_hight, eye_frame_width, rectangles[player_list[0].location].x + 16, rectangles[player_list[0].location].y + 28, eye_ball_hight, eye_ball_width)
        case 90:
            set_face(rectangles[player_list[0].location].x+25, rectangles[player_list[0].location].y + 13, eye_frame_hight, eye_frame_width, rectangles[player_list[0].location].x + 28, rectangles[player_list[0].location].y + 16, eye_ball_hight, eye_ball_width)

def set_face(eye_frame_x, eye_frame_y, eye_frame_hight, eye_frame_width, eye_ball_x, eye_ball_y, eye_ball_hight, eye_ball_width):
    pygame.draw.rect(screen, white, (eye_frame_x, eye_frame_y, eye_frame_hight, eye_frame_width))
    pygame.draw.rect(screen, black, (eye_ball_x, eye_ball_y, eye_ball_hight, eye_ball_width))

def bord_patern_maker():
    for i in range(len(rectangles)):
        rectangles[i].color = (200,200,200)

def bord_painter():
    if game_mode == "LOWVIS":
        visebilety()
    secondery_wall_color = (150,150,150)
    secondery_player_color = (50,150,255)
    secondery_food_color = (200,200,200)
    for i in range(len(rectangles)):
        if rectangles[i].is_viseble == True:
            pygame.draw.rect(screen, rectangles[i].color, (rectangles[i].x, rectangles[i].y, rectangles[i].height_width, rectangles[i].height_width))
         
    
    for c in range(len(food_list)):
        if food_list[c].is_viseble == True:
            pygame.draw.rect(screen, food_list[c].color, (rectangles[food_list[c].location].x, rectangles[food_list[c].location].y, rectangles[food_list[c].location].height_width, rectangles[food_list[c].location].height_width))
            pygame.draw.rect(screen, secondery_food_color, (rectangles[food_list[c].location].x, rectangles[food_list[c].location].y, rectangles[food_list[c].location].height_width, rectangles[food_list[c].location].height_width),3)
    
    pygame.draw.rect(screen, player_list[0].color, (rectangles[player_list[0].location].x, rectangles[player_list[0].location].y, rectangles[player_list[0].location].height_width, rectangles[player_list[0].location].height_width))
    pygame.draw.rect(screen, secondery_player_color, (rectangles[player_list[0].location].x, rectangles[player_list[0].location].y, rectangles[player_list[0].location].height_width, rectangles[player_list[0].location].height_width),5)
    draw_player_face()
    if len(wall_list) !=0:
     for a in range(len(wall_list)):
        if wall_list[a].is_viseble == True:
            pygame.draw.rect(screen, wall_list[a].color, (rectangles[wall_list[a].location].x, rectangles[wall_list[a].location].y, rectangles[wall_list[a].location].height_width, rectangles[wall_list[a].location].height_width))
            pygame.draw.rect(screen, secondery_wall_color, (rectangles[wall_list[a].location].x, rectangles[wall_list[a].location].y, rectangles[wall_list[a].location].height_width, rectangles[wall_list[a].location].height_width),3)

def visebilety():
    for wall in wall_list:
        wall.is_viseble = False
    for food in food_list:
        food.is_viseble = False
    for rec in rectangles:
        rec.is_viseble = False
    
    visebilety_up = [player_list[0].location - grid_width, player_list[0].location - grid_width*2, player_list[0].location - (grid_width*2)-1, player_list[0].location - (grid_width*2)+1, player_list[0].location - grid_width*3, player_list[0].location - (grid_width*3)-1,player_list[0].location - (grid_width*3)+1, player_list[0].location - (grid_width*3)-2 ,player_list[0].location - (grid_width*3)+2,player_list[0].location - grid_width*4, player_list[0].location - (grid_width*4)-1,player_list[0].location - (grid_width*4)+1, player_list[0].location - (grid_width*4)-2 ,player_list[0].location - (grid_width*4)+2]
    visebilety_down = [player_list[0].location + grid_width, player_list[0].location + grid_width*2, player_list[0].location + (grid_width*2)-1, player_list[0].location + (grid_width*2)+1, player_list[0].location + grid_width*3, player_list[0].location + (grid_width*3)-1,player_list[0].location + (grid_width*3)+1, player_list[0].location + (grid_width*3)-2 ,player_list[0].location + (grid_width*3)+2, player_list[0].location + grid_width*4, player_list[0].location + (grid_width*4)-1, player_list[0].location + (grid_width*4)+1, player_list[0].location + (grid_width*4)-2 ,player_list[0].location + (grid_width*4)+2]
    visebilety_left = [player_list[0].location + 1, player_list[0].location + 2, player_list[0].location + 3, player_list[0].location + (grid_width)+2,player_list[0].location - (grid_width)+2,player_list[0].location + (grid_width)+3,player_list[0].location - (grid_width)+3, player_list[0].location + (grid_width*2)+3,player_list[0].location - (grid_width*2)+3]
    visebilety_right = [player_list[0].location - 1, player_list[0].location - 2, player_list[0].location - 3, player_list[0].location - (grid_width)-2,player_list[0].location + (grid_width)-2,player_list[0].location - (grid_width)-3,player_list[0].location + (grid_width)-3, player_list[0].location - (grid_width*2)-3,player_list[0].location + (grid_width*2)-3]

    if dir == 0:
        for wall in wall_list:
            if wall.location in visebilety_up:
                wall.is_viseble = True
        for food in food_list:
            if food.location in visebilety_up:
                food.is_viseble = True
        for rec in rectangles:
            if rec.id in visebilety_up:
                rec.is_viseble = True
    if dir == 90:
        for wall in wall_list:
            if wall.location in visebilety_left:
                wall.is_viseble = True
        for food in food_list:
            if food.location in visebilety_left:
                food.is_viseble = True
        for rec in rectangles:
            if rec.id in visebilety_left:
                rec.is_viseble = True
    if dir == 180:
        for wall in wall_list:
            if wall.location in visebilety_down:
                wall.is_viseble = True
        for food in food_list:
            if food.location in visebilety_down:
                food.is_viseble = True
        for rec in rectangles:
            if rec.id in visebilety_down:
                rec.is_viseble = True
    if dir == 270:
        for wall in wall_list:
            if wall.location in visebilety_right:
                wall.is_viseble = True
        for food in food_list:
            if food.location in visebilety_right:
                food.is_viseble = True
        for rec in rectangles:
            if rec.id in visebilety_right:
                rec.is_viseble = True

def game_high_score():
    global high_score
    file = open(txt_dock,'r',encoding='utf-8')
    lines_read = file.readlines()
    file.close()
    # this function writes new things to a txt dock
    if int(lines_read[0]) < player_list[0].score:
        file = open(txt_dock,'w',encoding='utf-8')
        file.writelines(str(player_list[0].score))
        file.close()
    file = open(txt_dock,'r',encoding='utf-8')
    high_score = font.render(f'High Score: {file.readline()}', True, white)

def game_over():
    global go
    go = True
    game_high_score()
    main_menu()

def game_start():
    global player_list, rectangles, food_list, wall_list, go
    go = False
    player_list = []
    rectangles = []
    food_list = []
    wall_list = []
    cube_printer()
    player_class_crator()
    squer_ocupation_checer()
    create_food(random_squer())
    create_food(random_squer())
    create_food(random_squer())
    stat_text_generator()

def stat_text_generator():
    global score_Rect, speed_Rect, score, speed, font, font_1, game_over_text, game_over_text_Rect
    font = pygame.font.SysFont('Corbel', 30)
    font_1 = pygame.font.SysFont('Corbel', 50)
    game_high_score()
    score = font.render(f'Score: {player_list[0].score}', True, white)
    score_Rect = score.get_rect()
    score_Rect.center = (50,400)
    speed = font.render(f'Speed: {player_list[0].speed}', True, white)
    speed_Rect = speed.get_rect()
    speed_Rect.center = (64,450)
    game_over_text = font_1.render(f'Game Over', True, red)
    game_over_text_Rect = speed.get_rect()
    game_over_text_Rect.center = (screen_width/2-30, screen_height/2-60)

def main_menu():
    global color_light, color_dark, r_text
    # white color  
    color_light = (170,170,170)  
    color_dark = (100,100,100)   
    small_font = pygame.font.SysFont('Corbel',30)  
    r_text = small_font.render('Retry press key "R"' , True , white) 

game_start()
# Main game loop
def game_loop():
    while True:
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT:  
                pygame.quit() 
                quit() 
        # Clear the screen
        screen.fill((0, 0, 0))      
    # superimposing the text onto our button
        if go == True:
            screen.blit(r_text, (screen_width/2-100,screen_height/2+30)) 
            screen.blit(game_over_text, game_over_text_Rect)
            screen.blit(score, (screen_width/2-35,screen_height/2-25))
            screen.blit(high_score, (screen_width/2-95,screen_height/2+3))
            change_gamode()
            player_move()
        else:
            screen.blit(score, score_Rect)
            screen.blit(speed, speed_Rect)
            player_move()
            bord_painter()
        # Draw rectangles from the list
        # Update the display
        pygame.display.flip()
game_loop()