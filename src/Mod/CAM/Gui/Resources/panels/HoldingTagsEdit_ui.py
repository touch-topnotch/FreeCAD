# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HoldingTagsEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(289, 466)
        self.gridLayout_2 = QGridLayout(TaskPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.parameterGroup = QWidget(TaskPanel)
        self.parameterGroup.setObjectName(u"parameterGroup")
        self.formLayout = QFormLayout(self.parameterGroup)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.parameterGroup)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.parameterGroup)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.parameterGroup)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.ifWidth = Gui_InputField(self.parameterGroup)
        self.ifWidth.setObjectName(u"ifWidth")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ifWidth)

        self.ifHeight = Gui_InputField(self.parameterGroup)
        self.ifHeight.setObjectName(u"ifHeight")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ifHeight)

        self.dsbAngle = QDoubleSpinBox(self.parameterGroup)
        self.dsbAngle.setObjectName(u"dsbAngle")
        self.dsbAngle.setMinimum(5.000000000000000)
        self.dsbAngle.setMaximum(90.000000000000000)
        self.dsbAngle.setSingleStep(15.000000000000000)
        self.dsbAngle.setValue(45.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dsbAngle)

        self.label_5 = QLabel(self.parameterGroup)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.ifRadius = Gui_InputField(self.parameterGroup)
        self.ifRadius.setObjectName(u"ifRadius")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ifRadius)


        self.gridLayout_2.addWidget(self.parameterGroup, 0, 0, 1, 1)

        self.lwTags = QListWidget(TaskPanel)
        self.lwTags.setObjectName(u"lwTags")

        self.gridLayout_2.addWidget(self.lwTags, 1, 0, 1, 1)

        self.removeEditAddGroup = QWidget(TaskPanel)
        self.removeEditAddGroup.setObjectName(u"removeEditAddGroup")
        self.gridLayout = QGridLayout(self.removeEditAddGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pbDelete = QPushButton(self.removeEditAddGroup)
        self.pbDelete.setObjectName(u"pbDelete")
        self.pbDelete.setEnabled(False)

        self.gridLayout.addWidget(self.pbDelete, 1, 0, 1, 1)

        self.pbEdit = QPushButton(self.removeEditAddGroup)
        self.pbEdit.setObjectName(u"pbEdit")
        self.pbEdit.setEnabled(False)

        self.gridLayout.addWidget(self.pbEdit, 1, 1, 1, 1)

        self.pbAdd = QPushButton(self.removeEditAddGroup)
        self.pbAdd.setObjectName(u"pbAdd")

        self.gridLayout.addWidget(self.pbAdd, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.removeEditAddGroup, 2, 0, 1, 1)

        self.cbTagGeneration = QGroupBox(TaskPanel)
        self.cbTagGeneration.setObjectName(u"cbTagGeneration")
        self.gridLayout_3 = QGridLayout(self.cbTagGeneration)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sbCount = QSpinBox(self.cbTagGeneration)
        self.sbCount.setObjectName(u"sbCount")
        self.sbCount.setMinimum(2)

        self.gridLayout_3.addWidget(self.sbCount, 1, 0, 1, 1)

        self.pbGenerate = QPushButton(self.cbTagGeneration)
        self.pbGenerate.setObjectName(u"pbGenerate")
        self.pbGenerate.setEnabled(False)

        self.gridLayout_3.addWidget(self.pbGenerate, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.cbTagGeneration, 3, 0, 1, 1)

        self.gbCopy = QGroupBox(TaskPanel)
        self.gbCopy.setObjectName(u"gbCopy")
        self.gbCopy.setEnabled(False)
        self.gridLayout_4 = QGridLayout(self.gbCopy)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cbSource = QComboBox(self.gbCopy)
        self.cbSource.setObjectName(u"cbSource")

        self.gridLayout_4.addWidget(self.cbSource, 0, 0, 1, 1)

        self.pbCopy = QPushButton(self.gbCopy)
        self.pbCopy.setObjectName(u"pbCopy")

        self.gridLayout_4.addWidget(self.pbCopy, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.gbCopy, 4, 0, 1, 1)


        self.retranslateUi(TaskPanel)

        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"Holding Tags", None))
        self.label_2.setText(QCoreApplication.translate("TaskPanel", u"Width", None))
        self.label_3.setText(QCoreApplication.translate("TaskPanel", u"Height", None))
        self.label_4.setText(QCoreApplication.translate("TaskPanel", u"Angle", None))
#if QT_CONFIG(tooltip)
        self.ifWidth.setToolTip(QCoreApplication.translate("TaskPanel", u"Width of the resulting holding tag", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ifHeight.setToolTip(QCoreApplication.translate("TaskPanel", u"Height of holding tag. Note that resulting tag might be smaller if the tag's width and angle result in a triangular shape.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dsbAngle.setToolTip(QCoreApplication.translate("TaskPanel", u"Plunge angle for ascent and descent of holding tag", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TaskPanel", u"Radius", None))
#if QT_CONFIG(tooltip)
        self.ifRadius.setToolTip(QCoreApplication.translate("TaskPanel", u"Radius of the fillet at the top. If the radius is too big for the tag shape it gets reduced to the maximum possible radius - resulting in a spherical shape.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lwTags.setToolTip(QCoreApplication.translate("TaskPanel", u"List of current tags. Edit coordinates by double click or Edit button. Tags are automatically disabled if they overlap with the previous tag, or don't lie on the base wire.", None))
#endif // QT_CONFIG(tooltip)
        self.pbDelete.setText(QCoreApplication.translate("TaskPanel", u"Delete", None))
        self.pbEdit.setText(QCoreApplication.translate("TaskPanel", u"Edit", None))
        self.pbAdd.setText(QCoreApplication.translate("TaskPanel", u"Add", None))
        self.cbTagGeneration.setTitle(QCoreApplication.translate("TaskPanel", u"Auto Generate", None))
        self.pbGenerate.setText(QCoreApplication.translate("TaskPanel", u"Replace All", None))
        self.gbCopy.setTitle(QCoreApplication.translate("TaskPanel", u"Copy From", None))
        self.pbCopy.setText(QCoreApplication.translate("TaskPanel", u"Replace All", None))
    # retranslateUi

