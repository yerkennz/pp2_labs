import pygame
import datetime

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock_mickey mouse")
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load('picture/idle.jpeg'), (800,600))
left = pygame.transform.scale(pygame.image.load('picture/left_hand2.png'), (38,305))
right = pygame.transform.scale(pygame.image.load('picture/right_hand2.png'), (54,234))

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, -1*angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    window.blit(bg, (0,0))
    blitRotateCenter(window, right, (372,183), minute*6)
    blitRotateCenter(window, left, (382,149), second*6)

    pygame.display.flip()

pygame.quit()