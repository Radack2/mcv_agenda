from model.contacto import Contacto
from model.cita import Cita
from model.model import model
from view.view import View
from controller.controller import controller

# c1 = Contacto(1,'Juan Perez','464-123-1234','jp@gmail.com','Salamnca gto')
# c2 = Contacto(2,'Eber Sanchez','469-100-1234','eber@gmail.com','Salamanca') 

# contactos = []

# contactos.append(c1)
# contactos.append(c2)

# """ print(c1.id_contacto)
# print(c1.nombre)
# print(c1.tel)
# print(c1.correo)
# print(c1.dir) """


# t1 = Cita(1,1,'Escuela', '17 febrero 2020','12:20','Clase se programacion')

# print(t1.id_cita)
# print(t1.id_contacto)
# print(t1.lugar)
# print(t1.fecha)
# print(t1.hora)
# print(t1.asunto)

# """ t = input('Ingresa un nombre: ')

# for c in contactos:
#     if t.lower() == c.nombre.lower():
#         print('Ya se encuentra en la lista')
#         break
# else:
#     print('No se encuentra en la lista')
#  """

# m= model()

# m.agregar_contacto(2,'Eber Sanchez','469-100-1234','eber@gmail.com','Salamanca')
# m.agregar_contacto(1,'Juan Perez','464-123-1234','jp@gmail.com','Salamnca gto')
# m.agregar_contacto(3,'javier perez','469-100-1234','udbr@gmail.com','Sal')



# s= m.leer_contacto(2)
# # print(s.nombre)

# m.agregar_cita(1,1,'Escuela', '17 febrero 2020','12:20','Clase de programacion')
# m.agregar_cita(2,1,'Casa', '17 febrero 2020','12:20','Estudiar')
# m.agregar_cita(3,2,'Mineria', '11 febrero 2020','2:00','clase de mineria Datos')
# e = m.leer_cita(1)
# print(e.lugar)

# # m.actualizar_contactos(2,n_nombre="radack")

# a = m.leer_contacto(2)

# # print(a.nombre)

# b = m.leer_contactos_letra('j')

# # m.borrar_contacto(1)

# con = m.leer_todoscontactos()

# for k in con:
#     print(k.nombre)

# citas = m.leer_todascitas()


# print('*****************')
# for k in citas:
#     print(k.asunto)

# v=View()

# s = m.leer_todoscontactos()
# v.mostar_contactos(s)

# # f,c = m.borrar_contacto(1)

# # if f:
# #     v.borrar_contacto(c)

# # else:
# #     v.contacto_no_existe(1)

# v.mostar_citas(citas)

cont = controller()

cont.start()
