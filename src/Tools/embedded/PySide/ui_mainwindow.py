# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Nov 20 18:03:04 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtWidgets, QtCore, QtGui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFreeCAD = QtWidgets.QMenu(self.menubar)
        self.menuFreeCAD.setObjectName("menuFreeCAD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEmbed = QtGui.QAction(MainWindow)
        self.actionEmbed.setObjectName("actionEmbed")
        self.actionDocument = QtGui.QAction(MainWindow)
        self.actionDocument.setObjectName("actionDocument")
        self.actionCube = QtGui.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.menuFreeCAD.addAction(self.actionEmbed)
        self.menuFreeCAD.addAction(self.actionDocument)
        self.menuFreeCAD.addAction(self.actionCube)
        self.menubar.addAction(self.menuFreeCAD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate(
                "MainWindow", "MainWindow", None, QtWidgets.QApplication.UnicodeUTF8
            )
        )
        self.menuFreeCAD.setTitle(
            QtWidgets.QApplication.translate(
                "MainWindow","ARCHI", None, QtWidgets.QApplication.UnicodeUTF8
            )
        )
        self.actionEmbed.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "Embed", None, QtWidgets.QApplication.UnicodeUTF8
            )
        )
        self.actionDocument.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "Document", None, QtWidgets.QApplication.UnicodeUTF8
            )
        )
        self.actionCube.setText(
            QtWidgets.QApplication.translate("MainWindow", "Cube", None, QtWidgets.QApplication.UnicodeUTF8)
        )
