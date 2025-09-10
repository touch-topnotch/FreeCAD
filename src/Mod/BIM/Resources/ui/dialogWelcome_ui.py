# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogWelcome.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import Arch_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(412, 602)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image = QLabel(Dialog)
        self.image.setObjectName(u"image")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QSize(400, 178))
        self.image.setBaseSize(QSize(400, 178))
        self.image.setPixmap(QPixmap(u":/icons/banner.png"))
        self.image.setScaledContents(False)

        self.verticalLayout.addWidget(self.image)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 382, 598))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Welcome", None))
        self.image.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"Welcome to the BIM workbench!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>This appears to be the first time that you are using the BIM workbench. If you press OK, the next screen will propose you to set a couple of typical FreeCAD options that are suitable for BIM work. You can change these options anytime later under menu <span style=\" font-weight:600;\">Manage -&gt; BIM Setup...</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"How to get started?", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"FreeCAD is a complex application. If this is your first contact with FreeCAD, or you have never worked with 3D or BIM before, you might want to take our <a href=\"https://wiki.freecad.org/BIM_ingame_tutorial\">BIM tutorial</a> first (Also available under menu <span style=\" font-weight:600;\">Help -&gt; BIM Tutorial</span>).", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"The BIM workbench also has a <a href=\"https://wiki.freecad.org/BIM_Workbench\">complete documentation</a>  available under the Help menu. The \"what's this?\" button will also open the help page of any tool from the toolbars.", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"A good way to start building a BIM model is by setting up basic characteristics of your project, under menu <span style=\" font-weight:600;\">Manage -&gt; Project setup</span>. You can also directly configure different floor plans for your project, under menu <span style=\" font-weight:600;\">Manage -&gt; Levels.</span>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"There is no mandatory behaviour here though, and you can also start creating walls and columns directly, and care about organizing things in levels later.", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>You might also want to start from an existing floor plan or 3D model made in another application. Under menu <span style=\" font-weight:600;\">File -&gt; Import</span>, you will find a wide range of file formats that can be imported into FreeCAD.</p></body></html>", None))
    # retranslateUi

