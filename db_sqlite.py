import sqlite3



class Db_SQLITE:

    #__path = "C:\trabajo\python\lista_aplicaciones\datos\aplicaciones.db"
    __path = ".\\datos\\cuentas.db"
    __BASE_DATOS = "cuentas.db"
    
    
    def __init__(self):
        self.instancia = {
            'database': Db_SQLITE.__BASE_DATOS
        }    

    def __enter__(self):
        self.conexion = sqlite3.connect("C:\\Users\\diego\\trabajo\\python\\cuentas\\cuentas\\datos\\cuentas.bd")
        self.cursor = self.conexion.cursor()
        return self.cursor

    def __exit__(self, tipoError, valorError, trazaError):
        if tipoError:
            self.conexion.rollback()
            print('Ha ocurrido un error y se ha revertido la transacción: (1) {tipoError} (2) {valorError}')
        else: 
            self.conexion.commit()
            self.cursor.close()
            self.conexion.close()


        #cursor = conexion.execute("SELECT DATE('now')")
        #cursor = conexion.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        #for fila in cursor:
        #print(fila)
        #conexion.close()
    
    

    