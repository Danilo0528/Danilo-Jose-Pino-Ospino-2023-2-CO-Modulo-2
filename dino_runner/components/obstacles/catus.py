import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.radiant(0,2)
        super().__init__(image,self.type)
        self.rect.y = 325
