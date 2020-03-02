class View:

    def mostrar_contacto(self, contacto):
        print('************ Datos del Contacto************')
        print('Nombre:',contacto.nombre)
        print('Telefono',contacto.tel)
        print('Correo',contacto.correo)
        print('Direccion',contacto.dir)
        print('********************************************')

    def mostar_contactos(self, contactos):
        print('************* contactos definidos***********')
        for c in contactos:
            print(c.nombre, c.tel, c.dir)
        print('********************************************')

    def agregar_contacto(self,contacto):
        print('********************************************')
        print(contacto.nombre,'Se ha agregado a la base de datos!')
    
    def borrar_contacto (self,contacto):
        print(contacto.nombre,'Se ha borrado de la base de datos!')
    
    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado correctamente!')

    def contacto_ya_existe(self, contacto):
        print('El contacto',contacto.id_contacto,'YA EXISTE EL CONTACTO EN LA BASE DE DATOS!')
    
    def contacto_no_existe(self, id_contacto):
        print(id_contacto,'NO EXISTE EN LA BASE DE DATOS!')

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Hasta luego, Adios!')


    #   Citas
    
    def mostrar_cita(self, citas):
        print('************ Datos de Cita************')
        print('id_contacto',citas.id_contacto)
        print('Lugar:',citas.lugar)
        print('Fecha',citas.fecha)
        print('Hora',citas.hora)
        print('Asunto',citas.asunto)
        print('********************************************')

    def mostar_citas(self, citas):
        print('************* citas agendadas***********')
        for c in citas:
            print(c.id_contacto,c.lugar, c.fecha, c.hora,c.asunto)
        print('********************************************')

    def crear_cita(self,cita):
        print('********************************************')
        print(cita.fecha,'Se ha agregado la cita!')

    def borrar_cita (self,cita):
        print(cita.fecha,'Se ha borrado de la base de datos!')
    
    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.lugar, 'Se ha modificado correctamente!')

    def cita_ya_existe(self, cita):
        print(cita.id_cita,'YA EXISTE LA CITA EN LA BASE DE DATOS!')
    
    def cita_no_existe(self, id_cita):
        print(id_cita,'NO EXISTE EN LA BASE DE DATOS!')

    def start(self):
        print('Este es un ejemplo sencillo')
        print('')
    
    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Buscar cita')
        print('7. Actualizar cita')
        print('8. Borrar cita')
        print('9. Salir')

    def end(self):
        print('*********Adios Hasta la proxima**********')
