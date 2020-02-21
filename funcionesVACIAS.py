from principal import *
from configuracion import *
import random
import math

def filtrar (cadena):
    cadena=cadena.replace("ñ","ni")
    cadena=cadena.replace("(","")
    cadena=cadena.replace(")","")
    cadena=cadena.replace("!","")
    cadena=cadena.replace("¡","")
    cadena=cadena.replace("¿","")
    cadena=cadena.replace("?","")
    cadena=cadena.replace(".","")
    cadena=cadena.replace(",","")
    cadena=cadena.replace("- ","")
    cadena=cadena.replace("-","")
    cadena=cadena.replace(":","")
    cadena=cadena.replace(";","")
    cadena=cadena.replace("_","")
    cadena=cadena.replace("á","a")
    cadena=cadena.replace("é","e")
    cadena=cadena.replace("í","i")
    cadena=cadena.replace("ó","o")
    cadena=cadena.replace("ú","u")
    cadena= cadena.replace("<i>","")
    cadena= cadena.replace("</i>","")
    return cadena.lower()

def lectura(archivo, subtitulo,n):
    datos=archivo.readlines()
    cont = 2
    while cont<len(datos):
        while datos[cont]!= "\n":
            dato_fil=filtrar (datos[cont])
            if len(dato_fil) > n:
                subtitulo.append(dato_fil[:-1])
            cont = cont + 1
        cont =  cont + 3

def seleccion(subtitulo):
    listaSubtitulo=[]
    aleatorio = random.randint (0, len(subtitulo) -1)
    aleatorio2 = random.randint (0, len(subtitulo))
    listaSubtitulo.append (subtitulo[aleatorio])
    listaSubtitulo.append (subtitulo[aleatorio + 1])
    while aleatorio == aleatorio2 or aleatorio +1 == aleatorio2:
        aleatorio2 = random.randint (0, len(subtitulo))
    listaSubtitulo.append (subtitulo[aleatorio2])

    return listaSubtitulo

def puntos(n):
    return 2**n

def listaNueva (cadena):
    listaNueva = []
    palabraNueva = ""
    for char in cadena:
        if char != " ":
            palabraNueva = palabraNueva + char
        else:
            listaNueva.append(palabraNueva)
            palabraNueva = ""
    listaNueva.append(palabraNueva)
    return  listaNueva

def aparece (lista, palabra):
    for cadena in lista:
        if cadena.lower() == palabra:
            return True
    return False





def procesar(palabraUsuario, mostrada,siguiente, otra, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    if aparece (listaNueva(siguiente), palabraUsuario):
        pygame.mixer.music.load("acierto.mp3")
        pygame.mixer.music.play()
        return puntos(correctas)
    pygame.mixer.music.load("error.mp3")
    pygame.mixer.music.play()
    return -1

