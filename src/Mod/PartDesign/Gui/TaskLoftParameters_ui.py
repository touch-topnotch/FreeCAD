# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskLoftParameters.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGroupBox, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_PartDesignGui_TaskLoftParameters(object):
    def setupUi(self, PartDesignGui__TaskLoftParameters):
        if not PartDesignGui__TaskLoftParameters.objectName():
            PartDesignGui__TaskLoftParameters.setObjectName(u"PartDesignGui__TaskLoftParameters")
        PartDesignGui__TaskLoftParameters.resize(262, 293)
        PartDesignGui__TaskLoftParameters.setWindowTitle(u"Form")
        self.verticalLayout_3 = QVBoxLayout(PartDesignGui__TaskLoftParameters)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBoxRuled = QCheckBox(PartDesignGui__TaskLoftParameters)
        self.checkBoxRuled.setObjectName(u"checkBoxRuled")

        self.verticalLayout_3.addWidget(self.checkBoxRuled)

        self.checkBoxClosed = QCheckBox(PartDesignGui__TaskLoftParameters)
        self.checkBoxClosed.setObjectName(u"checkBoxClosed")

        self.verticalLayout_3.addWidget(self.checkBoxClosed)

        self.groupprofile = QGroupBox(PartDesignGui__TaskLoftParameters)
        self.groupprofile.setObjectName(u"groupprofile")
        self.vboxLayout = QVBoxLayout(self.groupprofile)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.buttonProfileBase = QToolButton(self.groupprofile)
        self.buttonProfileBase.setObjectName(u"buttonProfileBase")
        self.buttonProfileBase.setCheckable(True)

        self.hboxLayout.addWidget(self.buttonProfileBase)

        self.profileBaseEdit = QLineEdit(self.groupprofile)
        self.profileBaseEdit.setObjectName(u"profileBaseEdit")

        self.hboxLayout.addWidget(self.profileBaseEdit)


        self.vboxLayout.addLayout(self.hboxLayout)


        self.verticalLayout_3.addWidget(self.groupprofile)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonRefAdd = QToolButton(PartDesignGui__TaskLoftParameters)
        self.buttonRefAdd.setObjectName(u"buttonRefAdd")
        self.buttonRefAdd.setEnabled(True)
        self.buttonRefAdd.setCheckable(True)
        self.buttonRefAdd.setChecked(False)

        self.horizontalLayout_4.addWidget(self.buttonRefAdd)

        self.buttonRefRemove = QToolButton(PartDesignGui__TaskLoftParameters)
        self.buttonRefRemove.setObjectName(u"buttonRefRemove")
        self.buttonRefRemove.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.buttonRefRemove)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.listWidgetReferences = QListWidget(PartDesignGui__TaskLoftParameters)
        self.listWidgetReferences.setObjectName(u"listWidgetReferences")
        self.listWidgetReferences.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout_3.addWidget(self.listWidgetReferences)

        self.line = QFrame(PartDesignGui__TaskLoftParameters)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.checkBoxUpdateView = QCheckBox(PartDesignGui__TaskLoftParameters)
        self.checkBoxUpdateView.setObjectName(u"checkBoxUpdateView")
        self.checkBoxUpdateView.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkBoxUpdateView)

        QWidget.setTabOrder(self.checkBoxRuled, self.checkBoxClosed)
        QWidget.setTabOrder(self.checkBoxClosed, self.buttonProfileBase)
        QWidget.setTabOrder(self.buttonProfileBase, self.profileBaseEdit)
        QWidget.setTabOrder(self.profileBaseEdit, self.buttonRefAdd)
        QWidget.setTabOrder(self.buttonRefAdd, self.buttonRefRemove)
        QWidget.setTabOrder(self.buttonRefRemove, self.listWidgetReferences)
        QWidget.setTabOrder(self.listWidgetReferences, self.checkBoxUpdateView)

        self.retranslateUi(PartDesignGui__TaskLoftParameters)

        QMetaObject.connectSlotsByName(PartDesignGui__TaskLoftParameters)
    # setupUi

    def retranslateUi(self, PartDesignGui__TaskLoftParameters):
        self.checkBoxRuled.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Ruled surface", None))
        self.checkBoxClosed.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Closed", None))
        self.groupprofile.setTitle(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Profile", None))
        self.buttonProfileBase.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Object", None))
        self.buttonRefAdd.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Add Section", None))
        self.buttonRefRemove.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Remove Section", None))
#if QT_CONFIG(tooltip)
        self.listWidgetReferences.setToolTip(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"List can be reordered by dragging", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxUpdateView.setText(QCoreApplication.translate("PartDesignGui::TaskLoftParameters", u"Recompute on change", None))
        pass
    # retranslateUi

