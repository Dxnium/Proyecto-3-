import pygame
from colors import *


# Botones generales para seleccionar el tipo de jugador
class Button:
    pos_x = 100
    pos_y = 100
    height = 100
    width = 200
    text = "Button"    
    text_surface = None
    text_rect = None
    clicked = False

    def __init__(self, pos_x, pos_y, text):
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_surface = font.render(text, True, black)
        print(type(self.text_surface))
        self.text_rect = self.text_surface.get_rect()
        print(type(self.text_rect))
        self.text_rect.center = ((self.pos_x + self.width/2),(self.pos_y + self.height/2))

    def draw(self, display):
        if self.clicked:
            pygame.draw.rect(display, red,(self.pos_x,self.pos_y,self.width,self.height))
        else:
            pygame.draw.rect(display, blue,(self.pos_x,self.pos_y,self.width,self.height))
        display.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_x, mouse_y):
        self.clicked = False
        if self.pos_y <= mouse_y <= self.pos_y + self.height:
            if self.pos_x <= mouse_x <= self.pos_x + self.width:
                self.clicked = True
        return self.clicked

# Botones para seleccionar los personajes
class Button2:
    pos_x = 100
    pos_y = 100
    height = 110
    width = 110
    text = "Button"    
    text_surface = None
    text_rect = None
    clicked = False

    def __init__(self, pos_x, pos_y, text):
        font = pygame.font.Font('freesansbold.ttf', 15)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_surface = font.render(text, True, black)
        print(type(self.text_surface))
        self.text_rect = self.text_surface.get_rect()
        print(type(self.text_rect))
        self.text_rect.center = ((self.pos_x + self.width/2),(self.pos_y + self.height/2))

    def draw(self, display):
        if self.clicked:
            pygame.draw.rect(display, red,(self.pos_x,self.pos_y,self.width,self.height))
        else:
            pygame.draw.rect(display, blue,(self.pos_x,self.pos_y,self.width,self.height))
        display.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_x, mouse_y):
        self.clicked = False
        if self.pos_y <= mouse_y <= self.pos_y + self.height:
            if self.pos_x <= mouse_x <= self.pos_x + self.width:
                self.clicked = True
        return self.clicked

# Botones para selelccionar la posicion en la cuadricula
class Button3:
    pos_x = 100
    pos_y = 100
    height = 100
    width = 78
    text = "Button"    
    text_surface = None
    text_rect = None
    clicked = False
    c = None
    f = None

    def __init__(self, pos_x, pos_y, text, c, f):
        font = pygame.font.Font('freesansbold.ttf', 15)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.c = c
        self.f = f
        self.text_surface = font.render(text, True, black)
        print(type(self.text_surface))
        self.text_rect = self.text_surface.get_rect()
        print(type(self.text_rect))
        self.text_rect.center = ((self.pos_x + self.width/2),(self.pos_y + self.height/2))

    def draw(self, display):
        if self.clicked:
            pygame.draw.rect(display, red,(self.pos_x,self.pos_y,self.width,self.height))
        else:
            pygame.draw.rect(display, blue,(self.pos_x,self.pos_y,self.width,self.height))
        display.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_x, mouse_y):
        self.clicked = False
        if self.pos_y <= mouse_y <= self.pos_y + self.height:
            if self.pos_x <= mouse_x <= self.pos_x + self.width:
                self.clicked = True
        return self.clicked

    def retornar_pos(self):
        return [self.c,self.f]

# Boton de listo
class Buttondone:
    pos_x = 100
    pos_y = 100
    height = 100
    width = 150
    text = "Button"
    text_surface = None
    text_rect = None
    clicked = False

    def __init__(self, pos_x, pos_y, text):
        font = pygame.font.Font('freesansbold.ttf', 30)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text_surface = font.render(text, True, black)
        print(type(self.text_surface))
        self.text_rect = self.text_surface.get_rect()
        print(type(self.text_rect))
        self.text_rect.center = ((self.pos_x + self.width/2),(self.pos_y + self.height/2))

    def draw(self, display):
        if self.clicked:
            pygame.draw.rect(display, red,(self.pos_x,self.pos_y,self.width,self.height))
        else:
            pygame.draw.rect(display, blue,(self.pos_x,self.pos_y,self.width,self.height))
        display.blit(self.text_surface, self.text_rect)

    def check_click(self, mouse_x, mouse_y):
        self.clicked = False
        if self.pos_y <= mouse_y <= self.pos_y + self.height:
            if self.pos_x <= mouse_x <= self.pos_x + self.width:
                self.clicked = True
        return self.clicked