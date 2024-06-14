# clases:
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Empleado:
    def __init__(self, id, nombre, apellido, edad, dni, departamento, direccion, obraSocial, telefono, sueldo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.departamento = departamento
        self.direccion = direccion
        self.obraSocial = obraSocial
        self.telefono = telefono
        self.sueldo = sueldo
    def crear(list):
        id = int(input('id:'))
        nombre = str(input('nombre:'))
        apellido = str(input('apellido:'))
        edad = int(input('edad:'))
        dni = int(input('dni:'))
        departamento = str(input('departamento:'))
        direccion = str(input('direccion:'))
        obraSocial = str(input('obraSocial:'))
        telefono = int(input('telefono:'))
        sueldo = int(input('sueldo:'))
        empleado = Empleado(id, nombre, apellido, edad, dni, departamento, direccion, obraSocial, telefono, sueldo)
        list.append(empleado)
    def eliminar(list):
        id = int(input('id:'))
        for i in range(len(list)):
            if list[i].id == id:
                list.pop(i)
            else:
                print('no se ha encontrado el id') 
    def buscar(list):
        id = int(input('id:'))
        for i in list:
            if i.id == id:
                emp = Empleado(id, i.nombre, i.apellido, i.edad, i.dni, i.departamento, i.direccion, i.obraSocial, i.telefono, i.sueldo)
                Empleado.toString(emp)
            else:
                print('no se ha encontrado el id') 
    def toString(obj):
        print("id:", obj.id, "nombre:", obj.nombre, "apellido:", obj.apellido, "edad:", obj.edad, "dni:" , obj.dni, "departamento:", obj.departamento, "direccion:", obj.direccion, "obraSocial:",obj.obraSocial, "telefono:", obj.telefono, "sueldo:", obj.sueldo)

class Desempenios:
    def __init__(self, id, nombre, calidadTrabajo, productividad, comunicacion, trabajoEnEquipo, asistencia, puntualidad, compromiso):
        self.id = id
        self.nombre = nombre
        self.calidadTrabajo = calidadTrabajo
        self.productividad =  productividad
        self.comunicacion = comunicacion
        self.trabajoEnEquipo = trabajoEnEquipo
        self.asistencia = asistencia
        self.puntualidad = puntualidad
        self.compromiso = compromiso
    def crear(list):
        id = int(input('id:'))
        nombre = str(input('nombre:'))
        calidadTrabajo =  int(input('calidad de trabajo:'))
        productividad = int(input('productividad:'))
        comunicacion = int(input('comunicacicon:'))
        trabajoEnEquipo = int(input('trabajo en equipo:'))
        asistencia = int(input('asistencia:'))
        puntualidad = int(input('puntualidad:'))
        compromiso = int(input('compromiso:'))
        desempenio = Desempenios(id, nombre, calidadTrabajo, productividad, comunicacion, trabajoEnEquipo, asistencia, puntualidad, compromiso)
        list.append(desempenio)
    def eliminar(list):
        id = int(input('id:'))
        for i in range(len(list)):
            if list[i].id == id:
                list.pop(i)
            else:
                print('no se ha encontrado el id') 
    def buscar(list):
        id = int(input('id:'))
        for i in list:
            if i.id == id:
                des = i
                Desempenios.toString(des)
    def toString(obj):
        print('id:', obj.id, 'nombre:',obj.nombre, 'calidadTrabajo:',obj.calidadTrabajo, 'productividad:',obj.productividad, 'comunicacion:',obj.comunicacion,'trabajoEnEquipo:',obj.trabajoEnEquipo, 'asistencia:', obj.asistencia,'puntualidad:',obj.puntualidad, 'compromiso:', obj.compromiso)
    
        
class Expediente:
    def __init__(self, id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fechaIngreso = fechaIngreso
        self.cargosOcupado = cargosOcupado
        self.proyectosRealizados = proyectosRealizados
#funciones:
    def crear(list):
        id = int(input('id:'))
        nombre = str(input('nombre:'))
        apellido = str(input('apellido:'))
        fechaIngreso = input('ingreso:')
        cargosOcupado = str(input('cargos:'))
        proyectosRealizados = int(input('proyectos:'))
        expediente = Expediente(id, nombre, apellido, fechaIngreso, cargosOcupado, proyectosRealizados)
        list.append(expediente)
    def eliminar(list):
        id = int(input('id:'))
        for i in range(len(list)):
            if list[i].id == id:
                list.pop(i)
            else:
                print('no se ha encontrado el id') 
    def buscar(list):
        id = int(input('id:'))
        for i in list:
            if i.id == id:
                exp = Expediente(id, i.nombre, i.apellido, i.fechaIngreso, i.cargosOcupado, i.proyectosRealizados)
                Expediente.toString(exp)
            else:
               print('no se ha encontrado el id') 

    def toString(obj):
        print('id:', obj.id, ' nombre:', obj.nombre, ' apellido:', obj.apellido, ' ingreso:', obj.fechaIngreso, ' cargos:', obj.cargosOcupado, ' proyectos:', obj.proyectosRealizados)

class Pantalla:    
    user = None
    expe = None
    expedientes = []
    empleados = []
    desempenios = []
    def login(self, list ):
        user = input('Usuario:')
        password = str(input('Contraseña:'))
        if list[0].username == user and list[0].password == password:
            print('acceso concedido.')  
            self.user = list[0] 
            self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)

    def menu(self, listaExpendiente, listaEmpleados, listaDesempenios):
        print('1. GESTIONAR EXPEDIENTES.\n2. GESTIONAR EMPLEADOS\n3. GESTIONAR DESEMPEÑOS')
        seleccion = int(input('Ingrese su seleccion:'))
        if seleccion == 1:
            seleccion2 = int(input('1.CREAR\n2.ELIMINAR\n3.MOSTRAR\n4.MOSTRAR TODOS\nIngrese su seleccion:'))
            if seleccion2 == 1:
                Expediente.crear(Pantalla.expedientes)
                print('se ha creado con exito')
                self.menu(Pantalla.expedientes,Pantalla.empleados, Pantalla.desempenios)
            elif seleccion2 == 2:
                Expediente.eliminar(Pantalla.expedientes)
                print('eliminado con exito')
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            elif seleccion2 == 3:
                Expediente.buscar(Pantalla.expedientes)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            elif seleccion2 ==4:
                for i in listaExpendiente:
                    Expediente.toString(i)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
        elif seleccion == 2:
            seleccion2 = int(input('1.CREAR\n2.ELIMINAR\n3.MOSTRAR\n4. MOSTRAR TODOS\nIngrese su seleccion:'))
            if seleccion2 == 1:
                Empleado.crear(Pantalla.empleados)
                print('se ha creado con exito')
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            if seleccion2 == 2:
                Empleado.eliminar(Pantalla.empleados)
                print("se ha borrado con exito")
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            if seleccion2 == 3:
                Empleado.buscar(Pantalla.empleados)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            if seleccion2 == 4:
                for i in listaEmpleados:
                    Empleado.toString(i)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
        elif seleccion == 3:
            seleccion2 = int(input('1.CREAR\n2.ELIMINAR\n3.MOSTRAR'))
            if seleccion2 == 1:
                Desempenios.crear(Pantalla.desempenios)
                print('se ha creado con exito')
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            if seleccion2 == 2:
                Desempenios.eliminar(Pantalla.desempenios)
                print('se ha borrado con exito')
            if seleccion2 == 3:
                Desempenios.buscar(Pantalla.desempenios)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)
            if seleccion2 == 4:
                for i in listaDesempenios:
                    Desempenios.buscar(i)
                self.menu(Pantalla.expedientes, Pantalla.empleados, Pantalla.desempenios)

#main:
users = []

user1 = User(1, '1', '1')        

users.append(user1)

p1 = Pantalla()
p1.login(users)
