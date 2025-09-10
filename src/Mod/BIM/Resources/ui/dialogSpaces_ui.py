# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogSpaces.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 641)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.treeWidget = QTreeWidget(Dialog)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setDefaultSectionSize(120)
        self.treeWidget.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.treeWidget)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_15, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_16, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.spinBox, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)

        self.colorButton = Gui_ColorButton(self.groupBox)
        self.colorButton.setObjectName(u"colorButton")

        self.gridLayout.addWidget(self.colorButton, 3, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.spinBox_2, 6, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Spaces manager", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"This screen will allow you to check the spaces configuration of your project and change some attributes.", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Dialog", u"Area", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Dialog", u"Color", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"Space", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Total", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Occupants", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"1.00 m\u00b2", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Electric consumption", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"0 W", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Space information", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Color", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Occupants", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"1.00 m\u00b2", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Label", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Electric consumption", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Level", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Level name", None))
        self.spinBox_2.setSuffix(QCoreApplication.translate("Dialog", u" W", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Use", None))
    # retranslateUi

