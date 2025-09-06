# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgBooleanOperation.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_PartGui_DlgBooleanOperation(object):
    def setupUi(self, PartGui__DlgBooleanOperation):
        if not PartGui__DlgBooleanOperation.objectName():
            PartGui__DlgBooleanOperation.setObjectName(u"PartGui__DlgBooleanOperation")
        PartGui__DlgBooleanOperation.resize(264, 408)
        self.gridLayout = QGridLayout(PartGui__DlgBooleanOperation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(PartGui__DlgBooleanOperation)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout1 = QGridLayout(self.groupBox)
#ifndef Q_OS_MAC
        self.gridLayout1.setSpacing(6)
#endif
#ifndef Q_OS_MAC
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
#endif
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.unionButton = QRadioButton(self.groupBox)
        self.unionButton.setObjectName(u"unionButton")
        self.unionButton.setChecked(True)

        self.gridLayout1.addWidget(self.unionButton, 0, 0, 1, 1)

        self.diffButton = QRadioButton(self.groupBox)
        self.diffButton.setObjectName(u"diffButton")

        self.gridLayout1.addWidget(self.diffButton, 0, 1, 1, 1)

        self.interButton = QRadioButton(self.groupBox)
        self.interButton.setObjectName(u"interButton")

        self.gridLayout1.addWidget(self.interButton, 1, 0, 1, 1)

        self.sectionButton = QRadioButton(self.groupBox)
        self.sectionButton.setObjectName(u"sectionButton")

        self.gridLayout1.addWidget(self.sectionButton, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.firstShape = QTreeWidget(PartGui__DlgBooleanOperation)
        QTreeWidgetItem(self.firstShape)
        QTreeWidgetItem(self.firstShape)
        QTreeWidgetItem(self.firstShape)
        QTreeWidgetItem(self.firstShape)
        self.firstShape.setObjectName(u"firstShape")
        self.firstShape.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.EditKeyPressed)
        self.firstShape.setRootIsDecorated(False)
        self.firstShape.setExpandsOnDoubleClick(False)

        self.gridLayout.addWidget(self.firstShape, 1, 0, 1, 1)

        self.secondShape = QTreeWidget(PartGui__DlgBooleanOperation)
        QTreeWidgetItem(self.secondShape)
        QTreeWidgetItem(self.secondShape)
        QTreeWidgetItem(self.secondShape)
        QTreeWidgetItem(self.secondShape)
        self.secondShape.setObjectName(u"secondShape")
        self.secondShape.setEditTriggers(QAbstractItemView.CurrentChanged|QAbstractItemView.EditKeyPressed)
        self.secondShape.setRootIsDecorated(False)
        self.secondShape.setExpandsOnDoubleClick(False)

        self.gridLayout.addWidget(self.secondShape, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(117, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.swapButton = QPushButton(PartGui__DlgBooleanOperation)
        self.swapButton.setObjectName(u"swapButton")

        self.gridLayout.addWidget(self.swapButton, 2, 1, 1, 1)


        self.retranslateUi(PartGui__DlgBooleanOperation)

        QMetaObject.connectSlotsByName(PartGui__DlgBooleanOperation)
    # setupUi

    def retranslateUi(self, PartGui__DlgBooleanOperation):
        PartGui__DlgBooleanOperation.setWindowTitle(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Boolean Operation", None))
        self.groupBox.setTitle(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Boolean Operation", None))
        self.unionButton.setText(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Union", None))
        self.diffButton.setText(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Difference", None))
        self.interButton.setText(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Intersection", None))
        self.sectionButton.setText(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Section", None))
        ___qtreewidgetitem = self.firstShape.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"First shape", None));

        __sortingEnabled = self.firstShape.isSortingEnabled()
        self.firstShape.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.firstShape.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Solids", None));
        ___qtreewidgetitem2 = self.firstShape.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Shells", None));
        ___qtreewidgetitem3 = self.firstShape.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Compounds", None));
        ___qtreewidgetitem4 = self.firstShape.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Faces", None));
        self.firstShape.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem5 = self.secondShape.headerItem()
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Second shape", None));

        __sortingEnabled1 = self.secondShape.isSortingEnabled()
        self.secondShape.setSortingEnabled(False)
        ___qtreewidgetitem6 = self.secondShape.topLevelItem(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Solids", None));
        ___qtreewidgetitem7 = self.secondShape.topLevelItem(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Shells", None));
        ___qtreewidgetitem8 = self.secondShape.topLevelItem(2)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Compounds", None));
        ___qtreewidgetitem9 = self.secondShape.topLevelItem(3)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Faces", None));
        self.secondShape.setSortingEnabled(__sortingEnabled1)

        self.swapButton.setText(QCoreApplication.translate("PartGui::DlgBooleanOperation", u"Swap Selection", None))
    # retranslateUi

