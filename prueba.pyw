from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
class lineaDistribuidos():
    def __init__(self):
        self.__pedido = ""
        self.__nomCliente = ""
        self.__nomEtiqueta = ""
        self.__cantMesesAnteriores = ""
        self.__valorizadaAnteriores = ""
        self.__cantDelMes = ""
        self.__valorizadaDelMes = ""
        self.__cantDespachada = ""
        self.__valorizafaDespachada = ""

    def archivoALista(self):
        listaRegistros = list()
        archivo = open("proy02.txt", "r")
        for linea in archivo:
            registro = list()
            self.__pedido = linea[0:6]
            registro.append(self.__pedido)
            self.__nomCliente = linea[7:28]
            registro.append(self.__nomCliente)
            self.__nomEtiqueta = linea[29:54]
            registro.append(self.__nomEtiqueta)
            self.__cantMesesAnteriores = linea[55:65]
            registro.append(self.__cantMesesAnteriores)
            self.__valorizadaAnteriores = linea[66:76]
            registro.append(self.__valorizadaAnteriores)
            self.__cantDelMes = linea[77:87]
            registro.append(self.__cantDelMes)
            self.__valorizadaDelMes = linea[88:98]
            registro.append(self.__valorizadaDelMes)
            self.__cantDespachada = linea[99:108]
            registro.append(self.__cantDespachada)
            self.__valorizafaDespachada = linea[109: 119]
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
my_array = lineaDistribuidos().archivoALista()

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        tablemodel = MyTableModel(my_array, ["Pedido","Nombre Cliente","Cantidad Meses Anteriores","Valorizacion de Meses Anteriores","Cantidad Despachada"," Valorizacion de Despachos"], self)
        tableview = QTableView()
        tableview.setModel(tablemodel)

        layout = QVBoxLayout(self)
        layout.addWidget(tableview)
        self.setLayout(layout)

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

if __name__ == "__main__":
    main()