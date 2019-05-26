lastCommand=$(fc -ln -2 | head -n 1 | awk '$1=$1')
if [ ! "${1}" == "" ]; then
  lastCommand="${1}"
fi
CURRENTDIR=$(pwd)
cd ${HOME}/bin
echo ${lastCommand} > _lastcommand_.txt
docker run --rm -v ${HOME}/.uploadcommand:/vagrant -v $(pwd):/workdir -w /workdir josanabr/gspread:0.0.1 python uploadcommand.py 
rm _lastcommand_.txt
cd ${CURRENTDIR}
