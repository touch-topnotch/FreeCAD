# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgInspectMaterial.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MatGui_DlgInspectMaterial(object):
    def setupUi(self, MatGui__DlgInspectMaterial):
        if not MatGui__DlgInspectMaterial.objectName():
            MatGui__DlgInspectMaterial.setObjectName(u"MatGui__DlgInspectMaterial")
        MatGui__DlgInspectMaterial.resize(400, 432)
        self.verticalLayout = QVBoxLayout(MatGui__DlgInspectMaterial)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(MatGui__DlgInspectMaterial)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 376, 408))
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
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeMaterials = QTreeView(self.groupBox_2)
        self.treeMaterials.setObjectName(u"treeMaterials")
        self.treeMaterials.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_3.addWidget(self.treeMaterials)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonClipboard = QPushButton(self.groupBox_2)
        self.buttonClipboard.setObjectName(u"buttonClipboard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClipboard.sizePolicy().hasHeightForWidth())
        self.buttonClipboard.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.buttonClipboard)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(MatGui__DlgInspectMaterial)

        QMetaObject.connectSlotsByName(MatGui__DlgInspectMaterial)
    # setupUi

    def retranslateUi(self, MatGui__DlgInspectMaterial):
        MatGui__DlgInspectMaterial.setWindowTitle(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Document", None))
        self.label.setText(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Document name", None))
#if QT_CONFIG(tooltip)
        self.editDocument.setToolTip(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Name of the active document", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Label / internal name", None))
        self.label_3.setText(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Sub.Shape / Type", None))
        self.label_4.setText(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Shape.TypeID / TypeID", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Material", None))
        self.buttonClipboard.setText(QCoreApplication.translate("MatGui::DlgInspectMaterial", u"Copy to Clipboard", None))
    # retranslateUi

