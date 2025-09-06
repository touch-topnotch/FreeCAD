# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolBitLibraryEdit.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QTreeView, QVBoxLayout,
    QWidget)
import resource_rc
import Path_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(954, 587)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.toolCreate = QPushButton(Dialog)
        self.toolCreate.setObjectName(u"toolCreate")
        icon = QIcon()
        icon.addFile(u":/icons/CAM_ToolBit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolCreate.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.toolCreate)

        self.toolAdd = QPushButton(Dialog)
        self.toolAdd.setObjectName(u"toolAdd")
        self.toolAdd.setMaximumSize(QSize(16777215, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/CAM_ToolDuplicate.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolAdd.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.toolAdd)

        self.toolDelete = QPushButton(Dialog)
        self.toolDelete.setObjectName(u"toolDelete")
        self.toolDelete.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/list-remove.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolDelete.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.toolDelete)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.toolTableGroup = QWidget(Dialog)
        self.toolTableGroup.setObjectName(u"toolTableGroup")
        self.horizontalLayout_3 = QHBoxLayout(self.toolTableGroup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addLibrary = QPushButton(self.toolTableGroup)
        self.addLibrary.setObjectName(u"addLibrary")
        self.addLibrary.setMaximumSize(QSize(16777215, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icons/document-new.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addLibrary.setIcon(icon3)
        self.addLibrary.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.addLibrary)

        self.exportLibrary = QPushButton(self.toolTableGroup)
        self.exportLibrary.setObjectName(u"exportLibrary")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Std_Export.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportLibrary.setIcon(icon4)

        self.verticalLayout.addWidget(self.exportLibrary)

        self.saveLibrary = QPushButton(self.toolTableGroup)
        self.saveLibrary.setObjectName(u"saveLibrary")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveLibrary.sizePolicy().hasHeightForWidth())
        self.saveLibrary.setSizePolicy(sizePolicy)
        self.saveLibrary.setMaximumSize(QSize(16777215, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/document-save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveLibrary.setIcon(icon5)

        self.verticalLayout.addWidget(self.saveLibrary)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.TableList = QTreeView(self.toolTableGroup)
        self.TableList.setObjectName(u"TableList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TableList.sizePolicy().hasHeightForWidth())
        self.TableList.setSizePolicy(sizePolicy1)
        self.TableList.setFrameShape(QFrame.Box)
        self.TableList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TableList.setProperty(u"showDropIndicator", False)

        self.horizontalLayout_3.addWidget(self.TableList)

        self.toolTable = QTableView(self.toolTableGroup)
        self.toolTable.setObjectName(u"toolTable")
        self.toolTable.setAcceptDrops(True)
        self.toolTable.setFrameShape(QFrame.Box)
        self.toolTable.setFrameShadow(QFrame.Sunken)
        self.toolTable.setLineWidth(1)
        self.toolTable.setMidLineWidth(0)
        self.toolTable.setDragEnabled(False)
        self.toolTable.setDragDropOverwriteMode(False)
        self.toolTable.setDragDropMode(QAbstractItemView.DragOnly)
        self.toolTable.setDefaultDropAction(Qt.IgnoreAction)
        self.toolTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.toolTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.toolTable.setSortingEnabled(True)
        self.toolTable.verticalHeader().setVisible(False)
        self.toolTable.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_3.addWidget(self.toolTable)


        self.verticalLayout_2.addWidget(self.toolTableGroup)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(65555555, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.okButton = QPushButton(Dialog)
        self.okButton.setObjectName(u"okButton")
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setMaximumSize(QSize(16777215, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/icons/edit_OK.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.okButton.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.okButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Library Manager", None))
        self.toolCreate.setText(QCoreApplication.translate("Dialog", u"Create Toolbit", None))
#if QT_CONFIG(tooltip)
        self.toolAdd.setToolTip(QCoreApplication.translate("Dialog", u"Adds the existing tool bit to the library", None))
#endif // QT_CONFIG(tooltip)
        self.toolAdd.setText(QCoreApplication.translate("Dialog", u"Add Existing", None))
#if QT_CONFIG(tooltip)
        self.toolDelete.setToolTip(QCoreApplication.translate("Dialog", u"Deletes the selected tool bits from the library", None))
#endif // QT_CONFIG(tooltip)
        self.toolDelete.setText(QCoreApplication.translate("Dialog", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.addLibrary.setToolTip(QCoreApplication.translate("Dialog", u"Add new tool table", None))
#endif // QT_CONFIG(tooltip)
        self.addLibrary.setText("")
#if QT_CONFIG(tooltip)
        self.exportLibrary.setToolTip(QCoreApplication.translate("Dialog", u"Save the selected library with a new name or export to another format", None))
#endif // QT_CONFIG(tooltip)
        self.exportLibrary.setText("")
#if QT_CONFIG(tooltip)
        self.saveLibrary.setToolTip(QCoreApplication.translate("Dialog", u"Save the current library", None))
#endif // QT_CONFIG(tooltip)
        self.saveLibrary.setText("")
#if QT_CONFIG(tooltip)
        self.toolTable.setToolTip(QCoreApplication.translate("Dialog", u"Table of tool bits of the library", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.okButton.setToolTip(QCoreApplication.translate("Dialog", u"Close the library editor", None))
#endif // QT_CONFIG(tooltip)
        self.okButton.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

