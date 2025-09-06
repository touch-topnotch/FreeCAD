# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SymbolChooser.ui'
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
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TechDrawGui_SymbolChooser(object):
    def setupUi(self, TechDrawGui__SymbolChooser):
        if not TechDrawGui__SymbolChooser.objectName():
            TechDrawGui__SymbolChooser.setObjectName(u"TechDrawGui__SymbolChooser")
        TechDrawGui__SymbolChooser.setWindowModality(Qt.WindowModal)
        TechDrawGui__SymbolChooser.resize(360, 280)
        TechDrawGui__SymbolChooser.setModal(True)
        self.verticalLayout = QVBoxLayout(TechDrawGui__SymbolChooser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lwSymbols = QListWidget(TechDrawGui__SymbolChooser)
        self.lwSymbols.setObjectName(u"lwSymbols")

        self.verticalLayout.addWidget(self.lwSymbols)

        self.bbButtons = QDialogButtonBox(TechDrawGui__SymbolChooser)
        self.bbButtons.setObjectName(u"bbButtons")
        self.bbButtons.setOrientation(Qt.Horizontal)
        self.bbButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bbButtons.setCenterButtons(False)

        self.verticalLayout.addWidget(self.bbButtons)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(TechDrawGui__SymbolChooser)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.fcSymbolDir = Gui_FileChooser(TechDrawGui__SymbolChooser)
        self.fcSymbolDir.setObjectName(u"fcSymbolDir")
        self.fcSymbolDir.setMode(Gui.FileChooser.Directory)

        self.gridLayout.addWidget(self.fcSymbolDir, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(TechDrawGui__SymbolChooser)
        self.bbButtons.accepted.connect(TechDrawGui__SymbolChooser.accept)
        self.bbButtons.rejected.connect(TechDrawGui__SymbolChooser.reject)

        QMetaObject.connectSlotsByName(TechDrawGui__SymbolChooser)
    # setupUi

    def retranslateUi(self, TechDrawGui__SymbolChooser):
        TechDrawGui__SymbolChooser.setWindowTitle(QCoreApplication.translate("TechDrawGui::SymbolChooser", u"Symbol Chooser", None))
#if QT_CONFIG(tooltip)
        self.lwSymbols.setToolTip(QCoreApplication.translate("TechDrawGui::SymbolChooser", u"Select a symbol that should be used", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TechDrawGui::SymbolChooser", u"Symbol directory", None))
#if QT_CONFIG(tooltip)
        self.fcSymbolDir.setToolTip(QCoreApplication.translate("TechDrawGui::SymbolChooser", u"Directory to welding symbols", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

