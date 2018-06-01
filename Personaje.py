from personaje_sprite import *

class Personajes:
    nombre = None
    pts_vida = 0
    puntos_atq = 0
    f = 0 #Fila
    c = 0 #Columna
    tipo = None
    jugador = None #True for servidor-->, False for Cliente<--
    movimiento = 0
    costo = 0
    #sprite
    url = None
    sprite = None

    m = [[None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None]]

    def __init__(self,nombre,pts_vida,pts_atq,tipo,jugador,f,c,movimiento,costo, url):
        self.nombre = nombre
        self.pts_vida = pts_vida
        self.puntos_atq = pts_atq
        self.tipo = tipo
        self.jugador = jugador
        self.f = f
        self.c = c
        self.movimiento = movimiento
        self.costo = costo
        self.url = url


    def posicion(self):
        if self.m[self.f-1][self.c-1] == None:
            self.m[self.f-1][self.c-1] = self
        else:
            print('Ya esta ocupado')

    def new_ubicacion(self):
        if self.jugador == True: #es servidor -->
            self.c = self.c + self.movimiento
            print('\n','Nueva ubicacion: ','C:',self.c,',','F:',self.f)
        else:
            self.c = self.c - self.movimiento #es cliente <--
            print('Nueva ubicacion: ','C:', self.c ,',','F:', self.f)
        
    def mover(self):
        if self.jugador == True: #es servidor -->
            if (self.c-1)+self.movimiento > 8:
                return None
            self.m[self.f-1][self.c-1]= None
            self.new_ubicacion()
            self.m[self.f-1][self.c-1]=self
        else:
            if (self.c-1)+self.movimiento < 0:
                return None
            self.m[self.f-1][self.c-1]= None
            self.new_ubicacion()
            self.m[self.f-1][self.c-1]=self
            

    def get_info(self):
        for elemnt in self.m:
            print(' ')
            for x in elemnt:
                if x != None:
                    print(x.nombre,',',end='')
                    continue
                print(x,',',end='')
          
    # Funcion que genera el ataque  
    def ataque(self):
        if self.nombre == "P001" or self.nombre == "P002":
            ver = verificar_fila_planta()
            if ver == 1:
                ataque_verde()
            elif ver == 2:
                pass
        elif self.nombre == "P003" or self.nombre == "P004":
            ver = verificar_fila_zombie()
            if ver == 1:
                ataque_zombie()
            elif ver == 2:
                pass
        return

    # Verifica si hay un jugador enemigo en la misma fila y lo ataca
    def verificar_fila_planta(self):
        fila = self.f
        if self.nombre == "P001":
            for element in matriz[fila]:
                if element != None:
                    if element.tipo == self.tipo:
                        print('hay un compañero al frente')
                        continue
                    else:
                        print('hay un enemigo al frete')
                        return 1
        return 2

    # Verifica si hay un jugador enemigo al lado y si es asi lo ataca
    def verificar_fila_zombie(self):
        fila = self.f
        lugar = self.c
        for element in matriz[fila]:
            if element != None:
                if element.tipo == self.tipo:
                        print('hay un compañero al frente')
                        continue
                else:                  
                    if element.c == lugar+1 or element.c == lugar-1:
                        return 1
        return 2

    def ataque_verde(self):
        fila = self.f
        for element in matriz[fila]:
            if element != None:
                    if element.tipo == self.tipo:
                        print('hay un compañero al frente')
                        continue
                    else:
                        element.pts_vida -= self.pts_atq
                        verificar_vida()
                        return

    def ataque_zombie(self):
        fila = self.f
        lugar = self.c
        for element in matriz[fila]:
            if element != None:
                if element.tipo == self.tipo:
                        print('hay un compañero al frente')                        
                        continue
                else:                  
                    if element.c == lugar+1 or element.c == lugar-1:
                        element.pts_vida -= self.pts_atq
                        verificar_vida()
                        return

    # Verifica que ninguna instancia haya muerto y si es asi la elimina
    def verificar_vida(self):
        for fila in matriz:
            for element in fila:
                if element.pts_vida <= 0:
                    element.c = None
                    # quitar sprite
        return