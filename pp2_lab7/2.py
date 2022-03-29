import pygame

pygame.init()

pygame.mixer.music.load('music/music1.mp3')
pygame.mixer.music.play(-1) 

songs = ['music/music1.mp3', 'music/music2.mp3', 'music/music3.mp3']
win = pygame.display.set_mode((500,500))
bg = pygame.image.load('picture/bgmusic.png')


pause = False
queue = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                if queue == len(songs)-1: 
                    queue = 0
                else:
                    queue += 1 
                pygame.mixer.music.load(songs[queue]) 
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_LEFT:
                if queue == 0: 
                    queue = len(songs)
                else:
                    queue -= 1 
                pygame.mixer.music.load(songs[queue]) 
                pygame.mixer.music.play(-1)

    win.fill((255,255,255))
    win.blit(bg,(0,0))
    pygame.display.flip()