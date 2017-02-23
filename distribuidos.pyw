# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distribuidos.ui'
#
# Created: Thu Feb 23 14:21:52 2017
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
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.lblFechaHoy = QtGui.QLabel(self.centralwidget)
        self.lblFechaHoy.setObjectName(_fromUtf8("lblFechaHoy"))
        self.gridLayout_2.addWidget(self.lblFechaHoy, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(78, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lblLogo = QtGui.QLabel(self.centralwidget)
        self.lblLogo.setObjectName(_fromUtf8("lblLogo"))
        self.gridLayout_5.addWidget(self.lblLogo, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 1, 1, 1)
        self.lblLogo2 = QtGui.QLabel(self.centralwidget)
        self.lblLogo2.setObjectName(_fromUtf8("lblLogo2"))
        self.gridLayout_4.addWidget(self.lblLogo2, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 3, 1, 1)
        self.cmbMeses = QtGui.QComboBox(self.centralwidget)
        self.cmbMeses.setObjectName(_fromUtf8("cmbMeses"))
        self.gridLayout_3.addWidget(self.cmbMeses, 1, 1, 1, 2)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_3.addWidget(self.tableView, 2, 0, 1, 4)
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
        spacerItem7 = QtGui.QSpacerItem(195, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 2, 1, 1)
        self.lblProdValstr = QtGui.QLabel(self.groupBox)
        self.lblProdValstr.setObjectName(_fromUtf8("lblProdValstr"))
        self.gridLayout.addWidget(self.lblProdValstr, 0, 3, 1, 1)
        self.lblProdVal = QtGui.QLabel(self.groupBox)
        self.lblProdVal.setObjectName(_fromUtf8("lblProdVal"))
        self.gridLayout.addWidget(self.lblProdVal, 0, 4, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(194, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 5, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(195, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 2, 2, 1)
        spacerItem10 = QtGui.QSpacerItem(194, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 1, 5, 2, 1)
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
        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 4)
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
        self.lblLogo.setText(_translate("MainWindow", "TextLabel", None))
        self.lblLogo2.setText(_translate("MainWindow", "TextLabel", None))
        self.groupBox.setTitle(_translate("MainWindow", "Totales", None))
        self.label.setText(_translate("MainWindow", "Cantidad de Productos:", None))
        self.lblCantProd.setText(_translate("MainWindow", "TextLabel", None))
        self.lblProdValstr.setText(_translate("MainWindow", "Productos Valorizados:", None))
        self.lblProdVal.setText(_translate("MainWindow", "TextLabel", None))
        self.label_5.setText(_translate("MainWindow", "Cantidad de Despachos:", None))
        self.lblCantDesp.setText(_translate("MainWindow", "TextLabel", None))
        self.label_7.setText(_translate("MainWindow", "Despachos Valorizados:", None))
        self.lblDespVal.setText(_translate("MainWindow", "TextLabel", None))

