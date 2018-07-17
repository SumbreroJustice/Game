import pygame
import sys

class player:
    def __init__(self, x, y,):

        pygame.sprite.Sprite.__init__(self)
        White = (255,255,255)
        self.x = x
        self.y = y
        self.image = pygame.image.load('triangle.png')
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0] * .05), (int(self.size[1] * .05)))) 
        self.image_b = self.image.get_rect()
        self.size = self.image.get_size()
        self.hitbox = pygame.Surface(self.size)
        self.hit = pygame.Rect(self.x, self.y, 5, 5)
        
        
    def render(self, background):
        background.blit(self.hitbox,(self.x, self.y))
    def movehit(self):
        self.hit = pygame.Rect(self.x - 15, self.y - 15, self.x , self.y)
                

