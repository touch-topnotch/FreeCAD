# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgProcessorChooser.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_DlgProcessorChooser(object):
    def setupUi(self, DlgProcessorChooser):
        if not DlgProcessorChooser.objectName():
            DlgProcessorChooser.setObjectName(u"DlgProcessorChooser")
        DlgProcessorChooser.resize(272, 107)
        self.formLayout = QFormLayout(DlgProcessorChooser)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DlgProcessorChooser)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(DlgProcessorChooser)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.argsLabel = QLabel(DlgProcessorChooser)
        self.argsLabel.setObjectName(u"argsLabel")
        self.argsLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.argsLabel)

        self.argsLineEdit = QLineEdit(DlgProcessorChooser)
        self.argsLineEdit.setObjectName(u"argsLineEdit")
        self.argsLineEdit.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.argsLineEdit)

        self.buttonBox = QDialogButtonBox(DlgProcessorChooser)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.buttonBox)


        self.retranslateUi(DlgProcessorChooser)
        self.buttonBox.accepted.connect(DlgProcessorChooser.accept)
        self.buttonBox.rejected.connect(DlgProcessorChooser.reject)

        QMetaObject.connectSlotsByName(DlgProcessorChooser)
    # setupUi

    def retranslateUi(self, DlgProcessorChooser):
        DlgProcessorChooser.setWindowTitle(QCoreApplication.translate("DlgProcessorChooser", u"Processor Selection", None))
        self.label.setText(QCoreApplication.translate("DlgProcessorChooser", u"Processor", None))
        self.argsLabel.setText(QCoreApplication.translate("DlgProcessorChooser", u"Arguments", None))
    # retranslateUi

