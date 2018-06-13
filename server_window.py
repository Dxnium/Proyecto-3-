import pygame
import threading
import socket
from button import *
from Juego import *
from personaje_sprite import *
import time 

class ServerWindow:
    #Jugador
    player_servidor = None
    # UI
    surface = None
    width = 1280
    height = 720    
    btn_done = None
    img_fondo = None 
    
    # Socket
    running = True
    socket_s = None
    socket_c = None

    # Game logic
    board = None

    #sprite a dibujar 
    new_sprite = None
    nombre = None 

    # Variables para verificar que ambos jugadores esten listos
    listo_s = False
    listo_c = False

    #Cursor
    x_matriz = 1
    y_matriz = 1
    Cursor = None
    x = 259
    y = 125
    velocidad = 100

    #matriz de sprites 
    m = [[None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None]]

    
    # Se llama desde main.py cuando se crea la ventana
    def start(self):        
        self.set_initial_ui()
        self.start_socket_async()
        self.player_servidor = Juego('Plants vs Zombies')
        self.player_servidor.crear_matriz()


    #actualiza la pantalla y dibuja los sprites para actualizarla  
    def dibuje_sprites(self):
        for fila in range(0,5):
            for colum in range (0,9):
                dato = self.m[fila][colum] 
                if dato == None:
                    continue
                else:
                    self.new_sprite = dato
                    lista = [fila+1,colum+1]
                    print(lista)
                    self.set_sprite_2(lista)

    #detiene la comunicacion con el socket 
    def stop(self):
        self.running = False
        if self.socket_s != None:
            self.socket_s.close()
        if self.socket_c != None:
            self.socket_c.close()

#get info para la matriz de sprites 
    def get_info(self):
        for elemnt in self.m:
            print(' ')
            for x in elemnt:
                if x != None:
                    print(type(x),',',end='')
                    continue
                print(x,',',end='')
#inicia toda la parte visual 
#crea el fondo y botnes invisibles 
    def set_initial_ui(self):
        pygame.display.set_caption('PvZ Duel - Server')
        self.surface = pygame.display.set_mode((self.width, self.height))
        # self.surface.blit(fondo_juego, (0,0))
        self.btn_done = Buttondone(1100, 160, "Listo")
        #cursor
        self.Cursor = cursor.convert_alpha()
                #botones Para crear personajes 
        self.plata_verde = Button2(62,94,'Planta Verde')
        self.Nuez = Button2(62,235,'Nuez')
        self.zombie1 = Button2(62,376,'zombie1')
        self.zombie2 = Button2(62,523,'zombie2')
        # Botones en la cuadricula
        self.cuad11 = Button3(209,130,'1,1', 1, 1)
        self.cuad12 = Button3(209,252,'1,2', 1, 2)
        self.cuad13 = Button3(209,368,'1,3', 1, 3)
        self.cuad14 = Button3(209,485,'1,4', 1, 4)
        self.cuad15 = Button3(209,602,'1,5', 1, 5)
        self.cuad21 = Button3(297,130,'2,1', 2, 1)
        self.cuad22 = Button3(297,252,'2,2', 2, 2)
        self.cuad23 = Button3(297,368,'2,3', 2, 3)
        self.cuad24 = Button3(297,485,'2,4', 2, 4)
        self.cuad25 = Button3(297,602,'2,5', 2, 5)
        self.cuad31 = Button3(395,130,'3,1', 3, 1)
        self.cuad32 = Button3(395,252,'3,2', 3, 2)
        self.cuad33 = Button3(395,368,'3,3', 3, 3)
        self.cuad34 = Button3(395,485,'3,4', 3, 4)
        self.cuad35 = Button3(395,602,'3,5', 3, 5)
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



    # Se utiliza para iniciar el socket en un hilo aparte
    def start_socket_async(self):
        # Crea un hilo y le dice que ejeucte el metodo start_socket
        t = threading.Thread(target=self.start_socket)
        t.start()

    # Crea un socket. Espera la conexion de un cliente. Lee constantemente de la conexion realizada.
    def start_socket(self):
        self.socket_s = socket.socket()
        self.socket_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_s.bind((socket.gethostbyname(socket.gethostname()), 5507))
        self.socket_s.listen(10)
        print("Esperando cliente:")
        self.socket_c, (host_c, puerto_c) = self.socket_s.accept()        
        print("Cliente conectado:")
        while self.running:            
            print("Leyendo del socket")
            try:
                read = self.socket_c.recv(1024).decode()
                self.player_servidor.dato_rec = read
                # self.player_servidor.crear_personaje()
                self.personajes_socket()
                print("Read:", read)
                #self.personajes_socket()
                #crear la matriz GUI
            except:
                print("Se cayo")

    #Crea los personajes que el socket le envia.
    def personajes_socket(self):
        personajes = self.player_servidor.dato_rec.split(";")
        personajes = self.player_servidor.dato_rec.split(",")
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
#toma los datos que le envia personaje socket ya separados 
#y crea las instancias y coloca los sprites 
    def sprite_socket(self,nombre,c,f):
        print('Creando personaje')
        if nombre =='P001':
            print('Planta Verde')
            self.new_sprite = PersonajeSprite("media/images/verdeF.png")
            print(c,f)
            lista = [c,f]
            print(lista)
            self.m[f-1][c-1] = self.new_sprite
            self.set_sprite(lista)

        if nombre == 'P002' :
            self.new_sprite = PersonajeSprite("media/images/nuezF.png")
            lista = [c,f]
            print(lista)
            self.m[f-1][c-1] = self.new_sprite
            self.set_sprite(lista)

        if nombre == 'P003'  :
            self.new_sprite = PersonajeSprite("media/images/zombie1F.png")
            lista = [c,f]
            print(lista)
            self.m[f-1][c-1] = self.new_sprite
            self.set_sprite(lista)

        if nombre == 'P004':
            self.new_sprite = PersonajeSprite("media/images/zombie2F.png")
            lista = [c,f]
            print(lista)
            self.m[f-1][c-1] = self.new_sprite
            self.set_sprite(lista)
        else:
            return None


 #manda los datos que tenga gurdados por el socket    
    def btn_done_click(self):
        if self.socket_c != None:
            self.socket_c.send(self.player_servidor.dato.encode())
            

#loop que revisa constantemente si se presiona un boton en la pantalla 
# crea instancias sprites y las gurda en sus atributos  
#manda a colocar el sprite que busca lo que hay guardado en los atributos 
#y con la posicion de del boton coloca el sprite 
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
                self.new_sprite = PersonajeSprite("media/images/verde.png")
                self.nombre = 'P001'

            elif self.Nuez.check_click(mouse_x,mouse_y):
                self.new_sprite = PersonajeSprite("media/images/nuez.png")
                self.nombre = 'P002'

            elif self.zombie1.check_click(mouse_x,mouse_y): 
                self.new_sprite = PersonajeSprite("media/images/zombie1.png")
                self.nombre = 'P003'

            elif self.zombie2.check_click(mouse_x,mouse_y):
                #crea el sprite 
                self.new_sprite = PersonajeSprite("media/images/zombie2.png")
                self.nombre = 'P004'
            
            elif self.cuad11.check_click(mouse_x,mouse_y):
                x = self.cuad11.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[1]-1][x[0]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad12.check_click(mouse_x,mouse_y):
                x = self.cuad12.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.set_sprite(x)

            elif self.cuad13.check_click(mouse_x,mouse_y):
                x = self.cuad13.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad14.check_click(mouse_x,mouse_y):
                x = self.cuad14.retornar_pos()
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad15.check_click(mouse_x,mouse_y):
                x = self.cuad15.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)


            elif self.cuad21.check_click(mouse_x,mouse_y):
                x = self.cuad21.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad22.check_click(mouse_x,mouse_y):
                x = self.cuad22.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad23.check_click(mouse_x,mouse_y):
                x = self.cuad23.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad24.check_click(mouse_x,mouse_y):
                x = self.cuad24.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad25.check_click(mouse_x,mouse_y):
                x = self.cuad25.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad31.check_click(mouse_x,mouse_y):
                x = self.cuad31.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad32.check_click(mouse_x,mouse_y):
                x = self.cuad32.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad33.check_click(mouse_x,mouse_y):
                x = self.cuad33.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad34.check_click(mouse_x,mouse_y):
                x = self.cuad34.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)

            elif self.cuad35.check_click(mouse_x,mouse_y):
                x = self.cuad35.retornar_pos()
                print('Matriz de Sprites')
                if self.player_servidor.dinero != 0:
                    self.m[x[0]-1][x[1]-1] = self.new_sprite
                    self.get_info() 
                    self.set_sprite(x)



                                                        



# fucnicon para colocar los sprites en pantalla 

    def set_sprite(self,x):
        #si tiene dinero puede crear sprites 
        if self.player_servidor.dinero != 0:
        #dependiendo del nombre que este en los atributos 
        #crea la instancia correspondiente 
            if self.nombre =='P001':
                print('hola desde el dinero')
                self.player_servidor.set_planta_verde(x[0],x[1])
            if self.nombre == 'P002':
                self.player_servidor.set_nuez(x[0],x[1])
            
            if self.nombre == 'P003':
                self.player_servidor.set_zombie(x[0],x[1])
            
            if self.nombre == 'P004':
                self.player_servidor.set_zombie_2(x[0],x[1])
           
            try:
                #con la posicion que le manda el boton x que una lista con [c,f]
                #coloca el sprite en la pantalla 
                if x[0] == 1:
                    if x[1] == 1 :
                        print('dibujando')
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
                return  1
            except:
                #si no tiene soles no puede colocar nada 
                print('No tiene soles')

 
    def set_sprite_2(self,x):
        try:
            if x[0] == 1:
                if x[1] == 1 :
                    print('dibujando')
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
            return  1
        except:
            print('No tiene soles')
        else:
            print('No dinero')













        # Dibuja sus elementos en pantalla
    def dibujese(self):
        #Primero dibuja el fondo 
        self.surface.blit(fondo_juego, (0,0))
        #LUEGO DIBUJA LO DEMAS 
        #imagen cursor
        if self.player_servidor.dinero != 0:
            self.surface.blit(cursor, (self.x,self.y))
        else:
            self.surface.blit(cursor2, (self.x,self.y))
        #Label soles
        font = pygame.font.Font(None, 70)
        font_color = (0,0,0)
        monedas = font.render(str(self.player_servidor.dinero), True, font_color)
        monedas_rect = monedas.get_rect()
        self.surface.blit(monedas, (345,45))
        #Label Turno 
        font = pygame.font.Font(None, 70)
        font_color = (0,0,0)
        turno = font.render('1', True, font_color)
        turno_rect = turno.get_rect()
        self.surface.blit(turno, (870,40))


        # PRIMERO dibuja el fondo
        # self.surface.blit(self.img_fondo, self.img_fondo.get_rect())

        # DESPUES dibuja lo demas
        # self.btn_done.draw(self.surface) # Boton de listo

        #Crear botones para selecionar personajes 

        # self.plata_verde.draw(self.surface)
        # self.Nuez.draw(self.surface)
        # self.zombie2.draw(self.surface)
        # self.zombie1.draw(self.surface)
        # self.cuad11.draw(self.surface)
        # self.cuad12.draw(self.surface)
        # self.cuad13.draw(self.surface)
        # self.cuad14.draw(self.surface)
        # self.cuad15.draw(self.surface)
        # self.cuad21.draw(self.surface)
        # self.cuad22.draw(self.surface)
        # self.cuad23.draw(self.surface)
        # self.cuad24.draw(self.surface)
        # self.cuad25.draw(self.surface)
        # self.cuad31.draw(self.surface)
        # self.cuad32.draw(self.surface)
        # self.cuad33.draw(self.surface)
        # self.cuad34.draw(self.surface)
        # self.cuad35.draw(self.surface)
