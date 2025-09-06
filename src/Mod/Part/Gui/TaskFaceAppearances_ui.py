# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskFaceAppearances.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_PartGui_TaskFaceAppearances(object):
    def setupUi(self, PartGui__TaskFaceAppearances):
        if not PartGui__TaskFaceAppearances.objectName():
            PartGui__TaskFaceAppearances.setObjectName(u"PartGui__TaskFaceAppearances")
        PartGui__TaskFaceAppearances.resize(247, 219)
        self.verticalLayout = QVBoxLayout(PartGui__TaskFaceAppearances)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PartGui__TaskFaceAppearances)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(PartGui__TaskFaceAppearances)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"Group box")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.faceLabel = QLabel(self.groupBox)
        self.faceLabel.setObjectName(u"faceLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceLabel.sizePolicy().hasHeightForWidth())
        self.faceLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.faceLabel)

        self.labelElement = QLabel(self.groupBox)
        self.labelElement.setObjectName(u"labelElement")
        self.labelElement.setText(u"[]")

        self.horizontalLayout.addWidget(self.labelElement)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widgetMaterial = MatGui_MaterialTreeWidget(self.groupBox)
        self.widgetMaterial.setObjectName(u"widgetMaterial")

        self.horizontalLayout_2.addWidget(self.widgetMaterial)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonCustomAppearance = QPushButton(self.groupBox)
        self.buttonCustomAppearance.setObjectName(u"buttonCustomAppearance")

        self.gridLayout.addWidget(self.buttonCustomAppearance, 0, 1, 1, 1)

        self.labelCustomAppearance = QLabel(self.groupBox)
        self.labelCustomAppearance.setObjectName(u"labelCustomAppearance")

        self.gridLayout.addWidget(self.labelCustomAppearance, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.defaultButton = QPushButton(PartGui__TaskFaceAppearances)
        self.defaultButton.setObjectName(u"defaultButton")

        self.gridLayout_2.addWidget(self.defaultButton, 0, 0, 1, 1)

        self.boxSelection = QPushButton(PartGui__TaskFaceAppearances)
        self.boxSelection.setObjectName(u"boxSelection")
        self.boxSelection.setCheckable(True)
        self.boxSelection.setChecked(False)
        self.boxSelection.setAutoDefault(False)
        self.boxSelection.setFlat(False)

        self.gridLayout_2.addWidget(self.boxSelection, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(PartGui__TaskFaceAppearances)

        self.boxSelection.setDefault(False)


        QMetaObject.connectSlotsByName(PartGui__TaskFaceAppearances)
    # setupUi

    def retranslateUi(self, PartGui__TaskFaceAppearances):
        PartGui__TaskFaceAppearances.setWindowTitle(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Appearance per Face", None))
        self.label.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Select the faces in the 3D view", None))
        self.faceLabel.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Faces", None))
        self.buttonCustomAppearance.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Appearance", None))
        self.labelCustomAppearance.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Custom appearance", None))
#if QT_CONFIG(tooltip)
        self.defaultButton.setToolTip(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Resets color for all faces of the part", None))
#endif // QT_CONFIG(tooltip)
        self.defaultButton.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Set to Default", None))
#if QT_CONFIG(tooltip)
        self.boxSelection.setToolTip(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Allows the selection of multiple faces by dragging a rectangle in the 3D view", None))
#endif // QT_CONFIG(tooltip)
        self.boxSelection.setText(QCoreApplication.translate("PartGui::TaskFaceAppearances", u"Box Selection", None))
    # retranslateUi

