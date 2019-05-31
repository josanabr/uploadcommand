# uploadcommand

Este es un aplicativo de línea de comandos que le permite a un(a) docente subir comandos digitados por él o ella en una terminal a la plataforma *Google Sheets*.
Una mayor descripción del proyecto se puede encontrar [aquí](https://docs.google.com/document/d/1q-v9qLnUhyM52kErt4e3qfNC8YugF7mFuxcF7AjZGE0/edit?usp=sharing).

Un video describiendo el uso de la herramienta también se puede encontrar [aquí](https://youtu.be/stqd0bu2I4w).

## Modo de uso

Una vez se ha instalado adecuadamente se debe ejecutar el commando `uploadcommand`. 

### Sin argumentos

Subirá el último comando que se digitó en la terminal.

```
uploadcommand
```

### Argumento númerico

Subirá los últimos `n` comandos digitados.

```
uploadcommand 4
```

Entonces subirá los últimos n comandos digitados por el usuario en la terminal.

### Cadena de caracteres

Se subirá la cadena de caracteres pasada como argumento.

```
uploadcommand "echo 'hola mundo'"
```

Subirá el comando `echo 'hola mundo'`.

### Limpiar datos de la hoja de cálculo

Para limpiar la información en la hoja de cálculo y volver a llenarla digitar

```
uc 0
```

---

El [Dockerfile](Dockerfile) provisto permite la creación del contenedor que se usa en el aplicativo. 
Para crear este contenedor (y como se encuentra invocado dentro del script [uploadcommand.sh](uploadcommand.sh)) se ejecuta el siguiente comando:

```
docker build -t josanabr/gspread:0.0.1 .
```

