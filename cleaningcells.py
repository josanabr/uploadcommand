#!/usr/bin/env python
#
# Este script en Python se encarga de limpiar las celdas de la primera 
# columna de la hoja de calculo. Ademas se encarga de reinicar el valor de la
# fila del archivo de configuracion 
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2019_05_31
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
# se traen las celdas
cell_list = wks.range('A1:A50')
print("Warning! se borran el rango de celdas A1:A50")
# se limpian las celdas
for cell in cell_list:
  cell.value = ''
wks.update_cells(cell_list)
wks.update_acell('A1','Comandos')
# reinicia el contador de las filas en la hoja de calculo
readjson.inicializarFila(readjson.FILENAME)
