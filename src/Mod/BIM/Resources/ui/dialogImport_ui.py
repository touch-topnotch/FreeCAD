# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogImport.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(551, 340)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboStrategy = QComboBox(Dialog)
        self.comboStrategy.addItem("")
        self.comboStrategy.addItem("")
        self.comboStrategy.addItem("")
        self.comboStrategy.setObjectName(u"comboStrategy")

        self.gridLayout.addWidget(self.comboStrategy, 1, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboSingleDoc = QComboBox(Dialog)
        self.comboSingleDoc.addItem("")
        self.comboSingleDoc.addItem("")
        self.comboSingleDoc.setObjectName(u"comboSingleDoc")

        self.gridLayout.addWidget(self.comboSingleDoc, 3, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboShapeMode = QComboBox(Dialog)
        self.comboShapeMode.addItem("")
        self.comboShapeMode.addItem("")
        self.comboShapeMode.addItem("")
        self.comboShapeMode.setObjectName(u"comboShapeMode")

        self.gridLayout.addWidget(self.comboShapeMode, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.checkSwitchWB = QCheckBox(Dialog)
        self.checkSwitchWB.setObjectName(u"checkSwitchWB")

        self.verticalLayout.addWidget(self.checkSwitchWB)

        self.checkLoadPsets = QCheckBox(Dialog)
        self.checkLoadPsets.setObjectName(u"checkLoadPsets")

        self.verticalLayout.addWidget(self.checkLoadPsets)

        self.checkLoadMaterials = QCheckBox(Dialog)
        self.checkLoadMaterials.setObjectName(u"checkLoadMaterials")

        self.verticalLayout.addWidget(self.checkLoadMaterials)

        self.checkLoadLayers = QCheckBox(Dialog)
        self.checkLoadLayers.setObjectName(u"checkLoadLayers")

        self.verticalLayout.addWidget(self.checkLoadLayers)

        self.checkAskAgain = QCheckBox(Dialog)
        self.checkAskAgain.setObjectName(u"checkAskAgain")
        self.checkAskAgain.setChecked(False)

        self.verticalLayout.addWidget(self.checkAskAgain)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.comboShapeMode.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"IFC import options", None))
        self.comboStrategy.setItemText(0, QCoreApplication.translate("Dialog", u"Only root object (default)", None))
        self.comboStrategy.setItemText(1, QCoreApplication.translate("Dialog", u"Project structure (levels)", None))
        self.comboStrategy.setItemText(2, QCoreApplication.translate("Dialog", u"All individual IFC objects", None))

#if QT_CONFIG(tooltip)
        self.comboStrategy.setToolTip(QCoreApplication.translate("Dialog", u"How the IFC file will initially be imported: Only one object, only project structure, or all individual objects.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"Initial import", None))
        self.comboSingleDoc.setItemText(0, QCoreApplication.translate("Dialog", u"Locked (IFC objects only)", None))
        self.comboSingleDoc.setItemText(1, QCoreApplication.translate("Dialog", u"Unlocked (non-IFC objects permitted)", None))

#if QT_CONFIG(tooltip)
        self.comboSingleDoc.setToolTip(QCoreApplication.translate("Dialog", u"This defines how the IFC data is stored in the FreeCAD document. 'Single IFC document' means that the FreeCAD document is the IFC document, anything you create in it belongs to the IFC document too. 'Use IFC document object' means that an object will be created inside the FreeCAD document to represent the IFC document. You will be able to add non-IFC objects alongside.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Lock document", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Representation type", None))
        self.comboShapeMode.setItemText(0, QCoreApplication.translate("Dialog", u"Load the shape (slower)", None))
        self.comboShapeMode.setItemText(1, QCoreApplication.translate("Dialog", u"Load 3D representation only, no shape (default)", None))
        self.comboShapeMode.setItemText(2, QCoreApplication.translate("Dialog", u"No 3D representation at all", None))

#if QT_CONFIG(tooltip)
        self.comboShapeMode.setToolTip(QCoreApplication.translate("Dialog", u"The type of object created at import. Mesh is faster, but Shapes are more precise. You can convert between the two anytime by right-clicking the object tree", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkSwitchWB.setToolTip(QCoreApplication.translate("Dialog", u"If this is checked, the workbench specified in Start preferences will be loaded after import", None))
#endif // QT_CONFIG(tooltip)
        self.checkSwitchWB.setText(QCoreApplication.translate("Dialog", u"Switch workbench after import", None))
#if QT_CONFIG(tooltip)
        self.checkLoadPsets.setToolTip(QCoreApplication.translate("Dialog", u"Preload property sets of all objects. It is advised to leave this unchecked and load property sets later, only when needed", None))
#endif // QT_CONFIG(tooltip)
        self.checkLoadPsets.setText(QCoreApplication.translate("Dialog", u"Preload property sets", None))
#if QT_CONFIG(tooltip)
        self.checkLoadMaterials.setToolTip(QCoreApplication.translate("Dialog", u"Preload all materials of the file. It is advised to leave this unchecked and load materials later, only when needed", None))
#endif // QT_CONFIG(tooltip)
        self.checkLoadMaterials.setText(QCoreApplication.translate("Dialog", u"Preload materials", None))
#if QT_CONFIG(tooltip)
        self.checkLoadLayers.setToolTip(QCoreApplication.translate("Dialog", u"Preload all layers of the file. It is advised to leave this unchecked and load layers later, only when needed", None))
#endif // QT_CONFIG(tooltip)
        self.checkLoadLayers.setText(QCoreApplication.translate("Dialog", u"Preload layers", None))
#if QT_CONFIG(tooltip)
        self.checkAskAgain.setToolTip(QCoreApplication.translate("Dialog", u"If this is unchecked, these settings will be applied automatically next time. You can change this later under menu Edit -> Preferences -> BIM -> Native IFC", None))
#endif // QT_CONFIG(tooltip)
        self.checkAskAgain.setText(QCoreApplication.translate("Dialog", u"Ask me again next time", None))
    # retranslateUi

