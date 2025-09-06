# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DogboneEdit.ui'
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
    QFrame, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QToolBox, QWidget)

class Ui_TaskPanel(object):
    def setupUi(self, TaskPanel):
        if not TaskPanel.objectName():
            TaskPanel.setObjectName(u"TaskPanel")
        TaskPanel.resize(376, 387)
        self.gridLayout_2 = QGridLayout(TaskPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolBox = QToolBox(TaskPanel)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.Dressup = QWidget()
        self.Dressup.setObjectName(u"Dressup")
        self.Dressup.setGeometry(QRect(0, 0, 358, 333))
        self.formLayout = QFormLayout(self.Dressup)
        self.formLayout.setObjectName(u"formLayout")
        self.styleLabel = QLabel(self.Dressup)
        self.styleLabel.setObjectName(u"styleLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.styleLabel)

        self.styleCombo = QComboBox(self.Dressup)
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.setObjectName(u"styleCombo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.styleCombo)

        self.sideLabel = QLabel(self.Dressup)
        self.sideLabel.setObjectName(u"sideLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.sideLabel)

        self.sideCombo = QComboBox(self.Dressup)
        self.sideCombo.addItem("")
        self.sideCombo.addItem("")
        self.sideCombo.setObjectName(u"sideCombo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sideCombo)

        self.incisionLabel = QLabel(self.Dressup)
        self.incisionLabel.setObjectName(u"incisionLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.incisionLabel)

        self.incisionCombo = QComboBox(self.Dressup)
        self.incisionCombo.addItem("")
        self.incisionCombo.addItem("")
        self.incisionCombo.addItem("")
        self.incisionCombo.setObjectName(u"incisionCombo")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.incisionCombo)

        self.custom = QDoubleSpinBox(self.Dressup)
        self.custom.setObjectName(u"custom")
        self.custom.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.custom)

        self.bones = QListWidget(self.Dressup)
        self.bones.setObjectName(u"bones")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bones.sizePolicy().hasHeightForWidth())
        self.bones.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.bones)

        self.customLabel = QLabel(self.Dressup)
        self.customLabel.setObjectName(u"customLabel")
        self.customLabel.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.customLabel)

        self.toolBox.addItem(self.Dressup, u"Dressup")

        self.gridLayout_2.addWidget(self.toolBox, 1, 0, 1, 1)


        self.retranslateUi(TaskPanel)

        self.toolBox.setCurrentIndex(0)
        self.sideCombo.setCurrentIndex(1)
        self.incisionCombo.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(TaskPanel)
    # setupUi

    def retranslateUi(self, TaskPanel):
        TaskPanel.setWindowTitle(QCoreApplication.translate("TaskPanel", u"Dogbones", None))
        self.styleLabel.setText(QCoreApplication.translate("TaskPanel", u"Style", None))
        self.styleCombo.setItemText(0, QCoreApplication.translate("TaskPanel", u"Dogbone", None))
        self.styleCombo.setItemText(1, QCoreApplication.translate("TaskPanel", u"T-bone horizontal", None))
        self.styleCombo.setItemText(2, QCoreApplication.translate("TaskPanel", u"T-bone vertical", None))
        self.styleCombo.setItemText(3, QCoreApplication.translate("TaskPanel", u"T-bone long edge", None))
        self.styleCombo.setItemText(4, QCoreApplication.translate("TaskPanel", u"T-bone short edge", None))

#if QT_CONFIG(tooltip)
        self.styleCombo.setToolTip(QCoreApplication.translate("TaskPanel", u"<html><head/><body><p>Select desired style of the bone dressup:</p><p><span style=\" font-weight:600; font-style:italic;\">Dogbone</span> ... take the shortest path to cover the corner,</p><p><span style=\" font-weight:600; font-style:italic;\">T-bone</span> ... extend a certain direction until corner is covered</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sideLabel.setText(QCoreApplication.translate("TaskPanel", u"Side", None))
        self.sideCombo.setItemText(0, QCoreApplication.translate("TaskPanel", u"Left", None))
        self.sideCombo.setItemText(1, QCoreApplication.translate("TaskPanel", u"Right", None))

#if QT_CONFIG(tooltip)
        self.sideCombo.setToolTip(QCoreApplication.translate("TaskPanel", u"On which side of the profile bones are inserted - this also determines which corners are dressed up. The default value is determined based on the profile being dressed up.", None))
#endif // QT_CONFIG(tooltip)
        self.incisionLabel.setText(QCoreApplication.translate("TaskPanel", u"Incision", None))
        self.incisionCombo.setItemText(0, QCoreApplication.translate("TaskPanel", u"Adaptive", None))
        self.incisionCombo.setItemText(1, QCoreApplication.translate("TaskPanel", u"Custom", None))
        self.incisionCombo.setItemText(2, QCoreApplication.translate("TaskPanel", u"Fixed", None))

#if QT_CONFIG(tooltip)
        self.incisionCombo.setToolTip(QCoreApplication.translate("TaskPanel", u"<html><head/><body><p>Determines the incision length of the bone to be inserted into the profile.</p><p><span style=\" font-weight:600; font-style:italic;\">adaptive</span> ... the length is adapted to cover the corner based on the angle of its edges, taking the current tool radius into account (default)</p><p><span style=\" font-weight:600; font-style:italic;\">fixed</span> ... is the same as adaptive for straight angles. For T-bones it's the radius of the tool (R) and for dogbones it's R * (2/\u221a2 - 1).</p><p><span style=\" font-weight:600; font-style:italic;\">custom</span> ... lets you specify a custom (fixed) length below</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.custom.setToolTip(QCoreApplication.translate("TaskPanel", u"<html><head/><body><p>Enter length for each bone if <span style=\" font-weight:600;\">Incision</span> is set to <span style=\" font-weight:600;\">custom</span>, ignored otherwise.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.bones.setToolTip(QCoreApplication.translate("TaskPanel", u"<html><head/><body><p>List of bone locations (with all bones at that location) that are part of this dressup. The list is determined by the corners in the profile and the selected <span style=\" font-weight:600;\">Side</span> for the bones. </p><p>You can <span style=\" font-weight:600;\">un-check</span> the bones you don't want to be dressed up.</p><p>If a bone is <span style=\" font-weight:600;\">grayed out</span> it means that it is already dressed up by a previous dressup. Or put another way, if you dress up this dogbone dressup again you will only be able to select the bones that are un-checked here.</p><p>If this list is empty it probably means you're trying to create bones on the wrong side of the profile.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.customLabel.setText(QCoreApplication.translate("TaskPanel", u"Length", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Dressup), QCoreApplication.translate("TaskPanel", u"Dressup", None))
    # retranslateUi

