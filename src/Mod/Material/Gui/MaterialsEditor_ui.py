# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MaterialsEditor.ui'
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
    QDialogButtonBox, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QTextEdit, QTreeView, QVBoxLayout, QWidget)

class Ui_MatGui_MaterialsEditor(object):
    def setupUi(self, MatGui__MaterialsEditor):
        if not MatGui__MaterialsEditor.objectName():
            MatGui__MaterialsEditor.setObjectName(u"MatGui__MaterialsEditor")
        MatGui__MaterialsEditor.resize(835, 542)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MatGui__MaterialsEditor.sizePolicy().hasHeightForWidth())
        MatGui__MaterialsEditor.setSizePolicy(sizePolicy)
        MatGui__MaterialsEditor.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(MatGui__MaterialsEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(MatGui__MaterialsEditor)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeMaterials = QTreeView(self.splitter)
        self.treeMaterials.setObjectName(u"treeMaterials")
        self.treeMaterials.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.treeMaterials.setHeaderHidden(True)
        self.splitter.addWidget(self.treeMaterials)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        sizePolicy.setHeightForWidth(self.tabGeneral.sizePolicy().hasHeightForWidth())
        self.tabGeneral.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.tabGeneral)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.labelParent = QLabel(self.tabGeneral)
        self.labelParent.setObjectName(u"labelParent")

        self.gridLayout.addWidget(self.labelParent, 3, 0, 1, 1)

        self.editDescription = QTextEdit(self.tabGeneral)
        self.editDescription.setObjectName(u"editDescription")

        self.gridLayout.addWidget(self.editDescription, 8, 2, 1, 1)

        self.label = QLabel(self.tabGeneral)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.labelSourceURL = QLabel(self.tabGeneral)
        self.labelSourceURL.setObjectName(u"labelSourceURL")

        self.gridLayout.addWidget(self.labelSourceURL, 4, 0, 1, 1)

        self.editName = QLineEdit(self.tabGeneral)
        self.editName.setObjectName(u"editName")

        self.gridLayout.addWidget(self.editName, 0, 2, 1, 1)

        self.labelDescription = QLabel(self.tabGeneral)
        self.labelDescription.setObjectName(u"labelDescription")

        self.gridLayout.addWidget(self.labelDescription, 8, 0, 1, 1)

        self.labelName = QLabel(self.tabGeneral)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.editTags = QLineEdit(self.tabGeneral)
        self.editTags.setObjectName(u"editTags")

        self.gridLayout.addWidget(self.editTags, 6, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.editSourceURL = QLineEdit(self.tabGeneral)
        self.editSourceURL.setObjectName(u"editSourceURL")

        self.horizontalLayout_2.addWidget(self.editSourceURL)

        self.buttonURL = QPushButton(self.tabGeneral)
        self.buttonURL.setObjectName(u"buttonURL")
        self.buttonURL.setMaximumSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.buttonURL)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 2, 1, 1)

        self.editAuthor = QLineEdit(self.tabGeneral)
        self.editAuthor.setObjectName(u"editAuthor")

        self.gridLayout.addWidget(self.editAuthor, 1, 2, 1, 1)

        self.labelAuthor = QLabel(self.tabGeneral)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.gridLayout.addWidget(self.labelAuthor, 1, 0, 1, 1)

        self.editParent = QLineEdit(self.tabGeneral)
        self.editParent.setObjectName(u"editParent")

        self.gridLayout.addWidget(self.editParent, 3, 2, 1, 1)

        self.labelSourceReference = QLabel(self.tabGeneral)
        self.labelSourceReference.setObjectName(u"labelSourceReference")

        self.gridLayout.addWidget(self.labelSourceReference, 5, 0, 1, 1)

        self.editSourceReference = QLineEdit(self.tabGeneral)
        self.editSourceReference.setObjectName(u"editSourceReference")

        self.gridLayout.addWidget(self.editSourceReference, 5, 2, 1, 1)

        self.editLicense = QLineEdit(self.tabGeneral)
        self.editLicense.setObjectName(u"editLicense")

        self.gridLayout.addWidget(self.editLicense, 2, 2, 1, 1)

        self.labelLicense = QLabel(self.tabGeneral)
        self.labelLicense.setObjectName(u"labelLicense")

        self.gridLayout.addWidget(self.labelLicense, 2, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.buttonNew = QPushButton(self.tabGeneral)
        self.buttonNew.setObjectName(u"buttonNew")

        self.horizontalLayout_3.addWidget(self.buttonNew)

        self.buttonInheritNew = QPushButton(self.tabGeneral)
        self.buttonInheritNew.setObjectName(u"buttonInheritNew")

        self.horizontalLayout_3.addWidget(self.buttonInheritNew)

        self.buttonFavorite = QPushButton(self.tabGeneral)
        self.buttonFavorite.setObjectName(u"buttonFavorite")

        self.horizontalLayout_3.addWidget(self.buttonFavorite)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabProperties = QWidget()
        self.tabProperties.setObjectName(u"tabProperties")
        self.verticalLayout_43 = QVBoxLayout(self.tabProperties)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer)

        self.buttonPhysicalAdd = QPushButton(self.tabProperties)
        self.buttonPhysicalAdd.setObjectName(u"buttonPhysicalAdd")
        self.buttonPhysicalAdd.setText(u"+")

        self.horizontalLayout_23.addWidget(self.buttonPhysicalAdd)

        self.buttonPhysicalRemove = QPushButton(self.tabProperties)
        self.buttonPhysicalRemove.setObjectName(u"buttonPhysicalRemove")
        self.buttonPhysicalRemove.setText(u"-")

        self.horizontalLayout_23.addWidget(self.buttonPhysicalRemove)


        self.verticalLayout_43.addLayout(self.horizontalLayout_23)

        self.treePhysicalProperties = QTreeView(self.tabProperties)
        self.treePhysicalProperties.setObjectName(u"treePhysicalProperties")

        self.verticalLayout_43.addWidget(self.treePhysicalProperties)

        self.tabWidget.addTab(self.tabProperties, "")
        self.tabAppearance = QWidget()
        self.tabAppearance.setObjectName(u"tabAppearance")
        self.verticalLayout_42 = QVBoxLayout(self.tabAppearance)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.layoutAppearance = QHBoxLayout()
        self.layoutAppearance.setObjectName(u"layoutAppearance")

        self.verticalLayout_42.addLayout(self.layoutAppearance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.buttonAppearanceAdd = QPushButton(self.tabAppearance)
        self.buttonAppearanceAdd.setObjectName(u"buttonAppearanceAdd")
        self.buttonAppearanceAdd.setText(u"+")

        self.horizontalLayout.addWidget(self.buttonAppearanceAdd)

        self.buttonAppearanceRemove = QPushButton(self.tabAppearance)
        self.buttonAppearanceRemove.setObjectName(u"buttonAppearanceRemove")
        self.buttonAppearanceRemove.setText(u"-")

        self.horizontalLayout.addWidget(self.buttonAppearanceRemove)


        self.verticalLayout_42.addLayout(self.horizontalLayout)

        self.treeAppearance = QTreeView(self.tabAppearance)
        self.treeAppearance.setObjectName(u"treeAppearance")

        self.verticalLayout_42.addWidget(self.treeAppearance)

        self.tabWidget.addTab(self.tabAppearance, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout.addWidget(self.splitter)

        self.standardButtons = QDialogButtonBox(MatGui__MaterialsEditor)
        self.standardButtons.setObjectName(u"standardButtons")
        self.standardButtons.setOrientation(Qt.Horizontal)
        self.standardButtons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.standardButtons)


        self.retranslateUi(MatGui__MaterialsEditor)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MatGui__MaterialsEditor)
    # setupUi

    def retranslateUi(self, MatGui__MaterialsEditor):
        MatGui__MaterialsEditor.setWindowTitle(QCoreApplication.translate("MatGui::MaterialsEditor", u"Materials", None))
        self.labelParent.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Parent", None))
        self.label.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Tags", None))
        self.labelSourceURL.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Source URL", None))
        self.labelDescription.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Description", None))
        self.labelName.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Name", None))
        self.buttonURL.setText("")
        self.labelAuthor.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Author", None))
        self.labelSourceReference.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Source reference", None))
        self.labelLicense.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"License", None))
        self.buttonNew.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"&New", None))
        self.buttonInheritNew.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Inherit New", None))
#if QT_CONFIG(tooltip)
        self.buttonFavorite.setToolTip(QCoreApplication.translate("MatGui::MaterialsEditor", u"Adds or removes to/from favorites", None))
#endif // QT_CONFIG(tooltip)
        self.buttonFavorite.setText(QCoreApplication.translate("MatGui::MaterialsEditor", u"Toggle Favorite", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QCoreApplication.translate("MatGui::MaterialsEditor", u"General", None))
#if QT_CONFIG(tooltip)
        self.buttonPhysicalAdd.setToolTip(QCoreApplication.translate("MatGui::MaterialsEditor", u"Add physical model", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonPhysicalRemove.setToolTip(QCoreApplication.translate("MatGui::MaterialsEditor", u"Delete physical model", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProperties), QCoreApplication.translate("MatGui::MaterialsEditor", u"Physical", None))
#if QT_CONFIG(tooltip)
        self.buttonAppearanceAdd.setToolTip(QCoreApplication.translate("MatGui::MaterialsEditor", u"Add appearance model", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonAppearanceRemove.setToolTip(QCoreApplication.translate("MatGui::MaterialsEditor", u"Delete appearance model", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAppearance), QCoreApplication.translate("MatGui::MaterialsEditor", u"Appearance", None))
    # retranslateUi

