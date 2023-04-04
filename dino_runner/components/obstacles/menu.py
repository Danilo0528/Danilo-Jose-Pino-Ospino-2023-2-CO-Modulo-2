import pygame
from dino_runner.utils.constants import Font_STYLE

class Menu:
    def __init__(self, message,screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(Font_STYLE,30)
        self.text = self.font.render (message,True,(0,0,0))
        self.text_rect = self.text.get_rect()

    def update(self):
        pass

    def draw (self ,screen):
        screen.blit(self.text,self.text_rect)