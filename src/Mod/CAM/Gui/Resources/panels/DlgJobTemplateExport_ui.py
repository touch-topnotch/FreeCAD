# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgJobTemplateExport.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(371, 711)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.postProcessingGroup = QGroupBox(Dialog)
        self.postProcessingGroup.setObjectName(u"postProcessingGroup")
        self.postProcessingGroup.setCheckable(True)
        self.verticalLayout_2 = QVBoxLayout(self.postProcessingGroup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.postProcessingHint = QLineEdit(self.postProcessingGroup)
        self.postProcessingHint.setObjectName(u"postProcessingHint")
        self.postProcessingHint.setEnabled(False)
        self.postProcessingHint.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.postProcessingHint)


        self.verticalLayout.addWidget(self.postProcessingGroup)

        self.toolsGroup = QGroupBox(Dialog)
        self.toolsGroup.setObjectName(u"toolsGroup")
        self.toolsGroup.setCheckable(True)
        self.verticalLayout_3 = QVBoxLayout(self.toolsGroup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolsList = QListWidget(self.toolsGroup)
        self.toolsList.setObjectName(u"toolsList")

        self.verticalLayout_3.addWidget(self.toolsList)


        self.verticalLayout.addWidget(self.toolsGroup)

        self.settingsGroup = QGroupBox(Dialog)
        self.settingsGroup.setObjectName(u"settingsGroup")
        self.settingsGroup.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.settingsGroup)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.settingOperationHeights = QCheckBox(self.settingsGroup)
        self.settingOperationHeights.setObjectName(u"settingOperationHeights")
        self.settingOperationHeights.setChecked(True)

        self.gridLayout_2.addWidget(self.settingOperationHeights, 1, 0, 1, 1)

        self.settingOperationDepths = QCheckBox(self.settingsGroup)
        self.settingOperationDepths.setObjectName(u"settingOperationDepths")
        self.settingOperationDepths.setChecked(True)

        self.gridLayout_2.addWidget(self.settingOperationDepths, 1, 1, 1, 1)

        self.settingToolRapid = QCheckBox(self.settingsGroup)
        self.settingToolRapid.setObjectName(u"settingToolRapid")
        self.settingToolRapid.setChecked(True)

        self.gridLayout_2.addWidget(self.settingToolRapid, 2, 0, 1, 1)

        self.settingCoolant = QCheckBox(self.settingsGroup)
        self.settingCoolant.setObjectName(u"settingCoolant")
        self.settingCoolant.setChecked(True)

        self.gridLayout_2.addWidget(self.settingCoolant, 2, 1, 1, 1)

        self.settingsOpsList = QListWidget(self.settingsGroup)
        self.settingsOpsList.setObjectName(u"settingsOpsList")

        self.gridLayout_2.addWidget(self.settingsOpsList, 3, 0, 1, 2)


        self.verticalLayout.addWidget(self.settingsGroup)

        self.stockGroup = QGroupBox(Dialog)
        self.stockGroup.setObjectName(u"stockGroup")
        self.stockGroup.setCheckable(True)
        self.gridLayout = QGridLayout(self.stockGroup)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stockExtent = QCheckBox(self.stockGroup)
        self.stockExtent.setObjectName(u"stockExtent")
        self.stockExtent.setChecked(True)

        self.gridLayout.addWidget(self.stockExtent, 0, 0, 1, 1)

        self.stockExtentHint = QLineEdit(self.stockGroup)
        self.stockExtentHint.setObjectName(u"stockExtentHint")
        self.stockExtentHint.setEnabled(False)
        self.stockExtentHint.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.stockExtentHint, 0, 1, 1, 1)

        self.stockPlacement = QCheckBox(self.stockGroup)
        self.stockPlacement.setObjectName(u"stockPlacement")
        self.stockPlacement.setChecked(True)

        self.gridLayout.addWidget(self.stockPlacement, 1, 0, 1, 1)

        self.stockPlacementHint = QLineEdit(self.stockGroup)
        self.stockPlacementHint.setObjectName(u"stockPlacementHint")
        self.stockPlacementHint.setEnabled(False)
        self.stockPlacementHint.setFocusPolicy(Qt.NoFocus)

        self.gridLayout.addWidget(self.stockPlacementHint, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.stockGroup)

        self.exportButtonBox = QWidget(Dialog)
        self.exportButtonBox.setObjectName(u"exportButtonBox")
        self.horizontalLayout = QHBoxLayout(self.exportButtonBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(267, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exportButton = QPushButton(self.exportButtonBox)
        self.exportButton.setObjectName(u"exportButton")

        self.horizontalLayout.addWidget(self.exportButton)


        self.verticalLayout.addWidget(self.exportButtonBox)

        self.dialogButtonBox = QDialogButtonBox(Dialog)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialogButtonBox)

        QWidget.setTabOrder(self.postProcessingGroup, self.stockExtent)
        QWidget.setTabOrder(self.stockExtent, self.stockPlacement)
        QWidget.setTabOrder(self.stockPlacement, self.settingsGroup)
        QWidget.setTabOrder(self.settingsGroup, self.settingOperationHeights)
        QWidget.setTabOrder(self.settingOperationHeights, self.settingOperationDepths)
        QWidget.setTabOrder(self.settingOperationDepths, self.settingToolRapid)
        QWidget.setTabOrder(self.settingToolRapid, self.toolsList)
        QWidget.setTabOrder(self.toolsList, self.dialogButtonBox)

        self.retranslateUi(Dialog)
        self.dialogButtonBox.accepted.connect(Dialog.accept)
        self.dialogButtonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Job Template Export", None))
#if QT_CONFIG(tooltip)
        self.postProcessingGroup.setToolTip(QCoreApplication.translate("Dialog", u"If enabled, include all post processing settings in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.postProcessingGroup.setTitle(QCoreApplication.translate("Dialog", u"Post Processing", None))
#if QT_CONFIG(tooltip)
        self.postProcessingHint.setToolTip(QCoreApplication.translate("Dialog", u"Hint about the current post processing configuration.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.toolsGroup.setToolTip(QCoreApplication.translate("Dialog", u"If enabled, tool controller definitions are stored in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.toolsGroup.setTitle(QCoreApplication.translate("Dialog", u"Tools", None))
#if QT_CONFIG(tooltip)
        self.toolsList.setToolTip(QCoreApplication.translate("Dialog", u"Check all tool controllers which should be included in the template.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settingsGroup.setToolTip(QCoreApplication.translate("Dialog", u"Enable to include values of the SetupSheet in the template.\n"
"\n"
"Any values of the SetupSheet that are changed from their default are preselected. If this field not selected the current SetupSheet was not modified.", None))
#endif // QT_CONFIG(tooltip)
        self.settingsGroup.setTitle(QCoreApplication.translate("Dialog", u"Setup Sheet", None))
#if QT_CONFIG(tooltip)
        self.settingOperationHeights.setToolTip(QCoreApplication.translate("Dialog", u"Enable to include the default heights for operations in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.settingOperationHeights.setText(QCoreApplication.translate("Dialog", u"Operation Heights", None))
        self.settingOperationDepths.setText(QCoreApplication.translate("Dialog", u"Operation Depths", None))
#if QT_CONFIG(tooltip)
        self.settingToolRapid.setToolTip(QCoreApplication.translate("Dialog", u"Enable to include the default rapid tool speeds in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.settingToolRapid.setText(QCoreApplication.translate("Dialog", u"Tool Rapid Speeds", None))
#if QT_CONFIG(tooltip)
        self.settingCoolant.setToolTip(QCoreApplication.translate("Dialog", u"Enable to include the default coolant mode in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.settingCoolant.setText(QCoreApplication.translate("Dialog", u"Coolant Mode", None))
#if QT_CONFIG(tooltip)
        self.settingsOpsList.setToolTip(QCoreApplication.translate("Dialog", u"Enable all operations for which the configuration values should be exported.\n"
"\n"
"Note that only operations which currently have configuration values set are listed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockGroup.setToolTip(QCoreApplication.translate("Dialog", u"If enabled, the creation of stock is included in the template. If a template does not include a stock definition the default stock creation algorithm will be used (creation from the Base object's bounding box).\n"
"\n"
"This option is most useful if stock is a box or cylinder, or if the machine has a standard placement for machining.\n"
"\n"
"Note that this option is disabled if a stock object from an existing solid is used in the job - they cannot be stored in a template.", None))
#endif // QT_CONFIG(tooltip)
        self.stockGroup.setTitle(QCoreApplication.translate("Dialog", u"Stock", None))
#if QT_CONFIG(tooltip)
        self.stockExtent.setToolTip(QCoreApplication.translate("Dialog", u"If enabled, the current size settings for the stock object are included in the template.\n"
"\n"
"For Box and Cylinder stocks this means the actual size of the stock solid being created.\n"
"\n"
"For stock from the Base object's bounding box it means the extra material in all directions. A stock object created from such a template will get its basic size from the new job's Base object and apply the stored extra settings.", None))
#endif // QT_CONFIG(tooltip)
        self.stockExtent.setText(QCoreApplication.translate("Dialog", u"Extent", None))
#if QT_CONFIG(tooltip)
        self.stockExtentHint.setToolTip(QCoreApplication.translate("Dialog", u"Hint about the current stock extent setting.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.stockPlacement.setToolTip(QCoreApplication.translate("Dialog", u"If enabled, the current placement of the stock solid is stored in the template.", None))
#endif // QT_CONFIG(tooltip)
        self.stockPlacement.setText(QCoreApplication.translate("Dialog", u"Placement", None))
#if QT_CONFIG(tooltip)
        self.stockPlacementHint.setToolTip(QCoreApplication.translate("Dialog", u"Hint about the current stock placement.", None))
#endif // QT_CONFIG(tooltip)
        self.exportButton.setText(QCoreApplication.translate("Dialog", u"Export", None))
    # retranslateUi

