# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MouseButtons.ui'
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
    QGridLayout, QGroupBox, QLabel, QSizePolicy,
    QWidget)

class Ui_Gui_Dialog_MouseButtons(object):
    def setupUi(self, Gui__Dialog__MouseButtons):
        if not Gui__Dialog__MouseButtons.objectName():
            Gui__Dialog__MouseButtons.setObjectName(u"Gui__Dialog__MouseButtons")
        Gui__Dialog__MouseButtons.resize(364, 239)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__MouseButtons)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(Gui__Dialog__MouseButtons)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.selectionLabel = QLabel(self.groupBox)
        self.selectionLabel.setObjectName(u"selectionLabel")
        self.selectionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.selectionLabel, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.panningLabel = QLabel(self.groupBox)
        self.panningLabel.setObjectName(u"panningLabel")
        self.panningLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.panningLabel, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.rotationLabel = QLabel(self.groupBox)
        self.rotationLabel.setObjectName(u"rotationLabel")
        self.rotationLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.rotationLabel, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.zoomingLabel = QLabel(self.groupBox)
        self.zoomingLabel.setObjectName(u"zoomingLabel")
        self.zoomingLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.zoomingLabel, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__MouseButtons)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__MouseButtons)
        self.buttonBox.accepted.connect(Gui__Dialog__MouseButtons.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__MouseButtons.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__MouseButtons)
    # setupUi

    def retranslateUi(self, Gui__Dialog__MouseButtons):
        Gui__Dialog__MouseButtons.setWindowTitle(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Mouse Buttons", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Configuration", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Selection", None))
        self.selectionLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Panning", None))
        self.panningLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Rotation", None))
        self.rotationLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::MouseButtons", u"Zooming", None))
        self.zoomingLabel.setText("")
    # retranslateUi

