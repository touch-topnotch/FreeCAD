# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageOpPocketExtEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(430, 617)
        Form.setWindowTitle(u"Form")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.enableExtensions = QCheckBox(Form)
        self.enableExtensions.setObjectName(u"enableExtensions")
        self.enableExtensions.setCheckable(True)
        self.enableExtensions.setChecked(False)

        self.horizontalLayout_2.addWidget(self.enableExtensions)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.extensionEdit = QWidget(Form)
        self.extensionEdit.setObjectName(u"extensionEdit")
        self.verticalLayout_2 = QVBoxLayout(self.extensionEdit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.extensionEdit)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.showExtensions = QCheckBox(self.widget_2)
        self.showExtensions.setObjectName(u"showExtensions")

        self.gridLayout.addWidget(self.showExtensions, 2, 0, 1, 1)

        self.extendCorners = QCheckBox(self.widget_2)
        self.extendCorners.setObjectName(u"extendCorners")
        self.extendCorners.setChecked(True)

        self.gridLayout.addWidget(self.extendCorners, 2, 1, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.defaultLength = Gui_QuantitySpinBox(self.widget_2)
        self.defaultLength.setObjectName(u"defaultLength")
        self.defaultLength.setMinimum(-999999999.000000000000000)
        self.defaultLength.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.defaultLength, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.extensionTree = QTreeView(self.extensionEdit)
        self.extensionTree.setObjectName(u"extensionTree")
        self.extensionTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.extensionTree.setTabKeyNavigation(True)
        self.extensionTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.extensionTree.setHeaderHidden(True)
        self.extensionTree.header().setHighlightSections(True)

        self.verticalLayout_2.addWidget(self.extensionTree)

        self.widget = QWidget(self.extensionEdit)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonEnable = QPushButton(self.widget)
        self.buttonEnable.setObjectName(u"buttonEnable")

        self.horizontalLayout.addWidget(self.buttonEnable)

        self.buttonDisable = QPushButton(self.widget)
        self.buttonDisable.setObjectName(u"buttonDisable")

        self.horizontalLayout.addWidget(self.buttonDisable)

        self.buttonClear = QPushButton(self.widget)
        self.buttonClear.setObjectName(u"buttonClear")

        self.horizontalLayout.addWidget(self.buttonClear)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.extensionEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.enableExtensions.setText(QCoreApplication.translate("Form", u"Enable extensions", None))
#if QT_CONFIG(tooltip)
        self.showExtensions.setToolTip(QCoreApplication.translate("Form", u"If selected all potential extensions are visualised. Enabled extensions in purple and not enabled extensions in yellow", None))
#endif // QT_CONFIG(tooltip)
        self.showExtensions.setText(QCoreApplication.translate("Form", u"Show All", None))
#if QT_CONFIG(tooltip)
        self.extendCorners.setToolTip(QCoreApplication.translate("Form", u"Extend the corner between two edges of a pocket. Selected adjacent edges are combined.", None))
#endif // QT_CONFIG(tooltip)
        self.extendCorners.setText(QCoreApplication.translate("Form", u"Extend corners", None))
        self.label.setText(QCoreApplication.translate("Form", u"Default length", None))
#if QT_CONFIG(tooltip)
        self.defaultLength.setToolTip(QCoreApplication.translate("Form", u"Set the extent of the dimension. The default value is half the tool diameter.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.extensionTree.setToolTip(QCoreApplication.translate("Form", u"Tree of existing edges and their potential extensions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonEnable.setToolTip(QCoreApplication.translate("Form", u"Enable the currently selected pocket extension", None))
#endif // QT_CONFIG(tooltip)
        self.buttonEnable.setText(QCoreApplication.translate("Form", u"Enable", None))
#if QT_CONFIG(tooltip)
        self.buttonDisable.setToolTip(QCoreApplication.translate("Form", u"Disable the currently selected pocket extension", None))
#endif // QT_CONFIG(tooltip)
        self.buttonDisable.setText(QCoreApplication.translate("Form", u"Disable", None))
#if QT_CONFIG(tooltip)
        self.buttonClear.setToolTip(QCoreApplication.translate("Form", u"Remove all currently enabled extensions - leaving the plain pocket operation", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClear.setText(QCoreApplication.translate("Form", u"Clear", None))
        pass
    # retranslateUi

