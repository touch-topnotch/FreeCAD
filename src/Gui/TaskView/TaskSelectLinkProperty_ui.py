# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskSelectLinkProperty.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Gui_TaskView_TaskSelectLinkProperty(object):
    def setupUi(self, Gui__TaskView__TaskSelectLinkProperty):
        if not Gui__TaskView__TaskSelectLinkProperty.objectName():
            Gui__TaskView__TaskSelectLinkProperty.setObjectName(u"Gui__TaskView__TaskSelectLinkProperty")
        Gui__TaskView__TaskSelectLinkProperty.resize(257, 313)
        self.verticalLayout = QVBoxLayout(Gui__TaskView__TaskSelectLinkProperty)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Remove = QToolButton(Gui__TaskView__TaskSelectLinkProperty)
        self.Remove.setObjectName(u"Remove")
        self.Remove.setText(u"\u2026")

        self.horizontalLayout.addWidget(self.Remove)

        self.Add = QToolButton(Gui__TaskView__TaskSelectLinkProperty)
        self.Add.setObjectName(u"Add")
        self.Add.setText(u"\u2026")

        self.horizontalLayout.addWidget(self.Add)

        self.Invert = QToolButton(Gui__TaskView__TaskSelectLinkProperty)
        self.Invert.setObjectName(u"Invert")
        self.Invert.setText(u"\u2026")

        self.horizontalLayout.addWidget(self.Invert)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Help = QToolButton(Gui__TaskView__TaskSelectLinkProperty)
        self.Help.setObjectName(u"Help")
        self.Help.setText(u"\u2026")

        self.horizontalLayout.addWidget(self.Help)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listWidget = QListWidget(Gui__TaskView__TaskSelectLinkProperty)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(Gui__TaskView__TaskSelectLinkProperty)

        QMetaObject.connectSlotsByName(Gui__TaskView__TaskSelectLinkProperty)
    # setupUi

    def retranslateUi(self, Gui__TaskView__TaskSelectLinkProperty):
        Gui__TaskView__TaskSelectLinkProperty.setWindowTitle(QCoreApplication.translate("Gui::TaskView::TaskSelectLinkProperty", u"Appearance", None))
    # retranslateUi

