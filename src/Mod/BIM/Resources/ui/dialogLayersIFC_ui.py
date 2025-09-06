# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogLayersIFC.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(795, 455)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree = QTreeView(Dialog)
        self.tree.setObjectName(u"tree")
        self.tree.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tree)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonNew = QPushButton(Dialog)
        self.buttonNew.setObjectName(u"buttonNew")

        self.horizontalLayout.addWidget(self.buttonNew)

        self.buttonIFC = QPushButton(Dialog)
        self.buttonIFC.setObjectName(u"buttonIFC")

        self.horizontalLayout.addWidget(self.buttonIFC)

        self.buttonDelete = QPushButton(Dialog)
        self.buttonDelete.setObjectName(u"buttonDelete")

        self.horizontalLayout.addWidget(self.buttonDelete)

        self.buttonSelectAll = QPushButton(Dialog)
        self.buttonSelectAll.setObjectName(u"buttonSelectAll")

        self.horizontalLayout.addWidget(self.buttonSelectAll)

        self.buttonToggle = QPushButton(Dialog)
        self.buttonToggle.setObjectName(u"buttonToggle")

        self.horizontalLayout.addWidget(self.buttonToggle)

        self.buttonIsolate = QPushButton(Dialog)
        self.buttonIsolate.setObjectName(u"buttonIsolate")

        self.horizontalLayout.addWidget(self.buttonIsolate)

        self.buttonAssign = QPushButton(Dialog)
        self.buttonAssign.setObjectName(u"buttonAssign")

        self.horizontalLayout.addWidget(self.buttonAssign)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonCancel = QPushButton(Dialog)
        self.buttonCancel.setObjectName(u"buttonCancel")

        self.horizontalLayout.addWidget(self.buttonCancel)

        self.buttonOK = QPushButton(Dialog)
        self.buttonOK.setObjectName(u"buttonOK")

        self.horizontalLayout.addWidget(self.buttonOK)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Layers Manager", None))
        self.buttonNew.setText(QCoreApplication.translate("Dialog", u"New", None))
#if QT_CONFIG(tooltip)
        self.buttonIFC.setToolTip(QCoreApplication.translate("Dialog", u"Adds this layer to an IFC project", None))
#endif // QT_CONFIG(tooltip)
        self.buttonIFC.setText("")
        self.buttonDelete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.buttonSelectAll.setText(QCoreApplication.translate("Dialog", u"Select All", None))
        self.buttonToggle.setText(QCoreApplication.translate("Dialog", u"Toggle Visibility", None))
        self.buttonIsolate.setText(QCoreApplication.translate("Dialog", u"Isolate", None))
#if QT_CONFIG(tooltip)
        self.buttonAssign.setToolTip(QCoreApplication.translate("Dialog", u"Assign selected objects to the selected layer", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAssign.setText(QCoreApplication.translate("Dialog", u"Assign", None))
        self.buttonCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.buttonOK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

