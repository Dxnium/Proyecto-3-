import pygame
from button import *
from colors import *


class StartWindow:
    surface = None
    width = 1280
    height = 720
    btn_servidor = None 
    btn_cliente = None 
        
    def start(self):
        pygame.display.set_caption('PvZ Duel - Menu')
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.surface.blit(fondo,(0,0))
        self.btn_servidor = Button(220, 500, "Crear Juego")
        self.btn_cliente = Button(860, 500, "Unirse")

    def dibujese(self):
        self.btn_servidor.draw(self.surface)
        self.btn_cliente.draw(self.surface)
        

    def main_loop_event(self, event):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        # Detecta el movimiento del mouse para cambiar el color del boton
        if event.type == pygame.MOUSEMOTION:
            self.btn_servidor.check_click(mouse_x, mouse_y)
            self.btn_cliente.check_click(mouse_x, mouse_y)

        # Detecta el click
        if event.type == pygame.MOUSEBUTTONUP:
            if self.btn_servidor.check_click(mouse_x, mouse_y):
                print("Click en servidor")
                return 1
            if self.btn_cliente.check_click(mouse_x, mouse_y):
                print("Click en cliente")
                return 2
        return 0