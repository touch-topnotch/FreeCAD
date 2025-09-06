# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssemblyInsertLink.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_TaskAssemblyInsertLink(object):
    def setupUi(self, TaskAssemblyInsertLink):
        if not TaskAssemblyInsertLink.objectName():
            TaskAssemblyInsertLink.setObjectName(u"TaskAssemblyInsertLink")
        TaskAssemblyInsertLink.resize(200, 200)
        self.gridLayout = QGridLayout(TaskAssemblyInsertLink)
        self.gridLayout.setObjectName(u"gridLayout")
        self.filterPartList = QLineEdit(TaskAssemblyInsertLink)
        self.filterPartList.setObjectName(u"filterPartList")

        self.gridLayout.addWidget(self.filterPartList, 0, 0, 1, 1)

        self.partList = QTreeWidget(TaskAssemblyInsertLink)
        self.partList.setObjectName(u"partList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partList.sizePolicy().hasHeightForWidth())
        self.partList.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.partList, 1, 0, 1, 1)

        self.hLayout = QHBoxLayout()
        self.hLayout.setObjectName(u"hLayout")
        self.label1 = QLabel(TaskAssemblyInsertLink)
        self.label1.setObjectName(u"label1")

        self.hLayout.addWidget(self.label1)

        self.openFileButton = QPushButton(TaskAssemblyInsertLink)
        self.openFileButton.setObjectName(u"openFileButton")

        self.hLayout.addWidget(self.openFileButton)


        self.gridLayout.addLayout(self.hLayout, 2, 0, 1, 1)

        self.CheckBox_ShowOnlyParts = Gui_PrefCheckBox(TaskAssemblyInsertLink)
        self.CheckBox_ShowOnlyParts.setObjectName(u"CheckBox_ShowOnlyParts")
        self.CheckBox_ShowOnlyParts.setChecked(False)
        self.CheckBox_ShowOnlyParts.setProperty(u"prefEntry", u"InsertShowOnlyParts")
        self.CheckBox_ShowOnlyParts.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_ShowOnlyParts, 3, 0, 1, 1)

        self.CheckBox_RigidSubAsm = Gui_PrefCheckBox(TaskAssemblyInsertLink)
        self.CheckBox_RigidSubAsm.setObjectName(u"CheckBox_RigidSubAsm")
        self.CheckBox_RigidSubAsm.setChecked(True)
        self.CheckBox_RigidSubAsm.setProperty(u"prefEntry", u"InsertRigidSubAssemblies")
        self.CheckBox_RigidSubAsm.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_RigidSubAsm, 4, 0, 1, 1)


        self.retranslateUi(TaskAssemblyInsertLink)

        QMetaObject.connectSlotsByName(TaskAssemblyInsertLink)
    # setupUi

    def retranslateUi(self, TaskAssemblyInsertLink):
        TaskAssemblyInsertLink.setWindowTitle(QCoreApplication.translate("TaskAssemblyInsertLink", u"Insert", None))
        self.filterPartList.setPlaceholderText(QCoreApplication.translate("TaskAssemblyInsertLink", u"Search parts\u2026", None))
        self.label1.setText(QCoreApplication.translate("TaskAssemblyInsertLink", u"Cannot find the part? ", None))
        self.openFileButton.setText(QCoreApplication.translate("TaskAssemblyInsertLink", u"Open File", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_ShowOnlyParts.setToolTip(QCoreApplication.translate("TaskAssemblyInsertLink", u"Shows only parts in the list", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_ShowOnlyParts.setText(QCoreApplication.translate("TaskAssemblyInsertLink", u"Show only parts", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_RigidSubAsm.setToolTip(QCoreApplication.translate("TaskAssemblyInsertLink", u"Sets whether the inserted sub-assemblies will be rigid or flexible.\n"
"Rigid means that the added sub-assembly will be considered as a solid unit within the parent assembly.\n"
"Flexible means that the added sub-assembly will allow movement of its individual components' joints within the parent assembly.\n"
"You can change this behavior at any time by either right-clicking the sub-assembly on the document tree and toggling the\n"
"'Turn rigid'/'Turn flexible' command there, or by editing its Rigid property in the property editor.", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_RigidSubAsm.setText(QCoreApplication.translate("TaskAssemblyInsertLink", u"Rigid sub-assemblies", None))
    # retranslateUi

