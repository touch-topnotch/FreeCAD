# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgInspectAppearance.ui'
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
    QLineEdit, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MatGui_DlgInspectAppearance(object):
    def setupUi(self, MatGui__DlgInspectAppearance):
        if not MatGui__DlgInspectAppearance.objectName():
            MatGui__DlgInspectAppearance.setObjectName(u"MatGui__DlgInspectAppearance")
        MatGui__DlgInspectAppearance.resize(739, 1556)
        self.verticalLayout = QVBoxLayout(MatGui__DlgInspectAppearance)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(MatGui__DlgInspectAppearance)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 711, 1528))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editObjectName = QLineEdit(self.groupBox)
        self.editObjectName.setObjectName(u"editObjectName")

        self.gridLayout.addWidget(self.editObjectName, 1, 2, 1, 1)

        self.editObjectLabel = QLineEdit(self.groupBox)
        self.editObjectLabel.setObjectName(u"editObjectLabel")

        self.gridLayout.addWidget(self.editObjectLabel, 1, 1, 1, 1)

        self.editSubShape = QLineEdit(self.groupBox)
        self.editSubShape.setObjectName(u"editSubShape")

        self.gridLayout.addWidget(self.editSubShape, 2, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.editDocument = QLineEdit(self.groupBox)
        self.editDocument.setObjectName(u"editDocument")

        self.gridLayout.addWidget(self.editDocument, 0, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.editSubShapeType = QLineEdit(self.groupBox)
        self.editSubShapeType.setObjectName(u"editSubShapeType")

        self.gridLayout.addWidget(self.editSubShapeType, 2, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.editShapeType = QLineEdit(self.groupBox)
        self.editShapeType.setObjectName(u"editShapeType")

        self.gridLayout.addWidget(self.editShapeType, 3, 1, 1, 2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabAppearance = QTabWidget(self.groupBox_2)
        self.tabAppearance.setObjectName(u"tabAppearance")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabAppearance.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabAppearance.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabAppearance)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(MatGui__DlgInspectAppearance)

        QMetaObject.connectSlotsByName(MatGui__DlgInspectAppearance)
    # setupUi

    def retranslateUi(self, MatGui__DlgInspectAppearance):
        MatGui__DlgInspectAppearance.setWindowTitle(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Document", None))
        self.label.setText(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Document name", None))
#if QT_CONFIG(tooltip)
        self.editDocument.setToolTip(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Name of the active document", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Label / internal name", None))
        self.label_3.setText(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Sub.Shape / Type", None))
        self.label_4.setText(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Shape.TypeID / TypeID", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Appearance", None))
        self.tabAppearance.setTabText(self.tabAppearance.indexOf(self.tab), QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Tab 1", None))
        self.tabAppearance.setTabText(self.tabAppearance.indexOf(self.tab_2), QCoreApplication.translate("MatGui::DlgInspectAppearance", u"Tab 2", None))
    # retranslateUi

