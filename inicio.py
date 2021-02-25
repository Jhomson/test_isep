import worker
import funciones

#Test #2, Jhomson arcas
#El siguiente brinda al Usuario un simple menu de opciones que le permiten hacer un CRUD sobre los datos
#de los Leads que se vayan registrando en el mismo, las opciones disponibles son las de consultar, registrar
#editar y eliminar Leads en esta pequeña app, tal como se pidio, se busca que los valores del Lead sean
#devueltos en forma de objeto, se busca crear una conexion a BD con un archivo .env y se busca hacer uso
#de git para hacer una copia en un repositorio github de los archivos del proyecto.

#Para eso, el ejercicio se compone de 4 archivos:
#1-inicio.py-> Para dar inicio al menu de opciones que se le presenta al Usuario.
#2-funciones.py-> Todas las funciones necesarias para hacer el CRUD con los Leads.
#3-worker.py-> Contiene las instrucciones para realizar la conexion a la BD usando el archivo .env
#4-objetos.py-> Contiene los obejtos que poseen los atributos que vas a ser insertados y devueltos por las
               #funciones de la app.

def menu():
    try:
        numero = int(input("Por favor, seleccione una opcion:\n"+
                           "1-Consultar Leads\n"+
                           "2-Registrar nuevo Lead\n"+
                           "3-Editar Lead\n"+
                           "4-Eliminar Lead\n\n"))

        #Se hace la evaluacion de la opcion seleccionada
        #Se inicia una conexion a la BD en caso de ser valida la opcion indicada por el Usuario.
        if numero == 1:
            conexion = worker.conectarBD()
            funciones.consultar_lead(conexion)

        if numero == 3:
            conexion = worker.conectarBD()
            funciones.editar_lead(conexion)

        if numero == 2:
            conexion = worker.conectarBD()
            funciones.registrar_lead(conexion)

        if numero == 4:
            conexion = worker.conectarBD()
            funciones.eliminar_lead(conexion)

    except:
        print("Introduzca una opcion valida.")
    #Esta clausula except se declara en caso de que no se indique una opcion valida
    

def ejercicio_A():

    menu()
           
if __name__ == "__main__":

    ejercicio_A()

#Para guardar este directorio de archivos en github se hace uso de git, primero para conectarse y luego sincronizar con los
#comandos init, add, status y push, entre otros.
#Una vez sincronizados los archivos, se crea una imagen o copia de los mismos en la nube, lo que permite
#Visualizarlos y obetenrlos con mucha facilidad gracias a esta poderosa herramienta como es git y github. 