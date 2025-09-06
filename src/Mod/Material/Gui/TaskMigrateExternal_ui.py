# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskMigrateExternal.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MatGui_TaskMigrateExternal(object):
    def setupUi(self, MatGui__TaskMigrateExternal):
        if not MatGui__TaskMigrateExternal.objectName():
            MatGui__TaskMigrateExternal.setObjectName(u"MatGui__TaskMigrateExternal")
        MatGui__TaskMigrateExternal.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MatGui__TaskMigrateExternal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(MatGui__TaskMigrateExternal)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listMaterialLibraries = QListWidget(MatGui__TaskMigrateExternal)
        self.listMaterialLibraries.setObjectName(u"listMaterialLibraries")

        self.verticalLayout.addWidget(self.listMaterialLibraries)

        self.label_2 = QLabel(MatGui__TaskMigrateExternal)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.listModelLibraries = QListWidget(MatGui__TaskMigrateExternal)
        self.listModelLibraries.setObjectName(u"listModelLibraries")

        self.verticalLayout.addWidget(self.listModelLibraries)

        self.label_3 = QLabel(MatGui__TaskMigrateExternal)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.textStatus = QTextEdit(MatGui__TaskMigrateExternal)
        self.textStatus.setObjectName(u"textStatus")
        self.textStatus.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout.addWidget(self.textStatus)


        self.retranslateUi(MatGui__TaskMigrateExternal)

        QMetaObject.connectSlotsByName(MatGui__TaskMigrateExternal)
    # setupUi

    def retranslateUi(self, MatGui__TaskMigrateExternal):
        MatGui__TaskMigrateExternal.setWindowTitle(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Materials Migration", None))
        self.label.setText(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Select material libraries", None))
#if QT_CONFIG(tooltip)
        self.listMaterialLibraries.setToolTip(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Select material libraries to migrate. Existing materials will not be overwritten.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Select model libraries", None))
#if QT_CONFIG(tooltip)
        self.listModelLibraries.setToolTip(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Select model libraries to migrate. Existing models will not be overwritten.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MatGui::TaskMigrateExternal", u"Status", None))
    # retranslateUi

