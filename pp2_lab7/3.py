import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))

x = 50
y = 50
R = 25
speed = 20

run = True
while run:
    pygame.time.delay(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 30:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 770:
        x += speed
    if keys[pygame.K_DOWN] and y < 570:
        y += speed
    if keys[pygame.K_UP] and y > 30:
        y -= speed

    win.fill((255,255,255))
    pygame.draw.circle(win,(255,0,0), (x,y), R)
    pygame.display.flip()