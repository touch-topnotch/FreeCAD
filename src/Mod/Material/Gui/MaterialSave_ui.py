# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaterialSave.ui'
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
    QDialog, QDialogButtonBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTreeView, QVBoxLayout, QWidget)

class Ui_MatGui_MaterialSave(object):
    def setupUi(self, MatGui__MaterialSave):
        if not MatGui__MaterialSave.objectName():
            MatGui__MaterialSave.setObjectName(u"MatGui__MaterialSave")
        MatGui__MaterialSave.resize(654, 708)
        self.verticalLayout = QVBoxLayout(MatGui__MaterialSave)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MatGui__MaterialSave)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboLibrary = QComboBox(MatGui__MaterialSave)
        self.comboLibrary.setObjectName(u"comboLibrary")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLibrary.sizePolicy().hasHeightForWidth())
        self.comboLibrary.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboLibrary)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.treeMaterials = QTreeView(MatGui__MaterialSave)
        self.treeMaterials.setObjectName(u"treeMaterials")

        self.verticalLayout.addWidget(self.treeMaterials)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttonNewFolder = QPushButton(MatGui__MaterialSave)
        self.buttonNewFolder.setObjectName(u"buttonNewFolder")

        self.horizontalLayout_3.addWidget(self.buttonNewFolder)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(MatGui__MaterialSave)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editFilename = QLineEdit(MatGui__MaterialSave)
        self.editFilename.setObjectName(u"editFilename")
        sizePolicy.setHeightForWidth(self.editFilename.sizePolicy().hasHeightForWidth())
        self.editFilename.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.editFilename)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.checkDerived = QCheckBox(MatGui__MaterialSave)
        self.checkDerived.setObjectName(u"checkDerived")

        self.horizontalLayout_4.addWidget(self.checkDerived)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.standardButtons = QDialogButtonBox(MatGui__MaterialSave)
        self.standardButtons.setObjectName(u"standardButtons")
        self.standardButtons.setOrientation(Qt.Horizontal)
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.standardButtons)


        self.retranslateUi(MatGui__MaterialSave)
        self.standardButtons.accepted.connect(MatGui__MaterialSave.accept)
        self.standardButtons.rejected.connect(MatGui__MaterialSave.reject)

        QMetaObject.connectSlotsByName(MatGui__MaterialSave)
    # setupUi

    def retranslateUi(self, MatGui__MaterialSave):
        MatGui__MaterialSave.setWindowTitle(QCoreApplication.translate("MatGui::MaterialSave", u"Save Material", None))
        self.label.setText(QCoreApplication.translate("MatGui::MaterialSave", u"Library", None))
        self.buttonNewFolder.setText(QCoreApplication.translate("MatGui::MaterialSave", u"New Folder", None))
        self.label_2.setText(QCoreApplication.translate("MatGui::MaterialSave", u"Filename", None))
        self.checkDerived.setText(QCoreApplication.translate("MatGui::MaterialSave", u"Save as inherited", None))
    # retranslateUi

