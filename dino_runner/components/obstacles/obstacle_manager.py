import pygame
from dino_runner.components.obstacles.catus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def generate_obstacle(self):
        #obstacle = Cactus(SMALL_CACTUS)
        obstacle = Cactus(SMALL_CACTUS, size='small')
        obstacle = Cactus(SMALL_CACTUS, 'small')
        obstacle = Cactus(LARGE_CACTUS, 'large')

        
        return obstacle
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

    def draw (self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)