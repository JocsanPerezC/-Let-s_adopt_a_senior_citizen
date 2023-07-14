#Elaborado por: Jocsan Pérez y José Andres Salazar
#Fecha de Creación: 05/05/2022 11:00am
#Fecha de última Modificación: 25/05/2022 10:00pm
#Versión: 3.10.2

#=========== Importación de librerías ============
from tkinter import *
import tkinter
from tkinter import font
import tkinter as tk
from Funciones import*
from tkinter import messagebox

#======================================================================================
ventana = tkinter.Tk() #VENTANA PRINCIPAL
#ventanaSecundaria = Toplevel(ventana) Hace como que esta ventana vaya a segundo plano
#-----------------------------------------#
insertarP = Toplevel(ventana)
insertarP.withdraw()#Oculta la ventana Insertar participante
#-----------------------------------------#
insertaNParti = Toplevel(ventana)
insertaNParti.withdraw()#Oculta la ventana Insertar N participantes
datosInsertados = Toplevel(ventana)
datosInsertados.withdraw()#Oculta la ventana de los datos insertados
#-----------------------------------------#
enlace = Toplevel(ventana)
enlace.withdraw() #Oculta la ventana enlace
#-----------------------------------------#
darDeBaja = Toplevel(ventana)
darDeBaja.withdraw() #Oculta la ventana dar de baja
justiDarDeBaja = Toplevel(ventana)
justiDarDeBaja.withdraw() #Oculta la ventana justificación dar de baja
SioNO = Toplevel(ventana)
SioNO.withdraw()#Oculta la ventana de elegir si o no
#-----------------------------------------#
carta = Toplevel(ventana)
carta.withdraw()#Oculta la ventana de escribir carta
#-----------------------------------------#
reportes = Toplevel(ventana)
reportes.withdraw()#Oculta la ventana de reportes
hobbies = Toplevel(ventana)
hobbies.withdraw()#Oculta la ventana de Hobbies
#-----------------------------------------#
#======================================================================================

#==============================================================
#================  FUNCIONES PARA LAS VENTANAS  ===============
#==============================================================
def cambiarEstado(): #cambia estado
    boton2['state'] = tk.NORMAL
    boton3["state"] = tk.NORMAL
    boton4["state"] = tk.NORMAL
    boton5["state"] = tk.NORMAL
    boton6["state"] = tk.NORMAL
    boton7["state"] = tk.NORMAL
    messagebox.showinfo(message="La base de datos de países ha sido cargada con éxito", title="Excelente trabajo")

def mostrar(ventana): ventana.deiconify()#mostrar una ventana
def ocultar(ventana):ventana.withdraw()#ocultar una ventana
def ejecutar(f): ventana.after(130,f)#para que haya un lapso de tiempo entre cerrar y abrir ventanas

def eliminarTexto(): #elimina texto
    entry1.delete(0,"end")
    entry3.delete(0,"end")
    entry4.delete(0,"end")
    entry9.delete("1.0","end")
    entry10.delete(0,"end")
    entry11.delete(0,"end")
    entry12.delete(0,"end")

#============================== FUNCION PARA INSERTAR PARTICIPANTES ======================
def recibirDatos(listaPersonas):
    fecha = entry1.get() #Fecha de nacimiento
    nombre = entry3.get()#Nombre completo
    hobbies = entry4.get() #Hobbies
    descripcion = entry9.get(1.0, "end-1c") #Descripcion
    eliminarTexto()
    if verificaNombre(nombre) == True:
        if verificaApellidos(nombre) == True:
            if verificaHobby(hobbies) == True:
                if verificafecha(fecha) == True:
                    fechaNacimi = AdultoMoVolun(fecha) #para ver si es adulto o voluntario
                    if fechaNacimi == "no participa":
                        messagebox.showinfo(message="Su edad no esta permitida para participar en nuestro evento\n Voluntario: entre 17 y 25 años\nAdulto mayor: mayor de 55 pero menor a chepito", 
                        title="Contenido erróneo")
                    else:
                        if fechaNacimi == False: #VOLUNTARIO
                            tipo = fechaNacimi 
                            codigo = generarIdentificacionv()
                            partipante = "Voluntario"
                        else: #ADULTO MAYOR
                            tipo = fechaNacimi
                            codigo = generarIdentificacionAm()
                            partipante = "Adulto Mayor"
                        nombreCompleto = remplazarletras(nombre)[1]
                        hobbies = EscogerHobbies(int(hobbies))
                        profe = ProfeuOfi()
                        correo = remplazarletras(nombre)[0]
                        paises = ElegirRegion()
                        estado = (defineEstado())
                        adoptado = False
                        miniLista = []
                        miniLista = [fecha,tipo,codigo,nombreCompleto,hobbies,profe,correo,paises,estado,descripcion,adoptado]
                        listaPersonas.append(miniLista)
                        hobbies = str(hobbies)[1:-1] #para escribirlo abajo
                        messagebox.showinfo(message = "Su Fecha de nacimiento es: " +str(fecha)+ 
                        "\nTipo de participante es: "+partipante+
                        "\nSu codigo es: " +str(codigo)+
                        "\nSu Nombre completo es: " +str(nombreCompleto[0])+" "+str(nombreCompleto[1])+" "+str(nombreCompleto[2])+
                        "\nSu Hobbies son: " +str(hobbies)+
                        "\nSu Profesión u oficio  es: " +str(profe[1])+
                        "\nSu correo electrónico: " +str(correo)+
                        "\nSu país es: " +str(paises[1])+
                        "\nSu estado es Activo"
                        "\nSu información adicional: " +str(descripcion),
                        title="Datos obtenidos")
                        return listaPersonas,ejecutar(ocultar(insertarP)),ejecutar(mostrar(ventana))
                else:
                    messagebox.showinfo(message="Debe de indicar una fecha valida", title="Contenido erróneo")
            else:
                messagebox.showinfo(message="Para el hobby debe de indicar un numero entre 1 y 3", title="Contenido erróneo")
        else:
            messagebox.showinfo(message="El nombre debe de contener dos apellidos", title="Contenido erróneo")
    else:
        messagebox.showinfo(message="El nombre debe de iniciar con mayúscula y al menos 2 caracteres de texto", title="Contenido erróneo")

#============================== FUNCIÓN PARA INSERTAR N PARTICIPANTES ======================
def obtenerDatosNParti():
    num = entry10.get()
    eliminarTexto()
    if verificaNum(num) == True:
        num = int(num)
        if num >= 10:
            Nparticipantes(num,listaPersonas)
            messagebox.showinfo(message="Se han generado " +str(num)+ " participantes con éxito", title="Felicidades")
            return ejecutar(ocultar(insertaNParti)),ejecutar(mostrar(ventana))
        else:
            messagebox.showinfo(message="Debe ser un numero mayor o igual a 10", title="Contenido erróneo")
    else:
        messagebox.showinfo(message="Debe de indicar un numero", title="Contenido erróneo")

#===================================== FUNCIÓN PARA ENLAZAR ======================
def enlazarAbuelos(listaPersonas):
    contaVoluntario = 0
    contaAbuelo = 0
    for i in listaPersonas:
        if i[1] == True: #si es abuelo
            contaAbuelo += 1
        else: #si es voluntario
            contaVoluntario += 1
    if contaAbuelo >= 1 and contaVoluntario >= 1: #con esto es por si no existen abuelos o voluntarios que se devuelva
        return enlazarAbuelosF(listaPersonas,diccionario),ejecutar(ocultar(ventana)),ejecutar(mostrar(enlace))
    messagebox.showinfo(message="Debe de haber al 1 o mas abuelos y voluntarios registrados", title="Necesitamos abuelos")
    return ejecutar(mostrar(ventana))

#=================================== FUNCIÓN PARA DAR DE BAJA ==================================
def verificaLista():
    if listaPersonas == []:
        return messagebox.showinfo(message="No existen abuelos o voluntarios ingresados", title="Sin abuelos o voluntarios")
    return ejecutar(ocultar(ventana)),ejecutar(mostrar(darDeBaja))

def darDeBajaCodigo():
    codigo = entry11.get()
    if verificaCodigo(codigo) == True:
        for i in listaPersonas:
            if codigo in i:
                return ejecutar(ocultar(darDeBaja)),ejecutar(mostrar(justiDarDeBaja))
        else:
            messagebox.showinfo(message="El codigo indicado no existe registrado", title="Codigo inexistente")
            eliminarTexto()
            return ejecutar(ocultar(darDeBaja)),ejecutar(mostrar(ventana))
    else:
        messagebox.showinfo(message="Debe de indicar un codigo valido\n Ejemplo: am##### o v#####", title="Codigo erróneo")
        eliminarTexto()

def darDeBajaJustificacion():
    codigo = entry11.get()
    justificacion = entry12.get()
    eliminarTexto()
    darDeBajaFuncion(listaPersonas,codigo,justificacion)
    return ejecutar(ocultar(SioNO)),ejecutar(mostrar(ventana)),messagebox.showinfo(message="Se ha dado de baja a la persona", title="Procedimiento exitoso")

#================================ FUNCION PARA ENVIAR CORREOS =====================================
def enviarCorreosPareja():
    if diccionario == {}:
        return messagebox.showinfo(message="No existen parejas registradas para mandar correos", title="No hay parejas")   
    return escribirCarta(diccionario),ejecutar(ocultar(ventana)),ejecutar(mostrar(carta))

#================================== FUNCIONES DE REPORTES =======================================
#================ FUNCION PARA OBTENER LOS DATOS COMPLETOS DE LOS PARTICIPANTES ====================
def mostrarBaseDedatos():
    if listaPersonas == []: 
        messagebox.showinfo(message="No existen personas registradas todavia", title="No hay personas") 
        return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))
    grabarBaseDeDatos("baseDeDatos.csv")
    messagebox.showinfo(message="Se ha creado un excel con los datos", title="Felicidades") 
    return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))

#================== FUNCION PARA LA LISTA DE ADULTOS MAYORES NO ADOPTADOS ===================
def adultosSinAdoptar():
    existe = False
    for i in listaPersonas:
        if i[1] == True and i[-1] == False: #que sean abuelos sin adoptar
            existe = True
    if existe == True:
        grabarAbuelosNoAdoptados("AbuelosNoAdoptados.csv")
        messagebox.showinfo(message="Se ha creado un excel con los abuelos sin adoptar", title="Felicidades")
        return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))
    messagebox.showinfo(message="No existen abuelos sin adoptar", title="Aviso")
    return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))

#====================== FUNCION PARA LOS ADULTOS MAYORES ENLAZADOS ==========================
def adultosEnlazados():
    if diccionario == {}:
        messagebox.showinfo(message="No existen abuelos enlazados", title="Aviso")
        return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))
    grabarEnlazamientos("Enlazamientos.csv")
    messagebox.showinfo(message="Se ha creado un excel con los abuelos enlazados", title="Felicidades")
    return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))

#====================== FUNCION PARA OBTENER LOS HOBBIES ==================================
def existenciaHobby():
    if listaPersonas == []:
        messagebox.showinfo(message="Todavia no existen personas registradas", title="Aviso")
        return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))
    return ejecutar(ocultar(reportes)),ejecutar(mostrar(hobbies))

def obtenerHobby():
    hobby = selec.get() #obtiene el valor asignado en cada boton
    if hobby == 0:
        return messagebox.showinfo(message="Debe seleccionar un hobby", title="Sin ingreso de datos")

    existe = False
    temp = hobby #temp seria el numero que llega
    if hobby <= 9: #para poder analizar los que empiezan en 0
        hobby = "Hobbie" #se vuelve un str
        hobby += "0" #sea agrega 0
        hobby += str(temp) #se agrega el valor original de hobby
    else:
        hobby = "Hobbie"
        hobby += str(temp)

    for i in listaPersonas:
        if hobby in i[4]:
            existe = True
    if existe == True:
        grabaParticipantesSegunHobby("ParticipantesYhobby.csv",hobby)
        messagebox.showinfo(message="Se ha creado un excel con los datos", title="Aviso")
        return ejecutar(ocultar(hobbies)),ejecutar(mostrar(ventana))
    messagebox.showinfo(message="No existen personas con ese hobby", title="Aviso")
    return ejecutar(ocultar(hobbies)),ejecutar(mostrar(ventana))

#============= FUNCION DE PARTICIPANTES INACTIVOS Y SU JUSTIFICACION ================
def partiInactivos():
    existe = False
    for i in listaPersonas:
        if i[-3][0] == 0: #para ver si esta activo
            existe = True
    if existe == True:
        grabaParticipantesInactivos("ParticipantesInactivos.csv")
        messagebox.showinfo(message="Se ha creado un excel con los datos", title="Aviso")
        return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))
    messagebox.showinfo(message="No existen personas inactivas", title="Aviso")
    return ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))

#==========================================================================================
#=============           CONFIGURACIÓN DE LAS VENTANAS SECUNDARIAS           ==============
#==========================================================================================
#==========================================================================================
#==========         Configuración de la ventana Insertar participantes        =============
#==========================================================================================
insertarP.geometry("650x1000") #Dimensiones: Anchura x ALtura  
insertarP.configure(background="white") #cambia de color el fondo

#========= Configuración del título ==================
Label(insertarP, text="Insertar un participante",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",18),).grid(row=0, column=0, sticky="w") 

textEntry = tk.StringVar()
textEntry.set("Activo")

#======== Configuración de etiquetas y cajas de textos ============
#-----Etiqueta Fecha de nacimiento----
Label(insertarP,text="Fecha de nacimiento (ejemplo: ##/##/####)", fg="black",bg="white", 
    font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry1 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14))
entry1.grid(row=1, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Tipo de participante----
Label(insertarP,text="Tipo de participante",
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=2, column=0, sticky="w")

seleccion = IntVar()
#Boton Adulto mayor
adulto = Radiobutton(insertarP, text="Adulto mayor",background="white",font=font.Font(family="Times", size=12), variable = seleccion, value =1).grid(
sticky="w", row=2,column=1, padx=5, ipadx=90, pady=3, ipady=3)
#Boton Voluntario
voluntario = Radiobutton(insertarP, text="Voluntario", background="white",font=font.Font(family="Times", size=12), variable = seleccion, value = 1).grid(
sticky="w", row=3, column=1, padx=5, ipadx=90, pady=3, ipady=3)

#-----Etiqueta Identificador de participante----
Label(insertarP,text="Identificador de participante", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=4, column=0, sticky="w")
#Caja de texto.
entry2 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14),textvariable = textEntry,state='disabled' )
entry2.grid(row=4, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Nombre completo----
Label(insertarP,text="Nombre completo", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=5, column=0, sticky="w")
#Caja de texto.
entry3 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14))
entry3.grid(row=5, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Hobbies----
Label(insertarP,text="Hobbies (numero de 1 a 3)", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=6, column=0, sticky="w")
#Caja de texto.
entry4 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14))
entry4.grid(row=6, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Profesión u oficio----
Label(insertarP,text="Profesión u oficio", fg="black", bg="white", 
    font=("Arial Baltic", 12)).grid(row=7, column=0, sticky="w")
#Caja de texto.
entry5 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14),textvariable = textEntry,state='disabled')
entry5.grid(row=7, column=1,padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Correo electrónico----
Label(insertarP,text="Correo electrónico", fg="black",bg="white", 
    font=("Arial Baltic", 12)).grid(row=8, column=0, sticky="w")
#Caja de texto.
entry6 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14),textvariable = textEntry,state='disabled')
entry6.grid(row=8, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta País de origen----
Label(insertarP,text="País de origen", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=9, column=0, sticky="w")
#Caja de texto.
entry7 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14),textvariable = textEntry,state='disabled')
entry7.grid(row=9, column=1, padx=10, ipadx=90, pady=15, ipady=10)

#-----Etiqueta Estado----
Label(insertarP,text="Estado", fg="black", bg="white", 
    font=("Arial Baltic", 12)).grid(row=10, column=0, sticky="w")
#Caja de texto.
entry8 = Entry(insertarP,background="#ffa500",font=font.Font(family="Times", size=14),textvariable = textEntry,state='disabled')
entry8.grid(row=10, column=1, padx=10, ipadx=90, pady=15, ipady=10)   

#-----Etiqueta Descripción----
Label(insertarP,text="Descripción o alguna \ninformación extra que desea agregar,\npor ejemplo un numero telefónico", fg="black", bg="white", 
    font=("Arial Baltic", 12)).grid(row=11, column=0, sticky="w")
#Caja de texto.
entry9 = Text(insertarP,background="#ffa500",font=font.Font(family="Times", size=14), width=40,height=7.5)
entry9.grid(row=11,column=1,)   

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton Insertar----
insertar = tkinter.Button(insertarP, text="Insertar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [recibirDatos(listaPersonas)]
    ).place(relx=0.04, rely=0.92, relwidth=0.3, relheight=0.05)

#----Boton Limpiar----
limpiar = tkinter.Button(insertarP, text="Limpiar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = eliminarTexto).place(relx=0.35, rely=0.92, relwidth=0.3, relheight=0.05)

#----Boton Regresar----
regresar = tkinter.Button(insertarP, text="Regresar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(insertarP)),ejecutar(mostrar(ventana)),eliminarTexto()]).place(relx=0.66, rely=0.92, relwidth=0.3, relheight=0.05)

#========================================================================================
#=============    Configuración de la ventana Insertar -N- participantes     ============
#========================================================================================
insertaNParti.geometry("500x200") #Dimensiones: Anchura x ALtura  
insertaNParti.configure(background="white") #cambia de color el fondo
insertaNParti.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(insertaNParti,text="Insertar N participantes",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",18),
    ).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label (insertaNParti,text="Cantidad a generar:\n (un numero mayor o igual a 10)", fg="black", bg="white", 
    font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")

#Caja de texto.
entry10 = Entry(insertaNParti,background="#ffa500",font=font.Font(family="Times", size=14))
entry10.grid(row=1, column=1, padx=10, ipadx=20, pady=15, ipady=10)

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton Insertar----
insertar = tkinter.Button(insertaNParti, text="Insertar", fg = "white", bg = "black", font = "Arial", 
    command = obtenerDatosNParti).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(insertaNParti, text="Limpiar",fg = "white", bg = "black", font = "Arial", 
    command= eliminarTexto).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(insertaNParti, text="Regresar", fg = "white", bg = "black", font = "Arial", 
    command = lambda: [eliminarTexto(),ejecutar(ocultar(insertaNParti)),ejecutar(mostrar(ventana))]).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)
#-------------------------------------------------------------------------------------------------------------------------------------#
#=================================================================================
#=============          Configuración de la ventana Enlaces           ============
#=================================================================================
enlace.geometry("240x150") #Dimensiones: Anchura x ALtura  
enlace.configure(background="white") #cambia de color el fondo
Label(enlace, text="Enlace creado \nsatisfactoriamente", fg = "black",bg="white", font=("Arial Baltic",20),).grid(row=0,column=1) 

#----Boton Regresar----
regresar = Button(enlace, text="Regresar", fg = "white", bg = "black", font = "Arial",
    command = lambda: [ejecutar(ocultar(enlace)),ejecutar(mostrar(ventana))]).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#-------------------------------------------------------------------------------------------------------------------------------------#
#===================================================================================
#=============          Configuración de la ventana Dar de Baja          ===========
#===================================================================================
darDeBaja.geometry("500x200") #Dimensiones: Anchura x ALtura  
darDeBaja.configure(background="white") #cambia de color el fondo
darDeBaja.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(darDeBaja, 
    text="Dar de baja",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",18),
    ).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label(darDeBaja,text="Código de participante", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry11 = Entry(darDeBaja,background="#ffa500",font=font.Font(family="Times", size=14))
entry11.grid(row=1,  column=1, padx=10, ipadx=50, pady=15, ipady=10)

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton Insertar----
insertar = tkinter.Button(darDeBaja, text="Insertar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: darDeBajaCodigo()
    ).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(darDeBaja, text="Limpiar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = eliminarTexto).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(darDeBaja, text="Regresar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [eliminarTexto(),ejecutar(ocultar(darDeBaja)),ejecutar(mostrar(ventana))]
).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)
#---------------------------------------------------------------
#=============== Justificación de dar de baja ==================
#---------------------------------------------------------------
justiDarDeBaja.geometry("500x200") #Dimensiones: Anchura x ALtura  
justiDarDeBaja.configure(background="white") #cambia de color el fondo
justiDarDeBaja.resizable(width=0, height=0)

#========= Configuración del título ======================
Label(justiDarDeBaja, 
    text="Razón de su \njustificación",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",18),
    ).grid(row=0, column=0, sticky="w") 

#========= Configuración de la etiqueta ======================
#-----Etiqueta Cantidad a generar----
Label(justiDarDeBaja,text="Justificación:", 
    fg="black",
    bg="white", 
    font=("Arial Baltic", 12)).grid(row=1, column=0, sticky="w")
#Caja de texto.
entry12 = Entry(justiDarDeBaja,background="#ffa500",font=font.Font(family="Times", size=14))
entry12.grid(row=1,column=1, padx=10, ipadx=50, pady=15, ipady=10)

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton Insertar----
insertar = tkinter.Button(justiDarDeBaja, text="Baja", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(justiDarDeBaja)),ejecutar(mostrar(SioNO))]
    ).place(relx=0.04, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Limpiar----
limpiar = tkinter.Button(justiDarDeBaja, text="Limpiar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = eliminarTexto).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton Regresar----
regresar = tkinter.Button(justiDarDeBaja, text="Regresar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [eliminarTexto(),ejecutar(ocultar(justiDarDeBaja)),ejecutar(mostrar(ventana))]
).place(relx=0.66, rely=0.7, relwidth=0.3, relheight=0.20)
#----------------------------------------------------------------------------------------------------
#=============== Ventana SI o NO ==================
#----------------------------------------------------------------------------------------------------
SioNO.geometry("240x150") #Dimensiones: Anchura x ALtura  
SioNO.configure(background="white") #cambia de color el fondo
Label(SioNO, text="Desea continuar?", fg = "black",bg="white", font=("Arial Baltic",20),).grid(row=0,column=1) 

#----Boton SI----
si = Button(SioNO, text="Si", fg = "white", bg = "black", font = "Arial",
    command = lambda: darDeBajaJustificacion()).place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.20)

#----Boton NO----
no = Button(SioNO, text="No", fg = "white", bg = "black", font = "Arial",
    command = lambda: [messagebox.showinfo(message="Se ha cancelado", title="Procedimiento cancelado"),
        eliminarTexto(),ejecutar(ocultar(SioNO)),ejecutar(mostrar(ventana))] ).place(relx=0.55, rely=0.7, relwidth=0.3, relheight=0.20)

#-------------------------------------------------------------------------------------------------------------------------------------#
#=====================================================================
#============= Configuración de la ventana Escribir carta ============
#=====================================================================
carta.geometry("300x150") #Dimensiones: Anchura x ALtura  
carta.configure(background="white") #cambia de color el fondo
#---Titulo---
Label(carta, 
    text="Correo enviado \nsatisfactoriamente",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",20),
    ).grid(row=0,column=1)

#----Boton Limpiar----
regresar = tkinter.Button(carta, text="Regresar", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(carta)),ejecutar(mostrar(ventana))]
).place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.20)
#-------------------------------------------------------------------------------------------------------------------------------------#
#==================================================================================
#============        Configuración de la ventana Reportes     =====================
#==================================================================================
reportes.title("Reportes")
reportes.geometry("500x500") #Dimensiones: Anchura x ALtura  
reportes.configure(background="white") #cambia de color el fondo
reportes.resizable(width=0, height=0)#con esto no se puede modificar la ventana

#----Titulo---
Label(reportes, 
    text="Reportes",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",20)).pack(anchor=CENTER) 

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton de Mostrar la base de datos completa---
datos = tkinter.Button(reportes,text= "Mostrar la base de datos completa" ,
    fg = "white", #Letras 
    bg = "black", #fondo 
    font = "Arial", #tipo de letra
    command= lambda: [mostrarBaseDedatos()]
).place(relx=0.15, rely=0.10, relwidth=0.7, relheight=0.1)

#---Boton de Lista de adultos mayores no adoptados---
noAdoptados = tkinter.Button(reportes,text= "Lista de adultos mayores no adoptados" ,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command= lambda: [adultosSinAdoptar()]
).place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.1)

#---Boton Lista de voluntarios con adultos mayores enlazados--
enlazados = tkinter.Button(reportes,text= "Lista de voluntarios con adultos mayores\n enlazados" ,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [adultosEnlazados()]
).place(relx=0.15, rely=0.40, relwidth=0.7, relheight=0.1)

#---Boton Participantes y rol según un hobby---
rolYhobbies = tkinter.Button(reportes,text= "Participantes y rol según un hobby" ,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [existenciaHobby()]
).place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#----------------------------------------------------------------------------------------
#============= Configuración de la ventana Participantes y rol según un hobby ============
#-----------------------------------------------------------------------------------------
hobbies.title("Hobbies") #da titulo a la hobbies
hobbies.geometry("740x500") #Dimensiones: Anchura x ALtura  
hobbies.configure(background="white") #cambia de color el fondo
hobbies.resizable(width=0, height=0)
#----Titulo----
Label(hobbies, 
    text="Seleccione un hobby",
    fg = "black", #Letras 
    bg = "cyan", #fondo 
    font=("Arial Baltic",18)).grid(row=0,column=0) 
Label(hobbies, 
    text="para mostrar las personas",
    fg = "black", #Letras 
    bg = "cyan", #fondo 
    font=("Arial Baltic",18)).grid(row=0,column=1) 
Label(hobbies, 
    text="que disfrutan de el.",
    fg = "black", #Letras 
    bg = "cyan", #fondo 
    font=("Arial Baltic",18)).grid(row=0,column=2) 
#============== Configuración de los botones de hobbies ===============
selec = IntVar()
#command = lambda: [ejecutar(ocultar(hobbies)),ejecutar(mostrar(ventana))]
#--------------------------------------------------------------#
#Hobby 1
adulto1 = Radiobutton(hobbies, text="Hobby 1",background="white",font=font.Font(family="Times", size=12), variable=selec, value=1).grid(
sticky="w",row=1, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 2
adulto2 = Radiobutton(hobbies, text="Hobby 2",background="white",font=font.Font(family="Times", size=12), variable=selec, value=2).grid(
sticky="w", row=1,column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 3
adulto3 = Radiobutton(hobbies, text="Hobby 3",background="white",font=font.Font(family="Times", size=12), variable=selec, value=3).grid(
sticky="w", row=1, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 4
adulto4 = Radiobutton(hobbies, text="Hobby 4",background="white",font=font.Font(family="Times", size=12), variable=selec, value=4).grid(
sticky="w", row=2,  column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 5
adulto = Radiobutton(hobbies, text="Hobby 5",background="white",font=font.Font(family="Times", size=12), variable=selec, value=5).grid(
sticky="w", row=2,  column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 6
adulto = Radiobutton(hobbies, text="Hobby 6",background="white",font=font.Font(family="Times", size=12), variable=selec, value=6).grid(
sticky="w", row=2,  column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 7
adulto = Radiobutton(hobbies, text="Hobby 7",background="white",font=font.Font(family="Times", size=12), variable=selec, value=7).grid(
sticky="w", row=3, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 8
adulto = Radiobutton(hobbies, text="Hobby 8",background="white",font=font.Font(family="Times", size=12), variable=selec, value=8).grid(
sticky="w", row=3, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 9
adulto = Radiobutton(hobbies, text="Hobby 9",background="white",font=font.Font(family="Times", size=12), variable=selec, value=9).grid(
sticky="w", row=3, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 10
adulto = Radiobutton(hobbies, text="Hobby 10",background="white",font=font.Font(family="Times", size=12), variable=selec, value=10).grid(
sticky="w", row=4,  column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 11
adulto = Radiobutton(hobbies, text="Hobby 11",background="white",font=font.Font(family="Times", size=12), variable=selec, value=11).grid(
sticky="w", row=4, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 12
adulto = Radiobutton(hobbies, text="Hobby 12",background="white",font=font.Font(family="Times", size=12), variable=selec, value=12).grid(
sticky="w", row=4, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 13
adulto = Radiobutton(hobbies, text="Hobby 13",background="white",font=font.Font(family="Times", size=12), variable=selec, value=13).grid(
sticky="w", row=5, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 14
adulto = Radiobutton(hobbies, text="Hobby 14",background="white",font=font.Font(family="Times", size=12), variable=selec, value=14).grid(
sticky="w", row=5, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 15
adulto = Radiobutton(hobbies, text="Hobby 15",background="white",font=font.Font(family="Times", size=12), variable=selec, value=15).grid(
sticky="w", row=5, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 16
adulto = Radiobutton(hobbies, text="Hobby 16",background="white",font=font.Font(family="Times", size=12), variable=selec, value=16).grid(
sticky="w", row=6, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 17
adulto = Radiobutton(hobbies, text="Hobby 17",background="white",font=font.Font(family="Times", size=12), variable=selec, value=17).grid(
sticky="w", row=6,column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 18
adulto = Radiobutton(hobbies, text="Hobby 18",background="white",font=font.Font(family="Times", size=12), variable=selec, value=18).grid(
sticky="w", row=6, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 19
adulto = Radiobutton(hobbies, text="Hobby 19",background="white",font=font.Font(family="Times", size=12), variable=selec, value=19).grid(
sticky="w", row=7, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 20
adulto = Radiobutton(hobbies, text="Hobby 20",background="white",font=font.Font(family="Times", size=12), variable=selec, value=20).grid(
sticky="w", row=7, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 21
adulto = Radiobutton(hobbies, text="Hobby 21",background="white",font=font.Font(family="Times", size=12), variable=selec, value=21).grid(
sticky="w", row=7, column=2, padx=5, ipadx=50, pady=3, ipady=3)
#--------------------------------------------------------------#
#Hobby 22
adulto = Radiobutton(hobbies, text="Hobby 22",background="white",font=font.Font(family="Times", size=12), variable=selec, value=22).grid(
sticky="w", row=8, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 23
adulto = Radiobutton(hobbies, text="Hobby 23",background="white",font=font.Font(family="Times", size=12), variable=selec, value=23).grid(
sticky="w", row=8, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 24
adulto = Radiobutton(hobbies, text="Hobby 24",background="white",font=font.Font(family="Times", size=12), variable=selec, value=24).grid(
sticky="w", row=8, column=2, padx=5, ipadx=50, pady=3, ipady=3)

#Hobby 25
adulto = Radiobutton(hobbies, text="Hobby 25",background="white",font=font.Font(family="Times", size=12), variable=selec, value=25).grid(
sticky="w", row=9, column=0, padx=5, ipadx=50, pady=3, ipady=3)

#Boton ver hobbies
verHobbies = tkinter.Button(hobbies,text="Ver hobby", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = obtenerHobby
    ).grid(
sticky="w", row=9, column=1, padx=5, ipadx=50, pady=3, ipady=3)

#----------------------------------------------------------------#
#---Boton de Participantes inactivos y su justificación---
#----------------------------------------------------------------#
boton5 = tkinter.Button(reportes,text= "Participantes inactivos y su justificación" ,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [partiInactivos()]
    )
boton5.place(relx=0.15, rely=0.70, relwidth=0.7, relheight=0.1)

#---Boton de salir---
salir = tkinter.Button(reportes, text="Salir", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(reportes)),ejecutar(mostrar(ventana))]
).place(relx=0.15, rely=0.85, relwidth=0.7, relheight=0.1)


#==================================================================================
#==================================================================================
#=============         Configuración de la ventana PRINCIPAL            ===========
#==================================================================================
#==================================================================================
ventana.title("Adopta a un abuelito") #da titulo a la ventana
ventana.geometry("500x700") #Dimensiones: Anchura x ALtura  
ventana.configure(background="white") #cambia de color el fondo
#ventana.resizable(width=0, height=0)#con esto no se puede modificar la ventana

#----Titulo---
Label(ventana, 
    text="Adoptemos a un adulto mayor",
    fg = "black", #Letras 
    bg = "white", #fondo 
    font=("Arial Baltic",20),
    ).grid(row = 0,column = 0)

#============== Configuración de los botones ===============
#width = Ancho del boton
#height = Altura del boton
#----Boton de países---
boton1 = tk.Button(ventana,text= "Cargar BD de países" ,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [cambiarEstado(),CargarBD("paises.txt")]
).place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.09)

#---Boton de Insertar un participante---
boton2 = tk.Button(ventana,text= "Insertar un participante",state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(ventana)),ejecutar(mostrar(insertarP))])
boton2.place(relx=0.15, rely=0.2, relwidth=0.7, relheight=0.09)

#---Boton de Insertar N participantes--
boton3 = tk.Button(ventana,text= "Insertar N participantes" ,state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(ventana)),ejecutar(mostrar(insertaNParti))])
boton3.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.09)

#---Boton de Enlazar con abuelos---
boton4 = tk.Button(ventana,text= "Enlazar con abuelos",state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [enlazarAbuelos(listaPersonas)])
boton4.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.09)

#---Boton de Dar de baja---
boton5 = tk.Button(ventana,text= "Dar de baja" ,state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: verificaLista())
boton5.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.09)

#---Boton de Escribe una carta a su correo---
boton6 = tk.Button(ventana,text= "Escribe una carta a su correo",state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: enviarCorreosPareja())
boton6.place(relx=0.15, rely=0.6, relwidth=0.7, relheight=0.09)

#---Boton de Reportes---
boton7 = tk.Button(ventana,text = "Reportes" ,state=tk.DISABLED,
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = lambda: [ejecutar(ocultar(ventana)),ejecutar(mostrar(reportes))])
boton7.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.09)

#---Boton de salir---
salir = tk.Button(ventana, text="Salir", 
    fg = "white", #Letras blancas
    bg = "black", #fondo negro
    font = "Arial", #tipo de letra
    command = ventana.destroy).place(relx=0.15, rely=0.8, relwidth=0.7, relheight=0.09)

#===== Bucle de la ventana ======
ventana.mainloop() #llama a la ventana principal