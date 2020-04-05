import pygame
import random

pygame.init()

background = pygame.image.load("back.jpg")

screen = pygame.display.set_mode((800, 600))

done = True
strike = False
# Player
x_play = 370
y_play = 480
#enemy
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
x_enemy_change = 4
y_enemy_change = 30
#bullet
#ready - > невидимая пуля
#fire -> видишь пулю когда стреляешь
bullet_x = 0
bullet_y = 480
y_bullet_change = 10

playerImage = pygame.image.load("player.png")
enemyImage = pygame.image.load("enemy.png")
bulletImage = pygame.image.load("bullet.png")

def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))

def bullet(x, y):
    screen.blit(bulletImage, (x, y)) #dlya korrectnogo mesta puli

def collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if (bullet_x >= enemy_x and bullet_x <= enemy_x + 64) and (bullet_y <= enemy_y + 64 and bullet_y >= enemy_y):
        return True
    return False

while done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x_play -= 5
    if pressed[pygame.K_RIGHT]:
        x_play += 5    
    if pressed[pygame.K_SPACE] and strike is False:
        bullet_x = x_play + 15
        bullet_y = y_play
        strike = True
    
    collis =  collision(enemy_x, enemy_y, bullet_x, bullet_y)

    if collis is True:
        bullet_x = 0
        bullet_y = 480
        enemy_x = random.randint(0, 800)
        enemy_y = random.randint(50, 150)
        strike = False

    if bullet_y < 0:
        bullet_x = 0
        bullet_y = 600
        strike = False

    if strike is not False:
        bullet_y -= y_bullet_change
        
    enemy_x += x_enemy_change
    if enemy_x <= 0:
        x_enemy_change = 4
        enemy_y +=y_enemy_change
    elif enemy_x >=736:
        x_enemy_change = -4
        enemy_y += y_enemy_change

    screen.blit(background, (0, 0))
    player(x_play, y_play)
    enemy(enemy_x, enemy_y)
    bullet(bullet_x, bullet_y)

    pygame.display.flip()