import pickle

class Profesor:
    def __init__(self, tipo, id, cui, nombre, curso):
        self.tipoP = tipo
        self.idP = id
        self.cuiP = cui
        self.nombreP = nombre
        self.cursoP = curso

class Estudiante:
    def __init__(self, tipo, id, cui, nombre, carnet):
        self.tipoE = tipo
        self.idE = id
        self.cuiE = cui
        self.nombreE = nombre
        self.carnetE = carnet

def guardar_registro(datos, archivo):
    with open(archivo, 'ab') as f:
        pickle.dump(datos, f)

def leer_registros(archivo):
    datos = []
    try:
        with open(archivo, 'rb') as f:
            while True:
                try:
                    dato = pickle.load(f)
                    datos.append(dato)
                except EOFError:
                    break
    except FileNotFoundError:
        pass
    return datos

def mostrar_registros(datos):
    for dato in datos:
        if isinstance(dato, Profesor):
            print("Tipo: ",dato.tipoP)
            print("ID:", dato.idP)
            print("CUI:", dato.cuiP)
            print("Nombre:", dato.nombreP)
            print("Curso:", dato.cursoP)
            
        elif isinstance(dato, Estudiante):
            print("Tipo: ", dato.tipoE)
            print("ID:", dato.idE)
            print("CUI:", dato.cuiE)
            print("Nombre:", dato.nombreE)
            print("Carnet:", dato.carnetE)
           
        print("--------------------")

def menu():
    archivo = "Datos.dot"   
    while True:
        print("\n")
        print("Gabriel Orlando Ajsivinac Xicay 201213010")
        print("*********** Menú ************")
        print("* 1. Registro de Profesor   *")
        print("* 2. Registro de Estudiante *")
        print("* 3. Ver Registros          *")
        print("* 4. Salir                  *")
        print("***************************")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':

            tipo = input("Ingrse Tipo: ")
            id = input("ID Profesor: ")
            cui = input("CUI Profesor: ")
            nombre = input("Nombre Profesor: ")
            curso = input("Curso Profesor: ")
            profesor = Profesor(tipo, id, cui, nombre, curso)
            guardar_registro(profesor, archivo)
            print("Registo guardado\n")
            
        elif opcion == '2':
            tipo = input("Ingrese Tipo: ")
            id = input("ID Estudiante: ")
            cui = input("CUI Estudiante: ")
            nombre = input("Nombre Estudiante: ")
            carnet = input("Carnet Estudiante: ")
            estudiante = Estudiante(tipo, id, cui, nombre, carnet)
            guardar_registro(estudiante, archivo)
            print("Registro guardado\n")
            
        elif opcion == '3':
            print("**Registros**")
            registros = leer_registros(archivo)
            mostrar_registros(registros)
            
        elif opcion == '4':
            print("Finalizado")
            break
        else:
            print("Invalido, intente de nuevo")

if __name__ == "__main__":
    menu()
