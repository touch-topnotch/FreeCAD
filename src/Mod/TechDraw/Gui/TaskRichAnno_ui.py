# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskRichAnno.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskRichAnno(object):
    def setupUi(self, TechDrawGui__TaskRichAnno):
        if not TechDrawGui__TaskRichAnno.objectName():
            TechDrawGui__TaskRichAnno.setObjectName(u"TechDrawGui__TaskRichAnno")
        TechDrawGui__TaskRichAnno.resize(409, 419)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskRichAnno.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskRichAnno.setSizePolicy(sizePolicy)
        TechDrawGui__TaskRichAnno.setMinimumSize(QSize(250, 0))
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_RichTextAnnotation.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskRichAnno.setWindowIcon(icon)
        self.gridLayout = QGridLayout(TechDrawGui__TaskRichAnno)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(TechDrawGui__TaskRichAnno)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.leBaseView = QLineEdit(self.frame)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leBaseView)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.dsbMaxWidth = Gui_QuantitySpinBox(self.frame)
        self.dsbMaxWidth.setObjectName(u"dsbMaxWidth")
        self.dsbMaxWidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbMaxWidth.setMinimum(-1.000000000000000)
        self.dsbMaxWidth.setValue(-1.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dsbMaxWidth)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.pbEditor = QPushButton(self.frame)
        self.pbEditor.setObjectName(u"pbEditor")
        self.pbEditor.setEnabled(True)

        self.gridLayout_2.addWidget(self.pbEditor, 2, 0, 1, 1)

        self.teAnnoText = QTextEdit(self.frame)
        self.teAnnoText.setObjectName(u"teAnnoText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.teAnnoText.sizePolicy().hasHeightForWidth())
        self.teAnnoText.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.teAnnoText, 3, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.cbShowFrame = QCheckBox(self.frame)
        self.cbShowFrame.setObjectName(u"cbShowFrame")
        self.cbShowFrame.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cbShowFrame)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.cpFrameColor = Gui_ColorButton(self.frame)
        self.cpFrameColor.setObjectName(u"cpFrameColor")
        self.cpFrameColor.setEnabled(False)
        self.cpFrameColor.setColor(QColor(0, 0, 0))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.cpFrameColor)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.dsbWidth = Gui_QuantitySpinBox(self.frame)
        self.dsbWidth.setObjectName(u"dsbWidth")
        self.dsbWidth.setEnabled(False)
        self.dsbWidth.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dsbWidth.setSingleStep(0.100000000000000)
        self.dsbWidth.setValue(0.500000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.dsbWidth)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.cFrameStyle = QComboBox(self.frame)
        self.cFrameStyle.addItem("")
        self.cFrameStyle.addItem("")
        self.cFrameStyle.addItem("")
        self.cFrameStyle.addItem("")
        self.cFrameStyle.addItem("")
        self.cFrameStyle.addItem("")
        self.cFrameStyle.setObjectName(u"cFrameStyle")
        self.cFrameStyle.setEnabled(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.cFrameStyle)


        self.gridLayout_2.addLayout(self.formLayout_2, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(TechDrawGui__TaskRichAnno)
        self.cbShowFrame.toggled.connect(self.cpFrameColor.setEnabled)
        self.cbShowFrame.toggled.connect(self.cFrameStyle.setEnabled)
        self.cbShowFrame.toggled.connect(self.dsbWidth.setEnabled)

        self.cFrameStyle.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(TechDrawGui__TaskRichAnno)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskRichAnno):
        TechDrawGui__TaskRichAnno.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Rich Text Annotation Block", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Base feature", None))
        self.label_2.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Max width", None))
#if QT_CONFIG(tooltip)
        self.dsbMaxWidth.setToolTip(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Maximal width, if -1 then automatic width", None))
#endif // QT_CONFIG(tooltip)
        self.pbEditor.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Start Rich Text Editor", None))
        self.label_3.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Show frame", None))
        self.cbShowFrame.setText("")
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Color", None))
#if QT_CONFIG(tooltip)
        self.cpFrameColor.setToolTip(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Line color", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Width", None))
#if QT_CONFIG(tooltip)
        self.dsbWidth.setToolTip(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Line width", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Style", None))
        self.cFrameStyle.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"NoLine", None))
        self.cFrameStyle.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Continuous", None))
        self.cFrameStyle.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Dash", None))
        self.cFrameStyle.setItemText(3, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Dot", None))
        self.cFrameStyle.setItemText(4, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"DashDot", None))
        self.cFrameStyle.setItemText(5, QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"DashDotDot", None))

#if QT_CONFIG(tooltip)
        self.cFrameStyle.setToolTip(QCoreApplication.translate("TechDrawGui::TaskRichAnno", u"Line style", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

