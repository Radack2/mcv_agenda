from model.model import model
from view.view import View

class controller:

    #Constructor
    def __init__(self):
        self.model = model()
        self.View = View()

    #Contactos controller

    def agregar_contacto(self,id_contacto,nombre,tel,correo,dir):
        b,c=self.model.agregar_contacto(id_contacto,nombre,tel,correo,dir)
        if b:
            self.View.agregar_contacto(c)
        else:
            self.contacto_ya_existe(c)
       
    def leer_contacto(self,id_contacto):
        e,c = self.model.leer_contacto(id_contacto)
        if e:
            self.View.mostrar_contacto(c)
        else:
            self.View.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c=self.model.leer_todoscontactos()
        self.View.mostar_contactos(c)

    def actualizar_contacto(self,id_contacto,n_nombre='',n_tel='',n_correo='', n_dir=''):
        e=self.model.actualizar_contacto(id_contacto,n_nombre,n_tel,n_correo, n_dir)
        if e:
            self.View.actualizar_contacto(id_contacto)
        else:
            self.View.contacto_no_existe(id_contacto)

    def borrar_contacto(self,id_contacto):
        e ,c = self.model.borrar_contacto(id_contacto)

        if e:
            self.View.borrar_contacto(c)
        else:
            self.View.contacto_no_existe(id_contacto)
        
    def leer_contactos_letra(self,letra):
        c = self.model.leer_contactos_letra(letra)
        self.View.mostar_contactos(c)

    #Pruebas

    def insertar_contactos(self):
        self.agregar_contacto(1,'Juan Perez','464-123-1234','jp@gmail.com','Salamnca gto')
        self.agregar_contacto(2,'Eber Sanchez','469-100-1234','eber@gmail.com','Salamanca')

    
    def insertar_citas(self):
        self.agregar_citas(1,1,'Escuela', '17 febrero 2020','12:20','Clase se programacion')
        self.agregar_citas(1,1,'Escuela', '17 febrero 2020','12:20','Clase se programacion')


    #Citas


    def agregar_citas(self,id_cita,id_contacto,lugar,fecha,hora,asunto):
        b,c=self.model.agregar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
        if b:
            self.View.crear_cita(c)
        else:
            self.View.cita_ya_existe(c)

    def leer_cita(self,id_cita):
        e,c = self.model.leer_cita(id_cita)
        if e:
            self.View.mostrar_cita(c)
        else:
            self.View.cita_no_existe(id_cita)

    def leer_todas_citas(self):
        c=self.model.leer_todascitas()
        self.View.mostar_citas(c)

    def actualizar_citas(self,id_cita,n_id_contacto='',n_lugar='',n_fecha='',n_hora='',n_asunto=''):
        e=self.model.actualizar_cita(id_cita,n_id_contacto,n_lugar,n_fecha,n_hora,n_asunto)
        if e:
            self.View.modificar_cita(id_cita)
        else:
            self.View.cita_no_existe(id_cita)

    def borrar_cita(self,id_cita):

        e ,c = self.model.borrar_cita(id_cita)

        if e:
            self.View.borrar_cita(c)
        else:
            self.View.cita_no_existe(id_cita)

    def leer_citas_fecha(self,fecha):
        c = self.model.leer_citas_fecha(fecha)
        self.View.mostar_citas(c)


    def start(self):
        self.View.start()
        self.menu()
        # self.leer_todos_contactos()
        # self.View.menu()
        # self.insertar_contactos()
        # self.insertar_citas()
        # self.leer_todas_citas()
        

        # self.leer_todos_contactos()
        # self.leer_todos_contactos_letra('e')


    def menu(self):
        #disp menu
        self.View.menu()
        o = input('Selecciona una opcion (1-9)')
        if o == '1':
            id_contacto = input('Agregue Id ')
            nombre = input('Ingrese nombre ')
            tel = input('Ingrese telefono ')
            correo = input('Ingrese correo ')
            dir = input('Ingrese Direccion ')
            self.agregar_contacto(id_contacto,nombre,tel,correo,dir)
            self.menu()

        elif o == '2':
            id_contacto = input('Ingrese el id del contacto a buscar ')
            self.leer_contacto(id_contacto)
            self.menu()
        elif o == '3':
            print('Escriba '' si no desea actualizar ')
            id_contacto = input('Id a actualizar ')
            nombre = input('Ingrese nuevo nombre ')
            tel = input('Ingrese nuevo telefono ')
            correo = input('Ingrese nuevo correo ')
            dir = input('Ingrese nueva Direccion ')
            self.actualizar_contacto(id_contacto,nombre,tel,correo,dir)
            self.menu()
           
        elif o == '4':
            id_contacto = input ('Ingrese el id a borrar ')
            self.borrar_contacto(id_contacto)
            self.menu()
        elif o == '5':
            # letra = input('Ingrese la letra ')
            # self.leer_contactos_letra(letra)
            id_cita = input('Agregue Id ')
            id_contacto = input('Ingrese id contacto ')
            lugar = input('Ingrese lugar ')
            fecha = input('Ingrese fecha ')
            hora = input('Ingrese hora ')
            asunto = input ('Ingrese un asunto ')
            self.agregar_citas(id_cita,id_contacto,lugar,fecha,hora,asunto)
            self.menu()

        elif o == '6':
            id_cita = input('Ingrese el id de la cita a buscar ')
            self.leer_cita(id_cita)
            self.menu()
        elif o == '7':
            print('Escriba '' si no desea actualizar ')
            id_cita = input('Agregue Id ')
            id_contacto = input('Ingrese id contacto ')
            lugar = input('Ingrese lugar ')
            fecha = input('Ingrese fecha ')
            hora = input('Ingrese hora ')
            asunto = input ('Ingrese un asunto ')
            self.actualizar_citas(id_cita,id_contacto,lugar,fecha,hora,asunto)
            self.menu()

        elif o == '8': 
            id_cita = input ('Ingrese el id a borrar ')
            self.borrar_cita(id_cita)
            self.menu()
        elif o == '9':
            pass
            self.View.end()
        else:
            self.View.opcion_no_valida()

        