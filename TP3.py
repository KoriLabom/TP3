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
        self.puntaje=0
        self.superlike = 1
        self.credito_revelar=1

class Moderador:
    def __init__ (self):
        self.id = 0
        self.email = " "
        self.contraseña = " "
        self.estado = True
        self.nombre = " "
        self.reportes_ignorados = 0
        self.reportes_aceptados = 0
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
        self.estado = 0

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
        alumno.puntaje = 0
        alumno.superlike = 1
        alumno.credito_revelar = 1
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
        alumno.puntaje = 0
        alumno.superlike = 1
        alumno.credito_revelar = 1
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
        alumno.puntaje = 0
        alumno.superlike = 1
        alumno.credito_revelar = 1
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
        alumno.puntaje = 0
        alumno.superlike = 1
        alumno.credito_revelar = 1
        formatearAlumnos(alumno)
        pickle.dump(alumno, arLoAlumnos)

        input()
    
    arFiModeradores = "moderadores.dat" #CREAR O ABRIR Moderadores
    if os.path.exists(arFiModeradores):
        arLoModeradores = open(arFiModeradores, "r+b")
    else:
        print("El archivo " + arFiModeradores + " no existía y fue creado")
        arLoModeradores = open(arFiModeradores, "w+b")
        #Moderador 1
        moderador = Moderador()
        moderador.id = 1
        moderador.email = "moderador1@ayed.com"
        moderador.contraseña = "111222"
        moderador.estado = True
        moderador.nombre = "Mateo Labombarda"
        moderador.reportes_ignorados = 0
        moderador.reportes_aceptados = 0

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
    
    arLoAlumnos.flush()
    arLoModeradores.flush()
    arLoAdmin.flush()
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
    alumnos.puntaje = str(alumnos.puntaje).ljust(5, ' ')
    alumnos.superlike = str(alumnos.superlike).ljust(5, ' ')
    alumnos.credito_revelar = str(alumnos.credito_revelar).ljust(5, ' ')
def formatearModeradores(moderador):
    moderador.id = str(moderador.id).ljust(5, ' ')
    moderador.email = moderador.email.ljust(32, ' ')
    moderador.contraseña = moderador.contraseña.ljust(32, ' ')
    moderador.nombre = moderador.nombre.ljust(32, ' ')
    moderador.reportes_ignorados = str(moderador.reportes_ignorados).ljust(5, ' ')
    moderador.reportes_aceptados = str(moderador.reportes_aceptados).ljust(5, ' ')
def formatearAdministradores(administrador):
    administrador.id = str(administrador.id).ljust(5, ' ')
    administrador.email = administrador.email.ljust(32, ' ')
    administrador.contraseña = administrador.contraseña.ljust(32, ' ')

def cls():
    os.system("cls")
#MENUS y OPCIONES
def enConstruccion():
    print("menu en construccion")
    input()
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
def subMenuGestionarCandidatosCredito(): #2 MUESTRA SUB MENU: GESTIONAR CANDIDATOS
    cls()
    print("***** GESTIONAR CANDIDATOS *****\n")
    print("   1. Ver candidatos")
    print("   2. Revelar candidato")
    print("   3. Reportar un candidato")
    print("   0. Volver.\n")
def gestCandidatos(): #GESTIONAR CANDIDATOS
    alumno=Alumno()
    opc = ""  # asignación interna para obligar al mientras a que entre aunque sea una vez
    while (opc!="0"):
        arLoAlumnos.seek(0,0)
        for i in range(0,id):
            alumno=pickle.load(arLoAlumnos)
        if int(alumno.credito_revelar)>=1:
            subMenuGestionarCandidatosCredito()        
            opc = input("\nIngrese una opción: ")
            while (opc<"0" or opc >"3"):
                opc = input("Ingreso inválido, ingrese otra opción: ")
            match opc:
                case "1": verCandidatos()
                case "2": revelarCandidato()
                case "3": reportarCandidato()
        else:
            subMenuGestionarCandidatos()        
            opc = input("\nIngrese una opción: ")
            while (opc<"0" or opc >"2"):
                opc = input("Ingreso inválido, ingrese otra opción: ")
            match opc:
                case "1": verCandidatos()
                case "2": reportarCandidato()
        
def matcheos():
    cls()
    print("***** MATCHEOS *****\n")
    input("En Construcción...")
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
    print("   0. Salir")
def opcmenuMod():
    global maxint
    opc = ""
    while(opc!= "0"):
        menuModerador()
        opc = input("\nIngrese una opción:  ")
        while (opc<"0" or opc>"2"):
            opc = input("ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": gestUsuarios()
            case "2": gestReportes()
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
def desactivarUsua():
    global opcE, opcsubp
    cls()
    opcion = " "
    # Mostrar todos los usuarios activos
    
    arLoAlumnos.seek(0, 0)  # Ir al inicio del archivo

    # Mostrar todos los alumnos activos en la lista
    while opcion != "":
        cls()
        print("***** DESACTIVAR USUARIO *****\n")
        print("Lista de estudiantes:")
        mostrarEstudiantes()
        try:
            while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
                alumno = pickle.load(arLoAlumnos)
        except EOFError:
            pass  # Final del archivo

        # Pedir al moderador que ingrese un ID, nombre o presione Enter para volver
        opcion = input("\nIngrese el ID o Nombre del usuario para desactivar, o presione Enter para volver: ")
        
        
        # Volver a buscar el usuario por ID o nombre, sin usar listas ni break
        usuario_encontrado = False
        arLoAlumnos.seek(0, 0)  # Volver al inicio del archivo

        try:
            while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos) and not usuario_encontrado:
                pos = arLoAlumnos.tell()  # Guardar la posición actual
                alumno = pickle.load(arLoAlumnos)

                # Compara ID o nombre
                if (str(alumno.id.strip()) == opcion or alumno.nombre.strip().lower() == opcion.lower()) and alumno.estado == True:
                    usuario_encontrado = True

                    # Confirmación de desactivación
                    print(f"\n¿Está seguro que desea desactivar el perfil de {alumno.nombre.strip()}?")
                    print(" 1. Desactivar")
                    print(" 0. Cancelar")
                    opc = input("\nIngrese una opción: ")
                    while opc not in ["0", "1"]:
                        opc = input("Ingreso inválido, ingrese otra opción: ")
                    
                    if opc == "1":
                        # Desactivar el usuario
                        arLoAlumnos.seek(pos, 0)  # Volver a la posición del usuario
                        alumno.estado = False  # Desactivar el alumno
                        formatearAlumnos(alumno)
                        pickle.dump(alumno, arLoAlumnos)
                        arLoAlumnos.flush()  # Asegurar que se guarda el cambio
                        print(f"\nEl usuario {alumno.nombre.strip()} ha sido desactivado correctamente!")
                        input("Presione Enter para continuar...")
                    else:
                        print("Operación cancelada.")
        except EOFError:
            pass  # Final del archivo

        if opcion != "" and not usuario_encontrado:
            print("El usuario se encuentra desactivado o no existe.")
            input("Presione Enter para continuar...")
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
#FIN MENUS

#Funciones estudiantes

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
        arLoAlumnos.seek(0)  # Comenzar desde el inicio del archivo
        alumno = None
        pos = None

        # Buscar el alumno por ID
        try:
            for i in range(0, id):
                pos = arLoAlumnos.tell()
                alumno = pickle.load(arLoAlumnos)
            if alumno:  # Si encontramos el alumno
                print("FECHA DE NACIMIENTO ACTUAL: " + alumno.fnac.strip())
            else:
                print("No se encontró el alumno.")
                return
        except EOFError:
            print("Error al leer el archivo o ID fuera de rango.")
            return

        print("")
        fNacimiento = input("Ingrese su nueva fecha de nacimiento (DD-MM-AAAA), o presione Enter para salir: ")

        if fNacimiento != "":
            if fechaValida(fNacimiento):
                arLoAlumnos.seek(pos)  # Mover al inicio del alumno encontrado
                alumno.fnac = fNacimiento
                formatearAlumnos(alumno)
                arLoAlumnos.seek(pos)  # Asegurarse de que el puntero esté en la posición correcta
                pickle.dump(alumno, arLoAlumnos)
                arLoAlumnos.flush()  # Asegurarse de escribir todo antes de cerrar
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
            arLoAlumnos.seek(pos)
            alumno.bio=biografia
            formatearAlumnos(alumno)
            arLoAlumnos.seek(pos)
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
def eliminarPerfil():
    global opcE, opcsubp
    opc = "1"
    arLoAlumnos.seek(0,0)
    for i in range(0,id):
        pos=arLoAlumnos.tell()
        alumno=pickle.load(arLoAlumnos)
    cls()
    print("***** ELIMINAR PERFIL *****\n")
    print("¿Está seguro que desea eliminar su perfil, " + alumno.nombre + "?")
    print(" 1. Eliminar")
    print(" 0. Salir")
    opc = input("\nIngrese una opción: ")
    while (opc<"0" or opc>"1"):
        opc = input("Ingreso inválido, ingrese otra opción: ")
    if opc == "1":

        arLoAlumnos.seek(pos,0)
        alumno.estado = False
        formatearAlumnos(alumno)
        pickle.dump(alumno,arLoAlumnos)
        arLoAlumnos.flush()
        print("Su usuario ha sido desactivado correctamente!")
        input()   
        opcE="0"
        opcsubp="0"
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
def validarUsuario(idR, archivoEstudiantes):
    global idReportado
    idActual = 1  # Contador para el ID actual en el archivo
    encontrado = False  # Variable para controlar si se encuentra el usuario

    # Intentar convertir idR a un entero
    try:
        idR_int = int(idR)
    except ValueError:
        idR_int = None

    # Reposicionar el archivo al principio
    archivoEstudiantes.seek(0, 0)

    # Leer los estudiantes del archivo
    while archivoEstudiantes.tell() < os.path.getsize(archivoEstudiantes.name):
        try:
            estudiante = pickle.load(archivoEstudiantes)  # Cargar cada estudiante del archivo
            
            # Verificar si el id o nombre coinciden y si el estado es "Activo"
            if (idR_int == idActual or idR.lower() == estudiante.nombre.strip().lower()) and estudiante.estado:
                idReportado = idActual
                encontrado = True
                break  # Detener la búsqueda si encontramos el estudiante correcto
        except EOFError:
            break  # Finalizamos si llegamos al final del archivo
        except pickle.UnpicklingError:
            print("Error al deserializar el archivo.")
            break  # Detenemos la lectura si hay un error de deserialización
        except Exception as e:
            print(f"Error inesperado: {e}")
            break  # Detenemos la lectura si hay otro error inesperado
        
        idActual += 1

    return encontrado
def reportarCandidato():
    global motivo, idReportado, id
    idReportado = " "
    motivo = ""
    opc = ''
    reporte=Reporte()
    while opc!="n" and opc != 's' and idReportado != "":
        cls()
        menuReportar()
        idReportado = input("\nIngrese el ID/Nombre del usuario que desea reportar o Enter para salir: ")        
        while opc!="n" and opc!="s" and idReportado != "":
            if validarUsuario(idReportado, arLoAlumnos):
                cls()
                menuReportar()
                arLoAlumnos.seek(0,0)
                for i in range(0,id):
                    alumno=pickle.load(arLoAlumnos)
                if idReportado == id or idReportado==alumno.nombre:
                    idReportado=input("No te puedes reportar a ti mismo! Ingrese otro ID/Nombre del usuario: ")
                else:
                    motivo = input("\nIngrese el Motivo del reporte: ")
                    opc = input("¿Desea guardar y enviar el reporte? (s/n): ")
                    while opc != 's' and opc != 'n':
                        opc = input("Respuesta inválida. ¿Desea guardar y enviar el reporte? (s/n): ")
                    if opc == "s":
                        arLoReportes.seek(0, 2)
                        reporte.id_reportado = idReportado
                        reporte.id_reportante = id
                        reporte.razon_reporte = motivo
                        reporte.estado = 0
                        pickle.dump(reporte, arLoReportes)
                        arLoReportes.flush()
                        input()

            else:
                cls()
                menuReportar()
                print("\nIngrese el ID/Nombre del usuario que desea reportar o Enter para salir: ")
                idReportado = input("\nEl usuario que desea reportar no se encuentra activo o no existe. Por favor, intente de nuevo: ")
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
def revelarCandidato():
    alumno=Alumno()
    cls()
    n=1
    opc =""
    arLoAlumnos.seek(0,0)
    for i in range(0,id):
        pos=arLoAlumnos.tell()
        alumno1=pickle.load(arLoAlumnos)
    print(f"¿Esta seguro que desea revelar candidatos?(s/n) Se revelaran un maximo de 3 estudiantes que le hayan dado like y se consumira un credito. Actualmente tienes {alumno1.credito_revelar} creditos")
    opc = input()
    while opc != 's' and opc != 'n':
        opc = input("Respuesta inválida. ¿desea revelar candidatos? (s/n): ")
    if opc=="s":
        arLoLikes.seek(0,0)
        while arLoLikes.tell() < os.path.getsize(arFiLikes):
            like=pickle.load(arLoLikes)
            if int(str(like.destinatario).strip())==id and n<=3:
                arLoAlumnos.seek(0,0)
                for i in range(0,int(str(like.remitente).strip())):
                    alumno=pickle.load(arLoAlumnos)
                print(f"||Candidato: {n}||Nombre:{alumno.nombre.strip()}||Fecha de nacimiento:{alumno.fnac.strip()}||Edad:{calcularEdad(alumno.fnac.strip())}||Biografia:{alumno.bio.strip()}||Hobbies:{alumno.hob.strip()}||")
                n+=1
        alumno1.credito_revelar = int(alumno1.credito_revelar)-1
        formatearAlumnos(alumno1)
        arLoAlumnos.seek(pos,0)
        pickle.dump(alumno1,arLoAlumnos)
        arLoAlumnos.flush()
        input()
def verCandidatos():
    cls()
    cantidadAlumnos = 0
    like = Like()
    print("***** LISTA DE CANDIDATOS *****\n")
    
    mostrarCandidatos()
    
    meGusta = input("\nIngrese el nombre o id del estudiante que le gustaría hacer un Matcheo, o presione Enter para salir: ")

    
    arLoAlumnos.seek(0, 0)  
    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
        alumno = pickle.load(arLoAlumnos)
        cantidadAlumnos += 1

    while meGusta != "":  
        encontrado = False
        id_estudiante = None  
        
        try:
            meGustaID = int(meGusta)
        except ValueError:
            meGustaID = None

        arLoAlumnos.seek(0, 0)
        
        for n in range(1, cantidadAlumnos + 1):  
            if not encontrado:  # 
                alumno = pickle.load(arLoAlumnos)  
                
                if (alumno.nombre.strip().lower() == meGusta.lower() or n == meGustaID) and alumno.estado: 
                    id_estudiante = alumno.id
                    encontrado = True  

        if encontrado and id_estudiante is not None:
            
            if int(id) == int(id_estudiante):
                print("No puedes dar like a ti mismo.")
            else:
                if buscarLike(id, id_estudiante):
                    print(f"Usted ya le ha dado like a {alumno.nombre.strip()}")
                else:
                    
                    arLoAlumnos.seek(0, 0)
                    emisor_encontrado = False
                    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos) and not emisor_encontrado:
                        pos = arLoAlumnos.tell()  
                        emisor = pickle.load(arLoAlumnos)  
                        
                        if emisor.id == id:  
                            emisor_encontrado = True

                    opc = ""
                    while opc not in ["1", "2", "0"]: 
                        cls()
                        print(f"BONUS TRACK 2: \nDesea utilizar su SuperLike con: {alumno.nombre.strip()}?")
                        print("1.   SuperLike")
                        print("2.   Like")
                        print("0.   Cancelar")
                        opc = input("Ingrese opción: ")
                    
                    if opc == "1":
                        # Este es el código donde hacemos la verificación del superlike y guardamos la información
                        print(f"Superlike actual del emisor: {emisor.superlike}")  # Verifica el valor antes de restar
                        input(f"Tipo de superlike: {type(emisor.superlike)}")  # Confirma el tipo de dato

                        # Verificación y manejo de SuperLike
                        if emisor.superlike.strip() == "1":  # Verificar que sea cadena con un solo dígito
                            print(f"\nUsted ha dado SuperLike a: {alumno.nombre.strip()}")

                            # Guardar el SuperLike (like de ida)
                            like.remitente = id
                            like.destinatario = id_estudiante
                            arLoLikes.seek(0, 2)  # Ir al final del archivo para añadir
                            pickle.dump(like, arLoLikes)
                            arLoLikes.flush()  # Asegurarse de que los datos se escriben en el archivo

                            # Guardar el SuperLike de vuelta (like de vuelta)
                            like.remitente = id_estudiante
                            like.destinatario = id
                            pickle.dump(like, arLoLikes)  # Añadir el SuperLike de vuelta
                            arLoLikes.flush()  # Asegurarse de que los datos se escriben en el archivo

                            print("SuperLike guardado exitosamente.")

                            # Convertir el superlike del emisor a número, restar 1 y convertirlo de vuelta a cadena
                            nuevo_superlike = str(int(emisor.superlike.strip()) - 1)  # Convertir a entero, restar y volver a cadena
                            emisor.superlike = nuevo_superlike  # Guardar el nuevo valor como cadena
                            print(f"Nuevo valor de superlike: {emisor.superlike}")

                            # Actualizar el registro del emisor en el archivo de alumnos
                            arLoAlumnos.seek(pos, 0)  # Volver a la posición del registro
                            formatearAlumnos(emisor)  # Asegurarse de que el registro esté formateado
                            pickle.dump(emisor, arLoAlumnos)  # Guardar el registro actualizado
                            arLoAlumnos.flush()

                            print("Perfil del emisor actualizado con el nuevo superlike.")
                        else:
                            print("\nNo tienes suficientes SuperLikes.")



                    elif opc == "2":
                        print(f"\nUsted ha dado like a: {alumno.nombre.strip()}")
                        # Guardar el like
                        like.remitente = id
                        like.destinatario = id_estudiante
                        arLoLikes.seek(0, 2)
                        pickle.dump(like, arLoLikes)
                        arLoLikes.flush()

        else:
            print("No se encontró el estudiante con ese nombre o ID, o el estudiante no está activo.")
        meGusta = input("\nIngrese el nombre o id del estudiante que le gustaría hacer un Matcheo, o presione Enter para salir: ")

def verificarMatch(remitente, destinatario):
    like = Like()
    encontrado = False
    pos = arLoLikes.tell()
    arLoLikes.seek(0, 0)
    while arLoLikes.tell() < os.path.getsize(arFiLikes) and not encontrado:
        like = pickle.load(arLoLikes)
        # Si el destinatario coincide con el remitente en el like
        if str(like.remitente).strip() == str(destinatario).strip() and str(like.destinatario).strip() == str(remitente).strip():
            encontrado = True  # Se encontró un match
    arLoLikes.seek(pos, 0)
    return encontrado

def reportesEstadisticos():
    cls()
    print("***** REPORTES ESTADISTICOS *****\n")

    likesRecibidosNoDevueltos = 0
    likesDadosNoDevueltos = 0
    matcheos = 0
    totalCandidatos = 0  # Candidatos distintos al usuario logueado

    arLoAlumnos.seek(0, 0)  # Asegurarse de empezar desde el principio del archivo de alumnos
    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
        alumno = pickle.load(arLoAlumnos)
        # Contar los candidatos (alumnos activos diferentes al usuario actual)
        if alumno.estado and alumno.id != id:
            totalCandidatos += 1

    arLoLikes.seek(0, 0)  # Asegurarse de empezar desde el principio del archivo de likes
    while arLoLikes.tell() < os.path.getsize(arFiLikes):
        like = pickle.load(arLoLikes)

        # Si el remitente es el usuario actual (id), es un like que diste
        if str(like.remitente).strip() == str(id).strip():
            if not verificarMatch(like.remitente, like.destinatario):
                likesDadosNoDevueltos += 1  # Likes dados que no han sido devueltos
            else:
                matcheos += 1  # Likes que han sido matcheados

        # Si el destinatario es el usuario actual (id), es un like que recibiste
        elif str(like.destinatario).strip() == str(id).strip():
            if not verificarMatch(like.remitente, like.destinatario):
                likesRecibidosNoDevueltos += 1  # Likes recibidos y no respondidos

    # Calcular el porcentaje de matcheos (sobre el total de candidatos activos)
    if totalCandidatos > 0:
        probabilidad = (matcheos / (totalCandidatos-1)) * 100
    else:
        probabilidad = 0  # Si no hay candidatos, la probabilidad es 0

    # Mostrar los resultados
    print("Porcentaje de matcheos sobre el total posible: {:.1f}%".format(probabilidad))
    print("Likes dados y no recibidos: " + str(likesDadosNoDevueltos))
    print("Likes recibidos y no respondidos: " + str(likesRecibidosNoDevueltos))

    input("\nPresione Enter para volver...")

#funciones Moderadores
def mostrarEstudiantes():
    cantidadAlumnos=1
    arLoAlumnos.seek(0,0)
    while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos):
        alumno=pickle.load(arLoAlumnos)
        cantidadAlumnos+=1
    arLoAlumnos.seek(0,0)
    for i in range (1,cantidadAlumnos):
        alumno=pickle.load(arLoAlumnos) 
        if alumno.estado:
            print(f"||Id:{i}||Nombre:{alumno.nombre.strip()}||Fecha de nacimiento:{alumno.fnac.strip()}||Edad:{calcularEdad(alumno.fnac.strip())}||Biografia:{alumno.bio.strip()}||Hobbies:{alumno.hob.strip()}||")
def mostrarReportes():
    idReporte=1
    alumno=Alumno()
    print("\n***** ESTUDIANTES *****\n")
    reporte=Reporte()
    arLoReportes.seek(0,0)
    mostrarEstudiantes()
    if os.path.getsize(arFiReportes)!=0: #entra si el archivo no esta vacio
        print("\n***** REPORTES *****\n")
        while arLoReportes.tell() < os.path.getsize(arFiReportes): #recorre el archivo
            pos=arLoReportes.tell()
            reporte=pickle.load(arLoReportes)#carga el primer reporte
            arLoAlumnos.seek(0,0)
            for i in range(0,reporte.id_reportante):#verifica que el reportante este activo
                alumno=pickle.load(arLoAlumnos)
            e1=alumno.estado
            arLoAlumnos.seek(0,0)
            for i in range(0,reporte.id_reportado):#verifica que el reportaod este activo
                alumno=pickle.load(arLoAlumnos)
            e2=alumno.estado
            if reporte.estado==0:
                if e1 and e2:#si ambos estan activos y el estado es 0 se muestra el reporte
                    print(f"||Id Reporte: {idReporte}||Id reportante: {reporte.id_reportante}||Id reportado: {reporte.id_reportado}||Motivo del reporte: {reporte.razon_reporte.strip()}||Estado del reporte: {reporte.estado}||")      
                else:#si alguno no esta activo
                    reporte.estado=(-1)
                    arLoReportes.seek(pos,0)
                    pickle.dump(reporte,arLoReportes)
                    arLoReportes.flush()
            idReporte+=1
def reportes():
    arLoModeradores.seek(0,0)
    for i in range(0, id):
        posm = arLoModeradores.tell()
        moderador = pickle.load(arLoModeradores)
    
    es_entero = False
    idreporte = " "
    
    while idreporte != "":
        idreporte = " "
        cantReportes = 0
        cls()
        mostrarReportes()
        idreporte = input("\nIngrese el id del reporte que desea juzgar o enter para volver: ")
        
        while not es_entero:
            if idreporte == "":  
                es_entero = True
            else:
                try:
                    idreporte = int(idreporte)
                    es_entero = True
                except ValueError:
                    cls()
                    mostrarReportes()
                    idreporte = input("El valor ingresado no es un número entero. Por favor, inténtelo de nuevo: ")

        es_entero = False
        
        arLoReportes.seek(0,0)
        while arLoReportes.tell() < os.path.getsize(arFiReportes):
            reporte = pickle.load(arLoReportes)
            cantReportes += 1

        if isinstance(idreporte, int) and (1 <= idreporte <= cantReportes) and reporte.estado == 0:
            arLoReportes.seek(0,0)
            for i in range(0, idreporte):
                posr = arLoReportes.tell()
                reporte = pickle.load(arLoReportes)
            arLoReportes.seek(posr,0)
            arLoModeradores.seek(posm, 0)
            opc = ""
            print("1.Ignorar reporte")
            print("2.Bloquear usuario reportado")
            print("0.Volver")
            opc = input("¿Cómo desea proceder con el reporte seleccionado?")
            
            while opc < "0" or opc > "2":
                opc = input("Ingreso inválido, ingrese otra opción: ")
            
            if opc == "1":
                reporte.estado = 2
                pickle.dump(reporte, arLoReportes)
                arLoReportes.flush()
                moderador.reportes_ignorados += 1
                pickle.dump(moderador, arLoModeradores)
                arLoModeradores.flush()
                idreporte = ""
            
            elif opc == "2":
                idreportado = reporte.id_reportado
                arLoAlumnos.seek(0, 0)
                # Recorre hasta el registro del alumno con id == idreportado
                for i in range(0, idreportado):
                    posa = arLoAlumnos.tell()  # Guarda la posición actual
                    alumno = pickle.load(arLoAlumnos)
                # Cambia el estado del alumno
                alumno.estado = False
                # Mueve el puntero a la posición del alumno leído para sobrescribirlo
                arLoAlumnos.seek(posa,0)
                formatearAlumnos(alumno)
                # Sobrescribe el registro del alumno en el archivo
                pickle.dump(alumno, arLoAlumnos)
                arLoAlumnos.flush()  # Asegura que los datos se escriban

                # Actualiza el reporte
                reporte.estado = 1
                pickle.dump(reporte, arLoReportes)
                arLoReportes.flush()  # Asegura que los datos se escriban
                moderador.reportes_aceptados += 1
                pickle.dump(moderador, arLoModeradores)
                arLoModeradores.flush()
                idreporte = ""
            
            elif opc == "0":
                idreporte = ""
        else:
            input("ID inválido")


def mostrarModeradores():
    cantidadModeradores=1
    arLoModeradores.seek(0,0)
    while arLoModeradores.tell() < os.path.getsize(arFiModeradores):
        moderador=pickle.load(arLoModeradores)
        cantidadModeradores+=1
    arLoModeradores.seek(0,0)
    for i in range (1,cantidadModeradores):
        moderador=pickle.load(arLoModeradores) 
        if moderador.estado:
            print(f"||Id:{i}||Nombre:{moderador.nombre.strip()}||Email:{moderador.email.strip()}")

#funciones admin
def menuAdmin():
    cls()
    print(" ***** MENÚ ADMIN *****\n")
    print("   1. Gestionar Usuarios")
    print("   2. Gestionar Reportes")
    print("   3. Reportes Estadísticos")
    print("   4. Bonus Track 1")
    print("   0. Salir")
def opcmenuAdmin():
    global maxint
    opc = ""
    while(opc!= "0"):
        menuAdmin()
        opc = input("\nIngrese una opción:  ")
        while (opc<"0" or opc>"4"):
            opc = input("ingreso inválido, ingrese otra opción: ")
        match opc:
            case "1": gestUsuariosAdm()
            case "2": enConstruccion()
            case "3": reportesEstadisticosAdmin()
            case "4": Bonustrack1()
            case "0": maxint = 0
def menuGestUsuariosAdm():
    cls()
    print("***** GESTIONAR USUARIOS *****\n")
    print("   1. Eliminar usuario")
    print("   2. Dar de alta un moderador")
    print("   3. Desactivar usuario")
    print("   0. Volver")
def gestUsuariosAdm():
    opc = ""
    while(opc!= "0"):
        menuGestUsuariosAdm()
        opc = input("\nIngrese opción:  ")
        while(opc<"0" or opc>"4"):
            opc = input("Ingreso invalido, ingrese otra opción: ")
        match opc:
            case "1": eliminarUsuario()
            case "2": darAltaMod()
            case "3": desactivarUsua()
def darAltaMod():
    cls()
    moderador = Moderador()
    arLoModeradores.seek(0, 0)

    # Calcular tamaño del registro
    moderador = pickle.load(arLoModeradores)
    tamReg = arLoModeradores.tell()
    tamArc = os.path.getsize(arFiModeradores)
    # Cantidad de registros
    cantReg = tamArc // tamReg
    id_mod = str(cantReg + 1)
    if len(id_mod) < 5:
        moderador.id = str(id_mod.ljust(5, ' '))
    else:
        moderador.id = id_mod
        
    arLoModeradores.seek(0, 2)  # Mover el puntero al final del archivo para agregar un nuevo registro

    salir = False

    # Ingreso de email
    email_valido = False
    while not email_valido and not salir:
        cls()
        print("***** DAR ALTA MODERADOR *****")
        email = str(input("Ingrese correo electrónico (MAX. 32 Carac) o presione Enter para salir: \n"))

        if email == "":
            salir = True
        elif len(email) > 32:
            cls()
            print("MAXIMO 32 CARACTERES!")
        elif len(email) < 12:
            cls()
            print("El correo debe tener mínimo 12 caracteres.")
        else:
            # Comprobar el email en los archivos
            encontrado = buscarMailRep(email, arLoAlumnos)
            if encontrado == 1:
                encontrado = buscarMailRep(email, arLoModeradores)
            if encontrado == 1:
                encontrado = buscarMailRep(email, arLoAdmin)

            if encontrado == 1:
                email_valido = True
                moderador.email = email.ljust(32, ' ')
            else:
                cls()
                print("El email ya está registrado, intente con otro.")

    # No continuar si salir está activado
    if not salir:
        # Solicitar y validar la contraseña
        contraseña_valida = False
        while not contraseña_valida and not salir:
            contraseña = input("Ingrese contraseña (MAX. 32 Carac) o presione Enter para salir: \n")

            if contraseña == "":
                salir = True
            elif len(contraseña) > 32:
                cls()
                print("MAXIMO 32 CARACTERES")
            elif len(contraseña) < 6:
                cls()
                print("La contraseña debe tener mínimo 6 caracteres.")
            else:
                contraseña_valida = True
                moderador.contraseña = contraseña.ljust(32, ' ')

    # No continuar si salir está activado
    if not salir:
        # Recolectar otros datos
        nombre_valido = False
        while not nombre_valido and not salir:
            nombre = input("Ingrese su nombre (MAX. 32 Carac) o presione Enter para salir: \n")

            if nombre == "":
                salir = True
            elif len(nombre) > 32:
                cls()
                print("MAXIMO 32 CARACTERES")
            elif len(nombre) < 3:
                cls()
                print("El nombre debe tener mínimo 3 caracteres.")
            else:
                nombre_valido = True
                moderador.nombre = nombre.ljust(32, ' ')

    # Guardar el nuevo registro en el archivo si no se activó la salida
    if not salir:
        moderador.reportes_ignorados = 0
        moderador.reportes_aceptados = 0
        moderador.reportes_ignorados = str(moderador.reportes_ignorados).ljust(5, ' ')
        moderador.reportes_aceptados = str(moderador.reportes_aceptados).ljust(5, ' ')
        pickle.dump(moderador, arLoModeradores)
        arLoModeradores.flush()
        print("Moderador dado de alta exitosamente.")
    else:
        print("Registro cancelado.")

    input("Presione Enter para continuar...")
def eliminarUsuario():
    global opcE, opcsubp
    cls()
    opcion = " "
    
    while opcion != "":
        cls()
        print("***** ELIMINAR USUARIO *****\n")
        
        # Preguntar si desea eliminar un estudiante o un moderador
        tipo_usuario = input("¿Desea eliminar un estudiante o un moderador? (E/M): ").strip().upper()
        
        while tipo_usuario not in ["E", "M"]:
            tipo_usuario = input("Ingreso inválido. Ingrese 'E' para Estudiante o 'M' para Moderador: ").strip().upper()
        
        if tipo_usuario == "E":
            # Mostrar lista de estudiantes
            print("Lista de estudiantes:")
            mostrarEstudiantes()  # Asumimos que esta función ya está definida
            
            # Pedir al moderador que ingrese un ID o nombre
            opcion = input("\nIngrese el ID o Nombre del estudiante para desactivar, o presione Enter para volver: ")
            
            # Buscar entre los alumnos
            usuario_encontrado = False
            arLoAlumnos.seek(0, 0)  # Volver al inicio del archivo de alumnos
            try:
                while arLoAlumnos.tell() < os.path.getsize(arFiAlumnos) and not usuario_encontrado:
                    pos = arLoAlumnos.tell()  # Guardar la posición actual
                    alumno = pickle.load(arLoAlumnos)

                    # Compara ID o nombre
                    if str(alumno.id.strip()) == opcion or alumno.nombre.strip().lower() == opcion.lower():
                        usuario_encontrado = True
                        # Confirmación de desactivación
                        print(f"\n¿Está seguro que desea desactivar el perfil de {alumno.nombre.strip()}?")
                        print(" 1. Desactivar")
                        print(" 0. Cancelar")
                        opc = input("\nIngrese una opción: ")
                        while opc not in ["0", "1"]:
                            opc = input("Ingreso inválido, ingrese otra opción: ")
                        
                        if opc == "1":
                            # Desactivar el alumno
                            arLoAlumnos.seek(pos, 0)  # Volver a la posición del usuario
                            alumno.estado = False  # Desactivar el alumno
                            formatearAlumnos(alumno)
                            pickle.dump(alumno, arLoAlumnos)
                            arLoAlumnos.flush()  # Asegurar que se guarda el cambio
                            print(f"\nEl usuario {alumno.nombre.strip()} ha sido desactivado correctamente!")
                            input("Presione Enter para continuar...")
                        else:
                            print("Operación cancelada.")
            
            except EOFError:
                pass  # Final del archivo de alumnos

        elif tipo_usuario == "M":
            # Mostrar lista de moderadores
            print("Lista de moderadores:")
            mostrarModeradores()  # Asumimos que esta función ya está definida
            
            # Pedir al moderador que ingrese un ID o nombre
            opcion = input("\nIngrese el ID o Nombre del moderador para desactivar, o presione Enter para volver: ")
            
            # Buscar entre los moderadores
            usuario_encontrado = False
            arLoModeradores.seek(0, 0)  # Volver al inicio del archivo de moderadores
            try:
                while arLoModeradores.tell() < os.path.getsize(arFiModeradores) and not usuario_encontrado:
                    pos = arLoModeradores.tell()  # Guardar la posición actual
                    moderador = pickle.load(arLoModeradores)

                    # Compara ID o nombre
                    if str(moderador.id).strip() == opcion or moderador.nombre.strip().lower() == opcion.lower():
                        usuario_encontrado = True
                        # Confirmación de desactivación
                        print(f"\n¿Está seguro que desea desactivar el perfil de {moderador.nombre.strip()}?")
                        print(" 1. Desactivar")
                        print(" 0. Cancelar")
                        opc = input("\nIngrese una opción: ")
                        while opc not in ["0", "1"]:
                            opc = input("Ingreso inválido, ingrese otra opción: ")
                        
                        if opc == "1":
                            # Desactivar el moderador
                            arLoModeradores.seek(pos, 0)  # Volver a la posición del usuario
                            moderador.estado = False  # Desactivar el moderador
                            pickle.dump(moderador, arLoModeradores)
                            arLoModeradores.flush()  # Asegurar que se guarda el cambio
                            print(f"\nEl moderador {moderador.nombre.strip()} ha sido desactivado correctamente!")
                            input("Presione Enter para continuar...")
                        else:
                            print("Operación cancelada.")
            
            except EOFError:
                pass  # Final del archivo de moderadores
        
        # Si no se encontró el usuario
        if opcion != "" and not usuario_encontrado:
            print("Usuario no encontrado.")
            input("Presione Enter para continuar...")
def reportesEstadisticosAdmin():
    cls()
    masIgnorados=""
    masAceptados=""
    masProcesados=""
    mi=0
    ma=0
    mp=0
    cantReportes=0
    cantReportesIgnorados=0
    cantReportesAceptados=0
    cantReportesDescartados=0
    arLoReportes.seek(0,0)
    while arLoReportes.tell()<os.path.getsize(arFiReportes):
        reporte=pickle.load(arLoReportes)
        cantReportes+=1
        if reporte.estado==2:
            cantReportesIgnorados+=1
        if reporte.estado==1:
            cantReportesAceptados+=1
        if reporte.estado==-1:
            cantReportesDescartados+=1
    arLoModeradores.seek(0,0)
    while arLoModeradores.tell()<os.path.getsize(arFiModeradores):
        moderador=pickle.load(arLoModeradores)
        if moderador.reportes_ignorados >= mi:
            mi=moderador.reportes_ignorados
            masIgnorados=moderador.nombre.strip()
        if moderador.reportes_aceptados >= ma:
            ma=moderador.reportes_aceptados
            masAceptados=moderador.nombre.strip()
        if moderador.reportes_ignorados+moderador.reportes_aceptados >= mp:
            mp=moderador.reportes_ignorados+moderador.reportes_aceptados
            masProcesados=moderador.nombre.strip()
    print(f"Cantidad de reportes realizados por los estudiantes: {cantReportes}")
    if cantReportes==0:
        print(f"Porcentaje de reportes ignorados: 0")
        print(f"Porcentaje de reportes aceptados: 0")
        print(f"Porcentaje de reportes descartados: 0")        
    else:
        print(f"Porcentaje de reportes ignorados: {(cantReportesIgnorados/cantReportes)*100}")
        print(f"Porcentaje de reportes aceptados: {(cantReportesAceptados/cantReportes)*100}")
        print(f"Porcentaje de reportes descartados: {(cantReportesDescartados/cantReportes)*100}")
    print(f"Moderador con mayor cantidad de reportes ignorados: {masIgnorados}")
    print(f"Moderador con mayor cantidad de reportes aceptados: {masAceptados}")
    print(f"Moderador con mayor cantidad de reportes procesados: {masProcesados}")
    input()
#bonus tracks
def Bonustrack1():
    idActual=0
    alumno=Alumno()
    like=Like()
    arLoAlumnos.seek(0,0)
    while arLoAlumnos.tell()<os.path.getsize(arFiAlumnos):#recorre archivo alumnos
        idActual+=1
        racha=0
        posAlumno=arLoAlumnos.tell()
        alumno = pickle.load(arLoAlumnos)
        alumno.puntaje=0
        if alumno.estado:#si el alumno esta activo recorre el archivo likes
            likeDevuelto = False
            arLoLikes.seek(0,0)
            while arLoLikes.tell()<os.path.getsize(arFiLikes):
                likepos=arLoLikes.tell()
                like = pickle.load(arLoLikes)
                if str(like.remitente).strip() == str(alumno.id).strip():#si el remitente de un like es el alumno actual
                    destinatario=like.destinatario
                    arLoLikes.seek(0,0)
                    while arLoLikes.tell()<os.path.getsize(arFiLikes):#busca el like correspondido
                        like = pickle.load(arLoLikes)
                        if verificarMatch(like.remitente,destinatario):
                            likeDevuelto = True
                    if likeDevuelto:#si le devuelven el like
                        if racha<3:#y la racha es menor a 3 le suma un punto y extiende la racha
                            alumno.puntaje=alumno.puntaje+1
                            racha+=1
                        else:#y la racha es mayor o igual a 3 le suma 2 pusntos y anade rtacha
                            alumno.puntaje=alumno.puntaje.strip()+2
                            racha+=1
                    else:#si no le devolvieron el like reinicia racha y le resta un punto
                        alumno.puntaje=alumno.puntaje.strip()-1
                        racha=0
                    arLoAlumnos.seek(posAlumno,0)
                    formatearAlumnos(alumno)
                    pickle.dump(alumno,arLoAlumnos)
                    arLoAlumnos.flush()
            #muestra al primer alumno

            print(f"||Id:{idActual}||Nombre:{alumno.nombre.strip()}||Puntaje:{str(alumno.puntaje).strip()}||")

    input()
                               
def registro():
    cls()
    print("***** REGISTRO *****")
    alumno = Alumno()

    if os.path.getsize(arFiAlumnos) == 0:
        alumno.id = 1
    else:
        arLoAlumnos.seek(0, 0)

        alumno = pickle.load(arLoAlumnos)
        tamReg = arLoAlumnos.tell()
        tamArc = os.path.getsize(arFiAlumnos)

        cantReg = tamArc // tamReg

        id_alum = str(cantReg + 2)
        alumno.id = id_alum
        arLoAlumnos.seek(0, 2)  

    email_valido = False
    while not email_valido:
        email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
        
        while len(email) > 32:
            cls()
            print("MAXIMO 32 CARACTERES!")
            email = str(input("Ingrese correo electrónico (MAX. 32 Carac): \n"))
        while len(email) < 12:
            cls()
            email = input("Su email debe tener mínimo 12 caracteres, intente nuevamente:\n")

        encontrado = buscarMailRep(email, arLoAlumnos)

        if encontrado == 1:
            encontrado = buscarMailRep(email, arLoModeradores)

        if encontrado == 1:
            encontrado = buscarMailRep(email, arLoAdmin)

        if encontrado == 1:
            email_valido = True
        else:
            cls()
            print("El email ya está registrado como alumno, moderador o administrador. Ingrese uno nuevo.")
    
    alumno.email = email

    contraseña = input("\nIngrese contraseña (MAX. 32 Carac): \n")
    while len(contraseña) > 32:
        cls()
        print("MAXIMO 32 CARACTERES")
        contraseña = input("Ingrese contraseña (MAX. 32 Carac): \n")
    while len(contraseña) < 6:
        cls()
        contraseña = input("Su contraseña debe tener mínimo 6 caracteres, intente nuevamente: \n")
   
    alumno.contraseña = contraseña

    nombre = str(input("\nIngrese su nombre (MAX. 32 Carac): \n"))
    while len(nombre) < 3:
        cls()
        nombre = input("Su nombre debe tener mínimo 3 caracteres, intente nuevamente:\n")
    while len(nombre) > 32:
        cls()
        print("MAXIMO 32 CARACTERES")
        nombre = str(input("Ingrese nombre (MAX. 32 Carac): \n"))
   
    alumno.nombre = nombre

    fNacimiento = str(input("\nIngrese su fecha de nacimiento (DD-MM-AAAA): "))
    fechaval = True
    while fechaval:
        if fechaValida(fNacimiento):
            fechaval = False
        else:
            print("Fecha ingresada no válida. Asegúrese de usar el formato DD-MM-AAAA, y una edad entre 18 y 122 años.")
            fNacimiento = input("Ingrese su fecha de nacimiento (DD-MM-AAAA): ")     
    alumno.fnac = fNacimiento

    bio = str(input("\nIngrese biografía (MAX. 255 Carac): \n"))
    while len(bio) > 255:
        cls()
        print("MAXIMO 255 CARACTERES")
        bio = str(input("Ingrese biografía (MAX. 255 Carac): \n"))
   
    alumno.bio = bio
    
    hob = str(input("\nIngrese hobbies (MAX. 255 Carac): \n"))
    while len(hob) > 255:
        cls()
        print("MAXIMO 255 CARACTERES")
        hob = str(input("Ingrese hobbies (MAX. 255 Carac): \n"))
    alumno.hob = hob
    
    sex = ""
    while sex != "M" and sex != "H" and sex != "N":
        sex = str(input("\nIngrese su sexo, M para mujer y H para hombre o N para no especificado\n"))
    alumno.sexo = sex
    # guardar el nuevo registro en el archivo
    alumno.credito_revelar = 1
    alumno.puntaje = 0
    alumno.superlike = 1
    formatearAlumnos(alumno)
    pickle.dump(alumno, arLoAlumnos)
    arLoAlumnos.flush()
    input("\nRegistro exitoso, presione Enter para continuar...")

def login():
    global id
    global salir
    global maxint

    maxint = 0
    encontrado = False 

    while not encontrado and maxint < 3:
        cls()
        print("***** LOGIN *****\n")
        print("Si realizas 3 intentos incorrectos, el programa se cerrará.")
        print(f"Intentos: {maxint}\n")
        email = input("Ingrese correo electrónico: ")
        contr = getpass.getpass("\nIngrese contraseña: ")

        if email == "" or contr == "":
            input("Ingrese un correo y contraseña válidos.\n")
            maxint += 1
        else:
            encontrado = buscarSecuencial(email, contr, arLoAlumnos, "alumno")
            
            # Si no se encontró en alumnos
            if not encontrado:
                encontrado = buscarSecuencial(email, contr, arLoModeradores, "moderador")
            
            # Si no se encontró en moderadores
            if not encontrado:
                encontrado = buscarSecuencial(email, contr, arLoAdmin, "administrador")

            if not encontrado:  # Si no se encontró un usuario válido
                input("Correo electrónico o contraseña inválidos, intente nuevamente:\n")
                maxint += 1
    
    if maxint == 3:
        cls()
        print("Has agotado tus 3 intentos. El programa se cerrará.")
        salir = "0"

def buscarSecuencial(email, contr, archivo, tipo_usuario):
    global id
    archivo.seek(0, 0) 
    usuario_encontrado = False  
    lectura_finalizada = False 

    while not usuario_encontrado and not lectura_finalizada:
        try:
            if archivo.tell() < os.path.getsize(archivo.name): 
                usuario = pickle.load(archivo) 
                
                if usuario.email.strip() == email and usuario.contraseña.strip() == contr:
                    
                    if usuario.estado == True:
                        cls()
                        input(f"\n|Bienvenido {usuario.nombre.strip()} ({tipo_usuario})|\n")
                        id = int(usuario.id)
                        if tipo_usuario == "alumno":
                            opcmenuEst()  
                        elif tipo_usuario == "moderador":
                            opcmenuMod()  
                        elif tipo_usuario == "administrador":
                            opcmenuAdmin()  
                        
                        usuario_encontrado = True  
                    else:
                        print(f"El usuario {usuario.nombre.strip()} está inactivo.")
                        input("Presione Enter para continuar...\n")
                        lectura_finalizada = True  
                
            else:
                lectura_finalizada = True  
        except EOFError:
            lectura_finalizada = True  
        except pickle.UnpicklingError:
            print("Error al cargar un registro, archivo corrupto o mal formado.")
            lectura_finalizada = True  
        except Exception as e:
            print(f"Error inesperado: {e}")
            lectura_finalizada = True  

    return usuario_encontrado  
def buscarMailRep(email, archivo):
    archivo.seek(0, 0)  
    lectura_finalizada = False 

    try:
        while not lectura_finalizada:
            if archivo.tell() < os.path.getsize(archivo.name):  
                usuario = pickle.load(archivo)  

                if usuario.email.strip() == email:
                    # Verificar si el estado es activo
                    if usuario.estado == True:
                        print(f"El Email {usuario.email.strip()} ya está registrado, intente con otro.\n")
                        input("Presione Enter para continuar...")
                        return -1
                    else:
                        print(f"El Email {usuario.email.strip()} está inactivo, intente con otro.\n")
                        input("Presione Enter para continuar...")
                        return -1
            else:
                lectura_finalizada = True  
    except EOFError:
        lectura_finalizada = True  # Finalizamos si llegamos al final del archivo

    # no se encontro
    return 1
inicializarArchivos()
inicio()
cerrarArchivos()