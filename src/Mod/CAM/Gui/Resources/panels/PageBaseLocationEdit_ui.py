# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageBaseLocationEdit.ui'
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
        Form.resize(415, 430)
        Form.setWindowTitle(u"Form")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.baseList = QTableWidget(Form)
        if (self.baseList.columnCount() < 2):
            self.baseList.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.baseList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.baseList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.baseList.setObjectName(u"baseList")

        self.verticalLayout_2.addWidget(self.baseList)

        self.addRemoveEdit = QWidget(Form)
        self.addRemoveEdit.setObjectName(u"addRemoveEdit")
        self.gridLayout = QGridLayout(self.addRemoveEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.addLocation = QPushButton(self.addRemoveEdit)
        self.addLocation.setObjectName(u"addLocation")

        self.gridLayout.addWidget(self.addLocation, 0, 1, 1, 1)

        self.removeLocation = QPushButton(self.addRemoveEdit)
        self.removeLocation.setObjectName(u"removeLocation")

        self.gridLayout.addWidget(self.removeLocation, 0, 2, 1, 1)

        self.editLocation = QPushButton(self.addRemoveEdit)
        self.editLocation.setObjectName(u"editLocation")

        self.gridLayout.addWidget(self.editLocation, 0, 3, 1, 1)

        self.label = QLabel(self.addRemoveEdit)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 3)


        self.verticalLayout_2.addWidget(self.addRemoveEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        ___qtablewidgetitem = self.baseList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"X", None));
        ___qtablewidgetitem1 = self.baseList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Y", None));
#if QT_CONFIG(tooltip)
        self.baseList.setToolTip(QCoreApplication.translate("Form", u"List of locations to be processed", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addLocation.setToolTip(QCoreApplication.translate("Form", u"Opens a dialog to add arbitrary locations", None))
#endif // QT_CONFIG(tooltip)
        self.addLocation.setText(QCoreApplication.translate("Form", u"Add", None))
#if QT_CONFIG(tooltip)
        self.removeLocation.setToolTip(QCoreApplication.translate("Form", u"Remove selected location from the list. The operation is no longer applied to them.", None))
#endif // QT_CONFIG(tooltip)
        self.removeLocation.setText(QCoreApplication.translate("Form", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.editLocation.setToolTip(QCoreApplication.translate("Form", u"Edit selected location", None))
#endif // QT_CONFIG(tooltip)
        self.editLocation.setText(QCoreApplication.translate("Form", u"Edit", None))
        self.label.setText(QCoreApplication.translate("Form", u"All locations will be processed using the same operation properties", None))
        pass
    # retranslateUi

