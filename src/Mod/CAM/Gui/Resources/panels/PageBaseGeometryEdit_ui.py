# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PageBaseGeometryEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Path_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(476, 342)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setWindowTitle(u"Form")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_BaseGeometry.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.geometryImportList = QComboBox(Form)
        self.geometryImportList.setObjectName(u"geometryImportList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.geometryImportList.sizePolicy().hasHeightForWidth())
        self.geometryImportList.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.geometryImportList, 0, 0, 1, 2)

        self.geometryImportButton = QPushButton(Form)
        self.geometryImportButton.setObjectName(u"geometryImportButton")

        self.gridLayout.addWidget(self.geometryImportButton, 0, 2, 1, 1)

        self.baseList = QListWidget(Form)
        self.baseList.setObjectName(u"baseList")
        self.baseList.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.baseList.sizePolicy().hasHeightForWidth())
        self.baseList.setSizePolicy(sizePolicy2)
        self.baseList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.gridLayout.addWidget(self.baseList, 2, 0, 1, 3)

        self.addBase = QPushButton(Form)
        self.addBase.setObjectName(u"addBase")

        self.gridLayout.addWidget(self.addBase, 3, 0, 1, 1)

        self.deleteBase = QPushButton(Form)
        self.deleteBase.setObjectName(u"deleteBase")

        self.gridLayout.addWidget(self.deleteBase, 3, 1, 1, 1)

        self.clearBase = QPushButton(Form)
        self.clearBase.setObjectName(u"clearBase")

        self.gridLayout.addWidget(self.clearBase, 3, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 6, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
#if QT_CONFIG(tooltip)
        self.geometryImportList.setToolTip(QCoreApplication.translate("Form", u"List of operations with base geometry in the current job", None))
#endif // QT_CONFIG(tooltip)
        self.geometryImportButton.setText(QCoreApplication.translate("Form", u"Import", None))
#if QT_CONFIG(tooltip)
        self.baseList.setToolTip(QCoreApplication.translate("Form", u"Select one or more features in the 3D view and press 'Add' to add them as the base items for this operation. Selected features can be deleted entirely.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.addBase.setToolTip(QCoreApplication.translate("Form", u"Add selected features to the list of base geometries for this operation", None))
#endif // QT_CONFIG(tooltip)
        self.addBase.setText(QCoreApplication.translate("Form", u"Add", None))
#if QT_CONFIG(tooltip)
        self.deleteBase.setToolTip(QCoreApplication.translate("Form", u"Remove the selected list items from the list of base geometries. The operation will not be applied to them.", None))
#endif // QT_CONFIG(tooltip)
        self.deleteBase.setText(QCoreApplication.translate("Form", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.clearBase.setToolTip(QCoreApplication.translate("Form", u"Clears list of base geometries", None))
#endif // QT_CONFIG(tooltip)
        self.clearBase.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Form", u"All objects will be processed using the same operation properties", None))
        pass
    # retranslateUi

