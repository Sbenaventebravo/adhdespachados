# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distribuidos.ui'
#
# Created: Thu Feb 23 12:53:24 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(784, 401)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lblFechaHoy = QtGui.QLabel(self.centralwidget)
        self.lblFechaHoy.setObjectName(_fromUtf8("lblFechaHoy"))
        self.horizontalLayout_2.addWidget(self.lblFechaHoy)
        spacerItem = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(377, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 2, 0, 1, 4)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lblCantProd = QtGui.QLabel(self.groupBox)
        self.lblCantProd.setObjectName(_fromUtf8("lblCantProd"))
        self.gridLayout.addWidget(self.lblCantProd, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(195, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        self.lblProdValstr = QtGui.QLabel(self.groupBox)
        self.lblProdValstr.setObjectName(_fromUtf8("lblProdValstr"))
        self.gridLayout.addWidget(self.lblProdValstr, 0, 3, 1, 1)
        self.lblProdVal = QtGui.QLabel(self.groupBox)
        self.lblProdVal.setObjectName(_fromUtf8("lblProdVal"))
        self.gridLayout.addWidget(self.lblProdVal, 0, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(194, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(195, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 2, 1)
        spacerItem5 = QtGui.QSpacerItem(194, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 5, 2, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lblCantDesp = QtGui.QLabel(self.groupBox)
        self.lblCantDesp.setObjectName(_fromUtf8("lblCantDesp"))
        self.gridLayout.addWidget(self.lblCantDesp, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)
        self.lblDespVal = QtGui.QLabel(self.groupBox)
        self.lblDespVal.setObjectName(_fromUtf8("lblDespVal"))
        self.gridLayout.addWidget(self.lblDespVal, 2, 4, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.cmbMeses = QtGui.QComboBox(self.centralwidget)
        self.cmbMeses.setObjectName(_fromUtf8("cmbMeses"))
        self.gridLayout_2.addWidget(self.cmbMeses, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_6.setText(_translate("MainWindow", "Fecha Actual:", None))
        self.lblFechaHoy.setText(_translate("MainWindow", "TextLabel", None))
        self.groupBox.setTitle(_translate("MainWindow", "Totales", None))
        self.label.setText(_translate("MainWindow", "Cantidad de Productos:", None))
        self.lblCantProd.setText(_translate("MainWindow", "TextLabel", None))
        self.lblProdValstr.setText(_translate("MainWindow", "Productos Valorizados:", None))
        self.lblProdVal.setText(_translate("MainWindow", "TextLabel", None))
        self.label_5.setText(_translate("MainWindow", "Cantidad de Despachos:", None))
        self.lblCantDesp.setText(_translate("MainWindow", "TextLabel", None))
        self.label_7.setText(_translate("MainWindow", "Despachos Valorizados:", None))
        self.lblDespVal.setText(_translate("MainWindow", "TextLabel", None))

