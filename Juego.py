from Personaje import *
from personaje_sprite import *

class Juego:
    nombre = None
    Matriz = None
    jugador = None
    lista = []
    turno = 0
    dinero = 100
    #Dato tipo str que va a ser enviado por el socket
    dato = '' #str
    #dato que recibo del socket
    dato_rec = None
    #perosnaje
    perosnaje = None


    
    def __init__(self,nombre,jugador=True):
        self.nombre = nombre
        self.jugador = jugador

    #crea la mtriz donde se van a meter las instancias de personajes 
    def crear_matriz(self):
            self.Matriz = Personajes('Matriz',0,0,'Matiz',True,0,0,0,0,None)

#mueve lo elementos de la matriz
#se mueven de acuerdo a los argumentos establecidos en la clase perosnjae
    def mover_matriz(self):
        for elemnt in self.Matriz.m:
            tmp = None
            for x in elemnt:
                if x != None and tmp != x:
                    print (x.nombre,'se esta moviendo')
                    x.mover()
                    tmp = x
                else:
                    continue
    # Genera instancias de los datos recibidos del socket
    def crear_personaje(self):
        print(1,self.dato_rec)
        personajes = self.dato_rec.split(",")
        personajes = personajes[:len(self.dato_rec)-2]
        print(2,personajes)
        for elem in personajes:
            tmp_personaje = elem.split(";")
            print(3,tmp_personaje)
            contador = 0
            nombre = None
            f = None
            c = None
            jugador = None
            for elem2 in tmp_personaje:
                if contador == 0:
                    nombre = elem2
                    contador += 1
                    continue
                elif contador == 1:
                    c = int(elem2)
                    contador += 1
                    continue
                elif contador == 2:
                    f = int(elem2)
                    contador += 1
                    continue
                elif contador == 3:
                    jugador = bool(elem2)
                    continue
            print(4,nombre)
            self.crear_personaje_aux(nombre, c, f, jugador)
#funcion aux para crear personaje 
    def crear_personaje_aux(self, nombre, c, f, jugador):
        if nombre == "P001":
            self.set_planta_verde_socket(c, f, jugador)
        elif nombre == "P002":
            self.set_nuez_socket(c, f, jugador)
        elif nombre == "P003":
            self.set_zombie_socket(c, f, jugador)
        elif nombre == 'P004':
            self.set_zombie_2_socket(c, f, jugador)
        else:
            return None


    #Crea un perosnaje Y asigna su posicion
    def set_planta_verde(self,c,f):
        if self.dinero < 25:
            print('no tiene dinero')
        else: 
            if self.jugador:
                if c > 3 or f > 5:
                    print('Fuera de los limites permitidos')   
                else:
                    self.perosnaje = Personajes('Verde',100,25,'P001',self.jugador,f,c,0,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    print(self.dinero)
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P001;"+str(f)+";"+str(c)+";"+"True,")
            else:
                if c < 7 or c > 9 or f > 5:
                    print('Fuera de los limites permitidos')

                    
                else:
                    self.perosnaje = Personajes('Verde',100,25,'P001',self.jugador,f,c,0,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    print('hola')
                    self.dato+=("P001;"+str(f)+";"+str(c)+";"+"False,")

#crea la instancia de una planta del socket 
    def set_planta_verde_socket(self, f, c, jugador):
        planta = Personajes('Verde',100,25,'P001',jugador,f,c,0,25, None)
        planta.posicion()
        planta.get_info()
#crea la instancia de un personaje de set nuez 
    def set_nuez(self,c,f):
        if self.dinero < 25:
            print('no tiene dinero')
        else: 
            if self.jugador:
                if c > 3 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Nuez',100,25,'P002',self.jugador,f,c,0,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    print(self.dinero)
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P002;"+str(f)+";"+str(c)+";"+"True,")
            else:
                if c < 7 or c > 9 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Nuez',100,25,'P002',self.jugador,f,c,0,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P002;"+str(f)+";"+str(c)+";"+"False,")
#crea la instancia de un personaje de set nuez 
    def set_nuez_aux(self, f, c, jugador):
        planta = Personajes('Nuez',200,0,'P002',self.jugador,f,c,0,25, None)
        # self.dato += ','+planta.tipo
        planta.posicion()
        planta.get_info()
#crea la instancia de un personaje de zombie  
    def set_zombie(self,c,f):
        if self.dinero < 25:
            print('no tiene dinero')
        else: 
            if self.jugador:
                if c > 3 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Zombie',100,25,'P003',self.jugador,f,c,2,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    print(self.dinero)
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P003;"+str(f)+";"+str(c)+";"+"True,")
            else:
                if c < 7 or c > 9 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Zombie',100,25,'P003',self.jugador,f,c,2,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P003;"+str(f)+";"+str(c)+";"+"False,")
 #crea la instancia de un personaje de zombie           
    def set_zombie_socket(self, f, c, jugador):
        zombie = Personajes('Zombie',100,20,'P002',self.jugador,f,c,1,25, None)
        zombie.posicion()
        zombie.get_info()
#crea la instancia de un personaje de zombie  
    def set_zombie_2(self,c,f):
        if self.dinero < 25:
            print('no tiene dinero')
        else: 
            if self.jugador:
                if c > 3 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Zombie2',100,25,'P004',self.jugador,f,c,1,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    print(self.dinero)
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P004;"+str(f)+";"+str(c)+";"+"True,")
            else:
                if c < 7 or c > 9 or f > 5:
                    print('Fuera de los limites permitidos')
                else:
                    self.perosnaje = Personajes('Zombie',100,25,'P004',self.jugador,f,c,1,25,'plant.png')
                    self.dinero -= self.perosnaje.costo
                    self.perosnaje.posicion()
                    self.perosnaje.get_info()
                    self.dato+=("P004;"+str(f)+";"+str(c)+";"+"False,")
#crea la instancia de un personaje de zombie 
    def set_zombie_2_socket(self, f, c, jugador):
        zombie = Personajes('Zombie Alien',100,20,'P003',self.jugador,f,c,1,25, None)
        zombie.posicion()
        zombie.get_info()
