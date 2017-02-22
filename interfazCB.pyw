#!/usr/bin/python
# -*- coding: utf8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import distribuidos, datetime
from pathlib import Path
from operator import attrgetter
from win_unc import UncDirectory, UncDirectoryConnection
import os
import winshell
class lineaDistribuidos():
    def __init__(self):
        self.__pedido = ""
        self.__nomCliente = ""
        self.__nomEtiqueta = ""
        self.__cantMesesAnteriores = ""
        self.__valorizadaAnteriores = ""
        self.__cantDespachada = ""
        self.__valorizafaDespachada = ""

    def archivoALista(self):
        listaRegistros = list()
        archivo = open("proy02.txt", "r")
        for linea in archivo:
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
                self.__valorizafaDespachada = linea[109: 119].strip()
                registro.append(self.__valorizafaDespachada)
                listaRegistros.append(registro)
        archivo.close()
        return listaRegistros
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8}".format(self.__pedido,
                                                            self.__nomCliente,
                                                            self.__nomEtiqueta,
                                                            self.__cantMesesAnteriores,
                                                            self.__valorizadaAnteriores,
                                                            self.__cantDelMes,
                                                            self.__valorizadaDelMes,
                                                            self.__cantDespachada,
                                                            self.__valorizafaDespachada)

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

"Generar Libreria de funciones "

class vInforme1(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = distribuidos.Ui_MainWindow()
        self.ui.setupUi(self)
        my_array = lineaDistribuidos().archivoALista()
        headerData = ["Pedido","Nombre Cliente","Nombre Etiqueta","Cantidad Meses Anteriores","Valorizacion de Meses Anteriores","Cantidad Despachada"," Valorizacion de Despachos"]
        tablemodel = MyTableModel(my_array, headerData, self)
        self.ui.tableView.setModel(tablemodel)
        self.ui.tableView.setColumnWidth(0, 200)
        self.ui.tableView.setColumnWidth(1, 200)
        self.ui.tableView.setColumnWidth(2, 200)
        self.ui.tableView.setColumnWidth(3, 200)
        self.ui.tableView.setColumnWidth(4, 200)
        self.ui.tableView.setColumnWidth(5, 200)
        self.ui.tableView.setColumnWidth(6, 200)
        self.ui.tableView.setColumnWidth(7, 200)
        self.ui.tableView.setColumnWidth(8, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = vInforme1()
    myWindow.show()
    sys.exit(app.exec_())