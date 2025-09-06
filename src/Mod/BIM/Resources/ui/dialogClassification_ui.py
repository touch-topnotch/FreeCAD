# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogClassification.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSplitter, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_bimDialogClassification(object):
    def setupUi(self, bimDialogClassification):
        if not bimDialogClassification.objectName():
            bimDialogClassification.setObjectName(u"bimDialogClassification")
        bimDialogClassification.resize(629, 516)
        self.verticalLayout = QVBoxLayout(bimDialogClassification)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(bimDialogClassification)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupMaterials = QGroupBox(self.splitter)
        self.groupMaterials.setObjectName(u"groupMaterials")
        self.groupMaterials.setMinimumSize(QSize(300, 0))
        self.groupMaterials.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupMaterials)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.onlyVisible = QCheckBox(self.groupMaterials)
        self.onlyVisible.setObjectName(u"onlyVisible")
        self.onlyVisible.setChecked(True)

        self.verticalLayout_2.addWidget(self.onlyVisible)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupMaterials)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.groupMode = QComboBox(self.groupMaterials)
        icon = QIcon()
        iconThemeName = u"format-text-direction-ltr"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon, "")
        icon1 = QIcon()
        iconThemeName = u"application-drawing"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.groupMode.addItem(icon1, "")
        self.groupMode.addItem("")
        self.groupMode.addItem("")
        self.groupMode.setObjectName(u"groupMode")

        self.horizontalLayout_4.addWidget(self.groupMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.treeObjects = QTreeWidget(self.groupMaterials)
        self.treeObjects.setObjectName(u"treeObjects")
        self.treeObjects.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeObjects.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.treeObjects.setAutoExpandDelay(-1)
        self.treeObjects.header().setCascadingSectionResizes(True)
        self.treeObjects.header().setDefaultSectionSize(200)
        self.treeObjects.header().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.treeObjects)

        self.splitter.addWidget(self.groupMaterials)
        self.groupClasses = QGroupBox(self.splitter)
        self.groupClasses.setObjectName(u"groupClasses")
        self.verticalLayout_3 = QVBoxLayout(self.groupClasses)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboSystem = QComboBox(self.groupClasses)
        self.comboSystem.setObjectName(u"comboSystem")

        self.verticalLayout_3.addWidget(self.comboSystem)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.treeClass = QTreeWidget(self.groupClasses)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeClass.setHeaderItem(__qtreewidgetitem)
        self.treeClass.setObjectName(u"treeClass")
        self.treeClass.header().setVisible(False)

        self.verticalLayout_3.addWidget(self.treeClass)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonApply = QPushButton(self.groupClasses)
        self.buttonApply.setObjectName(u"buttonApply")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonApply.sizePolicy().hasHeightForWidth())
        self.buttonApply.setSizePolicy(sizePolicy1)
        self.buttonApply.setMinimumSize(QSize(16, 0))

        self.horizontalLayout_3.addWidget(self.buttonApply)

        self.buttonRename = QPushButton(self.groupClasses)
        self.buttonRename.setObjectName(u"buttonRename")

        self.horizontalLayout_3.addWidget(self.buttonRename)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.checkPrefix = QCheckBox(self.groupClasses)
        self.checkPrefix.setObjectName(u"checkPrefix")
        self.checkPrefix.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkPrefix)

        self.splitter.addWidget(self.groupClasses)

        self.verticalLayout.addWidget(self.splitter)

        self.labelDownload = QLabel(bimDialogClassification)
        self.labelDownload.setObjectName(u"labelDownload")
        self.labelDownload.setWordWrap(True)
        self.labelDownload.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.labelDownload)

        self.buttonBox = QDialogButtonBox(bimDialogClassification)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(bimDialogClassification)
        self.buttonBox.rejected.connect(bimDialogClassification.reject)

        QMetaObject.connectSlotsByName(bimDialogClassification)
    # setupUi

    def retranslateUi(self, bimDialogClassification):
        bimDialogClassification.setWindowTitle(QCoreApplication.translate("bimDialogClassification", u"Classification Manager", None))
        self.groupMaterials.setTitle(QCoreApplication.translate("bimDialogClassification", u"Objects && Materials", None))
        self.onlyVisible.setText(QCoreApplication.translate("bimDialogClassification", u"Only visible objects", None))
        self.label.setText(QCoreApplication.translate("bimDialogClassification", u"Sort by", None))
        self.groupMode.setItemText(0, QCoreApplication.translate("bimDialogClassification", u"Alphabetical", None))
        self.groupMode.setItemText(1, QCoreApplication.translate("bimDialogClassification", u"IFC type", None))
        self.groupMode.setItemText(2, QCoreApplication.translate("bimDialogClassification", u"Material", None))
        self.groupMode.setItemText(3, QCoreApplication.translate("bimDialogClassification", u"Model structure", None))

        ___qtreewidgetitem = self.treeObjects.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("bimDialogClassification", u"Class", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("bimDialogClassification", u"Object/Material", None));
        self.groupClasses.setTitle(QCoreApplication.translate("bimDialogClassification", u"Available classification systems", None))
#if QT_CONFIG(tooltip)
        self.comboSystem.setToolTip(QCoreApplication.translate("bimDialogClassification", u"Classification systems found on this computer", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonApply.setToolTip(QCoreApplication.translate("bimDialogClassification", u"Apply the selected class to selected objects", None))
#endif // QT_CONFIG(tooltip)
        self.buttonApply.setText(QCoreApplication.translate("bimDialogClassification", u"<< Apply to Selected", None))
#if QT_CONFIG(tooltip)
        self.buttonRename.setToolTip(QCoreApplication.translate("bimDialogClassification", u"Use this class as object name", None))
#endif // QT_CONFIG(tooltip)
        self.buttonRename.setText(QCoreApplication.translate("bimDialogClassification", u"<< Set as Name", None))
        self.checkPrefix.setText(QCoreApplication.translate("bimDialogClassification", u"Prefix with classification system name", None))
        self.labelDownload.setText(QCoreApplication.translate("bimDialogClassification", u"XML or IFC files of several classification systems can be downloaded from <a href=\"https://github.com/Moult/IfcClassification\">https://github.com/Moult/IfcClassification</a> and placed in %s", None))
    # retranslateUi

