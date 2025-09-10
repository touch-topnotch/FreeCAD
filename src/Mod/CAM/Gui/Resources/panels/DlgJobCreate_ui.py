# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgJobCreate.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHeaderView, QSizePolicy, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(532, 616)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(Dialog)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.templateGroup = QGroupBox(self.widget_4)
        self.templateGroup.setObjectName(u"templateGroup")
        self.verticalLayout = QVBoxLayout(self.templateGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.jobTemplate = QComboBox(self.templateGroup)
        self.jobTemplate.setObjectName(u"jobTemplate")
        self.jobTemplate.setEnabled(True)

        self.verticalLayout.addWidget(self.jobTemplate)


        self.gridLayout_2.addWidget(self.templateGroup, 0, 0, 1, 1)

        self.modelGroup = QGroupBox(self.widget_4)
        self.modelGroup.setObjectName(u"modelGroup")
        self.verticalLayout_6 = QVBoxLayout(self.modelGroup)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.modelTree = QTreeView(self.modelGroup)
        self.modelTree.setObjectName(u"modelTree")
        self.modelTree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.modelTree.setTabKeyNavigation(True)

        self.verticalLayout_6.addWidget(self.modelTree)


        self.gridLayout_2.addWidget(self.modelGroup, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create Job", None))
        self.templateGroup.setTitle(QCoreApplication.translate("Dialog", u"Template", None))
#if QT_CONFIG(tooltip)
        self.jobTemplate.setToolTip(QCoreApplication.translate("Dialog", u"Select a template to be used for the job. In case there are no templates you can create one through the popup menu of an existing job. Name the file job_*.json and place it in the macro or the path directory (see preferences) in order to be selectable from this list.", None))
#endif // QT_CONFIG(tooltip)
        self.modelGroup.setTitle(QCoreApplication.translate("Dialog", u"Model", None))
    # retranslateUi

