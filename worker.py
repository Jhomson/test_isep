import pymysql
import socket
import os
from dotenv import load_dotenv

#socket.getaddrinfo('tommy.heliohost.org');

#Se usa la libreria dotenv para cargar variables de entorno y hacer la conexion a la base de datos, la idea de
#este propcedimiento es poder resguardar las variables importantes y en caso de subirlas a un repositorio con
#git, existe la posibilidad de que este archivo sea ignorao por seguridad configurando ./gitignore
load_dotenv()

#Se ha configurado la conexion para hacer uso de una BD local usando el programa XAMPP solo para este ejemplo.
def conectarBD():
    try:
        conexion = pymysql.connect(host=os.getenv("HOST"),user=os.getenv("USER"),password=os.getenv("PASSWORD"),db=os.getenv("DB"))
        print("Conexion exitosa!")
        return conexion
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrio un error al intentar conectar a la BD:\n\n", e)