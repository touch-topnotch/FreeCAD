# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemeshGmsh.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_MeshGui_RemeshGmsh(object):
    def setupUi(self, MeshGui__RemeshGmsh):
        if not MeshGui__RemeshGmsh.objectName():
            MeshGui__RemeshGmsh.setObjectName(u"MeshGui__RemeshGmsh")
        MeshGui__RemeshGmsh.resize(458, 506)
        self.gridLayout_3 = QGridLayout(MeshGui__RemeshGmsh)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.remeshParam = QGroupBox(MeshGui__RemeshGmsh)
        self.remeshParam.setObjectName(u"remeshParam")
        self.remeshParam.setMaximumSize(QSize(16777215, 1677215))
        self.gridLayout_2 = QGridLayout(self.remeshParam)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelMethod = QLabel(self.remeshParam)
        self.labelMethod.setObjectName(u"labelMethod")

        self.gridLayout_2.addWidget(self.labelMethod, 0, 0, 1, 1)

        self.method = QComboBox(self.remeshParam)
        self.method.setObjectName(u"method")

        self.gridLayout_2.addWidget(self.method, 0, 1, 1, 1)

        self.labelMax = QLabel(self.remeshParam)
        self.labelMax.setObjectName(u"labelMax")

        self.gridLayout_2.addWidget(self.labelMax, 1, 0, 1, 1)

        self.maxSize = Gui_QuantitySpinBox(self.remeshParam)
        self.maxSize.setObjectName(u"maxSize")
        self.maxSize.setProperty(u"unit", u"mm")
        self.maxSize.setMinimum(0.000000000000000)
        self.maxSize.setMaximum(1000.000000000000000)
        self.maxSize.setSingleStep(0.100000000000000)
        self.maxSize.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.maxSize, 1, 1, 1, 1)

        self.labelMin = QLabel(self.remeshParam)
        self.labelMin.setObjectName(u"labelMin")

        self.gridLayout_2.addWidget(self.labelMin, 2, 0, 1, 1)

        self.minSize = Gui_QuantitySpinBox(self.remeshParam)
        self.minSize.setObjectName(u"minSize")
        self.minSize.setProperty(u"unit", u"mm")
        self.minSize.setMinimum(0.000000000000000)
        self.minSize.setMaximum(1000.000000000000000)
        self.minSize.setSingleStep(0.100000000000000)
        self.minSize.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.minSize, 2, 1, 1, 1)

        self.labelAngle = QLabel(self.remeshParam)
        self.labelAngle.setObjectName(u"labelAngle")

        self.gridLayout_2.addWidget(self.labelAngle, 3, 0, 1, 1)

        self.angle = Gui_QuantitySpinBox(self.remeshParam)
        self.angle.setObjectName(u"angle")
        self.angle.setProperty(u"unit", u"deg")
        self.angle.setMinimum(20.000000000000000)
        self.angle.setMaximum(120.000000000000000)
        self.angle.setValue(40.000000000000000)

        self.gridLayout_2.addWidget(self.angle, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.remeshParam, 0, 0, 1, 1)

        self.gmshOutput = QGroupBox(MeshGui__RemeshGmsh)
        self.gmshOutput.setObjectName(u"gmshOutput")
        self.gmshOutput.setMaximumSize(QSize(16777215, 1677215))
        self.gridLayout = QGridLayout(self.gmshOutput)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gmshOutput)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.fileChooser = Gui_PrefFileChooser(self.gmshOutput)
        self.fileChooser.setObjectName(u"fileChooser")
        self.fileChooser.setProperty(u"prefEntry", u"gmshExe")
        self.fileChooser.setProperty(u"prefPath", u"Mod/Mesh/Meshing")

        self.horizontalLayout.addWidget(self.fileChooser)

        self.killButton = QPushButton(self.gmshOutput)
        self.killButton.setObjectName(u"killButton")
        self.killButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.killButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.outputWindow = QTextEdit(self.gmshOutput)
        self.outputWindow.setObjectName(u"outputWindow")
        self.outputWindow.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout.addWidget(self.outputWindow, 1, 0, 1, 2)

        self.labelTime = QLabel(self.gmshOutput)
        self.labelTime.setObjectName(u"labelTime")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTime.sizePolicy().hasHeightForWidth())
        self.labelTime.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.labelTime.setFont(font)

        self.gridLayout.addWidget(self.labelTime, 2, 0, 1, 1)

        self.clearButton = QPushButton(self.gmshOutput)
        self.clearButton.setObjectName(u"clearButton")

        self.gridLayout.addWidget(self.clearButton, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.gmshOutput, 1, 0, 1, 1)

        QWidget.setTabOrder(self.method, self.maxSize)
        QWidget.setTabOrder(self.maxSize, self.minSize)
        QWidget.setTabOrder(self.minSize, self.angle)
        QWidget.setTabOrder(self.angle, self.killButton)
        QWidget.setTabOrder(self.killButton, self.outputWindow)

        self.retranslateUi(MeshGui__RemeshGmsh)

        QMetaObject.connectSlotsByName(MeshGui__RemeshGmsh)
    # setupUi

    def retranslateUi(self, MeshGui__RemeshGmsh):
        MeshGui__RemeshGmsh.setWindowTitle(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Remesh by Gmsh", None))
        self.remeshParam.setTitle(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Remeshing Parameter", None))
        self.labelMethod.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Meshing", None))
        self.labelMax.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Max element size (0.0 = Auto)", None))
        self.labelMin.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Min element size (0.0 = Auto)", None))
        self.labelAngle.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Angle", None))
        self.gmshOutput.setTitle(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Gmsh", None))
        self.label.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Path", None))
#if QT_CONFIG(tooltip)
        self.fileChooser.setToolTip(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Leave empty to use default gmsh executable", None))
#endif // QT_CONFIG(tooltip)
        self.killButton.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Kill", None))
        self.labelTime.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Time", None))
        self.clearButton.setText(QCoreApplication.translate("MeshGui::RemeshGmsh", u"Clear", None))
    # retranslateUi

