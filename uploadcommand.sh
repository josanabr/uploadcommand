uploadLastCommand() {
  echo ${1} > _lastcommand_.txt
  echo "uploading '${1}'"
  docker run --rm -v ${HOME}/.uploadcommand:/vagrant -v $(pwd):/workdir -w /workdir josanabr/gspread:0.0.1 python uploadcommand.py 
  if [ $? -ne 0 ]; then
    echo "Error uploading ${1}"
  fi 
}

CURRENTDIR=$(pwd)
cd ${HOME}/bin
if [ ! "${1}" == "" ]; then
# No se digito una cada vacia
  re='^[0-9]+$'
  if  [[ ${1} =~ ${re} ]]; then
  # Es un valor numerico. Se desea enviar los ultimos comandos
    n=${1}
    n=$(( n + 1 ))
    while [ ${n} -gt 1 ]; do
      lastCommand=$(fc -ln -${n} | head -n 1 |  awk '$1=$1')
      uploadLastCommand "${lastCommand}"
      n=$(( n - 1 ))
    done
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
