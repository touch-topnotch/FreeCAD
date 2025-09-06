# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageBaseHoleGeometryEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(415, 573)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.baseList = QTableWidget(Form)
        if (self.baseList.columnCount() < 2):
            self.baseList.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.baseList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.baseList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.baseList.setObjectName(u"baseList")
        self.baseList.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.baseList, 0, 0, 1, 3)

        self.addBase = QPushButton(Form)
        self.addBase.setObjectName(u"addBase")

        self.gridLayout.addWidget(self.addBase, 1, 0, 1, 1)

        self.deleteBase = QPushButton(Form)
        self.deleteBase.setObjectName(u"deleteBase")

        self.gridLayout.addWidget(self.deleteBase, 1, 1, 1, 1)

        self.resetBase = QPushButton(Form)
        self.resetBase.setObjectName(u"resetBase")

        self.gridLayout.addWidget(self.resetBase, 1, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.baseList, self.addBase)
        QWidget.setTabOrder(self.addBase, self.deleteBase)
        QWidget.setTabOrder(self.deleteBase, self.resetBase)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        ___qtablewidgetitem = self.baseList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Feature", None));
        ___qtablewidgetitem1 = self.baseList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Diameter", None));
#if QT_CONFIG(tooltip)
        self.baseList.setToolTip(QCoreApplication.translate("Form", u"Table of hole features and the determined radius of the associated hole.\n"
"\n"
"Add features for processing by selecting them and then pressing 'Add'. If a feature is accidentally added to the list, it can be removed through 'Remove' and will no longer be processed.\n"
"\n"
"Reset deletes all current items from the list and fills the list with all circular holes eligible for the operation from the model. Refine the list afterwards by enabling/disabling, removing and adding features.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addBase.setToolTip(QCoreApplication.translate("Form", u"Add selected items from 3D view to the list of base geometries", None))
#endif // QT_CONFIG(tooltip)
        self.addBase.setText(QCoreApplication.translate("Form", u"Add", None))
#if QT_CONFIG(tooltip)
        self.deleteBase.setToolTip(QCoreApplication.translate("Form", u"Remove selected list items from the list of base geometries. The operation is no longer applied to them.", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBase.setText(QCoreApplication.translate("Form", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.resetBase.setToolTip(QCoreApplication.translate("Form", u"Remove all list items and fill list with all eligible features from the job's base object.", None))
#endif // QT_CONFIG(tooltip)
        self.resetBase.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.label.setText(QCoreApplication.translate("Form", u"All objects will be processed using the same operation properties.", None))
        pass
    # retranslateUi

