import pygame
from server_window import *
from start_window import *
from client_window import *
from personaje_sprite import *
from colors import *
#python arduino
import serial
import time
x=[1]
y=[1]

variable = False
if variable == False:
    try:
        ser = serial.Serial('COM6', 9600, timeout=0)
    except:
        variable = True
pygame.init()
#
def start_arduino_async():
    # Crea un hilo y le dice que ejeucte el metodo start_socket
    t = threading.Thread(target=start_arduino)
    t.start()
def start_arduino():
    while 1:
        datos = leerArduino()
        if(datos.find("%") != -1):
            comando = datos[:datos.index("%")]
            valor = datos[datos.index("%")+1:]
            print("comando: ",comando, "  valor: ", valor)
            if server_window != None:
                if comando == 'arriba':
                    server_window.y_matriz -= 1
                    server_window.y-= 120
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if comando == 'abajo':
                    server_window.y_matriz += 1
                    server_window.y+= 120
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if comando == 'izquierda':
                    server_window.x_matriz -= 1
                    server_window.x-=server_window.velocidad
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if comando == 'derecha':
                    server_window.x_matriz += 1
                    server_window.x+=server_window.velocidad
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                #comndos botones para creas instancias y sprites 

                if comando == 'planta':
                    if server_window.player_servidor.dinero != 0:
                        server_window.new_sprite = PersonajeSprite("media/images/verde.png")
                        lista = [server_window.x_matriz,server_window.y_matriz]
                        server_window.player_servidor.set_planta_verde(lista[0],lista[1])
                        server_window.m[lista[0]-1][lista[1]-1] = server_window.new_sprite
                        print(lista)
                        server_window.dibujese()
                        server_window.dibuje_sprites()

                if comando == 'nuez':
                    if server_window.player_servidor.dinero != 0:
                        server_window.new_sprite = PersonajeSprite("media/images/nuez.png")
                        lista = [server_window.x_matriz,server_window.y_matriz]
                        server_window.player_servidor.set_nuez(lista[0],lista[1])
                        server_window.m[lista[0]-1][lista[1]-1] = server_window.new_sprite
                        print(lista)
                        server_window.set_sprite(lista)

                if comando == 'zombie1':
                    if server_window.player_servidor.dinero != 0:
                        server_window.new_sprite = PersonajeSprite("media/images/zombie1.png")
                        lista = [server_window.x_matriz,server_window.y_matriz]
                        server_window.player_servidor.set_zombie(lista[0],lista[1])
                        server_window.m[lista[0]-1][lista[1]-1] = server_window.new_sprite
                        print(lista)
                        server_window.set_sprite(lista)

                if comando == 'zombie2':
                    if server_window.player_servidor.dinero != 0:
                        server_window.new_sprite = PersonajeSprite("media/images/zombie2.png")
                        lista = [server_window.x_matriz,server_window.y_matriz]
                        server_window.player_servidor.set_zombie_2(lista[0],lista[1])
                        server_window.m[lista[0]-1][lista[1]-1] = server_window.new_sprite
                        print(lista)
                        server_window.set_sprite(lista)

            else:
                if comando == 'arriba':
                    client_window.x_matriz -= 1
                    client_window.y-=120
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if comando == 'abajo':
                    client_window.x_matriz += 1
                    client_window.y+=120
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if comando == 'izquierda':
                    client_window.y_matriz -= 1
                    client_window.x-=client_window.velocidad
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if comando == 'derecha':
                    client_window.y_matriz += 1
                    client_window.x+=client_window.velocidad
                    client_window.dibujese()
                    client_window.dibuje_sprites()

                ####comandos botones arduino
                if comando == 'planta':
                    if client_window.player_client.dinero != 0:
                        client_window.new_sprite = PersonajeSprite("media/images/verdeF.png")
                        lista = [client_window.x_matriz,client_window.y_matriz]
                        client_window.player_client.set_planta_verde(lista[1],lista[0])
                        client_window.m[lista[0]-1][lista[1]-1] = client_window.new_sprite
                        print(lista)
                        client_window.dibujese()
                        client_window.dibuje_sprites()

                if comando == 'nuez':
                    if client_window.player_client.dinero != 0:
                        client_window.new_sprite = PersonajeSprite("media/images/nuezF.png")
                        lista = [client_window.x_matriz,client_window.y_matriz]
                        client_window.player_client.set_nuez(lista[1],lista[0])
                        client_window.m[lista[0]-1][lista[1]-1] = client_window.new_sprite
                        print(lista)
                        client_window.dibujese()
                        client_window.dibuje_sprites()

                if comando == 'zombie1':
                    if client_window.player_client.dinero != 0:
                        client_window.new_sprite = PersonajeSprite("media/images/zombie1F.png")
                        lista = [client_window.x_matriz,client_window.y_matriz]
                        client_window.player_client.set_zombie(lista[1],lista[0])
                        client_window.m[lista[0]-1][lista[1]-1] = client_window.new_sprite
                        print(lista)
                        client_window.dibujese()
                        client_window.dibuje_sprites()

                if comando == 'zombie2':
                    if client_window.player_client.dinero != 0:
                        client_window.new_sprite = PersonajeSprite("media/images/zombie2F.png")
                        lista = [client_window.x_matriz,client_window.y_matriz]
                        client_window.player_client.set_zombie_2(lista[1],lista[0])
                        client_window.m[lista[0]-1][lista[1]-1] = client_window.new_sprite
                        print(lista)
                        client_window.dibujese()
                        client_window.dibuje_sprites()
#Lee los datos que envia el arduino por el serial 
def leerArduino():
    while 1:
        try:
            entrada = str(ser.readline());
            datos = entrada[entrada.index("'")+1: entrada.index("\\")]
            #print(entrada)
            return datos

        except:
            print('Data could not be read')
            time.sleep(1)


# Ventanas
server_window = None
client_window = None
start_window = StartWindow()
start_window.start()
start_arduino_async()






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



    # Obtiself.surface.blit(cursor, (self.x,self.y))ene los eventos del usuario y se los pasa a las ventanas
    for event in pygame.event.get():      

        # Si es el evento de quit, cierra los sockets y las ventantas
        if event.type == pygame.QUIT:
            running = False
            if server_window != None:
                server_window.stop()
            if client_window != None:
                client_window.stop()
        if event.type == pygame.KEYDOWN:
            if server_window != None:
                if event.key == pygame.K_LEFT:
                    server_window.x-=server_window.velocidad
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if event.key == pygame.K_RIGHT:
                    server_window.x+=server_window.velocidad
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if event.key== pygame.K_UP:
                    server_window.y-=120
                    server_window.dibujese()
                    server_window.dibuje_sprites()
                if event.key == pygame.K_DOWN:
                    server_window.y+=120
                    server_window.dibujese()
                    server_window.dibuje_sprites()
            else:
                if event.key == pygame.K_LEFT:
                    client_window.x-=client_window.velocidad
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if event.key == pygame.K_RIGHT:
                    client_window.x+=client_window.velocidad
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if event.key== pygame.K_UP:
                    client_window.y-=120
                    client_window.dibujese()
                    client_window.dibuje_sprites()
                if event.key == pygame.K_DOWN:
                    client_window.y+=120
                    client_window.dibujese()
                    client_window.dibuje_sprites()



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