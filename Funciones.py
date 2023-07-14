#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 07/05/2022 11:00am
#Fecha de última Modificación: 25/05/2022 10:00pm
#Version: 3.10.2


#=========== Importación de librerías ============
import codecs
from optparse import Values
import re
import pickle
import random
from secrets import choice

#======== Lista Globales =========
listaPersonas = []

diccionario = {}

listadeLlaves = []

listadecodigos = []

listaNombres = []

listadePaises = {}

listadeHobbies=["Hobbie01","Hobbie02","Hobbie03","Hobbie04","Hobbie05","Hobbie06","Hobbie07","Hobbie08","Hobbie09","Hobbie10","Hobbie11","Hobbie12",
"Hobbie13","Hobbie14","Hobbie15","Hobbie16","Hobbie17","Hobbie18","Hobbie19","Hobbie20","Hobbie21","Hobbie22","Hobbie23","Hobbie24","Hobbie25"]

listadeProfesiones = ["Bombero","Maestro(a)","Dentista","Arquitecto(a)","Chef","Medico","Actor/Actriz","Diseñador(a)","Autor","Periodista","Biólogo(a)","Contador(a)","Enfermero(a)","Abogado(a)"]
listadeOficios = ["Carpintero(a)","Albañil","Cajero(a)","Lechero(a)","Escultor(a)","Soldador(a)","Obrero(a)","Panadero(a)","Repartidor(a)","Sastre","Pastor(a)","Plomero(a)","Editor(a)","Vendedor(a)"]


#=========================== Verificaciones ======================
def verificafecha(fecha):
    if re.match("\d{2}/\d{2}/\d{4}",fecha):
        return True
    return False

def verificaNombre(nombre):#verifica que inicia con mayúscula y al menos 2 caracteres de texto
    if nombre == "":
        return False
    conta = 0
    if nombre[0].istitle() == False:
        return False
    for i in nombre:
        if i.isalpha() == True:
            conta += 1
    if conta >= 1:
        return True
    return False

def verificaApellidos(nombre):
    conta = 0
    for i in range(len(nombre)):
        if nombre[i] == " ":
            conta += 1
    if conta >= 2:
        return True
    return False

def verificaHobby(hobby):
    if hobby == "1" or hobby == "2" or hobby == "3":
        return True
    return False

def verificaNum(num):
    if re.match("\d",num):
        return True
    return False

def verificaCodigo(codigo): #que el codigo ingresado sea correcto
    if re.match("am\d{1,5}$",codigo) or re.match("v\d{1,5}$",codigo):
        return True
    return False

#============================== Funciones de procesamiento =============================================
#=============== Funciones para ingresar participantes ====================
# ====== define si es adulto o voluntario gracias a la fecha =============
def AdultoMoVolun(fecha):
    fecha = fecha.split("/")
    j = fecha[-1]
    j = 2022-int(j)
    if j >= 17 and j <= 25:
        return False # VOLUNTARIO
    elif j >= 55:
        return True # ADULTO MAYOR
    else:
        return "no participa"

#========= Esta se usa si es adulto mayor
def generarIdentificacionAm():
    codigo = "am"
    x = random.randint(00000,99999)
    x = str(x)
    codigo += x
    if codigo in listadecodigos:
        return generarIdentificacionAm(codigo)
    else:
        listadecodigos.append(codigo)
        return codigo

#========= Esta se usa si es voluntario
def generarIdentificacionv():
    codigo = "v"
    x = random.randint(00000,99999)
    x = str(x)
    codigo += x
    if codigo in listadecodigos:
        return generarIdentificacionAm(codigo)
    else:
        listadecodigos.append(codigo)
        return codigo

#==== Con esta función se crea el correo junto con el nombre
def crearCorreo(nombre):
    correo = ""
    nombre = nombre.split(" ")
    nombre1 = nombre[0]
    apellido1 = nombre[-2]
    apellido2 = nombre[-1]
    if len(nombre) == 3:
        correo += nombre[0][0]
        nombre[1] = nombre[1].lower()
        correo += nombre[1]
        correo += "@gmail.com"
        if nombre[-3] != nombre[0]:
            segundoNombre = nombre[-3]
            return correo,(nombre1,segundoNombre,apellido1,apellido2)
        return correo,(nombre1,apellido1,apellido2)
    else:
        correo+=nombre[0][0]
        nombre[2]=nombre[2].lower()
        correo+=nombre[2]
        correo+="@gmail.com"
        if nombre[-3] != nombre[0]:
            segundoNombre = nombre[-3]
            return correo,(nombre1,segundoNombre,apellido1,apellido2)
        return correo,(nombre1,apellido1,apellido2)

def remplazarletras(s):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"),)
    for a, b in replacements:
        s = s.replace(a, b)
    return crearCorreo(s)


#================= Escoger Hobbies aleatorios ==================
def EscogerHobbies(num=None):
    Hobbies = []
    if num == None:
        num = random.randint(1,3)
    num2 = 0
    while num2 != num:
        hobby = random.choice(listadeHobbies)
        if hobby not in Hobbies:
            Hobbies.append(hobby)
            num2 += 1
    return Hobbies

#==== Para elegir profesiones u oficios aleatorios
def ProfeuOfi():
    num = random.randint(0,1)
    if num == 0: #Profesion
        trabajo = random.choice(listadeProfesiones)
        salida = (num,trabajo)
        return salida
    else:
        trabajo = random.choice(listadeOficios)
        salida = (num,trabajo)
        return salida

#======== Elige un país aleatorio ===========
# Para el reto de los países
def SacarLlaves():
    lista = []
    for x in listadePaises.keys():
        lista.append(x)
    return lista
def ElegirRegion():
    lista = SacarLlaves()
    conti = random.choice(lista)
    paises = listadePaises.get(conti)
    paises = paises.split(",")
    paises = random.choice(paises)
    resultado = (conti,paises)
    return resultado

#==== Define el estado de una persona
def defineEstado():
    estado = (1,"")
    return estado

#---------------------------------------------------------------------------------------------------------------------------
#================ Funciones para definir N participantes ================
#FUNCION 1
def DefineNombre():
    nombre="Nombre"
    ap1="apellido"
    ap2="apellidos"
    num = random.randint(00000,99999)
    nombre += str(num)
    ap1 += str(num)
    ap2 += str(num)
    if nombre in listaNombres: #Aquí debería ser una lista donde se guarden todos los nombres que se generan al azar 
        return defineEstado()
    else:
        listaNombres.append(nombre)
        return (nombre,ap1,ap2) 
#Funcion 2
def defineCorreo(nombre): #es una lista
    correo = ""
    inicial = nombre[0][0]
    apellido = nombre[1]
    correo += inicial
    correo += apellido
    correo += "@gmail.com"
    return correo


#=========================================== Funciones de la interfaz ==========================================
#Reto 1
def CargarBD (nomArchLeer):
    lista = []
    try:
        f = codecs.open(nomArchLeer,"rb","utf-8") #utf-8 es la codificacion que usa el archivo
        for linea in f:
            lista.append(linea)
        f.close()
        ordenarlista(lista)
    except:
        print("Error al leer el archivo1: ", nomArchLeer)
    return ""

def ordenarlista(lista):
    for i in lista:
        if i == lista[-1]:
            i = i.split(":")
            listadePaises[i[0]]=i[1]
        else:
            i = i.split(":")
            listadePaises[i[0]]=i[1][:-2]


#===================== Funcion de n participantes ====================
def Nparticipantes(num,listaPersonas):
    for x in range(num):
        info = []
        fecha=""
        dia = random.randint(1,28)
        mes = random.randint(1,12)
        if x % 2 == 0:
            defineaño = random.randint(1901,1967)
            tipo=True
        else:
            defineaño = random.randint(1997,2005)
            tipo=False
        fecha+=str(dia)+"/"+str(mes)+"/"+str(defineaño)
        if defineaño >= 1901 and  defineaño<=1967:
            codigo=""
            codigo = generarIdentificacionAm()
        else:
            codigo=""
            codigo = generarIdentificacionv()
        nombreCompleto = DefineNombre()
        hobbies = EscogerHobbies()
        profe = ProfeuOfi()
        correo = defineCorreo(nombreCompleto)
        paises = ElegirRegion()
        estado = (1,"") # 1 = activo
        descripcion = "Descripcion artificial"
        adoptado = False
        info = [fecha,tipo,codigo,nombreCompleto,hobbies,profe,correo,paises,estado,descripcion,adoptado]
        listaPersonas.append(info)
    return listaPersonas

#================ Funciones para Enlazar Abuelos ================
def enlazarAbuelosF(listaPersonas,diccionario):
    listaAdultos = []
    listaVoluntarios = []
    for i in listaPersonas:
        if i[7][0] == 0: #por si fue dado de baja
            i[7][0] = 0
        elif i[-1] == True: #para que siga adoptado
            i[-1] = True
        elif i[1] == False:
            listaVoluntarios.append(i)#voluntario
        else:
            listaAdultos.append(i)#abuelitos sin enlazar o sin ser adoptados
    rango = len(listaAdultos)
    i = 0
    for x in range(int(rango*70/100)): #para usar el 70% de los abuelos que sigan sin enlazar
        listaAdultos[x][-1] = True
        diccionario[listaAdultos[x][2]] = listaAdultos[i][3],listaVoluntarios[i][2],listaVoluntarios[i][3] #codigo de abuelo: nombre abuelo, codigo persona,nombre persona
        i += 1
        if i == len(listaVoluntarios):
            i = 0
    for i in listaPersonas:
        for x in diccionario.keys():
            if i[2] == x:
                i[-1] = True
    return diccionario

#================ Funcion para Dar de baja ================
def darDeBajaFuncion(listaPersonas,codigo,justificacion):
    for i in listaPersonas:
        if codigo == i[2]:
            info = []
            fecha =  i[0]
            tipo = i[1]
            codigo = codigo
            nombreCompleto = i[3] 
            hobbies = i[4]
            profe = i[5]
            correo = i[6]
            paises = i[7]
            estado = (0,justificacion)
            descripcion = i[9] 
            adoptado = i[10]
            info = [fecha,tipo,codigo,nombreCompleto,hobbies,profe,correo,paises,estado,descripcion,adoptado]
            listaPersonas.remove(i)
            listaPersonas.append(info)
            return listaPersonas

#================ Funcion para Escribir carta ================
def escribirCarta(diccionario):
    miniLista = []
    for x in diccionario.keys(): #saca las llaves
        miniLista.append(x)
    pareja = random.choice(miniLista) #elige a una pareja del diccionario
    for i in diccionario:
        if pareja == i:
            if "Espero que te encuentres bien, saludos" == i[3]:#para no repetir las parejas que ya tienen correo
                break
            else:
                valor1 = diccionario[i][0] #Nombre del adulto
                valor2= diccionario[i][1] #codigo del voluntario    
                valor3 = diccionario[i][2] #Nombre del voluntario
                correo = "Espero que te encuentres bien, saludos"
                del i
                diccionario[pareja] = valor1,valor2,valor3,correo
                return diccionario

#============================================================================
#========================= Funciones de Excel ===============================
#============================================================================
#============= Mostrar base de datos completa  =====================
def grabarBaseDeDatos(nomArchLeer):
    try:
        hoja = open(nomArchLeer,"w")
        hoja.write("Base de datos completa \n\n")
        for i in listaPersonas:
            hoja.write(f"{i}\n")
        hoja.close()
    except:
        print("error")
    return

#============= Lista de Adultos mayores no adoptados  =====================
def grabarAbuelosNoAdoptados(nomArchLeer):
    try:
        hoja = open(nomArchLeer,"w")
        hoja.write("Abuelos no adoptados \n\n")
        abuelos = []
        for i in listaPersonas:
            if i[1] == True and i[-1] == False: #que sean abuelos sin adoptar
                abuelos.append(i)
        for i in abuelos:
            hoja.write(i[2]+", ")#codigo
            hoja.write(str(i[3][0])+" "+str(i[3][1])+" "+str(i[3][2])+", ")#nombre y apellidos
            hoja.write(i[0]+" ")#fecha
            if i[5][0] == 0:# 0 == profesión
                hoja.write("Fue profesional y fue: "+str(i[5][1])+", ")
            else:
                hoja.write("No fue profesional y trabajo en: "+str(i[5][1])+", ")
            hoja.write(i[7][0]+", ") #region
            hoja.write(i[7][1]+",") #país
            hoja.write(i[6]+", ")#correo
            hoja.write("Descripcion: "+i[9]+"\n") #descripcion
        hoja.close()
    except:
        print("error")
    return
#============= Lista de voluntarios con los adultos mayores enlazados  =====================
def grabarEnlazamientos(nomArchLeer):
    try:
        hoja = open(nomArchLeer,"w")
        hoja.write("Enlazamientos \n\n")
        enlazados = []
        for i in diccionario:
            miniLista = []
            codigoAbue = i
            nombreAbue = diccionario[i][0]
            codigoVolu = diccionario[i][1]
            nombreVolu = diccionario[i][2]
            correo = diccionario[i][-1]

            miniLista.append(codigoAbue)
            miniLista.append(nombreAbue)
            miniLista.append(codigoVolu)
            miniLista.append(nombreVolu)
            miniLista.append(correo)

            enlazados.append(miniLista)

        for i in enlazados:
            hoja.write("Abuelo: "+i[0]+", ")#codigo abuelo
            hoja.write(str(i[1][0])+" "+str(i[1][1])+" "+str(i[1][2])+", ")#Nombre abuelo
            hoja.write("Voluntario: "+i[2]+", ")#codigo voluntario
            hoja.write(str(i[3][0])+" "+str(i[3][1])+" "+str(i[3][2])+", ")#nombre voluntario
            if i[-1] == "Espero que te encuentres bien, saludos":
                hoja.write("Correo: Espero que te encuentres bien, saludos\n")
            else:
                hoja.write("\n")
            
        hoja.close()
    except:
        print("error")
    return
#============= Participantes y rol según un hobby  =====================
def grabaParticipantesSegunHobby(nomArchLeer,hobby):
    try:
        hoja = open(nomArchLeer,"w")
        hoja.write("Participantes Y hobby \n\n")
        for i in listaPersonas:
            if hobby in i[4]:
                hoja.write(i[2]+", ")#codigo 
                if i[5][0] == 0:#lo de profesión 1 o 0
                    hoja.write("Profesión: "+str(i[5][1])+", ")
                else:
                    hoja.write("Oficio: "+str(i[5][1])+", ")
                hoja.write(str(i[3][0])+" "+str(i[3][1])+" "+str(i[3][2])+", ")#nombre y apellidos
                hoja.write(i[7][0]+", ") #Region
                hoja.write(i[7][1]+"\n") #país
        hoja.close()
    except:
        print("error")
    return
#============= Participantes inactivos y su justificación  =====================
def grabaParticipantesInactivos(nomArchLeer):
    try:
        hoja = open(nomArchLeer,"w")
        hoja.write("Participantes Inactivos \n\n")
        listaAdultos = []
        listaVoluntarios = []
        for i in listaPersonas:
            if i[-3][0] == 0: #para ver si esta activo, 0 = inactivo
                if i[1] == True: #Adulto
                    listaAdultos.append(i)#adultos
                else:
                    listaVoluntarios.append(i)#voluntario
        for i in listaVoluntarios:
            hoja.write(i[2]+", ")#codigo 
            hoja.write(str(i[3][0])+" "+str(i[3][1])+" "+str(i[3][2])+", ")#nombre y apellidos
            if i[5][0] == 0:#lo de profesión 1 o 0
                hoja.write("Profesión: "+str(i[5][1])+", "+"\n")
            else:
                hoja.write("Oficio: "+str(i[5][1])+", "+"\n")
        for i in listaAdultos:
            hoja.write(i[2]+", ")#codigo 
            hoja.write(str(i[3][0])+" "+str(i[3][1])+" "+str(i[3][2])+", ")#nombre y apellidos
            if i[5][0] == 0:#lo de profesión 1 o 0
                hoja.write("Profesión: "+str(i[5][1])+", "+"\n")
            else:
                hoja.write("Oficio: "+str(i[5][1])+", "+"\n")
            hoja.write(i[-3][1])
    except:
        print("error")
    return

