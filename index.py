# clases:
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Expediente:
    
    def __init__(self, id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fechaIngreso = fechaIngreso
        self.cargosOcupado = cargosOcupado
        self.proyectosRealizados = proyectosRealizados

    def crear(list, id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados):
        expediente = Expediente(id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados)
        list.append(expediente)
    def eliminar(list, id):
        i = 0
        for i in range(len(list)):
            if list[i].id == id:
                list.pop(i)
    def buscar(list, id):
        for i in range(len(list)):
            if list[i].id == id:
                print(Expediente.toString(list[i]))
    def toString(obj):
        print('id:', obj.id, ' nombre:', obj.nombre, ' apellido:', obj.apellido, ' ingreso:', obj.fechaIngreso, ' cargos:', obj.cargosOcupado, ' proyectos:', obj.proyectosRealizados)
        
class Pantalla:    
    user = None
    expe = None
    expedientes = []
    def login(self, list ):
        user = input('Usuario:')
        password = str(input('Contraseña:'))
        if list[0].username == user and list[0].password == password:
            print('acceso concedido.')  
            self.user = list[0] 
            self.menu(Pantalla.expedientes)

    def menu(self, listaExpendiente):
        print('1. GESTIONAR EXPEDIENTES.\n2. GESTIONAR EMPLEADOS\n3. GESTIONAR DESEMPEÑOS')
        seleccion = int(input('Ingrese su seleccion:'))
        if seleccion == 1:
            seleccion2 = int(input('1.CREAR\n2.ELIMINAR\n3.MOSTRAR\nIngrese su seleccion:'))
            if seleccion2 == 1:
                id = int(input('id:'))
                nombre = str(input('nombre:'))
                apellido = str(input('apellido:'))
                fechaIngreso = input('ingreso:')
                cargosOcupado = str(input('cargos:'))
                proyectosRealizados = int(input('proyectos'))
                Expediente.crear(listaExpendiente, id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados)
                print('se ha creado con exito')
                self.menu(Pantalla.expedientes)
            elif seleccion2 == 2:
                id = int(input('id:'))
                Expediente.eliminar(Pantalla.expedientes, id)
                print('eliminado con exito')
                self.menu(Pantalla.expedientes)
            elif seleccion2 == 3:
                id = int(input('id:'))
                Expediente.buscar(Pantalla.expedientes, id)
                self.menu(Pantalla.expedientes)
        elif seleccion == 2:
            print('1.CREAR\n2.ELIMINAR\n3.MOSTRAR')
        else:
            print('1.CREAR\n2.ELIMINAR\n3.MOSTRAR')

#main:
users = []

user1 = User(1, '1', '1')        

users.append(user1)

p1 = Pantalla()
p1.login(users)

    