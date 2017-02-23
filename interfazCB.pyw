#!/usr/bin/python
# -*- coding: utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import distribuidos, datetime
from pathlib import Path
from win_unc import UncDirectory, UncDirectoryConnection
def validacionArchivo(conexion,nombreArchivo):
    p = Path(conexion.get_path())
    p = p / nombreArchivo
    if p.exists():
        p.resolve()
        return str(p)
    else:
        raise Exception("El archivo {0}, no existe en la carpeta de archivos".format(nombreArchivo))
class lineaDistribuidos():
    def __init__(self):
        self.__pedido = ""
        self.__nomCliente = ""
        self.__nomEtiqueta = ""
        self.__cantMesesAnteriores = ""
        self.__valorizadaAnteriores = ""
        self.__cantDespachada = ""
        self.__valorizadaDespachada = ""

    def archivoALista(self,archivo):
        try:
            simple_unc = UncDirectory(r'\\respaldoadh\archivosventa')  # se crea ruta unc
            # Setup a connection handler:
            conn = UncDirectoryConnection(simple_unc)  # se abre la carpeta unc
            conn.connect()  # se crea conexion con la carpeta
            lecturaArchivo = open(validacionArchivo(simple_unc, archivo), "r")
            listaRegistros = list()
            for linea in lecturaArchivo:
                if linea[0:6] != "\n":
                    registro = list()
                    self.__pedido = linea[0:6]
                    registro.append(self.__pedido)
                    self.__nomCliente = linea[7:28]
                    registro.append(self.__nomCliente)
                    self.__nomEtiqueta = linea[28:54]
                    registro.append(self.__nomEtiqueta)
                    self.__cantMesesAnteriores = linea[55:65].strip()
                    registro.append(self.__cantMesesAnteriores)
                    self.__valorizadaAnteriores = linea[66:76].strip()
                    registro.append(self.__valorizadaAnteriores)
                    self.__cantDespachada = linea[99:108].strip()
                    registro.append(self.__cantDespachada)
                    self.__valorizadaDespachada = linea[109: 119].strip()
                    registro.append(self.__valorizadaDespachada)
                    listaRegistros.append(registro)
            lecturaArchivo.close()
            conn.disconnect()  # se desconecta de la carpeta
            return listaRegistros
        except Exception as e:
            raise Exception("Error al conectarse con la carpeta compartida,"
                            "\nse debe comprobar que no hay cambios de configuracion en rutas\n"
                            "   y si el usuario se encuentra conectado a la red."
                            "\nSi el problema persiste conctarse con el programador:\ns.benaventebravo@gmail.com")
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8}".format(self.__pedido,
                                                            self.__nomCliente,
                                                            self.__nomEtiqueta,
                                                            self.__cantMesesAnteriores,
                                                            self.__valorizadaAnteriores,
                                                            self.__cantDelMes,
                                                            self.__valorizadaDelMes,
                                                            self.__cantDespachada,
                                                            self.__valorizadaDespachada)
    def calcularTotal(self, listaDatos, tipo):
        listacantidades = list()
        for reg in listaDatos:
            listacantidades.append(int(reg[tipo].replace('.','')))

        return sum(listacantidades)
class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()
class vInforme1(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = distribuidos.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Adh-Informes de Despacho")
        self.diccionarioMeses = {"ENERO": '01',"FEBRERO":'02',"MARZO":'03',"ABRIL":'04',"MAYO":'05',
                                 "JUNIO":'06',"JULIO":'07',"AGOSTO":'08',"SEPTIEMBRE":'09',
                                 "OCTUBRE":'10',"NOVIEMBRE":'11',"DICIEMBRE":'12'}
        pixmap = QPixmap('./2.jpg')
        self.ui.lblLogo.setPixmap(pixmap.scaled(250,100,Qt.KeepAspectRatio))
        self.ui.lblLogo2.setPixmap(pixmap.scaled(250,100, Qt.KeepAspectRatio))
        self.cargarCmbMeses()
        self.estadocero()
        self.ui.lblFechaHoy.setText("{0}/{1}/{2}".format(datetime.date.today().day,datetime.date.today().month,
                                                         datetime.date.today().year))
        QObject.connect(self.ui.cmbMeses, SIGNAL("currentIndexChanged(int)"), self.cmbMeses_click)
    def cargarCmbMeses(self, ):
        self.ui.cmbMeses.clear()
        self.ui.cmbMeses.addItem("--Seleccione el mes que quiere consultar--")
        self.listaReferencias = list()
        referencia = datetime.date.today().month
        self.listaReferencias.append(referencia)
        for i in range(0, 3):
            referencia += 1
            if referencia > 12:
                referencia = 1
            self.listaReferencias.append(referencia)
        for i in range(len(self.listaReferencias)):
            for k, v in self.diccionarioMeses.items():
                if (int(v) == self.listaReferencias[i]):
                    self.ui.cmbMeses.addItem(k)

    def cmbMeses_click(self):
        indice = -1
        mes = self.ui.cmbMeses.currentText()
        if str(mes).find("--S") == -1:
            for k, v in self.diccionarioMeses.items():
                if k == mes:
                    indice = v
            my_array = lineaDistribuidos().archivoALista("proy"+indice+".txt")
            headerData = ["Pedido", "Nombre Cliente", "Nombre Etiqueta", "Cantidad de Productos",
                          "Valorizacion de Productos", "Cantidad Despachada", " Valorizacion de Despachos"]
            tablemodel = MyTableModel(my_array, headerData, self)
            self.ui.tableView.setModel(tablemodel)
            self.ui.tableView.setColumnWidth(0, 100)
            self.ui.tableView.setColumnWidth(1, 180)
            self.ui.tableView.setColumnWidth(2, 180)
            self.ui.tableView.setColumnWidth(3, 180)
            self.ui.tableView.setColumnWidth(4, 180)
            self.ui.tableView.setColumnWidth(5, 180)
            self.ui.tableView.setColumnWidth(6, 180)
            self.ui.tableView.setColumnWidth(7, 180)
            self.ui.tableView.setColumnWidth(8, 180)
            self.ui.lblCantProd.setText('{:,}'.format(lineaDistribuidos().calcularTotal(my_array, 3)).replace(',', '.'))
            self.ui.lblCantDesp.setText('{:,}'.format(lineaDistribuidos().calcularTotal(my_array, 5)).replace(',', '.'))
            self.ui.lblProdVal.setText('${:,}'.format(lineaDistribuidos().calcularTotal(my_array, 4)).replace(',', '.'))
            self.ui.lblDespVal.setText('${:,}'.format(lineaDistribuidos().calcularTotal(my_array, 6)).replace(',', '.'))
            self.ui.tableView.showRow(0)
        else:
            self.estadocero()

    def estadocero(self):
        my_array = [["", "", "", "", "", "", ""]]
        headerData =["Pedido", "Nombre Cliente", "Nombre Etiqueta", "Cantidad de Productos",
                          "Valorizacion de Productos", "Cantidad Despachada", " Valorizacion de Despachos"]
        tablemodel = MyTableModel(my_array, headerData, self)
        self.ui.tableView.setModel(tablemodel)
        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 180)
        self.ui.tableView.setColumnWidth(2, 180)
        self.ui.tableView.setColumnWidth(3, 180)
        self.ui.tableView.setColumnWidth(4, 180)
        self.ui.tableView.setColumnWidth(5, 180)
        self.ui.tableView.setColumnWidth(6, 180)
        self.ui.tableView.setColumnWidth(7, 180)
        self.ui.tableView.setColumnWidth(8, 180)
        self.ui.tableView.hideRow(0)
        self.ui.lblCantProd.setText('0')
        self.ui.lblCantDesp.setText('0')
        self.ui.lblProdVal.setText('$0')
        self.ui.lblDespVal.setText('$0')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = vInforme1()
    myWindow.show()
    sys.exit(app.exec_())





