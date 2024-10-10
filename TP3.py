import pickle
import os
import os.path
import datetime
from datetime import date
import io

class Alumno:
    def __init__(self):
        self.id_est = 0
        self.email = " "
        self.contraseña = " "
        self.estado = True
        self.nombre = " "
        self.fnac = " "
        self.bio = " "
        self.hob = " "
        self.sexo = "N" 


class Moderador:
    def __init__ (self):
        self.id_mod = 0
        self.email = " "
        self.contraseña = " "
        self.estado = " "
        self.nombre = " "
class Administrador:
    def __init__ (self):
        self.id_adm = 0
        self.email = " "
        self.contraseña = " "
class Like: 
    def __init__ (self):
        self.remitente = 0
        self.destinatario = 0  
class Reporte:
    def __init__ (self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = " "
def inicializar(): #Abre o Crea (si no existen) TODOS los archivos
    global arFiAlumnos, arLoAlumnos
    global arFiModeradores, arLoModeradores
    global arFiAdmin, arLoAdmin
    global arFiLikes, arLoLikes
    global arFiReportes, arLoReportes

    arFiAlumnos = "alumnos.dat" #CREAR O ABRIR Alumnos
    if os.path.exists(arFiAlumnos):
        arLoAlumnos = open(arFiAlumnos, "r+b")

            
    else:
        print("El archivo " + arFiAlumnos + " no existía y fue creado")
        arLoAlumnos = open(arFiAlumnos, "w+b")
        #Alumno 1
        alumno = Alumno()
        alumno.id_est = 1
        alumno.email = "estudiante1@ayed.com"
        alumno.contraseña = "111222"
        alumno.estado = True
        alumno.nombre = "Juan Perez"
        alumno.fnac = "15-01-2000"
        alumno.bio = "Estudiante de ingeniería."
        alumno.hob = "leer, fútbol"
        alumno.sexo = "H"
        formatearAlumnos(alumno)
        pickle.dump(alumno, arLoAlumnos)

        #Alumno 2
        alumno.id_est = 2
        alumno.email = "estudiante2@ayed.com"
        alumno.contraseña = "333444"
        alumno.estado = True
        alumno.nombre = "Maria Gomez"
        alumno.fnac = "22-04-1998"
        alumno.bio = "Estudiante de medicina."
        alumno.hob = "pintar, natación"
        alumno.sexo = "M"
        formatearAlumnos(alumno)
        pickle.dump(alumno, arLoAlumnos)

        #Alumno 3
        alumno.id_est = 3
        alumno.email = "estudiante3@ayed.com"
        alumno.contraseña = "555666"
        alumno.estado = False
        alumno.nombre = "Luis Lopez"
        alumno.fnac = "05-09-1999"
        alumno.bio = "Estudiante de economía."
        alumno.hob = "ajedrez, ciclismo"
        alumno.sexo = "H"
        formatearAlumnos(alumno)
        pickle.dump(alumno, arLoAlumnos)

        #Alumno 4
        alumno.id_est = 4
        alumno.email = "estudiante4@ayed.com"
        alumno.contraseña = "777888"
        alumno.estado = True
        alumno.nombre = "Ana Martinez"
        alumno.fnac = "30-07-2001"
        alumno.bio = "Estudiante de derecho."
        alumno.hob = "bailar, viajar"
        alumno.sexo = "M"
        formatearAlumnos(alumno)
        pickle.dump(alumno, arLoAlumnos)

        input()
    
    arFiModeradores = "moderadores.dat" #CREAR O ABRIR Moderadores
    if os.path.exists(arFiModeradores):
        arLoModeradores = open(arFiModeradores, "r+b")
    else:
        print("El archivo " + arFiModeradores + " no existía y fue creado")
        arLoModeradores = open(arFiModeradores, "w+b")
        #Alumno 1
        moderador = Moderador()
        moderador.id_mod = 1
        moderador.email = "moderador1@ayed.com"
        moderador.contraseña = "111222"
        moderador.estado = True
        moderador.nombre = "Mateo Labombarda"

        pickle.dump(alumno, arLoAlumnos)
        input()
    
    arFiAdmin = "admin.dat" #CREAR O ABRIR Admin
    if os.path.exists(arFiAdmin):
        arLoAdmin = open(arFiAdmin, "r+b")
    else:
        print("El archivo " + arFiAdmin + " no existía y fue creado")
        arLoAdmin = open(arFiAdmin, "w+b")
        administrador = Administrador()
        administrador.id_adm = 1
        administrador.email = "admin1@ayed.com"
        administrador.contraseña = "111222"
        pickle.dump(alumno, arLoAlumnos)
        input()
    
    arFiLikes = "likes.dat" #CREAR O ABRIR Likes
    if os.path.exists(arFiLikes):
        arLoLikes = open(arFiLikes, "r+b")
    else:
        print("El archivo " + arFiLikes + " no existía y fue creado")
        arLoLikes = open(arFiLikes, "w+b")
        input()
    
    arFiReportes = "reportes.dat" #CREAR O ABRIR Reportes
    if os.path.exists(arFiReportes):
        arLoReportes = open(arFiReportes, "r+b")
    else:
        print("El archivo " + arFiReportes + " no existía y fue creado")
        arLoReportes = open(arFiReportes, "w+b")
        input()
def formatearAlumnos(alumnos):
    alumnos.id_est = str(alumnos.id_est).ljust(5, ' ')
    alumnos.email = str(alumnos.email).ljust(32, ' ')
    alumnos.contraseña = str(alumnos.contraseña).ljust(32, ' ')
    alumnos.nombre = alumnos.nombre.ljust(32, ' ')
    alumnos.fnac = alumnos.fnac.ljust(10, ' ')
    alumnos.bio = alumnos.bio.ljust(255, ' ')
    alumnos.hob = alumnos.hob.ljust(255, ' ')
def cls():
    os.system("cls")
#MENUS y OPCIONES
def menuEstudiante(): #MUESTRA MENU PRINCIPAL
    cls()
    print(" ***** MENÚ ESTUDIANTE *****\n")
    print("   1. Gestionar mi perfil")
    print("   2. Gestionar candidatos")
    print("   3. Matcheos")
    print("   4. Reportes estadísticos")
    print("   0. Salir")
def opcmenuEst(): #TOMA OPCION Y DERIVA
    global maxint
    global opcE
    opcE = ""  
    while (opcE != "0"):
        menuEstudiante()
        opcE = input("\nIngrese una opción: ")
        while (opcE<"0" or opcE>"4"):
            opcE = input("Ingreso inválido, ingrese otra opción: ")
        match opcE:
            case "1": gestPerfil()                                  
            case "2": gestCandidatos()                                 
            case "3": matcheos()   
            case "4": reportesEstadisticos()
            case "0": maxint = 0
def subMenuGestionarperfil(): #1 MUESTRA SUBMENU: GESTIONAR PERFIL
    cls()
    print("***** GESTIONAR MI PERFIL *****\n")
    print("   1. Editar mis datos personales")
    print("   2. Eliminar mi perfil")
    print("   0. Volver\n")
def opcionesEditar():
    cls()
    print("***** EDITAR DATOS PERSONALES *****\n")
    print("   ¿Qué desea modificar?")
    print("   1. Fecha de nacimiento")
    print("   2. Biografía")
    print("   3. Hobbies")
    print("   4. Sexo")
    print("   0. Volver") 
def editarDatos(): #EDITAR DATOS
    opc = "" # asignación interna para obligar al mientras a que entre aunque sea una vez
    while not (opc=="0"):
        opcionesEditar()
        opc = input("\nIngrese una opción: ")
        while (opc<"0" or opc>"4"):
            opc = input("Ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": fechaNac()
            case "2": cambiarBiografia()
            case "3": cambiarHobbies()
            case "4": cambiarSexo()
def subMenuGestionarCandidatos(): #2 MUESTRA SUB MENU: GESTIONAR CANDIDATOS
    cls()
    print("***** GESTIONAR CANDIDATOS *****\n")
    print("   1. Ver candidatos")
    print("   2. Reportar un candidato")
    print("   0. Volver.\n")
def gestCandidatos(): #GESTIONAR CANDIDATOS
    opc = ""  # asignación interna para obligar al mientras a que entre aunque sea una vez
    while (opc!="0"):
        subMenuGestionarCandidatos()        
        opc = input("\nIngrese una opción: ")
        while (opc<"0" or opc >"2"):
            opc = input("Ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": verCandidatos()
            case "2": reportarCandidato()
def matcheos():
    cls()
    print("NO SE HACE")
def menuReportar():
    cls()
    mostrarCandidatos()
    print("\n ***** REPORTAR CANDIDATO ***** \n")
    print(f"   ID/Nombre del usuario que desea reportar: {idReportado}")
    print(f"   Motivo del reporte: {motivo}")
def menuModerador():
    cls()
    print("*****  MENÚ MODERADOR *****\n")
    print("   1. Gestionar Usuarios")
    print("   2. Gestionar Reportes")
    print("   3. Reportes Estadisticos")
    print("   4. Bonus Track 1")
    print("   5. Bonus Track 2")
    print("   6. Bonus Track 3")
    print("   0. Salir")
def opcmenuMod():
    global maxint
    opc = ""
    while(opc!= "0"):
        menuModerador()
        opc = input("\nIngrese una opción:  ")
        while (opc<"0" or opc>"6"):
            opc = input("ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": gestUsuarios()
            case "2": gestReportes()
            case "3": repEstadisticos()
            case "4": Bonustrack1()
            case "5": Bonustrack2()
            case "6": Bonustrack3()
            case "0": maxint = 0
def gestUsuarios():
    opc = ""
    while(opc!= "0"):
        menuGestUsuarios()
        opc = input("\nIngrese opción:  ")
        while(opc<"0" or opc>"1"):
            opc = input("Ingreso invalido, ingrese otra opción: ")
        match opc:
            case "1": desactivarUsua()
def menuGestUsuarios():
    cls()
    print("***** GESTIONAR USUARIOS *****\n")
    print("   1. Desactivar usuario")
    print("   0. Volver")
def gestReportes():
    opc = ""
    while(opc!="0"):
        menuGestRep()
        opc=input("\nIngrese opción:  ")
        while(opc<"0" or opc>"1"):
            opc = input("Ingreso invalido, ingrese otra opción: ")
        if opc=="1":
            reportes()
def menuGestRep():
    cls()
    print("***** GESTIONAR REPORTES *****\n")
    print("   1. Ver reportes")
    print("   0. Volver")
def repEstadisticos():
    cls()
def inicio():
    global salir
    salir=""
    while salir!="0":
        cls()
        print("***** MENU DE INICIO *****\n")
        print("1. Login")
        print("2. Registrarse")
        print("0. Salir del programa")
        salir = input("\nIngrese una opción: ")
        while (salir<"0" or salir>"2"):
            cls()
            print("1. Login")
            print("2. Registrarse")
            print("0. Salir del programa")
            salir = input("\nIngreso inválido, ingrese otra opción: ")
        match salir:
                case "1": login()                      
                case "2": registro()                               
                case "0": finPrograma()
#FIN MENUS

def fechaValida(fechastr:str)->bool:
    try:
        fechanac = datetime.strptime(fechastr, '%d-%m-%Y').date()
        fechaactual = date.today()
        edad = fechaactual.year - fechanac.year - ((fechaactual.month, fechaactual.day) < (fechanac.month, fechanac.day))
        if 1924 <= fechanac.year <= fechaactual.year and 18 <= edad < 122:
            return True
        else:
            return False
    except ValueError:
        return False
def calcularEdad(fecha_nacimiento_str):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d-%m-%Y")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad
def cambiarBiografia():
    biografia = "_"
    while biografia != "":
        cls()
        arLoAlumnos.seek(0,0)
        for i in range(0,id):
            pos=arLoAlumnos.tell()
            alumno=pickle.load(arLoAlumnos)

        print("BIOGRAFIA ACTUAL: " + '"' + alumno.bio + '"')
        print("")
        biografia = input("Ingrese su nueva biografía, o Enter para salir: ")
        if biografia != "":
            cls()
            arLoAlumnos.seek(pos,0)
            alumno.bio=biografia
            formatearAlumnos(alumno)
            pickle.dump(alumno,arLoAlumnos)
            arLoAlumnos.flush()
            print("BIOGRAFIA ACTUALIZADA A: " + alumno.bio)
            input()

inicializar()
cambiarBiografia()
arLoAlumnos.close()