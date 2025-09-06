# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgExportHeaderStep.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_PartGui_DlgExportHeaderStep(object):
    def setupUi(self, PartGui__DlgExportHeaderStep):
        if not PartGui__DlgExportHeaderStep.objectName():
            PartGui__DlgExportHeaderStep.setObjectName(u"PartGui__DlgExportHeaderStep")
        PartGui__DlgExportHeaderStep.resize(445, 149)
        PartGui__DlgExportHeaderStep.setWindowTitle(u"STEP")
        self.gridLayout_4 = QGridLayout(PartGui__DlgExportHeaderStep)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBoxHeader = QGroupBox(PartGui__DlgExportHeaderStep)
        self.groupBoxHeader.setObjectName(u"groupBoxHeader")
        self.gridLayout_2 = QGridLayout(self.groupBoxHeader)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBoxHeader)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEditCompany = QLineEdit(self.groupBoxHeader)
        self.lineEditCompany.setObjectName(u"lineEditCompany")

        self.gridLayout_2.addWidget(self.lineEditCompany, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBoxHeader)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEditAuthor = QLineEdit(self.groupBoxHeader)
        self.lineEditAuthor.setObjectName(u"lineEditAuthor")

        self.gridLayout_2.addWidget(self.lineEditAuthor, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBoxHeader)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEditProduct = QLineEdit(self.groupBoxHeader)
        self.lineEditProduct.setObjectName(u"lineEditProduct")

        self.gridLayout_2.addWidget(self.lineEditProduct, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBoxHeader, 1, 0, 1, 1)

        QWidget.setTabOrder(self.lineEditCompany, self.lineEditAuthor)
        QWidget.setTabOrder(self.lineEditAuthor, self.lineEditProduct)

        self.retranslateUi(PartGui__DlgExportHeaderStep)

        QMetaObject.connectSlotsByName(PartGui__DlgExportHeaderStep)
    # setupUi

    def retranslateUi(self, PartGui__DlgExportHeaderStep):
#if QT_CONFIG(tooltip)
        self.groupBoxHeader.setToolTip(QCoreApplication.translate("PartGui::DlgExportHeaderStep", u"If not empty, field contents will be used in the STEP file header", None))
#endif // QT_CONFIG(tooltip)
        self.groupBoxHeader.setTitle(QCoreApplication.translate("PartGui::DlgExportHeaderStep", u"Header", None))
        self.label_2.setText(QCoreApplication.translate("PartGui::DlgExportHeaderStep", u"Company", None))
        self.label_3.setText(QCoreApplication.translate("PartGui::DlgExportHeaderStep", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("PartGui::DlgExportHeaderStep", u"Product", None))
        pass
    # retranslateUi

