from classes import *
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption(Name)
player = pygame.surface.Surface((50,50))
clock = pygame.time.Clock()
player.fill((255,0,0))
player_x,player_y=50,50
player_velx,player_vely=0,0
player_accel=(0,0)
xcap=10
jumping=False
falling=False
jFrames=0
MaxjFrames=10
while True:
    player_accel=(0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key in [pygame.K_SPACE,pygame.K_UP]:
                player_vely = -10 if not jumping or jFrames else player_vely
                jumping=True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_accel=(-1,0)
    elif keys[pygame.K_RIGHT]:
        player_accel=(1,0)
    player_x += player_velx
    player_velx -= 2 if player_velx > 0 else -2 if player_velx < 0 else 0
    player_velx += player_accel[0] if abs(player_velx) < xcap else 0
    player_y += player_vely
    player_vely += player_accel[1]
    if player_y < 450 and not jumping:
        player_vely=9
    if jumping or falling:
        jFrames+=1
        if jFrames >= MaxjFrames or falling:
            falling = True
            jumping=False
            jFrames-=1
        if falling and not jFrames:
            falling = False
    if player_y >= 450:
        player_vely=0
        if player_y > 450:
            player_y=450
    render(screen,[player],[(player_x,player_y)])
    print_at((0,0))
    clock.tick(FPS)