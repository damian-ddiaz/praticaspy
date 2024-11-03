#pip install mysql-connector-python mm
import mysql.connector

class CConexion:
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',password='Gemelas2000#',
                                               host='127.0.0.1',database='dbsaemp',port='3306')
            
            print("Conexion Correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Error al Conectarse a la bas de Datos {}".format(error))
            
    ConexionBaseDeDatos()