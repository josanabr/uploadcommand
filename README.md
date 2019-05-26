# uploadcommand

Este es un aplicativo de línea de comandos que le permite a un(a) docente subir comandos digitados por él o ella en una terminal a la plataforma *Google Sheets*.
Una mayor descripción del proyecto se puede encontrar [aquí](https://docs.google.com/document/d/1q-v9qLnUhyM52kErt4e3qfNC8YugF7mFuxcF7AjZGE0/edit?usp=sharing).

Un video describiendo el uso de la herramienta también se puede encontrar [aquí](https://youtu.be/stqd0bu2I4w).

---

El [Dockerfile](Dockerfile) provisto permite la creación del contenedor que se usa en el aplicativo. 
Para crear este contenedor (y como se encuentra invocado dentro del script [uploadcommand.sh](uploadcommand.sh)) se ejecuta el siguiente comando:

```
docker build -t josanabr/gspread:0.0.1 .
```

