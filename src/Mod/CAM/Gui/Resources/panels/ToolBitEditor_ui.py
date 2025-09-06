# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolBitEditor.ui'
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
    QGridLayout, QLabel, QLayout, QLineEdit,
    QPlainTextEdit, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 800)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 980, 849))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vBox = QVBoxLayout()
        self.vBox.setObjectName(u"vBox")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents_6)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QSize(650, 850))
        self.tabWidget.setBaseSize(QSize(650, 850))
        self.toolTab = QWidget()
        self.toolTab.setObjectName(u"toolTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolTab.sizePolicy().hasHeightForWidth())
        self.toolTab.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.toolTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.toolTabLayout = QVBoxLayout()
        self.toolTabLayout.setObjectName(u"toolTabLayout")

        self.verticalLayout_2.addLayout(self.toolTabLayout)

        self.widget = QWidget(self.toolTab)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.toolTab, "")
        self.notesTab = QWidget()
        self.notesTab.setObjectName(u"notesTab")
        sizePolicy.setHeightForWidth(self.notesTab.sizePolicy().hasHeightForWidth())
        self.notesTab.setSizePolicy(sizePolicy)
        self.notesTab.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.notesTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(6)
        self.label_4 = QLabel(self.notesTab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEditCoating = QLineEdit(self.notesTab)
        self.lineEditCoating.setObjectName(u"lineEditCoating")

        self.gridLayout.addWidget(self.lineEditCoating, 1, 1, 1, 1)

        self.label_3 = QLabel(self.notesTab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEditHardness = QLineEdit(self.notesTab)
        self.lineEditHardness.setObjectName(u"lineEditHardness")

        self.gridLayout.addWidget(self.lineEditHardness, 3, 1, 1, 1)

        self.label_2 = QLabel(self.notesTab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEditSupplier = QLineEdit(self.notesTab)
        self.lineEditSupplier.setObjectName(u"lineEditSupplier")

        self.gridLayout.addWidget(self.lineEditSupplier, 4, 1, 1, 1)

        self.lineEditMaterials = QLineEdit(self.notesTab)
        self.lineEditMaterials.setObjectName(u"lineEditMaterials")

        self.gridLayout.addWidget(self.lineEditMaterials, 2, 1, 1, 1)

        self.label = QLabel(self.notesTab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.plainTextEditNotes = QPlainTextEdit(self.notesTab)
        self.plainTextEditNotes.setObjectName(u"plainTextEditNotes")
        sizePolicy.setHeightForWidth(self.plainTextEditNotes.sizePolicy().hasHeightForWidth())
        self.plainTextEditNotes.setSizePolicy(sizePolicy)
        self.plainTextEditNotes.setMinimumSize(QSize(0, 0))
        self.plainTextEditNotes.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.plainTextEditNotes, 2, 0, 1, 1)

        self.gridLayout_2.setRowStretch(2, 1)
        self.tabWidget.addTab(self.notesTab, "")

        self.vBox.addWidget(self.tabWidget)


        self.verticalLayout_3.addLayout(self.vBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.tabWidget, self.lineEditCoating)
        QWidget.setTabOrder(self.lineEditCoating, self.lineEditMaterials)
        QWidget.setTabOrder(self.lineEditMaterials, self.lineEditHardness)
        QWidget.setTabOrder(self.lineEditHardness, self.lineEditSupplier)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Tool Parameter Editor", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolTab), QCoreApplication.translate("Dialog", u"Tool", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Coating", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Hardness", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Materials", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Supplier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), QCoreApplication.translate("Dialog", u"Notes", None))
    # retranslateUi

