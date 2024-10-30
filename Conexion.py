#pip install mysql-connector-python mm
import mysql.connector

class Cconexion:
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user=' ',password='',host='',database='',port='')
            
        except mysql.connector.Error as error:
            print("Error al Conectarse a la bas de Datos {}".format(error))