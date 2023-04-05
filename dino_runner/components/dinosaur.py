import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    DUCK_TIME = 20 # tiempo que el dinosaurio permanece agachado

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x =  self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 #que pierna toca
        self.dino_run = True #dice si esta corriendo
        self.dino_jump = False #dice si esta saltando
        self.jump_speed = self.JUMP_SPEED
        self.is_ducked = False #dice si esta agachado
        self.duck_time = 0 # Inicializa el tiempo que el dinosaurio permanece agachado en 0
        
    

    def update(self,user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False

        #if self.is_ducked: # Si el dinosaurio está agachado
        #    self.duck_time += 1 # Incrementa el tiempo que el dinosaurio ha permanecido agachado
        #    if self.duck_time > self.DUCK_TIME: # Si el tiempo ha pasado
        #        self.is_ducked = False # Establece la bandera de agachado como falsa
        #        self.duck_time = 0 # Reinicia el tiempo que el dinosaurio permanece agachado
        #elif user_input[pygame.K_DOWN] and not self.dino_jump: # Si el usuario pulsa la tecla de agacharse y el dinosaurio no está saltando ni agachado
        #    self.duck()
        #elif not self.dino_jump:
        #    self.run()

        
        # Comprueba si se ha presionado la tecla hacia abajo y si el dinosaurio no está saltando ni agachado
        if user_input[pygame.K_DOWN] and not self.dino_jump and not self.is_ducked:
            self.duck()
        # Comprueba si la tecla hacia abajo ya no se está presionando y si el dinosaurio está agachado
        elif not user_input[pygame.K_DOWN] and self.is_ducked:
            self.is_ducked = False
            self.run()
        
        # Si el dinosaurio está agachado, aumenta el tiempo que ha estado agachado y comprueba si ya ha pasado el tiempo máximo
        if self.is_ducked:
            self.duck_time += 1
            if self.duck_time > self.DUCK_TIME:
                self.is_ducked = False
                #self.duck_time = 0

        if self.step_index >= 10:
            self.step_index = 0


    

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
        

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y = self.jump_speed *4
        self.jump_speed -= 0.8

        if self.jump_speed < - self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED




    def duck(self):
        self.image = DUCKING[0]  # Cambia la imagen del dinosaurio a la imagen de agacharse
        self.dino_rect = self.image.get_rect()  # Ajusta la posición
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 40 #más 40 unidades para simular el efecto de que el dinosaurio se agacha
        self.is_ducked = True  # Establece la bandera de agachado como verdadera

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))

    def reset_dinosaur(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x =  self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 #que pierna toca
        self.dino_run = True #dice si esta corriendo
        self.dino_jump = False #dice si esta saltando
        self.jump_speed = self.JUMP_SPEED
        self.is_ducked = False #dice si esta agachado
        self.duck_time = 0 

