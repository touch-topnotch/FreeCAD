# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DocumentRecovery.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_Gui_Dialog_DocumentRecovery(object):
    def setupUi(self, Gui__Dialog__DocumentRecovery):
        if not Gui__Dialog__DocumentRecovery.objectName():
            Gui__Dialog__DocumentRecovery.setObjectName(u"Gui__Dialog__DocumentRecovery")
        Gui__Dialog__DocumentRecovery.resize(576, 495)
        self.gridLayout = QGridLayout(Gui__Dialog__DocumentRecovery)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Gui__Dialog__DocumentRecovery)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DocumentRecovery)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)

        self.buttonCleanup = QPushButton(Gui__Dialog__DocumentRecovery)
        self.buttonCleanup.setObjectName(u"buttonCleanup")
        self.buttonCleanup.setEnabled(True)

        self.gridLayout.addWidget(self.buttonCleanup, 4, 0, 1, 1)

        self.label_2 = QLabel(Gui__Dialog__DocumentRecovery)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.treeWidget = QTreeWidget(Gui__Dialog__DocumentRecovery)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.gridLayout.addWidget(self.treeWidget, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DocumentRecovery)
        self.buttonBox.accepted.connect(Gui__Dialog__DocumentRecovery.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DocumentRecovery.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DocumentRecovery)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DocumentRecovery):
        Gui__Dialog__DocumentRecovery.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Document Recovery", None))
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Press 'Start Recovery' to start the recovery process of the document listed below.\n"
"\n"
"The 'Status' column shows whether the document could be recovered.", None))
        self.buttonCleanup.setText(QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Cleanup", None))
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Status of recovered documents", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Status", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Gui::Dialog::DocumentRecovery", u"Document name", None));
    # retranslateUi

