import pickle ; import os ; import os.path ; import datetime ; from datetime import datetime, date ; import io ; import getpass

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
        self.estado = True
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

def inicializarArchivos(): #Abre o Crea (si no existen) TODOS los archivos
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

        pickle.dump(moderador, arLoModeradores)
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
        pickle.dump(administrador, arLoAdmin)
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
def cerrarArchivos():
    arLoAlumnos.close()
    arLoModeradores.close()
    arLoAdmin.close()
    arLoLikes.close()
    arLoReportes.close()
    input("Archivos cerrados. Finalizando programa...")
def formatearAlumnos(alumnos):
    alumnos.id_est = str(alumnos.id_est).ljust(5, ' ')
    alumnos.email = str(alumnos.email).ljust(32, ' ')
    alumnos.contraseña = str(alumnos.contraseña).ljust(32, ' ')
    alumnos.nombre = alumnos.nombre.ljust(32, ' ')
    alumnos.fnac = alumnos.fnac.ljust(10, ' ')
    alumnos.bio = alumnos.bio.ljust(255, ' ')
    alumnos.hob = alumnos.hob.ljust(255, ' ')
def formatearModeradores(moderador):
    moderador.id_mod = str(moderador.id_mod).ljust(5, ' ')
    moderador.email = moderador.email.ljust(32, ' ')
    moderador.contraseña = moderador.contraseña.ljust(32, ' ')
    moderador.nombre = moderador.nombre.ljust(32, ' ')
def formatearAdministradores(administrador):
    administrador.id_adm = str(administrador.id_adm).ljust(5, ' ')
    administrador.email = administrador.email.ljust(32, ' ')
    administrador.contraseña = administrador.contraseña.ljust(32, ' ')

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
def gestPerfil(): #GESTIONAR PERFIL
    global opcsubp
    opcsubp = ""  # asignación interna para obligar al mientras a que entre aunque sea una vez
    while (opcsubp!="0"):
        subMenuGestionarperfil()        
        opcsubp = input("\nIngrese una opción: ")
        while (opcsubp<"0" or opcsubp >"2"):
            opcsubp = input("Ingreso inválido, ingrese otra opción: ")
        match opcsubp:
            case "1": 
                editarDatos()
            case "2": 
                eliminarPerfil()
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
def fechaNac():
    fNacimiento = "_"
    while fNacimiento != "":
        cls()
        arLoAlumnos.seek(0,0)
        for i in range(0,id):
            pos=arLoAlumnos.tell()
            alumno=pickle.load(arLoAlumnos)
        print("FECHA DE NACIMIENTO ACTUAL: " + alumno.fnac.strip())
        print("")
        fNacimiento = input("Ingrese su nueva fecha de nacimiento (DD-MM-AAAA), o presione Enter para salir: ")
        if fNacimiento != "":
            if fechaValida(fNacimiento):
                arLoAlumnos.seek(pos,0)
                alumno.fnac = fNacimiento
                formatearAlumnos(alumno)
                pickle.dump(alumno,arLoAlumnos)
                arLoAlumnos.flush()
                cls()
                print("FECHA ACTUALIZADA A: " + alumno.fnac.strip())
                input("")
            else:
                print("Fecha ingresada no válida. Asegúrese de usar el formato DD-MM-AAAA, y una edad entre 18 y 122 años.")
                input("Presione Enter para continuar\n")
def cambiarBiografia():
    biografia = "_"
    while biografia != "":
        cls()
        arLoAlumnos.seek(0,0)
        for i in range(0,id):
            pos=arLoAlumnos.tell()
            alumno=pickle.load(arLoAlumnos)

        print("BIOGRAFIA ACTUAL: " + '"' + alumno.bio.strip() + '"')
        print("")
        biografia = input("Ingrese su nueva biografía, o presione Enter para salir: ")
        if biografia != "":
            cls()
            arLoAlumnos.seek(pos,0)
            alumno.bio=biografia
            formatearAlumnos(alumno)
            pickle.dump(alumno,arLoAlumnos)
            arLoAlumnos.flush()
            print("BIOGRAFIA ACTUALIZADA A: " + alumno.bio.strip())
            input()
def cambiarHobbies():
    hobbies = "_"
    while hobbies != "":
        cls()
        arLoAlumnos.seek(0,0)
        for i in range(0,id):
            pos=arLoAlumnos.tell()
            alumno=pickle.load(arLoAlumnos)

        print("HOBBIES ACTUALES: " + '"' + alumno.hob.strip() + '"')
        print("")
        hobbies = input("Ingrese sus nuevos hobbies, o presione Enter para salir: ")
        if hobbies != "":
            cls()
            arLoAlumnos.seek(pos,0)
            alumno.hob=hobbies
            formatearAlumnos(alumno)
            pickle.dump(alumno,arLoAlumnos)
            arLoAlumnos.flush()
            print("HOBBIES ACTUALIZADOS A: " + alumno.hob.strip())
            input()
def cambiarSexo():
    sexo = "_"
    arLoAlumnos.seek(0,0)
    for i in range(0,id):
        pos=arLoAlumnos.tell()
        alumno=pickle.load(arLoAlumnos)
    while sexo != "":
        cls()
        if alumno.sexo == "H":
            s="Hombre"
        elif alumno.sexo == "M":
            s="Mujer"
        if alumno.sexo == "N":
            s="No especificado"
        print("SU SEXO ACTUAL ES: " + s)
        print("   Cambiar sexo a: ")
        print("   1. Hombre")
        print("   2. Mujer")
        print("   3. No especificar")
        sexo = input("\nIngrese una opción, o Enter para volver: ")
        if sexo == "1":
            alumno.sexo = "H"
        elif sexo == "2":
            alumno.sexo = "M"
        elif sexo == "3":
            alumno.sexo = "N"
        arLoAlumnos.seek(pos,0)
        formatearAlumnos(alumno)
        pickle.dump(alumno,arLoAlumnos)
        arLoAlumnos.flush()
def registro():
    cls()
    alumno = Alumno()
    
    if os.path.getsize(arFiAlumnos) == 0:
        alumno.id_est = 1
    else:
        arLoAlumnos.seek(0, 0)
        alumno = pickle.load(arLoAlumnos)
        tamReg = arLoAlumnos.tell()
        tamArc = os.path.getsize(arFiAlumnos)

        cantReg = tamArc//tamReg

        alumno.id_est = cantReg + 1
    
    email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
    while len(email)>32:
        cls()
        print("MAXIMO 32 CARACTERES!")
        email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
    if len(email) < 32:
        alumno.email = email.ljust(32, ' ')
    elif len(email) == 32:
        alumno.email = email
    
    contraseña = getpass.getpass("Ingrese contraseña (MAX. 32 Carac): ")
    while len(contraseña)>32:
        cls()
        print("MAXIMO 32 CARACTERES")
        contraseña = getpass.getpass("Ingrese contraseña (MAX. 32 Carac): \n")
    if len(contraseña)< 32:
        alumno.contraseña = contraseña.ljust(32, ' ')
    elif len(contraseña) == 32:
        alumno.contraseña = contraseña
    
    nombre = str(input("Ingrese su nombre para finalizar el registro (MAX. 32 Carac):"))
    while len(nombre)<= 2:
        cls()
        nombre = input("Su nombre debe tener minimo 3 caracteres, intente nuevamente:\n")
    while len(nombre)>32:
        cls()
        print("MAXIMO 32 CARACTERES")
        nombre = str(input("Ingrese contraseña (MAX. 32 Carac): \n"))
    if len(nombre)< 32:
        alumno.nombre = nombre.ljust(32, ' ')
    elif len(nombre) == 32:
        alumno.nombre = nombre

    pickle.dump(alumno, arLoAlumnos)
    print(alumno.email, alumno.nombre)
    input()

def login():
    global id
    global salir
    global maxint
    global arLoAlumnos  # Archivo global de alumnos
    global arLoModeradores  # Archivo global de moderadores

    maxint = 0
    encontrado = False  # Variable para controlar si se encontró un usuario válido

    while not encontrado and maxint < 3:
        id = 1
        cls()
        print("*****  *****\n")
        print("Si realizas 3 intentos incorrectos, el programa se cerrará.")
        print(f"Intentos: {maxint}\n")
        email = input("Ingrese correo electrónico: ")
        contr = getpass.getpass("\nIngrese contraseña: ")

        if email == "" or contr == "":
            input("Ingrese un correo y contraseña válidos.\n")
            maxint += 1
        else:
            # Variable para controlar si se encontró el alumno o moderador
            usuario_encontrado = False

            # 1. Leer archivo de alumnos
            arLoAlumnos.seek(0, 0)  # Volver al inicio del archivo
            while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos) and not usuario_encontrado:
                try:
                    alumno = pickle.load(arLoAlumnos)
                    if email == alumno.email.strip() and contr == alumno.contraseña.strip():
                        usuario_encontrado = True
                        encontrado = True
                        if alumno.estado == True:
                            cls()
                            input(f"\n|Bienvenido {alumno.nombre.strip()}|\n")
                            opcmenuEst()  # Función para menú de estudiantes
                        else:
                            cls()
                            input("Usuario inactivo, intente nuevamente\nPresione enter para continuar:\n")
                    else:
                        id+=1
                except EOFError:
                    break  # Se alcanza el final del archivo de alumnos

            # 2. Si no es alumno, buscar en archivo de moderadores
            if not usuario_encontrado:
                arLoModeradores.seek(0)  # Volver al inicio del archivo de moderadores
                while arLoModeradores.tell() < os.path.getsize(arFiModeradores) and not usuario_encontrado:
                    try:
                        moderador = pickle.load(arLoModeradores)
                        if email == moderador.email.strip() and contr == moderador.contraseña.strip():
                            usuario_encontrado = True
                            encontrado = True
                            cls()
                            input(f"\n|Bienvenido {moderador.nombre.strip()}|\n")
                            opcmenuMod()  # Función para menú de moderadores
                    except EOFError:
                        break  # Se alcanza el final del archivo de moderadores

            if not usuario_encontrado:  # Si no se encontró un usuario válido
                input("Correo electrónico o contraseña inválidos, intente nuevamente:\n")
                maxint += 1

    # 3. Si se agotan los intentos
    if maxint == 3:
        cls()
        print("Has agotado tus 3 intentos. El programa se cerrará.")
        salir = "0"

inicializarArchivos()
# cambiarBiografia()
inicio()
cerrarArchivos()
