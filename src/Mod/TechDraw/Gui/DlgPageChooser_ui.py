# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgPageChooser.ui'
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
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TechDrawGui_DlgPageChooser(object):
    def setupUi(self, TechDrawGui__DlgPageChooser):
        if not TechDrawGui__DlgPageChooser.objectName():
            TechDrawGui__DlgPageChooser.setObjectName(u"TechDrawGui__DlgPageChooser")
        TechDrawGui__DlgPageChooser.setWindowModality(Qt.WindowModal)
        TechDrawGui__DlgPageChooser.resize(360, 280)
        TechDrawGui__DlgPageChooser.setModal(True)
        self.verticalLayout = QVBoxLayout(TechDrawGui__DlgPageChooser)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lPrompt = QLabel(TechDrawGui__DlgPageChooser)
        self.lPrompt.setObjectName(u"lPrompt")
        self.lPrompt.setWordWrap(True)

        self.verticalLayout.addWidget(self.lPrompt)

        self.lwPages = QListWidget(TechDrawGui__DlgPageChooser)
        self.lwPages.setObjectName(u"lwPages")

        self.verticalLayout.addWidget(self.lwPages)

        self.bbButtons = QDialogButtonBox(TechDrawGui__DlgPageChooser)
        self.bbButtons.setObjectName(u"bbButtons")
        self.bbButtons.setOrientation(Qt.Horizontal)
        self.bbButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bbButtons.setCenterButtons(False)

        self.verticalLayout.addWidget(self.bbButtons)


        self.retranslateUi(TechDrawGui__DlgPageChooser)
        self.bbButtons.accepted.connect(TechDrawGui__DlgPageChooser.accept)
        self.bbButtons.rejected.connect(TechDrawGui__DlgPageChooser.reject)

        QMetaObject.connectSlotsByName(TechDrawGui__DlgPageChooser)
    # setupUi

    def retranslateUi(self, TechDrawGui__DlgPageChooser):
        TechDrawGui__DlgPageChooser.setWindowTitle(QCoreApplication.translate("TechDrawGui::DlgPageChooser", u"Page Chooser", None))
#if QT_CONFIG(tooltip)
        TechDrawGui__DlgPageChooser.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lPrompt.setText(QCoreApplication.translate("TechDrawGui::DlgPageChooser", u"FreeCAD could not determine which page to use. Select a page.", None))
#if QT_CONFIG(tooltip)
        self.lwPages.setToolTip(QCoreApplication.translate("TechDrawGui::DlgPageChooser", u"Select a page that should be used", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

