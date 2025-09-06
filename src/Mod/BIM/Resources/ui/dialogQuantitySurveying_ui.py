# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogQuantitySurveying.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QListView, QPushButton, QScrollBar, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 600)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 10, 98, 27))
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 180, 381, 121))
        self.verticalScrollBar = QScrollBar(Dialog)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(380, 180, 16, 121))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 120, 381, 51))
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 381, 51))
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 310, 361, 51))
        self.label_4.setWordWrap(True)
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 370, 121, 22))
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 390, 121, 22))
        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 410, 121, 22))
        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 430, 121, 22))
        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(10, 310, 121, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 460, 361, 51))
        self.label_5.setWordWrap(True)
        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(10, 460, 121, 22))
        self.checkBox_7 = QCheckBox(Dialog)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(10, 510, 121, 22))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 510, 361, 51))
        self.label_6.setWordWrap(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"This display lists all the components of the current document. Select them to create a FreeCAD spreadsheet containing information from them.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"This dialog window will help generate a list of components, dimensions, and materials from an opened BIM file for quantity surveyor purposes.", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Select from these options the values desired from each component. FreeCAD will generate a line in the spreadsheet with these values (if they are present).", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"object.Length", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Shape.Volume", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"object.Label", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"count", None))
        self.checkBox_5.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Select these components from the list to hide the rest of them and move to survey mode.", None))
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Select these components from the list to hide the rest of them and move to schedule definition mode.", None))
    # retranslateUi

