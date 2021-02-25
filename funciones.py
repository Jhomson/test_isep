import pymysql
from objetos import lead

#Aca se muestran todas las funciones que hacen posible el CRUD en el app, en algunos casos se tuvo que usar 
#dos cursores para poder hacer consultas multiples o anidadas, ya que como la base d edatos tiene relacionada
#tablas entre si, entonces se debe hacer relacion entre la primary y la foreing key para tener un buen orden
#en el sistema.

#Se puede observar en la instruccion import que se importa el objeto lead del modulo o archivo objetos, esto
#se hace para garantizar que los resultados que cada funcion devuelvan pertenezcan a los atributos del objeto
#lead.

#En caso de las consultas UPDATE, DELETE, O INSERT por lo general se usa la instruccion commit, con esta se
#garantiza el correcto funcionamiento del app ya que se asegura que se ejecute la consulta antes de cerrar la
#conexion con la instriccion close.

def registrar_lead(conexion):
    try:
        with conexion.cursor() as cursor:
            lead.nom = input('Indique nombre del Lead:\n')
            lead.ape = input('Indique apellido del Lead:\n')
            lead.tel = input('Indique numero telefonico del Lead:\n')
            lead.email = input('Indique e-mail del Lead:\n')
            lead.eqventas = input('Indique el equipo de ventas asignado al Lead (si posee):\n')
            lead.notas = input('Algunas notas adicionales del Lead:\n')
            lead.producto = input('Indique el producto consultado por el Lead:\n')
            lead.user = input('Indique el usuario asignado al Lead:\n')

            insertquery = "INSERT INTO data_lead(NOM, APE, TEL, EMAIL) VALUES (%s, %s, %s, %s);"
            insertqueryb = "INSERT INTO isep_data(EQVENTAS, NOTAS, CONSULTAS, USER) VALUES (%s, %s, %s, %s);"

            cursor.execute(insertquery, (lead.nom, lead.ape, lead.tel, lead.email))
            cursor.execute(insertqueryb, (lead.eqventas, lead.notas, lead.producto, lead.user))
            print('Registro realizado con exito.')
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error al insertar la data del nuevo Lead.\n", e)
    finally:
        conexion.close()

def consultar_lead(conexion):
    try:
        cursor = conexion.cursor()
        cursorb = conexion.cursor()

        readquery = "SELECT ID, NOM, APE, TEL, EMAIL FROM data_lead;"

        cursor.execute(readquery)
            
        #leads = cursor.fetchall()

        #Recorrer e imprimir, siempre debemos selecionar todos los campos para evitar errores
        #en la seleccion de datos, por ejemplo, si ignoro el campo ID, el programa generara un error.
        #La instruccion fetchall es para obtener todas las filas de la consulta, pero no es algo
        #muy util si se quiere que el resultado se devuelva como un objeto.
        for (ID, NOM, APE, TEL, EMAIL) in cursor:

            #Se asignasn los primeros valores al objeto
            lead.nom = NOM
            lead.ape = APE
            lead.tel = TEL
            lead.email = EMAIL

            readqueryb = "SELECT EQVENTAS, NOTAS, CONSULTAS, USER FROM isep_data WHERE ID = %s;"
            cursorb.execute(readqueryb, (ID))

            for (EQVENTAS, NOTAS, CONSULTAS, USER) in cursorb:

                #Se asignan los valores restantes al objeto
                lead.eqventas = EQVENTAS
                lead.notas = NOTAS
                lead.producto = CONSULTAS
                lead.user = USER
                
            print('Nombre: ', lead.nom)
            print('Apellido: ', lead.ape)
            print('Telefono: ', lead.tel)
            print('E-mail: ', lead.email)
            print('Equipo de ventas: ', lead.eqventas)
            print('Notas adicionales: ', lead.notas)
            print('Producto: ', lead.producto)
            print('Usuario asignado: ', lead.user+'\n\n')

        print('Consulta realizada con exito.')
            
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error al consultar la data de los Lead.\n", e)
    finally:
        conexion.close()

def editar_lead(conexion):
    try:
        with conexion.cursor() as cursor:

            readquery = "SELECT ID, NOM, APE, TEL, EMAIL FROM data_lead;"

            cursor.execute(readquery)
            
            leads = cursor.fetchall()

            #Recorrer e imprimir
            for lead in leads:
                print(lead)
            valor = ''#Nuevo valor que reemplazara al anterior en la BD.
            updatequery = ''#Query que hara update de la informacion segun la opcion seleccionada.

            cual = int(input('Indique el ID del Lead que desea editar:\n'))

            numero = int(input('\n Por favor indique el valor que desea editar:\n'+
                    '1-Nombre\n'+
                    '2-Apellido\n'+
                    '3-Telefono\n'+
                    '4-Email\n'+
                    '5-Equipo de ventas\n'+
                    '6-Notas adicionales\n'+
                    '7-Solicitud de nuevo producto\n'+
                    '8-Usuario asignado\n\n'))

            #Se hace la evaluacion de la opcion seleccionada
            if numero == 1:
                valor = input('Indique el nuevo nombre:\n')
                updatequery = "UPDATE data_lead SET NOM = %s WHERE ID = %s;"
            if numero == 2:
                valor = input('Indique el nuevo apellido:\n')
                updatequery = "UPDATE data_lead SET APE = %s WHERE ID = %s;"
            if numero == 3:
                valor = input('Indique el nuevo numero de telefono:\n')
                updatequery = "UPDATE data_lead SET TEL = %s WHERE ID = %s;"
            if numero == 4:
                valor = input('Indique el nuevo e-mail:\n')
                updatequery = "UPDATE data_lead SET EMAIL = %s WHERE ID = %s;"
            if numero == 5:
                valor = input('Indique el nuevo equipo de ventas asignado:\n')
                updatequery = "UPDATE isep_data SET EQVENTAS = %s WHERE ID = %s;"
            if numero == 6:
                valor = input('Indique las nuevas notas adicionales:\n')
                updatequery = "UPDATE isep_data SET NOTAS = %s WHERE ID = %s;"
            if numero == 7:
                valor = input('Indique el nuevo producto solicitado:\n')
                updatequery = "UPDATE isep_data SET CONSULTAS = %s WHERE ID = %s;"
            if numero == 8:
                valor = input('Indique el nuevo Usuario asignado para seguimiento:\n')
                updatequery = "UPDATE isep_data SET USER = %s WHERE ID = %s;"

            cursor.execute(updatequery, (valor, cual))
            print('¡Actualizacion realizada con exito!')
        #Recuerde siempre hacer commit para efectuar cambios en la BD.
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error al insertar la data del nuevo Lead.\n", e)
    finally:
        conexion.close()

def eliminar_lead(conexion):
    try:
        with conexion.cursor() as cursor:

            readquery = "SELECT ID, NOM, APE, TEL, EMAIL FROM data_lead;"

            cursor.execute(readquery)
            
            #Recorrer e imprimir
            for (ID, NOM, APE, TEL, EMAIL) in cursor:

                lead.id = ID
                lead.nom = NOM
                lead.ape = APE
                lead.tel = TEL
                lead.email = EMAIL
                print('ID: ', lead.id)
                print('Nombre: ', lead.nom)
                print('Apellido: ', lead.ape)
                print('Telefono: ', lead.tel)
                print('E-mail: ', lead.email+'\n\n')

            cual = int(input('Indique el ID del Lead que desea eliminar:\n'))

            deletequery = "DELETE FROM data_lead WHERE ID = %s;"
            deletequeryb = "DELETE FROM isep_data WHERE ID = %s;"

            cursor.execute(deletequery, (cual))
            cursor.execute(deletequeryb, (cual))

            print('Consulta realizada con exito.')
        
        conexion.commit()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error al insertar la data del nuevo Lead.\n", e)
    finally:
        conexion.close()