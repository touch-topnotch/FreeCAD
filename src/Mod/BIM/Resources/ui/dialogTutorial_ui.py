# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogTutorial.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 476)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextBrowser(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.labelTasks = QLabel(Form)
        self.labelTasks.setObjectName(u"labelTasks")
        font = QFont()
        font.setBold(True)
        self.labelTasks.setFont(font)

        self.verticalLayout.addWidget(self.labelTasks)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelGoal1 = QLabel(Form)
        self.labelGoal1.setObjectName(u"labelGoal1")

        self.gridLayout.addWidget(self.labelGoal1, 0, 0, 1, 1)

        self.labelIcon1 = QLabel(Form)
        self.labelIcon1.setObjectName(u"labelIcon1")
        self.labelIcon1.setLayoutDirection(Qt.LeftToRight)
        self.labelIcon1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelIcon1, 0, 1, 1, 1)

        self.labelGoal2 = QLabel(Form)
        self.labelGoal2.setObjectName(u"labelGoal2")

        self.gridLayout.addWidget(self.labelGoal2, 1, 0, 1, 1)

        self.labelIcon2 = QLabel(Form)
        self.labelIcon2.setObjectName(u"labelIcon2")
        self.labelIcon2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelIcon2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonPrevious = QPushButton(Form)
        self.buttonPrevious.setObjectName(u"buttonPrevious")

        self.horizontalLayout.addWidget(self.buttonPrevious)

        self.buttonNext = QPushButton(Form)
        self.buttonNext.setObjectName(u"buttonNext")

        self.horizontalLayout.addWidget(self.buttonNext)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(10)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"BIM tutorial", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Fira Sans'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Loading tutorials contents from the FreeCAD wiki. Please wait...</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If this is the first time you are using the tutorial, this can take a while, since we need to download many images. On next runs, this will be faster as the images are cached locally.</p>\n"
"<p style=\"-qt-paragr"
                        "aph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When the tutorial is fully written, we'll think of a faster system to avoid this annoying loading time. Please bear with us in the meantime! ;)</p></body></html>", None))
        self.labelTasks.setText(QCoreApplication.translate("Form", u"Tasks to complete:", None))
        self.labelGoal1.setText(QCoreApplication.translate("Form", u"Goal1", None))
        self.labelIcon1.setText(QCoreApplication.translate("Form", u"icon", None))
        self.labelGoal2.setText(QCoreApplication.translate("Form", u"Goal2", None))
        self.labelIcon2.setText(QCoreApplication.translate("Form", u"icon", None))
        self.buttonPrevious.setText(QCoreApplication.translate("Form", u"<< Previous", None))
        self.buttonNext.setText(QCoreApplication.translate("Form", u"Next >>", None))
    # retranslateUi

