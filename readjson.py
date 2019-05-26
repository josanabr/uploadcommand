#!/usr/bin/env python
import json

FILENAME="/vagrant/uploadcommand.conf"

# Este metodo recibe un nombre de archivo
def abrirArchivo(f):
  with open(f,"r") as json_file:
    return json.load(json_file)

# Este metodo recibe un objeto de tipo json y lee la llave 'col'
def leerCol(j):
  return j['col']

# Este metodo recibe un objeto de tipo json y lee la llave 'row'
def leerFila(j):
  return j['row']

# Este metodo recibe un nombre de archivo que contiene datos en formato JSON
# y lee el valor de la llave 'row'
def filaActual(f):
  return leerFila(abrirArchivo(f))

# Este metodo recibe un nombre de archivo que contiene datos en formato JSON 
# y lee el valor de la llave 'col'
def colActual(f):
  return leerCol(abrirArchivo(f))

# Este metodo recibe como argumento un objeto de tipo JSON y retorna el valor
# cuya llave es 'spreadsheetkey'
def leerHojaCalculo(j):
  return j['spreadsheetkey']

def leerJSONKeys(j):
  return j['jsonkeys']

# Este metodo dado un nombre de archivo devuelve una cadena de caracteres que
# que representa la llave de la hoja de calculo
def keyActual(f):
  return leerHojaCalculo(abrirArchivo(f))

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
  with open(f,"w") as json_file:
    data['row'] = val
    json.dump(data,json_file)

def inicializarColumna(f,val = 1):
  with open(f,"w") as json_file:
    data['col'] = val
    json.dump(data,json_file)

def inicializarKey(f,val = "<digite su key>"):
  with open(f,"w") as json_file:
    data['spreadsheetkey'] = val
    json.dump(data,json_file)

#filename = 'uploadcommand.conf'
#incrementarCol(filename)
