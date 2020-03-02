from .contacto import Contacto
from .cita import Cita


class model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self,id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True,c
        return False,0

    def esta_cita(self,id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True,c
        return False,0

    # Contacto methods
    
    def agregar_contacto(self,id_contacto,nombre,tel,correo,dir):
        
        e,c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto,nombre,tel,correo,dir)
            self.contactos.append(c)
            return True,c
        return False,c
        
        return False,id_contacto

    def leer_contacto(self, id_contacto):
        e,c = self.esta_id(id_contacto)
        return e,c

    


    def actualizar_contactos(self,id_contacto,n_nombre,n_tel,n_correo, n_dir):

        e,c = self.esta_id(id_contacto)
        if e:
            if n_nombre != "":
                c.nombre = n_nombre
            if n_tel != "":
                c.tel = n_tel
            if n_correo != "": 
                c.tel = n_tel
            if n_dir != "":
                c.dir = n_dir
            return True
        return False
        
    

    def borrar_contacto(self,id_contacto):

        e,contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
               self.citas.remove(c)
            return True,contacto
        return False,0
    

    def leer_todoscontactos(self):
        return self.contactos

    #Cita Methods


    def agregar_cita(self,id_cita,id_contacto,lugar,fecha,hora,asunto):
        
        e,c = self.esta_cita(id_cita)
        if not e:
            c = Cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
            self.citas.append(c)
            return True,c
        return False,c
        
        return False,id_contacto
    def leer_cita(self, id_cita):
        e,c = self.esta_cita(id_cita)
        if e:
            return e,c 
        return False,id_cita

    def actualizar_cita(self,id_cita,n_id_contacto,n_lugar,n_fecha,n_hora,n_asunto):

        e,c = self.esta_cita(id_cita)
        if e:
            if n_id_contacto != '':
                c.id_contacto = n_id_contacto
            if n_lugar != '':
                c.lugar = n_lugar
            if n_hora != '': 
                c.hora = n_hora
            if n_asunto != '':
                c.asunto = n_asunto
            return True
        return False
        
    

    def borrar_cita(self,id_cita):

        e,c = self.esta_cita(id_cita)
        if e:
            self.citas.remove(c)
            return True
        return False

    def leer_contactos_letra(self,letra):
        lista=[]
        for c in self.contactos:
            # if c.nombre.lower().startswith(letra):
            if c.nombre[0].lower() == letra.lower():
                lista.append(c)
        return lista

    def leer_citas_fecha(self, fecha):
        lista =[]
        # lista = [c for c in self.citas if c.fecha == fecha]
        for c in self.citas:
            if c.fecha == fecha:
                lista.append(c)
        return lista

    def leer_todascitas(self):
        return self.citas

    