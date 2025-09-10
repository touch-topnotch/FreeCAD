# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TextureMapping.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QSizePolicy, QWidget)

class Ui_Gui_Dialog_TextureMapping(object):
    def setupUi(self, Gui__Dialog__TextureMapping):
        if not Gui__Dialog__TextureMapping.objectName():
            Gui__Dialog__TextureMapping.setObjectName(u"Gui__Dialog__TextureMapping")
        Gui__Dialog__TextureMapping.resize(218, 122)
        self.gridLayout_2 = QGridLayout(Gui__Dialog__TextureMapping)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Gui__Dialog__TextureMapping)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkGlobal = QCheckBox(self.groupBox)
        self.checkGlobal.setObjectName(u"checkGlobal")

        self.gridLayout.addWidget(self.checkGlobal, 0, 0, 1, 1)

        self.checkEnv = QCheckBox(self.groupBox)
        self.checkEnv.setObjectName(u"checkEnv")

        self.gridLayout.addWidget(self.checkEnv, 0, 1, 1, 1)

        self.fileChooser = Gui_FileChooser(self.groupBox)
        self.fileChooser.setObjectName(u"fileChooser")

        self.gridLayout.addWidget(self.fileChooser, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__TextureMapping)

        QMetaObject.connectSlotsByName(Gui__Dialog__TextureMapping)
    # setupUi

    def retranslateUi(self, Gui__Dialog__TextureMapping):
        Gui__Dialog__TextureMapping.setWindowTitle(QCoreApplication.translate("Gui::Dialog::TextureMapping", u"Texture", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::TextureMapping", u"Texture mapping", None))
        self.checkGlobal.setText(QCoreApplication.translate("Gui::Dialog::TextureMapping", u"Global", None))
        self.checkEnv.setText(QCoreApplication.translate("Gui::Dialog::TextureMapping", u"Environment", None))
    # retranslateUi

