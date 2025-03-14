from PyQt6 import QtCore, QtGui, uic, QtWidgets
from db_sqlite import Db_SQLITE

from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem



class bd:
    sql = 'select id,cuenta from t_cuentas where id_padre is null order by cuenta'

    def ejecuta():
        
        try:
            with Db_SQLITE() as cursor:
                cursor.execute(bd.sql)
                resultados = cursor.fetchall()
                return resultados
                #for resultado in resultados: print(list(resultado)[0])
        except Exception as error: print(f'Ha ocurrido un error: (1) {type(error)} (2) {error}')

    

    def refresca(tb_datos,datos):
        tb_datos.setHeaderLabels(['Cuentas'])
        tb_datos.setColumnCount(1)
        tb_datos.resizeColumnToContents(0)
        

        level = 0
        for registro in datos:
            uno = QTreeWidgetItem(tb_datos)
            uno.setText(0,str(registro[0])+".- "+str(registro[1]))
#            uno.setText(1,str(registro[1]))
            #uno.isExpanded(True)
            tb_datos.insertTopLevelItem(level,uno)
            
            bd.tienehijos(tb_datos,level,uno,str(registro[0]))

    def tienehijos(tb_datos,level,uno,id):
        bd.sql = 'select id,cuenta from t_cuentas where id_padre='+ id + ' order by cuenta'
        datos = bd.ejecuta()
        level =+ 1
        for registro in datos:
            dos = QTreeWidgetItem(uno)
            dos.setText(0,str(registro[0])+".- "+str(registro[1]))
            #dos.setText(1,str(registro[1]))
            
            uno.addChild(dos)
            bd.tienehijos(tb_datos,level,dos,str(registro[0]))
        


     
        

            
            
        
        
        





    def ordena():
        bd.__sql = bd.__sql + " order by id_tipo"
        bd.inicio()
