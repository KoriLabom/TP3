import pickle
import os
import os.path
import datetime
from datetime import date
import io

class Alumnos:
    def __init__ (self):
        self.id_est = 0
        self.email = " "
        self.contraseña = " "
        self.estado = " "
        self.nombre = " "
        self.fnac = 0
        self.bio = " "
        self.hob = " "
        self.sexo = " " 
class Moderadores:
    def __init__ (self):
        self.id_mod = 0
        self.email = " "
        self.contraseña = " "
        self.estado = " "
        self.nombre = " "
class Administradores:
    def __init__ (self):
        self.id_adm = 0
        self.email = " "
        self.contraseña = " "
class Likes: 
    def __init__ (self):
        self.remitente = 0
        self.destinatario = 0  
class Reportes:
    def __init__ (self):
        self.id_reportante = 0
        self.id_reportado = 0
        self.razon_reporte = " "

def cls():
    os.system("cls")

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
def calcularEdad(fecha_nacimiento_str):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d-%m-%Y")
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad
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
inicio()