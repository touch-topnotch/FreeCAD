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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Single IFC Document", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Convert this document to an IFC document? Selecting 'Yes' will enable automatic creation of IFC objects. Selecting 'No' will allow a mix of IFC and non-IFC elements within the file.", None))
#if QT_CONFIG(tooltip)
        self.checkStructure.setToolTip(QCoreApplication.translate("Dialog", u"Adds a default building structure consisting of IfcSite, IfcBuilding, and IfcBuildingStorey. The structure can also be added manually at a later stage.", None))
#endif // QT_CONFIG(tooltip)
        self.checkStructure.setText(QCoreApplication.translate("Dialog", u"Also create a default structure", None))
#if QT_CONFIG(tooltip)
        self.checkAskAgain.setToolTip(QCoreApplication.translate("Dialog", u"Prevents further prompts when creating new FreeCAD documents. New documents will not be converted to IFC automatically, but conversion remains possible later via Utils \u2192 Create IFC Project.", None))
#endif // QT_CONFIG(tooltip)
        self.checkAskAgain.setText(QCoreApplication.translate("Dialog", u"Do not ask again", None))
    # retranslateUi

