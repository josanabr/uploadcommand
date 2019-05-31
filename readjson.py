#!/usr/bin/env python
#
# Este script es un utilitario que provee una diversidad de metodos que permite
# facilmente acceder a la informacion  provista en un archivo JSON que tiene
# la siguiente estructura:
#
# {
#     "col": 1,
#     "jsonkeys": "<SUARCHIVOJSONAQUI>",
#     "row": 1,
#     "spreadsheetkey": "<IDHOJADECALCULOENGOOGLE>"
# }
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2019_05_24
#
import json

FILENAME="/vagrant/uploadcommand.conf"

# Este metodo recibe un nombre de archivo y devuelve un diccionario que contiene
# informacion asociada a un archivo JSON
def abrirArchivo(f):
  with open(f,"r") as json_file:
    return json.load(json_file)

# Esta es una funcion mas generica que dado un diccionario y la llave entrega
# el valor asociado a esa llave
def leerLlave(j,key):
  return j[key]

# Este metodo recibe un objeto de tipo json y retorna el valor asociado a la 
# llave 'col'
def leerCol(j):
  return j['col']

# Este metodo recibe un objeto de tipo json y retorna el valor asociado a la 
# llave 'row'
def leerFila(j):
  return j['row']

# Este metodo recibe un nombre de archivo que contiene datos en formato JSON
# y retorna el valor de la llave 'row'
def filaActual(f):
  return leerFila(abrirArchivo(f))

# Este metodo recibe un nombre de archivo que contiene datos en formato JSON 
# y retorna el valor de la llave 'col'
def colActual(f):
  return leerCol(abrirArchivo(f))

# Este metodo recibe como argumento un objeto de tipo JSON y retorna el valor
# cuya llave es 'spreadsheetkey'
def leerHojaCalculo(j):
  return j['spreadsheetkey']

# Este metodo recibe como argumento un objeto de tipo JSON y retorna el valor
# cuya llave es 'jsonkeys'
def leerJSONKeys(j):
  return j['jsonkeys']

# Este metodo dado un nombre de archivo devuelve una cadena de caracteres que
# que representa la llave de la hoja de calculo
def keyActual(f):
  return leerHojaCalculo(abrirArchivo(f))

# Este metodo dado un nombre de archivo devuelve una cadena de caracteres que
# que representa el archivo que contiene las llaves de autenticacion de Google 
def jsonKeysActual(f):
  return leerJSONKeys(abrirArchivo(f))

def modificarFila(f,n):
  with open(f,"r") as json_file:
    data = json.load(json_file)
  with open(f,"w") as json_file:
    data['row'] = n
    json.dump(data,json_file)

def modificarCol(f,n):
  with open(f,"r") as json_file:
    data = json.load(json_file)
  with open(f,"w") as json_file:
    data['col'] = n
    json.dump(data,json_file)

def incrementarFila(f):
  x = int(filaActual(f))
  x = x + 1
  modificarFila(f,x)

def incrementarCol(f):
  x = int(colActual(f))
  x = x + 1
  modificarCol(f,x)

def inicializarFila(f,val = 1):
  modificarFila(f,val)

def inicializarColumna(f,val = 1):
  modificarCol(f,val)

def inicializarKey(f,val = "<digite su key>"):
  with open(f,"w") as json_file:
    data['spreadsheetkey'] = val
    json.dump(data,json_file)

#filename = 'uploadcommand.conf'
#incrementarCol(filename)
