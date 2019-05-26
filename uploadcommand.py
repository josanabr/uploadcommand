#!/usr/bin/env python
#
# Este script en Python se encarga de:
#   - Cargar las credenciales generadas por Google y que permiten el acceso a 
#     la manipulación de hojas de cálculo de Google Sheets
#   - Cargar el archivo de configuración que determina cual es la hoja de 
#     cálculo que se va a actualizar y en que celda de la hoja de cálculo se va 
#     a insertar el comando
#   - Se envia el comando a la hoja de cálculo
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2019_05_24
#

import gspread
import sys
import readjson
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/vagrant/%s'%(readjson.jsonKeysActual(readjson.FILENAME)), scope)

gc = gspread.authorize(credentials)
sh = gc.open_by_key(readjson.keyActual(readjson.FILENAME))
wks = sh.get_worksheet(0)
readjson.incrementarFila(readjson.FILENAME)
fila = readjson.filaActual(readjson.FILENAME)
col = readjson.colActual(readjson.FILENAME)
f = open("_lastcommand_.txt","r")
contents = f.read()
f.close()
wks.update_cell(int(fila),int(col),contents[:-1])
