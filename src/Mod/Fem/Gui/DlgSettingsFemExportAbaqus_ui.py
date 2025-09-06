# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsFemExportAbaqus.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_FemGui_DlgSettingsFemExportAbaqus(object):
    def setupUi(self, FemGui__DlgSettingsFemExportAbaqus):
        if not FemGui__DlgSettingsFemExportAbaqus.objectName():
            FemGui__DlgSettingsFemExportAbaqus.setObjectName(u"FemGui__DlgSettingsFemExportAbaqus")
        FemGui__DlgSettingsFemExportAbaqus.resize(400, 98)
        self.gridLayout_4 = QGridLayout(FemGui__DlgSettingsFemExportAbaqus)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(FemGui__DlgSettingsFemExportAbaqus)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.girdLayoutAbaqus = QGridLayout()
        self.girdLayoutAbaqus.setObjectName(u"girdLayoutAbaqus")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")

        self.girdLayoutAbaqus.addWidget(self.label1, 0, 0, 1, 1)

        self.comboBoxElemChoiceParam = Gui_PrefComboBox(self.groupBox)
        self.comboBoxElemChoiceParam.addItem("")
        self.comboBoxElemChoiceParam.addItem("")
        self.comboBoxElemChoiceParam.addItem("")
        self.comboBoxElemChoiceParam.setObjectName(u"comboBoxElemChoiceParam")
        self.comboBoxElemChoiceParam.setProperty(u"prefEntry", u"AbaqusElementChoice")
        self.comboBoxElemChoiceParam.setProperty(u"prefPath", u"Mod/Fem/Abaqus")

        self.girdLayoutAbaqus.addWidget(self.comboBoxElemChoiceParam, 0, 1, 1, 1)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")

        self.girdLayoutAbaqus.addWidget(self.label2, 1, 0, 1, 1)

        self.checkBoxWriteGroups = Gui_PrefCheckBox(self.groupBox)
        self.checkBoxWriteGroups.setObjectName(u"checkBoxWriteGroups")
        self.checkBoxWriteGroups.setChecked(False)
        self.checkBoxWriteGroups.setProperty(u"prefEntry", u"AbaqusWriteGroups")
        self.checkBoxWriteGroups.setProperty(u"prefPath", u"Mod/Fem/Abaqus")

        self.girdLayoutAbaqus.addWidget(self.checkBoxWriteGroups, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.girdLayoutAbaqus, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 82, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(FemGui__DlgSettingsFemExportAbaqus)

        QMetaObject.connectSlotsByName(FemGui__DlgSettingsFemExportAbaqus)
    # setupUi

    def retranslateUi(self, FemGui__DlgSettingsFemExportAbaqus):
        FemGui__DlgSettingsFemExportAbaqus.setWindowTitle(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"INP", None))
        self.groupBox.setTitle(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"Export", None))
        self.label1.setText(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"Which mesh elements to export", None))
        self.comboBoxElemChoiceParam.setItemText(0, QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"All", None))
        self.comboBoxElemChoiceParam.setItemText(1, QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"Highest", None))
        self.comboBoxElemChoiceParam.setItemText(2, QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"FEM", None))

#if QT_CONFIG(tooltip)
        self.comboBoxElemChoiceParam.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"All: All elements will be exported.\n"
"\n"
"Highest: Only the highest elements will be exported. This means volumes for a volume mesh and faces for a shell mesh.\n"
"\n"
"FEM: Only FEM elements will be exported. This means only edges\n"
"not belonging to faces and faces not belonging to volumes.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comboBoxElemChoiceParam.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBoxElemChoiceParam.setWhatsThis(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"element parameter: All: all elements, highest: highest elements only, FEM: FEM elements only (only edges not belonging to faces and faces not belonging to volumes)", None))
#endif // QT_CONFIG(whatsthis)
        self.label2.setText(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"Export group data", None))
#if QT_CONFIG(tooltip)
        self.checkBoxWriteGroups.setToolTip(QCoreApplication.translate("FemGui::DlgSettingsFemExportAbaqus", u"Mesh groups are exported too.\n"
"Every analysis feature and, if there are different materials,\n"
"material consists of two mesh groups, faces and nodes where\n"
"the constraint or material is applied.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxWriteGroups.setText("")
    # retranslateUi

