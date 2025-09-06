# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArchNest.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(266, 475)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Container = QListWidget(self.groupBox)
        self.Container.setObjectName(u"Container")
        self.Container.setMaximumSize(QSize(16777215, 24))

        self.horizontalLayout_2.addWidget(self.Container)

        self.ButtonContainer = QPushButton(self.groupBox)
        self.ButtonContainer.setObjectName(u"ButtonContainer")

        self.horizontalLayout_2.addWidget(self.ButtonContainer)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Shapes = QListWidget(self.groupBox_2)
        self.Shapes.setObjectName(u"Shapes")

        self.verticalLayout_2.addWidget(self.Shapes)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ButtonShapes = QPushButton(self.groupBox_2)
        self.ButtonShapes.setObjectName(u"ButtonShapes")

        self.horizontalLayout.addWidget(self.ButtonShapes)

        self.ButtonRemove = QPushButton(self.groupBox_2)
        self.ButtonRemove.setObjectName(u"ButtonRemove")

        self.horizontalLayout.addWidget(self.ButtonRemove)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.Tolerance = QDoubleSpinBox(self.groupBox_3)
        self.Tolerance.setObjectName(u"Tolerance")
        self.Tolerance.setDecimals(8)
        self.Tolerance.setValue(0.000100000000000)

        self.gridLayout.addWidget(self.Tolerance, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Subdivisions = QSpinBox(self.groupBox_3)
        self.Subdivisions.setObjectName(u"Subdivisions")
        self.Subdivisions.setMinimum(1)
        self.Subdivisions.setValue(4)

        self.gridLayout.addWidget(self.Subdivisions, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Rotations = QLineEdit(self.groupBox_3)
        self.Rotations.setObjectName(u"Rotations")
        self.Rotations.setText(u"0,90,180,270")

        self.gridLayout.addWidget(self.Rotations, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar = QProgressBar(self.groupBox_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(1)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ButtonStart = QPushButton(self.groupBox_4)
        self.ButtonStart.setObjectName(u"ButtonStart")

        self.horizontalLayout_3.addWidget(self.ButtonStart)

        self.ButtonStop = QPushButton(self.groupBox_4)
        self.ButtonStop.setObjectName(u"ButtonStop")

        self.horizontalLayout_3.addWidget(self.ButtonStop)

        self.ButtonPreview = QPushButton(self.groupBox_4)
        self.ButtonPreview.setObjectName(u"ButtonPreview")

        self.horizontalLayout_3.addWidget(self.ButtonPreview)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nesting", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Container", None))
        self.ButtonContainer.setText(QCoreApplication.translate("Form", u"Pick Selected", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Shapes", None))
        self.ButtonShapes.setText(QCoreApplication.translate("Form", u"Add Selected", None))
        self.ButtonRemove.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Nesting parameters", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tolerance", None))
#if QT_CONFIG(tooltip)
        self.Tolerance.setToolTip(QCoreApplication.translate("Form", u"Closer than this, two points are considered equal", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Arcs subdivisions", None))
#if QT_CONFIG(tooltip)
        self.Subdivisions.setToolTip(QCoreApplication.translate("Form", u"The number of segments to divide non-linear edges into for calculations. If curved shapes overlap, try raising this value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Subdivisions.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Rotations", None))
#if QT_CONFIG(tooltip)
        self.Rotations.setToolTip(QCoreApplication.translate("Form", u"A comma-separated list of angles to try and rotate the shapes", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Nesting operation", None))
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"pass %p", None))
        self.ButtonStart.setText(QCoreApplication.translate("Form", u"Start", None))
        self.ButtonStop.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.ButtonPreview.setText(QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

