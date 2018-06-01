import pygame
import threading
import socket
from button import *
from Juego import *
from personaje_sprite import *


class ClientWindow:
    #Jugador
    player_client = None
    # UI
    surface = None
    width = 1280
    height = 720
    btn_done = None
    

    # Socket
    socket_c = None
    running = True
    
    #sprite 
    new_sprite = None
    nombre = None
        
         
    def start(self):
        self.set_initial_ui()
        self.start_socket_async()
        self.player_client = Juego('Plants vs Zombies',False)
        self.player_client.crear_matriz()

    #detiene todo y cierra la ventana 
    def stop(self):
        if self.socket_c != None:
            self.socket_c.close()
#inicia toda la parte grafic, creando la ventana y tambien el socket
    def set_initial_ui(self):
        pygame.display.set_caption('PvZ Duel - Client')
        self.surface = pygame.display.set_mode((self.width,self.height))
        self.surface.blit(fondo_juego, (0,0))
        self.btn_done = Buttondone(1100, 160, "Listo")
        #botones Para crear personajes 
        self.plata_verde = Button2(62,94,'Planta Verde')
        self.Nuez = Button2(62,235,'Nuez')
        self.zombie1 = Button2(62,376,'zombie1')
        self.zombie2 = Button2(62,523,'zombie2')
        #botones de cuadricula 
        self.cuad71 = Button3(783,130,'7,1', 7, 1)
        self.cuad72 = Button3(783,252,'7,2', 7, 2)
        self.cuad73 = Button3(783,368,'7,3', 7, 3)
        self.cuad74 = Button3(783,485,'7,4', 7, 4)
        self.cuad75 = Button3(783,602,'7,5', 7, 5)
        self.cuad81 = Button3(881,130,'8,1', 8, 1)
        self.cuad82 = Button3(881,252,'8,2', 8, 2)
        self.cuad83 = Button3(881,368,'8,3', 8, 3)
        self.cuad84 = Button3(881,485,'8,4', 8, 4)
        self.cuad85 = Button3(881,602,'8,5', 8, 5)
        self.cuad91 = Button3(980,130,'9,1', 9, 1)
        self.cuad92 = Button3(980,252,'9,2', 9, 2)
        self.cuad93 = Button3(980,368,'9,3', 9, 3)
        self.cuad94 = Button3(980,485,'9,4', 9, 4)
        self.cuad95 = Button3(980,602,'9,5', 9, 5)

    def start_socket_async(self):
        t = threading.Thread(target=self.start_socket)
        t.start()

    def start_socket(self):
        
        self.socket_c = socket.socket()
        #toma la ip a la que va a concetar 
        #self.socket_c.connect((ip, 5507))
        #Porner manualmente la ip del servidor 
        #self.socket_c.connect((socket.gethostbyname(socket.gethostname()), 5507))
        self.socket_c.connect(("192.168.43.77", 5507))
        while self.running:
            read = self.socket_c.recv(1024).decode()
            self.player_client.dato_rec = read
            print("Read:", read)
            # self.player_client.crear_personaje()
            self.personajes_socket()
            #self.player_client.mover_matriz()
            pass

    #toma los datos recibidos por el socket
    #Y crea las instancias de personajes y
    #crea los sprites para mostrar en pantallas 
    def personajes_socket(self):
        personajes = self.player_client.dato_rec.split(";")
        personajes = self.player_client.dato_rec.split(",")
        # personajes = personajes[:len(self.dato_rec)-2]
        print(personajes)
        for elem in personajes:
            tmp_personaje = elem.split(";")
            print(3,tmp_personaje)
            if tmp_personaje == ['']:
                nombre = None
                c = None
                f = None
                return None
            else:
                contador = 0
                nombre = None
                c = None
                f = None
                jugador = None
            for elem2 in tmp_personaje:
                if contador == 0:
                    nombre = elem2
                    contador += 1
                    continue
                elif contador == 1:
                    f = int(elem2)
                    contador += 1
                    continue
                elif contador == 2:
                    c = int(elem2)
                    contador += 1
                    continue
                elif contador == 3:
                    jugador = bool(elem2)
                    continue
            self.sprite_socket(nombre,c,f)

    #Crea los sprites y define la posion 
    #deoendiendo del boton que sea presionado del board 
    def sprite_socket(self,nombre,c,f):
        print('Creando personaje')
        if nombre =='P001':
            print('Planta Verde')
            self.new_sprite = PersonajeSprite("media/images/verde.png")
            lista = [c,f]
            print(lista)
            self.set_sprite(lista)

        if nombre == 'P002' :
            self.new_sprite = PersonajeSprite("media/images/nuez.png")
            lista = [c,f]
            print(lista)
            self.set_sprite(lista)
        if nombre == 'P003'  :
            self.new_sprite = PersonajeSprite("media/images/zombie1.png")
            lista = [c,f]
            print(lista)
            self.set_sprite(lista)
        if nombre == 'P004':
            self.new_sprite = PersonajeSprite("media/images/zombie2.png")
            lista = [c,f]
            print(lista)
            self.set_sprite(lista)
        else:
            return None




    def btn_done_click(self):
        if self.socket_c != None:
            self.socket_c.send(self.player_client.dato.encode())


    # def handle_event(self, event):
    #     mouse_x = pygame.mouse.get_pos()[0]
    #     mouse_y = pygame.mouse.get_pos()[1]
    #     self.btn_done.draw(self.surface)

    #     # Detecta el movimiento del mouse para cambiar el color del boton
    #     if event.type == pygame.MOUSEMOTION:
    #         self.btn_done.check_click(mouse_x, mouse_y)

    #     # Detecta el click
    #     if event.type == pygame.MOUSEBUTTONUP:
    #         if self.btn_done.check_click(mouse_x, mouse_y):
    #             self.btn_done_click()                
    #             return 1
    #     return 0

    def main_loop_event(self, event):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        # Detecta el movimiento del mouse para cambiar el color del boton
        if event.type == pygame.MOUSEMOTION:
            self.btn_done.check_click(mouse_x, mouse_y)
            self.plata_verde.check_click(mouse_x,mouse_y)

        # Detecta el click
        if event.type == pygame.MOUSEBUTTONUP:
            if self.btn_done.check_click(mouse_x, mouse_y):
                self.btn_done_click()
                return 1

            elif self.plata_verde.check_click(mouse_x,mouse_y):
                self.new_sprite = PersonajeSprite("media/images/verdeF.png")
                self.nombre = 'P001'

            elif self.Nuez.check_click(mouse_x,mouse_y):
                self.new_sprite = PersonajeSprite("media/images/nuezF.png")
                self.nombre = 'P002'

            elif self.zombie1.check_click(mouse_x,mouse_y): 
                self.new_sprite = PersonajeSprite("media/images/zombie1F.png")
                self.nombre = 'P003'

            elif self.zombie2.check_click(mouse_x,mouse_y):
                #crea el sprite 
                self.new_sprite = PersonajeSprite("media/images/zombie2F.png")
                self.nombre = 'P004'
            
            elif self.cuad71.check_click(mouse_x,mouse_y):
                x = self.cuad71.retornar_pos()
                self.set_sprite(x)

            elif self.cuad72.check_click(mouse_x,mouse_y):
                x = self.cuad72.retornar_pos()
                self.set_sprite(x)

            elif self.cuad73.check_click(mouse_x,mouse_y):
                x = self.cuad73.retornar_pos()
                self.set_sprite(x)

            elif self.cuad74.check_click(mouse_x,mouse_y):
                x = self.cuad74.retornar_pos()
                self.set_sprite(x)

            elif self.cuad75.check_click(mouse_x,mouse_y):
                x = self.cuad75.retornar_pos()
                self.set_sprite(x)


            elif self.cuad81.check_click(mouse_x,mouse_y):
                x = self.cuad81.retornar_pos()
                self.set_sprite(x)

            elif self.cuad82.check_click(mouse_x,mouse_y):
                x = self.cuad82.retornar_pos()
                self.set_sprite(x)

            elif self.cuad83.check_click(mouse_x,mouse_y):
                x = self.cuad83.retornar_pos()
                self.set_sprite(x)

            elif self.cuad84.check_click(mouse_x,mouse_y):
                x = self.cuad84.retornar_pos()
                self.set_sprite(x)

            elif self.cuad85.check_click(mouse_x,mouse_y):
                x = self.cuad85.retornar_pos()
                self.set_sprite(x)

            elif self.cuad91.check_click(mouse_x,mouse_y):
                x = self.cuad91.retornar_pos()
                self.set_sprite(x)

            elif self.cuad92.check_click(mouse_x,mouse_y):
                x = self.cuad92.retornar_pos()
                self.set_sprite(x)

            elif self.cuad93.check_click(mouse_x,mouse_y):
                x = self.cuad93.retornar_pos()
                self.set_sprite(x)

            elif self.cuad94.check_click(mouse_x,mouse_y):
                x = self.cuad94.retornar_pos()
                self.set_sprite(x)

            elif self.cuad95.check_click(mouse_x,mouse_y):
                x = self.cuad95.retornar_pos()
                self.set_sprite(x)
    #dibuja los sprites en la pantalla 
    def set_sprite(self,x):
        print('Creando personaje')
        if self.nombre =='P001':
            self.player_client.set_planta_verde(x[0],x[1])
        if self.nombre == 'P002':
            self.player_client.set_nuez(x[0],x[1])
        
        if self.nombre == 'P003':
            self.player_client.set_zombie(x[0],x[1])
        
        if self.nombre == 'P004':
            self.player_client.set_zombie_2(x[0],x[1])
            # self.player_client.set_planta_verde(x[0],x[1])
        try:
            if x[0] == 1:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,259,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,259,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,259,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,259,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,259,617)
            elif x[0]==2:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,347,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,347,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,347,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,347,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,347,617)
            elif x[0] == 3:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,445,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,445,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,445,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,445,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,445,617)
            #######################################################
            elif x[0] == 7:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,833,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,833,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,833,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,833,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,833,617)
            elif x[0]==8:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,931,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,931,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,931,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,931,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,931,617)
            elif x[0] == 9:
                if x[1] == 1 :
                    self.new_sprite.dibujese(self.surface,1030,150)
                if x[1] == 2 :
                    self.new_sprite.dibujese(self.surface,1030,267)
                if x[1] == 3 :
                    self.new_sprite.dibujese(self.surface,1030,381)
                if x[1] == 4 :
                    self.new_sprite.dibujese(self.surface,1030,500)
                if x[1] == 5 :
                    self.new_sprite.dibujese(self.surface,1030,617)
            print("hola")
            return 1
        except:
            print('No tiene soles')

        # Dibuja sus elementos en pantalla
    def dibujese(self):
        print('')
        # PRIMERO dibuja el fondo
        

        # DESPUES dibuja lo demas
        # self.btn_done.draw(self.surface) # Boton de listo

        # #Crear botones para selecionar personajes 
        # self.plata_verde.draw(self.surface)
        # self.Nuez.draw(self.surface)
        # self.zombie2.draw(self.surface)
        # self.zombie1.draw(self.surface)
