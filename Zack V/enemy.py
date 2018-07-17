import pygame

class bullet:
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        White = (255,255,255)
        Red = (0, 255, 0)
        length, width = 29, 29
        size = (length,width)
        self.x = x
        self.y = y
        self.image = pygame.image.load('C:\\Users\\iD Student\\Desktop\\Zack V\\bullet.png')
        self.size = self.image.get_size()
        self.hitbox = pygame.Surface(self.size)
        self.hit = pygame.Rect(self.x - 7.5, self.y - 7.5, 5, 5)

        #self.image = pygame.transform.scale(self.image, (int(self.size[0] * .5), (int(self.size[1] * .5)))) 
        
    def render(self, background):
        
        self.hitbox.blit(self.image,(0,0))
        background.blit(self.hitbox,(self.x, self.y))
    def collision(self, player_rect):
            col = self.hit.colliderect(player_rect)
            return col
    def movehit(self):
        self.hit = pygame.Rect(self.x - 15, self.y - 15, self.x , self.y)
        
        
   

