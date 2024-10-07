import pickle
import os
import os.path
import datetime
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