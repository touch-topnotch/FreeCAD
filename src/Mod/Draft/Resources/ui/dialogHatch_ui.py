# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogHatch.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QLabel, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(227, 142)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.File = Gui_FileChooser(Form)
        self.File.setObjectName(u"File")

        self.gridLayout.addWidget(self.File, 0, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Pattern = QComboBox(Form)
        self.Pattern.setObjectName(u"Pattern")

        self.gridLayout.addWidget(self.Pattern, 1, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.Scale = QDoubleSpinBox(Form)
        self.Scale.setObjectName(u"Scale")
        self.Scale.setMaximum(999999.000000000000000)
        self.Scale.setValue(1000.000000000000000)

        self.gridLayout.addWidget(self.Scale, 2, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.Rotation = QDoubleSpinBox(Form)
        self.Rotation.setObjectName(u"Rotation")
        self.Rotation.setSuffix(u"\u00b0")
        self.Rotation.setMaximum(359.990000000000009)

        self.gridLayout.addWidget(self.Rotation, 3, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.Translate = QCheckBox(Form)
        self.Translate.setObjectName(u"Translate")

        self.gridLayout.addWidget(self.Translate, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Hatch", None))
        self.label.setText(QCoreApplication.translate("Form", u"PAT file", None))
        self.File.setFilter(QCoreApplication.translate("Form", u"Pattern files (*.pat *.PAT)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Pattern", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.Scale.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Rotation", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Align to face", None))
#if QT_CONFIG(tooltip)
        self.Translate.setToolTip(QCoreApplication.translate("Form", u"Aligns the pattern with the base object.\n"
"Otherwise, the pattern aligns with the global coordinate system.\n"
"This setting modifies the Translate property.", None))
#endif // QT_CONFIG(tooltip)
        self.Translate.setText("")
    # retranslateUi

