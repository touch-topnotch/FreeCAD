# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModelSelect.ui'
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTabWidget, QTableView, QTextEdit,
    QTreeView, QVBoxLayout, QWidget)

class Ui_MatGui_ModelSelect(object):
    def setupUi(self, MatGui__ModelSelect):
        if not MatGui__ModelSelect.objectName():
            MatGui__ModelSelect.setObjectName(u"MatGui__ModelSelect")
        MatGui__ModelSelect.resize(705, 489)
        self.verticalLayout = QVBoxLayout(MatGui__ModelSelect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(MatGui__ModelSelect)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeModels = QTreeView(self.splitter)
        self.treeModels.setObjectName(u"treeModels")
        self.splitter.addWidget(self.treeModels)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabGeneral.sizePolicy().hasHeightForWidth())
        self.tabGeneral.setSizePolicy(sizePolicy)
        self.tabGeneral.setMaximumSize(QSize(365, 409))
        self.verticalLayout_2 = QVBoxLayout(self.tabGeneral)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelURL = QLabel(self.tabGeneral)
        self.labelURL.setObjectName(u"labelURL")

        self.gridLayout.addWidget(self.labelURL, 1, 0, 1, 1)

        self.label = QLabel(self.tabGeneral)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.labelDOI = QLabel(self.tabGeneral)
        self.labelDOI.setObjectName(u"labelDOI")

        self.gridLayout.addWidget(self.labelDOI, 2, 0, 1, 1)

        self.editDescription = QTextEdit(self.tabGeneral)
        self.editDescription.setObjectName(u"editDescription")
        self.editDescription.setReadOnly(True)

        self.gridLayout.addWidget(self.editDescription, 3, 1, 1, 1)

        self.editName = QLineEdit(self.tabGeneral)
        self.editName.setObjectName(u"editName")
        self.editName.setEnabled(True)
        self.editName.setReadOnly(True)

        self.gridLayout.addWidget(self.editName, 0, 1, 1, 1)

        self.labelName = QLabel(self.tabGeneral)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.editDOI = QLineEdit(self.tabGeneral)
        self.editDOI.setObjectName(u"editDOI")
        self.editDOI.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.editDOI)

        self.buttonDOI = QPushButton(self.tabGeneral)
        self.buttonDOI.setObjectName(u"buttonDOI")
        self.buttonDOI.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_3.addWidget(self.buttonDOI)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.editURL = QLineEdit(self.tabGeneral)
        self.editURL.setObjectName(u"editURL")
        self.editURL.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.editURL)

        self.buttonURL = QPushButton(self.tabGeneral)
        self.buttonURL.setObjectName(u"buttonURL")
        self.buttonURL.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.buttonURL)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonFavorite = QPushButton(self.tabGeneral)
        self.buttonFavorite.setObjectName(u"buttonFavorite")

        self.horizontalLayout.addWidget(self.buttonFavorite)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabProperties = QWidget()
        self.tabProperties.setObjectName(u"tabProperties")
        self.verticalLayout_3 = QVBoxLayout(self.tabProperties)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableProperties = QTableView(self.tabProperties)
        self.tableProperties.setObjectName(u"tableProperties")

        self.verticalLayout_3.addWidget(self.tableProperties)

        self.tabWidget.addTab(self.tabProperties, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout.addWidget(self.splitter)

        self.standardButtons = QDialogButtonBox(MatGui__ModelSelect)
        self.standardButtons.setObjectName(u"standardButtons")
        self.standardButtons.setOrientation(Qt.Horizontal)
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.standardButtons)


        self.retranslateUi(MatGui__ModelSelect)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MatGui__ModelSelect)
    # setupUi

    def retranslateUi(self, MatGui__ModelSelect):
        MatGui__ModelSelect.setWindowTitle(QCoreApplication.translate("MatGui::ModelSelect", u"Material Models", None))
        self.labelURL.setText(QCoreApplication.translate("MatGui::ModelSelect", u"URL", None))
        self.label.setText(QCoreApplication.translate("MatGui::ModelSelect", u"Description", None))
        self.labelDOI.setText(QCoreApplication.translate("MatGui::ModelSelect", u"DOI", None))
        self.labelName.setText(QCoreApplication.translate("MatGui::ModelSelect", u"Name", None))
        self.buttonDOI.setText("")
        self.buttonURL.setText("")
#if QT_CONFIG(tooltip)
        self.buttonFavorite.setToolTip(QCoreApplication.translate("MatGui::ModelSelect", u"Adds or removes to/from favorites", None))
#endif // QT_CONFIG(tooltip)
        self.buttonFavorite.setText(QCoreApplication.translate("MatGui::ModelSelect", u"Toggle Favorites", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QCoreApplication.translate("MatGui::ModelSelect", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProperties), QCoreApplication.translate("MatGui::ModelSelect", u"Properties", None))
    # retranslateUi

