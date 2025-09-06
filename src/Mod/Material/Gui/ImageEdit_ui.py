# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageEdit.ui'
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
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MatGui_ImageEdit(object):
    def setupUi(self, MatGui__ImageEdit):
        if not MatGui__ImageEdit.objectName():
            MatGui__ImageEdit.setObjectName(u"MatGui__ImageEdit")
        MatGui__ImageEdit.resize(498, 626)
        self.verticalLayout = QVBoxLayout(MatGui__ImageEdit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.label = QLabel(MatGui__ImageEdit)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignTop)

        self.labelThumb = MatGui_ImageLabel(MatGui__ImageEdit)
        self.labelThumb.setObjectName(u"labelThumb")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelThumb.sizePolicy().hasHeightForWidth())
        self.labelThumb.setSizePolicy(sizePolicy)
        self.labelThumb.setMinimumSize(QSize(64, 64))
        self.labelThumb.setFrameShape(QFrame.Box)

        self.verticalLayout_4.addWidget(self.labelThumb, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.buttonFileSelect = QPushButton(MatGui__ImageEdit)
        self.buttonFileSelect.setObjectName(u"buttonFileSelect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonFileSelect.sizePolicy().hasHeightForWidth())
        self.buttonFileSelect.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.buttonFileSelect, 0, Qt.AlignRight|Qt.AlignTop)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelHeight = QLabel(MatGui__ImageEdit)
        self.labelHeight.setObjectName(u"labelHeight")

        self.gridLayout.addWidget(self.labelHeight, 1, 0, 1, 1)

        self.labelWidth = QLabel(MatGui__ImageEdit)
        self.labelWidth.setObjectName(u"labelWidth")

        self.gridLayout.addWidget(self.labelWidth, 0, 0, 1, 1)

        self.editHeight = QLineEdit(MatGui__ImageEdit)
        self.editHeight.setObjectName(u"editHeight")
        self.editHeight.setEnabled(False)
        self.editHeight.setReadOnly(True)

        self.gridLayout.addWidget(self.editHeight, 1, 1, 1, 1)

        self.editWidth = QLineEdit(MatGui__ImageEdit)
        self.editWidth.setObjectName(u"editWidth")
        self.editWidth.setEnabled(False)
        self.editWidth.setReadOnly(True)

        self.gridLayout.addWidget(self.editWidth, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelImage = MatGui_ImageLabel(MatGui__ImageEdit)
        self.labelImage.setObjectName(u"labelImage")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelImage.sizePolicy().hasHeightForWidth())
        self.labelImage.setSizePolicy(sizePolicy2)
        self.labelImage.setMinimumSize(QSize(480, 480))
        self.labelImage.setFrameShape(QFrame.Box)

        self.verticalLayout.addWidget(self.labelImage, 0, Qt.AlignTop)

        self.standardButtons = QDialogButtonBox(MatGui__ImageEdit)
        self.standardButtons.setObjectName(u"standardButtons")
        self.standardButtons.setOrientation(Qt.Horizontal)
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.standardButtons)


        self.retranslateUi(MatGui__ImageEdit)
        self.standardButtons.accepted.connect(MatGui__ImageEdit.accept)
        self.standardButtons.rejected.connect(MatGui__ImageEdit.reject)

        QMetaObject.connectSlotsByName(MatGui__ImageEdit)
    # setupUi

    def retranslateUi(self, MatGui__ImageEdit):
        MatGui__ImageEdit.setWindowTitle(QCoreApplication.translate("MatGui::ImageEdit", u"Image", None))
        self.label.setText(QCoreApplication.translate("MatGui::ImageEdit", u"Thumbnail", None))
        self.labelThumb.setText("")
        self.buttonFileSelect.setText(QCoreApplication.translate("MatGui::ImageEdit", u"File", None))
        self.labelHeight.setText(QCoreApplication.translate("MatGui::ImageEdit", u"Height", None))
        self.labelWidth.setText(QCoreApplication.translate("MatGui::ImageEdit", u"Width", None))
        self.labelImage.setText("")
    # retranslateUi

