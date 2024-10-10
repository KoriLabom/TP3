import pickle ; import os ; import os.path ; import datetime ; from datetime import datetime, date ; import io ; import getpass

class Alumno:
    def __init__(self):
        self.id = 0
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
        self.id = 0
        self.email = " "
        self.contraseña = " "
        self.estado = True
        self.nombre = " "
class Administrador:
    def __init__ (self):
        self.id = 0
        self.email = " "
        self.contraseña = " "
        self.estado = True
        self.nombre = " "
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
        alumno.id = 1
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
        alumno.id = 2
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
        alumno.id = 3
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
        alumno.id = 4
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
        moderador.id = 1
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
        administrador.id = 1
        administrador.email = "admin1@ayed.com"
        administrador.contraseña = "111222"
        administrador.estado = True
        administrador.nombre = "Pato Martin"
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
    alumnos.id = str(alumnos.id).ljust(5, ' ')
    alumnos.email = str(alumnos.email).ljust(32, ' ')
    alumnos.contraseña = str(alumnos.contraseña).ljust(32, ' ')
    alumnos.nombre = alumnos.nombre.ljust(32, ' ')
    alumnos.fnac = alumnos.fnac.ljust(10, ' ')
    alumnos.bio = alumnos.bio.ljust(255, ' ')
    alumnos.hob = alumnos.hob.ljust(255, ' ')
def formatearModeradores(moderador):
    moderador.id = str(moderador.id).ljust(5, ' ')
    moderador.email = moderador.email.ljust(32, ' ')
    moderador.contraseña = moderador.contraseña.ljust(32, ' ')
    moderador.nombre = moderador.nombre.ljust(32, ' ')
def formatearAdministradores(administrador):
    administrador.id = str(administrador.id).ljust(5, ' ')
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
    print("   3. Bonus Track 1")
    print("   4. Bonus Track 2")
    print("   5. Bonus Track 3")
    print("   0. Salir")
def opcmenuMod():
    global maxint
    opc = ""
    while(opc!= "0"):
        menuModerador()
        opc = input("\nIngrese una opción:  ")
        while (opc<"0" or opc>"5"):
            opc = input("ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": gestUsuarios()
            case "2": gestReportes()
            case "3": Bonustrack1()
            case "4": Bonustrack2()
            case "5": Bonustrack3()
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
def finPrograma():
    cls()
    print("GRACIAS POR USAR NUESTRO PROGRAMA")
def menuAdmin():
    cls()
    print(" ***** MENÚ ADMIN *****\n")
    print("   1. Gestionar Usuarios")
    print("   2. Gestionar Reportes")
    print("   3. Reportes Estadísticos")
    print("   0. Salir")
def opcmenuAdmin():
    global maxint
    opc = ""
    while(opc!= "0"):
        menuAdmin()
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
def buscarLike(dador, receptor):
    if os.path.getsize(arFiLikes) != 0:  # Si el archivo no está vacío
        arLoLikes.seek(0, 0)  # Posicionamos el puntero al inicio del archivo
        while arLoLikes.tell() < os.path.getsize(arFiLikes):
            like = pickle.load(arLoLikes)  # Cargamos cada 'like' guardado
            # Si encontramos un "like" donde el remitente y destinatario coinciden, retornamos True
            if like.remitente == dador and like.destinatario == receptor:
                return True
    # Si no encontramos ninguna coincidencia después de revisar todo, retornamos False
    return False

def verCandidatos():
    cls()
    cantidadAlumnos = 0
    like = Like()
    print("***** LISTA DE CANDIDATOS *****\n")
    
    mostrarCandidatos()
    
    meGusta = input("\nIngrese el nombre o id del estudiante que le gustaría hacer un Matcheo, o presione Enter para salir: ")

    # Contar la cantidad de alumnos
    arLoAlumnos.seek(0, 0)  # Nos aseguramos de que el puntero esté al principio
    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
        alumno = pickle.load(arLoAlumnos)
        cantidadAlumnos += 1

    # Verificar que el nombre ingresado sea correcto
    while meGusta != "":
        encontrado = False
        id_estudiante = None  # Inicializamos variable de control
        
        try:
            meGustaID = int(meGusta)
        except ValueError:
            meGustaID = None

        # Reposicionamos el puntero al inicio del archivo antes de cada búsqueda
        arLoAlumnos.seek(0, 0)
        
        # Ciclo para recorrer los alumnos otra vez
        for n in range(1, cantidadAlumnos + 1):  
            if not encontrado:  # Solo procesar si no hemos encontrado aún
                alumno = pickle.load(arLoAlumnos)  # Leer cada alumno desde el archivo
                # Si el nombre o ID coinciden y el estado es True
                if (alumno.nombre.strip().lower() == meGusta.lower() or n == meGustaID) and alumno.estado: 
                    id_estudiante = alumno.id_est
                    encontrado = True  # Marcamos que se ha encontrado el alumno

        # Después del ciclo, si se encontró el alumno con estado True
        if encontrado and id_estudiante is not None:
            # Verificamos que el dador y el receptor no sean el mismo
            if int(id) == int(id_estudiante):
                print("No puedes dar like a ti mismo.")
            else:
                if buscarLike(id, id_estudiante):
                    print(f"Usted ya le ha dado like a {alumno.nombre.strip()}")
                else:
                    print("")
                    print(f"Le gustaría hacer un Matcheo con: {alumno.nombre.strip()}")
                    # Guardar el like
                    like.remitente = id
                    like.destinatario = id_estudiante
                    pickle.dump(like, arLoLikes)
                    arLoLikes.flush()

        else:
            print("No se encontró el estudiante con ese nombre o ID, o el estudiante no está activo.")

        # Pedir nueva entrada para otro estudiante o salir
        meGusta = input("\nIngrese el nombre o id del estudiante que le gustaría hacer un Matcheo, o presione Enter para salir: ")

def mostrarCandidatos():
    cantidadAlumnos=1
    arLoAlumnos.seek(0,0)
    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
        alumno=pickle.load(arLoAlumnos)
        cantidadAlumnos+=1
    arLoAlumnos.seek(0,0)
    for i in range (1,cantidadAlumnos):
        alumno=pickle.load(arLoAlumnos) 
        if alumno.estado and i != id:
            print(f"||Id:{i}||Nombre:{alumno.nombre.strip()}||Fecha de nacimiento:{alumno.fnac.strip()}||Edad:{calcularEdad(alumno.fnac.strip())}||Biografia:{alumno.bio.strip()}||Hobbies:{alumno.hob.strip()}||")
        


def registro():
    cls()
    alumno = Alumno()
    
    if os.path.getsize(arFiAlumnos) == 0:
        alumno.id = 1
    else:
        arLoAlumnos.seek(0, 0)
        alumno = pickle.load(arLoAlumnos)
        tamReg = arLoAlumnos.tell()
        tamArc = os.path.getsize(arFiAlumnos)

        cantReg = tamArc//tamReg

        alumno.id = cantReg + 1
    
    email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
    while len(email)>32:
        cls()
        print("MAXIMO 32 CARACTERES!")
        email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
    while len(email)< 12:
        cls()
        email = input("Su email debe tener minimo 12 caracteres, intente nuevamente:\n")    
    if len(email) < 32:
        alumno.email = email.ljust(32, ' ')
    elif len(email) == 32:
        alumno.email = email
    
    contraseña = getpass.getpass("Ingrese contraseña (MAX. 32 Carac): \n")
    while len(contraseña)>32:
        cls()
        print("MAXIMO 32 CARACTERES")
        contraseña = getpass.getpass("Ingrese contraseña (MAX. 32 Carac): \n")
    while len(contraseña) < 8:
        cls()
        contraseña = input("Su contraseña debe tener minimo 8 caracteres, intente nuevamente: \n")
    if len(contraseña)< 32:
        alumno.contraseña = contraseña.ljust(32, ' ')
    elif len(contraseña) == 32:
        alumno.contraseña = contraseña
    
    nombre = str(input("Ingrese su nombre para finalizar el registro (MAX. 32 Carac): \n"))
    while len(nombre)< 3:
        cls()
        nombre = input("Su nombre debe tener minimo 3 caracteres, intente nuevamente:\n")
    while len(nombre)>32:
        cls()
        print("MAXIMO 32 CARACTERES")
        nombre = str(input("Ingrese nombre (MAX. 32 Carac): \n"))
    if len(nombre)< 32:
        alumno.nombre = nombre.ljust(32, ' ')
    elif len(nombre) == 32:
        alumno.nombre = nombre

    fNacimiento = str(input("Ingrese su fecha de nacimiento (DD-MM-AAAA): "))
    fechaval = True
    while fechaval:
        if fechaValida(fNacimiento):
            cls()
            fechaval=False
        else:
            print("Fecha ingresada no válida. Asegúrese de usar el formato DD-MM-AAAA, y una edad entre 18 y 122 años.")
            fNacimiento = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ")     
    alumno.fnac = fNacimiento

    bio = str(input("Ingrese biografia (MAX. 255 Carac): \n"))
    while len(bio)>255:
        cls()
        print("MAXIMO 255 CARACTERES")
        bio = str(input("Ingrese biografia (MAX. 255 Carac): \n"))
    if len(bio)<255:
        alumno.bio = bio.ljust(255, ' ')
    else:
        alumno.bio = bio
    
    hob = str(input("Ingrese hobbies (MAX. 255 Carac): \n"))
    while len(hob)>255:
        cls()
        print("MAXIMO 255 CARACTERES")
        hob = str(input("Ingrese hobbies (MAX. 255 Carac): \n"))
    if len(hob)<255:
        alumno.hob = hob.ljust(255, ' ')
    else:
        alumno.hob = hob


    pickle.dump(alumno, arLoAlumnos)
    arLoAlumnos.flush()
    print(alumno.email, alumno.nombre)
    input()
def login():
    global id
    global salir
    global maxint

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
            # Búsqueda secuencial en Alumnos
            encontrado = buscarSecuencial(email, contr, arLoAlumnos, "alumno")
            
            # Si no se encontró en alumnos, buscar en Moderadores
            if not encontrado:
                encontrado = buscarSecuencial(email, contr, arLoModeradores, "moderador")
            
            # Si no se encontró en moderadores, buscar en Administradores
            if not encontrado:
                encontrado = buscarSecuencial(email, contr, arLoAdmin, "administrador")

            if not encontrado:  # Si no se encontró un usuario válido
                input("Correo electrónico o contraseña inválidos, intente nuevamente:\n")
                maxint += 1

    # 3. Si se agotan los intentos
    if maxint == 3:
        cls()
        print("Has agotado tus 3 intentos. El programa se cerrará.")
        salir = "0"

def buscarSecuencial(email, contr, archivo, tipo_usuario):
    global id
    archivo.seek(0, 0)  # Volver al inicio del archivo
    usuario_encontrado = False  # Controla si encontramos un usuario
    lectura_finalizada = False  # Controla si llegamos al final del archivo

    while not usuario_encontrado and not lectura_finalizada:
        try:
            if archivo.tell() < os.path.getsize(archivo.name):  # Si no hemos llegado al final del archivo
                usuario = pickle.load(archivo)  # Cargar el usuario actual

                # Verificar si el email coincide
                if usuario.email.strip() == email and usuario.contraseña.strip() == contr:
                    # Verificar si el estado es activo
                    if usuario.estado == True:
                        cls()
                        input(f"\n|Bienvenido {usuario.nombre.strip()} ({tipo_usuario})|\n")
                        id=int(usuario.id_est)
                        if tipo_usuario == "alumno":
                            opcmenuEst()  # Función para menú de estudiantes
                        elif tipo_usuario == "moderador":
                            opcmenuMod()  # Función para menú de moderadores
                        elif tipo_usuario == "administrador":
                            opcmenuAdmin()  # Función para menú de administradores
                        
                        usuario_encontrado = True  # Usuario encontrado
                    else:
                        cls()
                        input("Usuario inactivo, intente nuevamente\nPresione enter para continuar:\n")
                        lectura_finalizada = True  # Detenemos la lectura ya que el usuario está inactivo
                # Si el email no coincide, seguimos buscando
            else:
                lectura_finalizada = True  # Si llegamos al final del archivo
        except EOFError:
            lectura_finalizada = True  # Finalizamos si llegamos al final del archivo por un error
        except pickle.UnpicklingError:
            print("Error al cargar un registro, archivo corrupto o mal formado.")
            lectura_finalizada = True  # Detenemos la lectura si hay un error de deserialización
        except Exception as e:
            print(f"Error inesperado: {e}")
            lectura_finalizada = True  # Detenemos la lectura si hay otro error inesperado

    return usuario_encontrado  # Devuelve si se encontró el usuario o no

inicializarArchivos()
inicio()
cerrarArchivos()
