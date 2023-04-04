import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, SCREEN_WIDTH


class Cactus(Obstacle):
    def __init__(self, image, size):
        super().__init__(image, size)
        self.image = image
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        if size == 'small':
            self.type = random.randint(0, 2)
            self.rect.y = 325
        elif size == 'large':
            self.type = random.randint(3, 5)
            self.rect.y = 300
