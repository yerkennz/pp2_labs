import pygame
import sys
import random, time
from pygame.locals import *
pygame.init()

# Parametrs of objects
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 4
SCORE = 0

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 60)
score_font = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Screen parametrs
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Racer test")
bg = pygame.image.load("images/street.png")
# ---------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200,555)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 40:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < 355:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -STEP)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, STEP-2)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
# ----------------------------------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), 0)

    def update(self):
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(65, 335), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
# -----------------------------------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/Coin.png'), (35,35))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(65, SCREEN_WIDTH - 65), -100)

    def update(self):
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(65, 335), -100)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
# ----------------------------------------------------
pygame.mixer.music.load('sound/bg_s.wav')
pygame.mixer.music.play(-1)

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
# -------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    P1.update()
    E1.update()
    C1.update()

    WIN.blit(bg, (0,0))

    P1.draw(WIN)
    C1.draw(WIN)
    E1.draw(WIN)

    score_img = score_font.render(str(SCORE), True, BLACK)
    WIN.blit(score_img, (10,10))

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('sound/mcoin.wav').play()
        SCORE += 1
        for c in coins:
            c.kill()
        C1 = Coin()
        coins.add(C1)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.pause()
        pygame.mixer.Sound('sound/crash.wav').play()
        time.sleep(0.5)

        WIN.fill((255,0,0))
        WIN.blit(game_over, (30,250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)