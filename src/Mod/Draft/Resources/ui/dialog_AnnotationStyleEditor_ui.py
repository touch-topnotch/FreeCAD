# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_AnnotationStyleEditor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFontComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(416, 542)
        self.verticalLayout_1 = QVBoxLayout(Dialog)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.groupBox_1 = QGroupBox(Dialog)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.horizontalLayout_1 = QHBoxLayout(self.groupBox_1)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.comboBoxStyles = QComboBox(self.groupBox_1)
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.addItem("")
        self.comboBoxStyles.setObjectName(u"comboBoxStyles")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxStyles.sizePolicy().hasHeightForWidth())
        self.comboBoxStyles.setSizePolicy(sizePolicy)
        self.comboBoxStyles.setMinimumSize(QSize(60, 0))
        self.comboBoxStyles.setEditable(False)

        self.horizontalLayout_1.addWidget(self.comboBoxStyles)

        self.pushButtonRename = QPushButton(self.groupBox_1)
        self.pushButtonRename.setObjectName(u"pushButtonRename")
        self.pushButtonRename.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButtonRename.sizePolicy().hasHeightForWidth())
        self.pushButtonRename.setSizePolicy(sizePolicy)
        self.pushButtonRename.setMinimumSize(QSize(60, 0))
        self.pushButtonRename.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_1.addWidget(self.pushButtonRename)

        self.pushButtonDelete = QPushButton(self.groupBox_1)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButtonDelete.sizePolicy().hasHeightForWidth())
        self.pushButtonDelete.setSizePolicy(sizePolicy)
        self.pushButtonDelete.setMinimumSize(QSize(60, 0))
        self.pushButtonDelete.setMaximumSize(QSize(110, 16777215))

        self.horizontalLayout_1.addWidget(self.pushButtonDelete)

        self.pushButtonImport = QPushButton(self.groupBox_1)
        self.pushButtonImport.setObjectName(u"pushButtonImport")

        self.horizontalLayout_1.addWidget(self.pushButtonImport)

        self.pushButtonExport = QPushButton(self.groupBox_1)
        self.pushButtonExport.setObjectName(u"pushButtonExport")

        self.horizontalLayout_1.addWidget(self.pushButtonExport)


        self.verticalLayout_1.addWidget(self.groupBox_1)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 383, 589))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_1 = QGridLayout(self.groupBox_2)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.label_ScaleMultiplier = QLabel(self.groupBox_2)
        self.label_ScaleMultiplier.setObjectName(u"label_ScaleMultiplier")

        self.gridLayout_1.addWidget(self.label_ScaleMultiplier, 0, 0, 1, 1)

        self.ScaleMultiplier = QDoubleSpinBox(self.groupBox_2)
        self.ScaleMultiplier.setObjectName(u"ScaleMultiplier")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScaleMultiplier.sizePolicy().hasHeightForWidth())
        self.ScaleMultiplier.setSizePolicy(sizePolicy1)
        self.ScaleMultiplier.setMinimumSize(QSize(60, 0))
        self.ScaleMultiplier.setMinimum(0)
        self.ScaleMultiplier.setMaximum(10000)

        self.gridLayout_1.addWidget(self.ScaleMultiplier, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_FontName = QLabel(self.groupBox_3)
        self.label_FontName.setObjectName(u"label_FontName")

        self.gridLayout_2.addWidget(self.label_FontName, 0, 0, 1, 1)

        self.FontName = QFontComboBox(self.groupBox_3)
        self.FontName.setObjectName(u"FontName")
        sizePolicy.setHeightForWidth(self.FontName.sizePolicy().hasHeightForWidth())
        self.FontName.setSizePolicy(sizePolicy)
        self.FontName.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.FontName, 0, 1, 1, 1)

        self.label_FontSize = QLabel(self.groupBox_3)
        self.label_FontSize.setObjectName(u"label_FontSize")

        self.gridLayout_2.addWidget(self.label_FontSize, 1, 0, 1, 1)

        self.FontSize = Gui_InputField(self.groupBox_3)
        self.FontSize.setObjectName(u"FontSize")
        self.FontSize.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.FontSize, 1, 1, 1, 1)

        self.label_LineSpacing = QLabel(self.groupBox_3)
        self.label_LineSpacing.setObjectName(u"label_LineSpacing")

        self.gridLayout_2.addWidget(self.label_LineSpacing, 2, 0, 1, 1)

        self.LineSpacing = QDoubleSpinBox(self.groupBox_3)
        self.LineSpacing.setObjectName(u"LineSpacing")

        self.gridLayout_2.addWidget(self.LineSpacing, 2, 1, 1, 1)

        self.label_TextColor = QLabel(self.groupBox_3)
        self.label_TextColor.setObjectName(u"label_TextColor")

        self.gridLayout_2.addWidget(self.label_TextColor, 3, 0, 1, 1)

        self.TextColor = Gui_ColorButton(self.groupBox_3)
        self.TextColor.setObjectName(u"TextColor")

        self.gridLayout_2.addWidget(self.TextColor, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_ShowLine = QLabel(self.groupBox_4)
        self.label_ShowLine.setObjectName(u"label_ShowLine")

        self.gridLayout_3.addWidget(self.label_ShowLine, 0, 0, 1, 1)

        self.ShowLine = QCheckBox(self.groupBox_4)
        self.ShowLine.setObjectName(u"ShowLine")
        self.ShowLine.setLayoutDirection(Qt.LeftToRight)
        self.ShowLine.setChecked(True)

        self.gridLayout_3.addWidget(self.ShowLine, 0, 1, 1, 1)

        self.label_LineWidth = QLabel(self.groupBox_4)
        self.label_LineWidth.setObjectName(u"label_LineWidth")

        self.gridLayout_3.addWidget(self.label_LineWidth, 2, 0, 1, 1)

        self.LineWidth = QSpinBox(self.groupBox_4)
        self.LineWidth.setObjectName(u"LineWidth")

        self.gridLayout_3.addWidget(self.LineWidth, 2, 1, 1, 1)

        self.label_ArrowType = QLabel(self.groupBox_4)
        self.label_ArrowType.setObjectName(u"label_ArrowType")

        self.gridLayout_3.addWidget(self.label_ArrowType, 3, 0, 1, 1)

        self.ArrowType = QComboBox(self.groupBox_4)
        self.ArrowType.addItem("")
        self.ArrowType.addItem("")
        self.ArrowType.addItem("")
        self.ArrowType.addItem("")
        self.ArrowType.addItem("")
        self.ArrowType.setObjectName(u"ArrowType")
        sizePolicy1.setHeightForWidth(self.ArrowType.sizePolicy().hasHeightForWidth())
        self.ArrowType.setSizePolicy(sizePolicy1)
        self.ArrowType.setMinimumSize(QSize(60, 0))

        self.gridLayout_3.addWidget(self.ArrowType, 3, 1, 1, 1)

        self.label_ArrowSize = QLabel(self.groupBox_4)
        self.label_ArrowSize.setObjectName(u"label_ArrowSize")

        self.gridLayout_3.addWidget(self.label_ArrowSize, 4, 0, 1, 1)

        self.ArrowSize = Gui_InputField(self.groupBox_4)
        self.ArrowSize.setObjectName(u"ArrowSize")
        self.ArrowSize.setProperty(u"unit", u"")

        self.gridLayout_3.addWidget(self.ArrowSize, 4, 1, 1, 1)

        self.label_LineColor = QLabel(self.groupBox_4)
        self.label_LineColor.setObjectName(u"label_LineColor")

        self.gridLayout_3.addWidget(self.label_LineColor, 5, 0, 1, 1)

        self.LineColor = Gui_ColorButton(self.groupBox_4)
        self.LineColor.setObjectName(u"LineColor")

        self.gridLayout_3.addWidget(self.LineColor, 5, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_ShowUnit = QLabel(self.groupBox_5)
        self.label_ShowUnit.setObjectName(u"label_ShowUnit")

        self.gridLayout_4.addWidget(self.label_ShowUnit, 0, 0, 1, 1)

        self.ShowUnit = QCheckBox(self.groupBox_5)
        self.ShowUnit.setObjectName(u"ShowUnit")
        self.ShowUnit.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_4.addWidget(self.ShowUnit, 0, 1, 1, 1)

        self.label_UnitOverride = QLabel(self.groupBox_5)
        self.label_UnitOverride.setObjectName(u"label_UnitOverride")

        self.gridLayout_4.addWidget(self.label_UnitOverride, 1, 0, 1, 1)

        self.UnitOverride = QLineEdit(self.groupBox_5)
        self.UnitOverride.setObjectName(u"UnitOverride")

        self.gridLayout_4.addWidget(self.UnitOverride, 1, 1, 1, 1)

        self.label_Decimals = QLabel(self.groupBox_5)
        self.label_Decimals.setObjectName(u"label_Decimals")

        self.gridLayout_4.addWidget(self.label_Decimals, 2, 0, 1, 1)

        self.Decimals = QSpinBox(self.groupBox_5)
        self.Decimals.setObjectName(u"Decimals")

        self.gridLayout_4.addWidget(self.Decimals, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_5 = QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_DimOvershoot = QLabel(self.groupBox_6)
        self.label_DimOvershoot.setObjectName(u"label_DimOvershoot")

        self.gridLayout_5.addWidget(self.label_DimOvershoot, 0, 0, 1, 1)

        self.DimOvershoot = Gui_InputField(self.groupBox_6)
        self.DimOvershoot.setObjectName(u"DimOvershoot")
        self.DimOvershoot.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.DimOvershoot, 0, 1, 1, 1)

        self.label_ExtLines = QLabel(self.groupBox_6)
        self.label_ExtLines.setObjectName(u"label_ExtLines")

        self.gridLayout_5.addWidget(self.label_ExtLines, 1, 0, 1, 1)

        self.ExtLines = Gui_InputField(self.groupBox_6)
        self.ExtLines.setObjectName(u"ExtLines")
        self.ExtLines.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.ExtLines, 1, 1, 1, 1)

        self.label_ExtOvershoot = QLabel(self.groupBox_6)
        self.label_ExtOvershoot.setObjectName(u"label_ExtOvershoot")

        self.gridLayout_5.addWidget(self.label_ExtOvershoot, 2, 0, 1, 1)

        self.ExtOvershoot = Gui_InputField(self.groupBox_6)
        self.ExtOvershoot.setObjectName(u"ExtOvershoot")
        self.ExtOvershoot.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.ExtOvershoot, 2, 1, 1, 1)

        self.label_TextSpacing = QLabel(self.groupBox_6)
        self.label_TextSpacing.setObjectName(u"label_TextSpacing")

        self.gridLayout_5.addWidget(self.label_TextSpacing, 3, 0, 1, 1)

        self.TextSpacing = Gui_InputField(self.groupBox_6)
        self.TextSpacing.setObjectName(u"TextSpacing")
        self.TextSpacing.setProperty(u"unit", u"")

        self.gridLayout_5.addWidget(self.TextSpacing, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_1.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_1.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Annotation Styles Editor", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Dialog", u"Style name", None))
        self.comboBoxStyles.setItemText(0, "")
        self.comboBoxStyles.setItemText(1, QCoreApplication.translate("Dialog", u"Add new...", None))

#if QT_CONFIG(tooltip)
        self.comboBoxStyles.setToolTip(QCoreApplication.translate("Dialog", u"The name of your style. Existing style names can be edited.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButtonRename.setToolTip(QCoreApplication.translate("Dialog", u"Renames the selected style", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRename.setText(QCoreApplication.translate("Dialog", u"Rename", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDelete.setToolTip(QCoreApplication.translate("Dialog", u"Deletes the selected style", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDelete.setText(QCoreApplication.translate("Dialog", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.pushButtonImport.setToolTip(QCoreApplication.translate("Dialog", u"Import styles from json file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonImport.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonExport.setToolTip(QCoreApplication.translate("Dialog", u"Export styles to json file", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonExport.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Annotations", None))
#if QT_CONFIG(tooltip)
        self.label_ScaleMultiplier.setToolTip(QCoreApplication.translate("Dialog", u"A multiplier factor that affects the size of texts and markers", None))
#endif // QT_CONFIG(tooltip)
        self.label_ScaleMultiplier.setText(QCoreApplication.translate("Dialog", u"Scale multiplier", None))
#if QT_CONFIG(tooltip)
        self.ScaleMultiplier.setToolTip(QCoreApplication.translate("Dialog", u"A multiplier factor that affects the size of texts and markers", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Texts", None))
#if QT_CONFIG(tooltip)
        self.label_FontName.setToolTip(QCoreApplication.translate("Dialog", u"The font to use for texts and dimensions", None))
#endif // QT_CONFIG(tooltip)
        self.label_FontName.setText(QCoreApplication.translate("Dialog", u"Font name", None))
#if QT_CONFIG(tooltip)
        self.FontName.setToolTip(QCoreApplication.translate("Dialog", u"The font to use for texts and dimensions", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_FontSize.setToolTip(QCoreApplication.translate("Dialog", u"The font size in system units", None))
#endif // QT_CONFIG(tooltip)
        self.label_FontSize.setText(QCoreApplication.translate("Dialog", u"Font size", None))
#if QT_CONFIG(tooltip)
        self.FontSize.setToolTip(QCoreApplication.translate("Dialog", u"The font size in system units", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_LineSpacing.setToolTip(QCoreApplication.translate("Dialog", u"The line spacing for multi-line texts and labels (relative to the font size)", None))
#endif // QT_CONFIG(tooltip)
        self.label_LineSpacing.setText(QCoreApplication.translate("Dialog", u"Line spacing factor", None))
#if QT_CONFIG(tooltip)
        self.LineSpacing.setToolTip(QCoreApplication.translate("Dialog", u"The line spacing for multi-line texts and labels (relative to the font size)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_TextColor.setToolTip(QCoreApplication.translate("Dialog", u"The color of texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.label_TextColor.setText(QCoreApplication.translate("Dialog", u"Text color", None))
#if QT_CONFIG(tooltip)
        self.TextColor.setToolTip(QCoreApplication.translate("Dialog", u"The color of texts, dimension texts and label texts", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Lines and arrows", None))
#if QT_CONFIG(tooltip)
        self.label_ShowLine.setToolTip(QCoreApplication.translate("Dialog", u"If it is checked it will display the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.label_ShowLine.setText(QCoreApplication.translate("Dialog", u"Show dimension line", None))
#if QT_CONFIG(tooltip)
        self.ShowLine.setToolTip(QCoreApplication.translate("Dialog", u"If it is checked it will display the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.ShowLine.setText("")
#if QT_CONFIG(tooltip)
        self.label_LineWidth.setToolTip(QCoreApplication.translate("Dialog", u"The width of the lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_LineWidth.setText(QCoreApplication.translate("Dialog", u"Line width", None))
#if QT_CONFIG(tooltip)
        self.LineWidth.setToolTip(QCoreApplication.translate("Dialog", u"The width of the lines", None))
#endif // QT_CONFIG(tooltip)
        self.LineWidth.setSuffix(QCoreApplication.translate("Dialog", u" px", None))
#if QT_CONFIG(tooltip)
        self.label_ArrowType.setToolTip(QCoreApplication.translate("Dialog", u"The type of arrows or markers to use for dimensions and labels", None))
#endif // QT_CONFIG(tooltip)
        self.label_ArrowType.setText(QCoreApplication.translate("Dialog", u"Arrow type", None))
        self.ArrowType.setItemText(0, QCoreApplication.translate("Dialog", u"Dot", None))
        self.ArrowType.setItemText(1, QCoreApplication.translate("Dialog", u"Circle", None))
        self.ArrowType.setItemText(2, QCoreApplication.translate("Dialog", u"Arrow", None))
        self.ArrowType.setItemText(3, QCoreApplication.translate("Dialog", u"Tick", None))
        self.ArrowType.setItemText(4, QCoreApplication.translate("Dialog", u"Tick-2", None))

#if QT_CONFIG(tooltip)
        self.ArrowType.setToolTip(QCoreApplication.translate("Dialog", u"The type of arrows or markers to use for dimensions and labels", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_ArrowSize.setToolTip(QCoreApplication.translate("Dialog", u"The size of the arrows or markers in system units", None))
#endif // QT_CONFIG(tooltip)
        self.label_ArrowSize.setText(QCoreApplication.translate("Dialog", u"Arrow size", None))
#if QT_CONFIG(tooltip)
        self.ArrowSize.setToolTip(QCoreApplication.translate("Dialog", u"The size of the arrows or markers in system units", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_LineColor.setToolTip(QCoreApplication.translate("Dialog", u"The color of lines and arrows", None))
#endif // QT_CONFIG(tooltip)
        self.label_LineColor.setText(QCoreApplication.translate("Dialog", u"Line and arrow color", None))
#if QT_CONFIG(tooltip)
        self.LineColor.setToolTip(QCoreApplication.translate("Dialog", u"The color of lines and arrows", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Units", None))
#if QT_CONFIG(tooltip)
        self.label_ShowUnit.setToolTip(QCoreApplication.translate("Dialog", u"If it is checked it will show the unit next to the dimension value", None))
#endif // QT_CONFIG(tooltip)
        self.label_ShowUnit.setText(QCoreApplication.translate("Dialog", u"Show unit", None))
#if QT_CONFIG(tooltip)
        self.ShowUnit.setToolTip(QCoreApplication.translate("Dialog", u"If it is checked it will show the unit next to the dimension value", None))
#endif // QT_CONFIG(tooltip)
        self.ShowUnit.setText("")
#if QT_CONFIG(tooltip)
        self.label_UnitOverride.setToolTip(QCoreApplication.translate("Dialog", u"Specify a valid length unit like mm, m, in, ft, to force displaying the dimension value in this unit", None))
#endif // QT_CONFIG(tooltip)
        self.label_UnitOverride.setText(QCoreApplication.translate("Dialog", u"Unit override", None))
#if QT_CONFIG(tooltip)
        self.UnitOverride.setToolTip(QCoreApplication.translate("Dialog", u"Specify a valid length unit like mm, m, in, ft, to force displaying the dimension value in this unit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_Decimals.setToolTip(QCoreApplication.translate("Dialog", u"The number of decimals to show for dimension values", None))
#endif // QT_CONFIG(tooltip)
        self.label_Decimals.setText(QCoreApplication.translate("Dialog", u"Number of decimals", None))
#if QT_CONFIG(tooltip)
        self.Decimals.setToolTip(QCoreApplication.translate("Dialog", u"The number of decimals to show for dimension values", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Dimension details", None))
#if QT_CONFIG(tooltip)
        self.label_DimOvershoot.setToolTip(QCoreApplication.translate("Dialog", u"The distance the dimension line is additionally extended", None))
#endif // QT_CONFIG(tooltip)
        self.label_DimOvershoot.setText(QCoreApplication.translate("Dialog", u"Dimension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.DimOvershoot.setToolTip(QCoreApplication.translate("Dialog", u"The distance the dimension line is additionally extended", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_ExtLines.setToolTip(QCoreApplication.translate("Dialog", u"The length of the extension lines", None))
#endif // QT_CONFIG(tooltip)
        self.label_ExtLines.setText(QCoreApplication.translate("Dialog", u"Extension line length", None))
#if QT_CONFIG(tooltip)
        self.ExtLines.setToolTip(QCoreApplication.translate("Dialog", u"The length of the extension lines", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_ExtOvershoot.setToolTip(QCoreApplication.translate("Dialog", u"The distance the extension lines are additionally extended beyond the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.label_ExtOvershoot.setText(QCoreApplication.translate("Dialog", u"Extension line overshoot", None))
#if QT_CONFIG(tooltip)
        self.ExtOvershoot.setToolTip(QCoreApplication.translate("Dialog", u"The distance the extension lines are additionally extended beyond the dimension line", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_TextSpacing.setToolTip(QCoreApplication.translate("Dialog", u"The distance between the dimension text and the dimension line", None))
#endif // QT_CONFIG(tooltip)
        self.label_TextSpacing.setText(QCoreApplication.translate("Dialog", u"Text spacing", None))
#if QT_CONFIG(tooltip)
        self.TextSpacing.setToolTip(QCoreApplication.translate("Dialog", u"The distance between the dimension text and the dimension line", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

