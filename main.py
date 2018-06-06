import pygame
from server_window import *
from start_window import *
from client_window import *
from colors import *

pygame.init()

# Ventanas
server_window = None
client_window = None
start_window = StartWindow()
start_window.start()

clock = pygame.time.Clock()
running = True
cont = 0 
while running:

    # Dibuja la ventana aunque no haya event
    if start_window != None:
        start_window.dibujese()
    elif client_window != None:
        #client_window.dibujese()
        if cont == 0:
            client_window .dibujese()
            cont += 1
    elif server_window != None:
        if cont == 0:
            server_window .dibujese()
            cont += 1



    # Obtiene los eventos del usuario y se los pasa a las ventanas
    for event in pygame.event.get():      

        # Si es el evento de quit, cierra los sockets y las ventantas
        if event.type == pygame.QUIT:
            running = False
            if server_window != None:
                server_window.stop()
            if client_window != None:
                client_window.stop()

        # En caso de que sea otro tipo de evento
        else:

            # Ventana principal
            if start_window != None:
                next_window = start_window.main_loop_event(event)
                if next_window == 1:
                    start_window = None
                    server_window = ServerWindow()
                    server_window.start()
                elif next_window == 2:
                    start_window = None
                    client_window = ClientWindow()
                    client_window.start()
                   

            # Ventana servidor
            elif server_window != None:
                server_window.main_loop_event(event)

            # Ventana cliente
            elif client_window != None:
                client_window.main_loop_event(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()