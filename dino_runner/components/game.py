from turtle import _Screen
import pygame
import os

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
class Game:
    GAME_SPEED = 20
    HIGHSCORE_FILE = "highscore.txt"
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu("Press and key to start..." ,self.screen)
        self.running = False
        self.death_count = 0
        self.score = 0
        self.highscore = self.load_highscore()
        self.total_deaths = 0 #contar las muertes
    #si se dediene por algun motivo se cierre
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing: #error en linea 27
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

        
    def run(self):
        self.obstacle_manager.reset_obstacle()
        self.player.reset_dinosaur()
        self.score = 0 
        self.game_speed = self.GAME_SPEED
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score() #dibuja el cuadro del conteo en pantalla
        pygame.display.update()
        
        
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.menu.reset_screen_color(self.screen)

        if self.death_count == 0: #si el contador de muertes es igual a 0, 
            #el método dibuja el menú en la pantalla. Si el contador de muertes 
            #es mayor que 0, el método actualiza el mensaje del menú para 
            # mostrar la puntuación actual del jugador 
            self.menu.draw(self.screen)
        else:
            #self.menu.update_message(f"Your score: {self.score} +\n Highscore: {self.highscore}")#antes estava new message
            self.menu.update_message(f"Your score: {self.score} \n Highscore: {self.highscore}")
            #self.menu.update_message(f"Your score: {self.score}")#muestra la puntuacion
            self.draw_score()

            self.menu.draw(self.screen)
            self.save_highscore()
            self.total_deaths += 1
        self.screen.blit(ICON,(half_screen_width-50,half_screen_height-140))
        #muestra una imagen del dinosaurio
        self.menu.update(self)
    #guarda el puntaje mas alto

    def save_highscore(self):
        # Si la puntuación actual del jugador es mayor que la puntuación máxima anterior
        if self.score > self.highscore:
            # Se abre el archivo "highscore.txt" en modo escritura
            with open(self.HIGHSCORE_FILE, "w") as f:
                # Se escribe la puntuación actual en el archivo
                f.write(str(self.score))
            # Se actualiza la puntuación máxima con la puntuación actual
            self.highscore = self.score

    def load_highscore(self):
        # Revisa si existe el archivo de highscore
        if os.path.exists(self.HIGHSCORE_FILE):
            with open(self.HIGHSCORE_FILE, "r") as f:
                # Carga la puntuación máxima anterior guardada en el archivo
                highscore = int(f.read())
        else:
            # Si el archivo no existe, se deja la puntuación en 0
            highscore = 0
        return highscore  # Retorna la puntuación máxima

    def update_score(self):#aumenta el valor de score
        self.score += 1
        if self.score % 100 == 0 and self.game_speed < 500: #aumenta la velocida
            self.game_speed +=5
        
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}',True,(0,0,0))
        #muestra el hig score en pantalla puntuacion maxima
        highscore_text = font.render(f'Highscore: {self.highscore}', True, (0, 0, 0))
        total_deaths_text = font.render(f'Total deaths: {self.total_deaths}', True, (0, 0, 0))
        text_rect = text.get_rect()
        highscore_rect = highscore_text.get_rect()
        total_deaths_rect = total_deaths_text.get_rect()
        text_rect.center = (1000, 50)
        #score_rect.center = (1000, 50)
        highscore_rect.center = (1000, 80)
        total_deaths_rect.center = (1000, 110)
        self.screen.blit(text, text_rect)
        #self.screen.blit(score_text, score_rect)
        self.screen.blit(highscore_text, highscore_rect)
        self.screen.blit(total_deaths_text, total_deaths_rect)

