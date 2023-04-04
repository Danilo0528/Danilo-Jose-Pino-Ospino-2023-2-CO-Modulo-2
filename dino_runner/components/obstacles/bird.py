import pygame
import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_HEIGHTS


class Bird(Obstacle):
    def __init__(self, image, x, y):
        self.type = 0
        super().__init__(image, self.type, x, y)
        self.heights = BIRD_HEIGHTS
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.choice(self.heights)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1
#Este código muestra una clase llamada "Bird" 
# que representa un pájaro en un juego. 
# El constructor de la clase recibe una imagen, 
# una posición x e y como parámetros y 
# crea un rectángulo para la imagen del pájaro.
#Además, la clase tiene un método llamado 
# "draw" que dibuja la imagen del pájaro en la 
# pantalla utilizando la función "blit" del objeto "SCREEN". 
# La imagen del pájaro se anima cambiando la imagen que se 
# muestra en la pantalla cada vez que se llama al método "draw".