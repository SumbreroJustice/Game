import pygame
import sys
from enemy import bullet
from player import player
import random 

length, width = 600, 600
screen = (width, length)
red = (255, 0, 0)
White = (255, 255, 255)
pygame.display.init()
char_x = 10
char_y = 10
x_velocity = 0 
y_velocity = 0
speed = .5
bullet = bullet(100, 100)
running = True

def vel_change():
    global x_velocity
    global y_velocity
    global speed
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player.x > 5:
                x_velocity -= speed
            if event.key == pygame.K_s and player.y < 590:
                y_velocity += speed
            if event.key == pygame.K_d and player.y < 590:
                x_velocity += speed
            if event.key == pygame.K_w and player.y > 5:
                y_velocity -= speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.x > 5:
                x_velocity = 0
            if event.key == pygame.K_s and player.y < 590:
                y_velocity = 0
            if event.key == pygame.K_d and player.x < 590:
                x_velocity = 0
            if event.key == pygame.K_w and player.x > 5:
                y_velocity = 0




    

Display = pygame.display.set_mode(screen)
pygame.display.flip()
background = pygame.Surface(screen)

player = player(char_x, char_y)


def movement():
    global x_velocity

    

    


    if x_velocity != 0:
        player.x += x_velocity
        
    if y_velocity != 0:
        player.y += y_velocity
    if char_x > 590 or char_x < 5:
        player.x = 0
    if char_y > 590 or char_y < 5:
        player.y = 0

        
while running:

    
    
    background.fill(White)
    pygame.draw.rect(background, red, (0, 0, 600, 600), 25)
    bullet.hitbox.fill(White)
    player.hitbox.fill(White)
    player.hitbox.blit(player.image,(0,0))
    player.render(background)
    bullet.render(background)
    Display.blit(background,(0,0))
    player.movehit()
    if bullet.collision(player.hit):
        print(random.random())
        
    else:
        pass
    pygame.display.update()
    vel_change()
    movement()
