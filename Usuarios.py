from Conexion import *

class CUsuarios:
    def ingresarUsuarios(nombre,correo,clave,estatus):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor() 
            sql = "insert into usuarios valus (null,%s,%s,%s,%s);"
            #La Variable Valores tiene que ser una tupla
            #Como la minima expresion es: (valos,) la coma hace que se una tupla
            # las tuplas son listas inmutables, eso quiere decir que no se pueden modificar
            
            valores = (nombre,correo,clave,estatus)
            cursor.execute(sql.valores)
            cone.commit()
            
            print(cursor.rowcount,"Registro Ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de Ingreso de datos {}".format(error))
