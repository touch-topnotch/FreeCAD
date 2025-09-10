# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskAssemblyCreateView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_TaskAssemblyCreateView(object):
    def setupUi(self, TaskAssemblyCreateView):
        if not TaskAssemblyCreateView.objectName():
            TaskAssemblyCreateView.setObjectName(u"TaskAssemblyCreateView")
        TaskAssemblyCreateView.resize(376, 387)
        self.gridLayout = QGridLayout(TaskAssemblyCreateView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.CheckBox_PartsAsSingleSolid = Gui_PrefCheckBox(TaskAssemblyCreateView)
        self.CheckBox_PartsAsSingleSolid.setObjectName(u"CheckBox_PartsAsSingleSolid")
        self.CheckBox_PartsAsSingleSolid.setChecked(True)
        self.CheckBox_PartsAsSingleSolid.setProperty(u"prefEntry", u"PartsAsSingleSolid")
        self.CheckBox_PartsAsSingleSolid.setProperty(u"prefPath", u"Mod/Assembly")

        self.gridLayout.addWidget(self.CheckBox_PartsAsSingleSolid, 0, 0, 1, 1)

        self.stepList = QListWidget(TaskAssemblyCreateView)
        self.stepList.setObjectName(u"stepList")

        self.gridLayout.addWidget(self.stepList, 2, 0, 1, 1)

        self.btnAlignDragger = QPushButton(TaskAssemblyCreateView)
        self.btnAlignDragger.setObjectName(u"btnAlignDragger")

        self.gridLayout.addWidget(self.btnAlignDragger, 3, 0, 1, 1)

        self.LabelAlignDragger = QLabel(TaskAssemblyCreateView)
        self.LabelAlignDragger.setObjectName(u"LabelAlignDragger")

        self.gridLayout.addWidget(self.LabelAlignDragger, 4, 0, 1, 1)

        self.btnRadialExplosion = QPushButton(TaskAssemblyCreateView)
        self.btnRadialExplosion.setObjectName(u"btnRadialExplosion")

        self.gridLayout.addWidget(self.btnRadialExplosion, 5, 0, 1, 1)


        self.retranslateUi(TaskAssemblyCreateView)

        QMetaObject.connectSlotsByName(TaskAssemblyCreateView)
    # setupUi

    def retranslateUi(self, TaskAssemblyCreateView):
        TaskAssemblyCreateView.setWindowTitle(QCoreApplication.translate("TaskAssemblyCreateView", u"Create Exploded View", None))
#if QT_CONFIG(tooltip)
        self.CheckBox_PartsAsSingleSolid.setToolTip(QCoreApplication.translate("TaskAssemblyCreateView", u"If checked, Parts will be selected as a single solid.", None))
#endif // QT_CONFIG(tooltip)
        self.CheckBox_PartsAsSingleSolid.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Parts as single solid", None))
        self.btnAlignDragger.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Align dragger", None))
        self.LabelAlignDragger.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Aligning dragger:\n"
"Select a feature.\n"
"Press ESC to cancel.", None))
        self.btnRadialExplosion.setText(QCoreApplication.translate("TaskAssemblyCreateView", u"Explode radially", None))
    # retranslateUi

