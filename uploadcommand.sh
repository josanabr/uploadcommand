# Este script en bash se encarga de subir uno o varios comandos que se 
# encuentran en la historia de ejecucion del usuario.
# 
# Autor: John Sanabria
# Fecha: 2019_05_24
# Modificado: 
# - 2019_05_31: se adiciona la funcion de borrar el contenido de la hoja de 
#               calculo.
# 
#
# Esta funcion se encarga de subir UN COMANDO que se encuentra en un archivo de
# texto a la hoja de calculo.
#
uploadLastCommand() {
  echo ${1} > _lastcommand_.txt
  echo "uploading '${1}'"
  docker run --rm -v ${HOME}/.uploadcommand:/vagrant -v $(pwd):/workdir -w /workdir josanabr/gspread:0.0.1 python uploadcommand.py 
  if [ $? -ne 0 ]; then
    echo "Error uploading ${1}"
  fi 
}

#
# Esta  funcion se encarga de borrar "todas" las celdas de la primera columna 
# de la hoja de calculo
#
cleanCells() {
  echo "cleaning cells"
  docker run --rm -v ${HOME}/.uploadcommand:/vagrant -v $(pwd):/workdir -w /workdir josanabr/gspread:0.0.1 python cleaningcells.py 
  if [ $? -ne 0 ]; then
    echo "Error cleaning cells"
  fi
}

# Se ubica en el directorio donde estan los scripts en Python de la aplicacion
CURRENTDIR=$(pwd)
cd ${HOME}/bin
if [ ! "${1}" == "" ]; then
# Se paso un argumento
  re='^[0-9]+$'
  if  [[ ${1} =~ ${re} ]]; then
  # Es un valor numerico. Se desea enviar los ultimos comandos
    if [ ${1} -eq 0 ]; then
    # Se desea limpiar las celdas donde se almacenan los comandos
      cleanCells
    else
    # Se itera sobre todos los 'n' comandos anteriores
      n=${1}
      n=$(( n + 1 ))
      while [ ${n} -gt 1 ]; do
        lastCommand=$(fc -ln -${n} | head -n 1 |  awk '$1=$1')
        uploadLastCommand "${lastCommand}"
        n=$(( n - 1 ))
      done
    fi
  else 
  # No es un valor numerico, es un comando per-se
    uploadLastCommand "${1}"
  fi 
else
# No se le paso argumentos al script. Es efectivamente el ultimo comando
  lastCommand=$(fc -ln -2 | head -n 1 | awk '$1=$1')
  uploadLastCommand "${lastCommand}"
fi
rm -f _lastcommand_.txt
cd ${CURRENTDIR}
