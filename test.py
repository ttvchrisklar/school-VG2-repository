import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
player, dir, size = pygame.Rect(100,100,20,20), (0, 0), 20
MOVEEVENT, t, trail = pygame.USEREVENT+1, 250, []
pygame.time.set_timer(MOVEEVENT, t)
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: dir = 0, -1
    if keys[pygame.K_a]: dir = -1, 0
    if keys[pygame.K_s]: dir = 0, 1
    if keys[pygame.K_d]: dir = 1, 0
    
    if pygame.event.get(pygame.QUIT): break
    for e in pygame.event.get():
        if e.type == MOVEEVENT: # is called every 't' milliseconds
            trail.append(player.inflate((-10, -10)))
            trail = trail[-5:]
            player.move_ip(*[v*size for v in dir])
            
    screen.fill((0,120,0))
    for t in trail:
        pygame.draw.rect(screen, (255,0,0), t)
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.display.flip()
