# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferencesNativeIFC.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 663)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox = Gui_PrefComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setProperty(u"prefEntry", u"ImportStrategy")
        self.comboBox.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.comboBox_2 = Gui_PrefComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setProperty(u"prefEntry", u"ShapeMode")
        self.comboBox_2.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.gridLayout.addWidget(self.comboBox_2, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.checkBox_3 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setProperty(u"prefEntry", u"SwitchWB")
        self.checkBox_3.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_7 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setProperty(u"prefEntry", u"LoadPsets")
        self.checkBox_7.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_9 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setProperty(u"prefEntry", u"LoadTypes")
        self.checkBox_9.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_8 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setProperty(u"prefEntry", u"LoadMaterials")
        self.checkBox_8.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_11 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setProperty(u"prefEntry", u"LoadLayers")
        self.checkBox_11.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_11)

        self.checkBox_10 = Gui_PrefCheckBox(self.groupBox)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setProperty(u"prefEntry", u"KeepAggregated")
        self.checkBox_10.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.checkBox = Gui_PrefCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.checkBox.setProperty(u"prefEntry", u"AskAgain")
        self.checkBox.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_2.addWidget(self.checkBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = Gui_PrefCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setProperty(u"prefEntry", u"AskBeforeSaving")
        self.checkBox_2.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_13 = Gui_PrefCheckBox(self.groupBox_4)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setProperty(u"prefEntry", u"SingleDoc")
        self.checkBox_13.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_5.addWidget(self.checkBox_13)

        self.checkBox_12 = Gui_PrefCheckBox(self.groupBox_4)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setProperty(u"prefEntry", u"SingleDocAskAgain")
        self.checkBox_12.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_5.addWidget(self.checkBox_12)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_4 = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setProperty(u"prefEntry", u"ProjectFull")
        self.checkBox_4.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_4.addWidget(self.checkBox_4)

        self.checkBox_5 = Gui_PrefCheckBox(self.groupBox_3)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setProperty(u"prefEntry", u"ProjectAskAgain")
        self.checkBox_5.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_4.addWidget(self.checkBox_5)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_14 = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setProperty(u"prefEntry", u"ConvertTypeKeepOriginal")
        self.checkBox_14.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_6.addWidget(self.checkBox_14)

        self.checkBox_15 = Gui_PrefCheckBox(self.groupBox_5)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setProperty(u"prefEntry", u"ConvertTypeAskAgain")
        self.checkBox_15.setProperty(u"prefPath", u"Mod/NativeIFC")

        self.verticalLayout_6.addWidget(self.checkBox_15)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        self.comboBox_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Native IFC", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Import", None))
        self.label.setText(QCoreApplication.translate("Form", u"Initial import", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Only root object (default)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Project structure (levels)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"All individual IFC objects", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Form", u"How the IFC file will initially be imported: Only one object, only project structure, or all individual objects.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Representation type", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Load full shape (slower)", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Load 3D representation only, no shape (default)", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"No 3D representation", None))

#if QT_CONFIG(tooltip)
        self.comboBox_2.setToolTip(QCoreApplication.translate("Form", u"The type of object created at import. Coin only is much faster, but does not provide the full shape information. Convert between the two anytime by right-clicking the object tree", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkBox_3.setToolTip(QCoreApplication.translate("Form", u"If this is checked, the BIM workbench will be loaded after import", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"Switch to BIM workbench after import", None))
#if QT_CONFIG(tooltip)
        self.checkBox_7.setToolTip(QCoreApplication.translate("Form", u"Load all property sets automatically when opening an IFC file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"Preload property sets", None))
#if QT_CONFIG(tooltip)
        self.checkBox_9.setToolTip(QCoreApplication.translate("Form", u"Load all types automatically when opening an IFC file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_9.setText(QCoreApplication.translate("Form", u"Preload types", None))
#if QT_CONFIG(tooltip)
        self.checkBox_8.setToolTip(QCoreApplication.translate("Form", u"Load all materials automatically when opening an IFC file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_8.setText(QCoreApplication.translate("Form", u"Preload materials", None))
#if QT_CONFIG(tooltip)
        self.checkBox_11.setToolTip(QCoreApplication.translate("Form", u"Load all layers automatically when opening an IFC file", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_11.setText(QCoreApplication.translate("Form", u"Preload layers", None))
#if QT_CONFIG(tooltip)
        self.checkBox_10.setToolTip(QCoreApplication.translate("Form", u"When enabling this, the original version of objects dropped onto an IFC project tree will not be deleted", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_10.setText(QCoreApplication.translate("Form", u"Keep original version of aggregated objects", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Form", u"If this is checked, a dialog will be shown at each import", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Form", u"Show options dialog when importing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Export", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Show warning when saving", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"New Document", None))
        self.checkBox_13.setText(QCoreApplication.translate("Form", u"Always lock new documents", None))
        self.checkBox_12.setText(QCoreApplication.translate("Form", u"Ask every time", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"New Project", None))
#if QT_CONFIG(accessibility)
        self.checkBox_4.setAccessibleName(QCoreApplication.translate("Form", u"If this is checked, when creating a new projects, a default structure (site, building and storey) will be added under the project", None))
#endif // QT_CONFIG(accessibility)
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"Create a default structure", None))
#if QT_CONFIG(accessibility)
        self.checkBox_5.setAccessibleName(QCoreApplication.translate("Form", u"Enables asking the above question every time a project is created", None))
#endif // QT_CONFIG(accessibility)
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"Ask every time", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"New Type", None))
#if QT_CONFIG(tooltip)
        self.checkBox_14.setToolTip(QCoreApplication.translate("Form", u"When enabled, converting objects to IFC types will always keep the original object", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_14.setText(QCoreApplication.translate("Form", u"Always keep original object when converting to type", None))
#if QT_CONFIG(tooltip)
        self.checkBox_15.setToolTip(QCoreApplication.translate("Form", u"When enabled, a dialog will be shown each time when converting objects to IFC types", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_15.setText(QCoreApplication.translate("Form", u"Show dialog when converting to type", None))
    # retranslateUi

