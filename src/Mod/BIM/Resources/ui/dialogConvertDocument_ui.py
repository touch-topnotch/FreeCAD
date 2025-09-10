# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogConvertDocument.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(307, 219)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.checkStructure = QCheckBox(Dialog)
        self.checkStructure.setObjectName(u"checkStructure")

        self.verticalLayout.addWidget(self.checkStructure)

        self.checkAskAgain = QCheckBox(Dialog)
        self.checkAskAgain.setObjectName(u"checkAskAgain")
        self.checkAskAgain.setChecked(False)

        self.verticalLayout.addWidget(self.checkAskAgain)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.No|QDialogButtonBox.Yes)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Single IFC document", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Do you wish to convert this document to an IFC document? Replying 'Yes' will automatically turn all new objects to IFC, while 'No' will allow you to have both IFC and non-IFC elements in the file.", None))
#if QT_CONFIG(tooltip)
        self.checkStructure.setToolTip(QCoreApplication.translate("Dialog", u"Add a default building structure (IfcSite, IfcBuilding and IfcBuildingStorey). You can also add the structure manually later.", None))
#endif // QT_CONFIG(tooltip)
        self.checkStructure.setText(QCoreApplication.translate("Dialog", u"Also create a default structure", None))
#if QT_CONFIG(tooltip)
        self.checkAskAgain.setToolTip(QCoreApplication.translate("Dialog", u"If this is checked, you won't be asked again when creating a new FreeCAD document,\n"
"and that document won't be turned into an IFC document automatically.\n"
"You can still turn a FreeCAD document into an IFC document manually, using\n"
"Utils -> Make IFC project", None))
#endif // QT_CONFIG(tooltip)
        self.checkAskAgain.setText(QCoreApplication.translate("Dialog", u"Do not ask again", None))
    # retranslateUi

