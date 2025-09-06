# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogWindows.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(245, 538)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.groupMode = QComboBox(Form)
        icon = QIcon()
        iconThemeName = u"cancel"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon, "")
        icon1 = QIcon()
        iconThemeName = u"up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon1, "")
        icon2 = QIcon()
        iconThemeName = u"user"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon2, "")
        icon3 = QIcon()
        iconThemeName = u"contact"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon3, "")
        icon4 = QIcon()
        iconThemeName = u"edit-clear"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon4, "")
        self.groupMode.setObjectName(u"groupMode")

        self.horizontalLayout.addWidget(self.groupMode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.windowsCount = QLabel(Form)
        self.windowsCount.setObjectName(u"windowsCount")
        self.windowsCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.windowsCount, 0, 1, 1, 1)

        self.doorsCount = QLabel(Form)
        self.doorsCount.setObjectName(u"doorsCount")
        self.doorsCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.doorsCount, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.windows = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Label");
        self.windows.setHeaderItem(__qtreewidgetitem)
        self.windows.setObjectName(u"windows")
        self.windows.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.windows.setColumnCount(2)
        self.windows.header().setVisible(False)
        self.windows.header().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.windows)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.windowMaterial = QPushButton(Form)
        self.windowMaterial.setObjectName(u"windowMaterial")

        self.gridLayout.addWidget(self.windowMaterial, 5, 1, 1, 1)

        self.windowTag = QLineEdit(Form)
        self.windowTag.setObjectName(u"windowTag")

        self.gridLayout.addWidget(self.windowTag, 4, 1, 1, 1)

        self.windowDescription = QLineEdit(Form)
        self.windowDescription.setObjectName(u"windowDescription")

        self.gridLayout.addWidget(self.windowDescription, 3, 1, 1, 1)

        self.windowLabel = QLineEdit(Form)
        self.windowLabel.setObjectName(u"windowLabel")

        self.gridLayout.addWidget(self.windowLabel, 2, 1, 1, 1)

        self.windowWidth = Gui_InputField(Form)
        self.windowWidth.setObjectName(u"windowWidth")
        self.windowWidth.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.windowWidth, 0, 1, 1, 1)

        self.windowHeight = Gui_InputField(Form)
        self.windowHeight.setObjectName(u"windowHeight")
        self.windowHeight.setProperty(u"unit", u"")

        self.gridLayout.addWidget(self.windowHeight, 1, 1, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)

        self.labelSpaces = QLabel(Form)
        self.labelSpaces.setObjectName(u"labelSpaces")
        self.labelSpaces.setWordWrap(True)

        self.gridLayout.addWidget(self.labelSpaces, 6, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Doors and Windows", None))
        self.label.setText(QCoreApplication.translate("Form", u"This screen lists all the windows of the current document. They can modified individually or together", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Group by", None))
        self.groupMode.setItemText(0, QCoreApplication.translate("Form", u"Do not group", None))
        self.groupMode.setItemText(1, QCoreApplication.translate("Form", u"Size", None))
        self.groupMode.setItemText(2, QCoreApplication.translate("Form", u"Clone", None))
        self.groupMode.setItemText(3, QCoreApplication.translate("Form", u"Tag", None))
        self.groupMode.setItemText(4, QCoreApplication.translate("Form", u"Material", None))

        self.label_10.setText(QCoreApplication.translate("Form", u"Total number of doors", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Total number of windows", None))
        self.windowsCount.setText(QCoreApplication.translate("Form", u"0", None))
        self.doorsCount.setText(QCoreApplication.translate("Form", u"0", None))
        ___qtreewidgetitem = self.windows.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"Tag", None));
        self.label_3.setText(QCoreApplication.translate("Form", u"Width", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Label", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Height", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Material", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Tag", None))
        self.windowMaterial.setText(QCoreApplication.translate("Form", u"None", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Spaces", None))
        self.labelSpaces.setText(QCoreApplication.translate("Form", u"None", None))
    # retranslateUi

