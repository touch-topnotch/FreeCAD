# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgProjectInformation.ui'
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
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)

class Ui_Gui_Dialog_DlgProjectInformation(object):
    def setupUi(self, Gui__Dialog__DlgProjectInformation):
        if not Gui__Dialog__DlgProjectInformation.objectName():
            Gui__Dialog__DlgProjectInformation.setObjectName(u"Gui__Dialog__DlgProjectInformation")
        Gui__Dialog__DlgProjectInformation.resize(597, 540)
        Gui__Dialog__DlgProjectInformation.setSizeGripEnabled(True)
        Gui__Dialog__DlgProjectInformation.setModal(True)
        self.gridLayout = QGridLayout(Gui__Dialog__DlgProjectInformation)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxInfo = QGroupBox(Gui__Dialog__DlgProjectInformation)
        self.groupBoxInfo.setObjectName(u"groupBoxInfo")
        self.gridLayout1 = QGridLayout(self.groupBoxInfo)
        self.gridLayout1.setSpacing(6)
        self.gridLayout1.setContentsMargins(11, 11, 11, 11)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(9, 9, 9, 9)
        self.textLabelName = QLabel(self.groupBoxInfo)
        self.textLabelName.setObjectName(u"textLabelName")
        self.textLabelName.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelName, 0, 0, 1, 1)

        self.lineEditName = QLineEdit(self.groupBoxInfo)
        self.lineEditName.setObjectName(u"lineEditName")
        self.lineEditName.setMinimumSize(QSize(0, 25))
        self.lineEditName.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditName, 0, 1, 1, 1)

        self.textLabelPath = QLabel(self.groupBoxInfo)
        self.textLabelPath.setObjectName(u"textLabelPath")
        self.textLabelPath.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelPath, 1, 0, 1, 1)

        self.lineEditPath = QLineEdit(self.groupBoxInfo)
        self.lineEditPath.setObjectName(u"lineEditPath")
        self.lineEditPath.setMinimumSize(QSize(0, 25))
        self.lineEditPath.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditPath, 1, 1, 1, 1)

        self.textLabelUuid = QLabel(self.groupBoxInfo)
        self.textLabelUuid.setObjectName(u"textLabelUuid")
        self.textLabelUuid.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelUuid, 2, 0, 1, 1)

        self.lineEditUuid = QLineEdit(self.groupBoxInfo)
        self.lineEditUuid.setObjectName(u"lineEditUuid")
        self.lineEditUuid.setMinimumSize(QSize(0, 25))
        self.lineEditUuid.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditUuid, 2, 1, 1, 1)

        self.textLabelProgramVersion = QLabel(self.groupBoxInfo)
        self.textLabelProgramVersion.setObjectName(u"textLabelProgramVersion")
        self.textLabelProgramVersion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelProgramVersion, 3, 0, 1, 1)

        self.lineEditProgramVersion = QLineEdit(self.groupBoxInfo)
        self.lineEditProgramVersion.setObjectName(u"lineEditProgramVersion")
        self.lineEditProgramVersion.setMinimumSize(QSize(0, 25))
        self.lineEditProgramVersion.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditProgramVersion, 3, 1, 1, 1)

        self.textLabelUnitSystem = QLabel(self.groupBoxInfo)
        self.textLabelUnitSystem.setObjectName(u"textLabelUnitSystem")
        self.textLabelUnitSystem.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelUnitSystem, 4, 0, 1, 1)

        self.comboBox_unitSystem = QComboBox(self.groupBoxInfo)
        self.comboBox_unitSystem.setObjectName(u"comboBox_unitSystem")

        self.gridLayout1.addWidget(self.comboBox_unitSystem, 4, 1, 1, 1)

        self.textLabelCreator = QLabel(self.groupBoxInfo)
        self.textLabelCreator.setObjectName(u"textLabelCreator")
        self.textLabelCreator.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelCreator, 5, 0, 1, 1)

        self.lineEditCreator = QLineEdit(self.groupBoxInfo)
        self.lineEditCreator.setObjectName(u"lineEditCreator")
        self.lineEditCreator.setMinimumSize(QSize(0, 25))

        self.gridLayout1.addWidget(self.lineEditCreator, 5, 1, 1, 1)

        self.textLabelCreateDate = QLabel(self.groupBoxInfo)
        self.textLabelCreateDate.setObjectName(u"textLabelCreateDate")
        self.textLabelCreateDate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelCreateDate, 6, 0, 1, 1)

        self.lineEditDate = QLineEdit(self.groupBoxInfo)
        self.lineEditDate.setObjectName(u"lineEditDate")
        self.lineEditDate.setMinimumSize(QSize(0, 25))
        self.lineEditDate.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditDate, 6, 1, 1, 1)

        self.textLabelLastMod = QLabel(self.groupBoxInfo)
        self.textLabelLastMod.setObjectName(u"textLabelLastMod")
        self.textLabelLastMod.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelLastMod, 7, 0, 1, 1)

        self.lineEditLastMod = QLineEdit(self.groupBoxInfo)
        self.lineEditLastMod.setObjectName(u"lineEditLastMod")
        self.lineEditLastMod.setMinimumSize(QSize(0, 25))

        self.gridLayout1.addWidget(self.lineEditLastMod, 7, 1, 1, 1)

        self.textLabelLastModDate = QLabel(self.groupBoxInfo)
        self.textLabelLastModDate.setObjectName(u"textLabelLastModDate")
        self.textLabelLastModDate.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelLastModDate, 8, 0, 1, 1)

        self.lineEditLastModDate = QLineEdit(self.groupBoxInfo)
        self.lineEditLastModDate.setObjectName(u"lineEditLastModDate")
        self.lineEditLastModDate.setMinimumSize(QSize(0, 25))
        self.lineEditLastModDate.setReadOnly(True)

        self.gridLayout1.addWidget(self.lineEditLastModDate, 8, 1, 1, 1)

        self.textLabelCompany = QLabel(self.groupBoxInfo)
        self.textLabelCompany.setObjectName(u"textLabelCompany")
        self.textLabelCompany.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelCompany, 9, 0, 1, 1)

        self.lineEditCompany = QLineEdit(self.groupBoxInfo)
        self.lineEditCompany.setObjectName(u"lineEditCompany")
        self.lineEditCompany.setMinimumSize(QSize(0, 25))

        self.gridLayout1.addWidget(self.lineEditCompany, 9, 1, 1, 1)

        self.textLabelLicense = QLabel(self.groupBoxInfo)
        self.textLabelLicense.setObjectName(u"textLabelLicense")
        self.textLabelLicense.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelLicense, 10, 0, 1, 1)

        self.comboLicense = QComboBox(self.groupBoxInfo)
        self.comboLicense.setObjectName(u"comboLicense")

        self.gridLayout1.addWidget(self.comboLicense, 10, 1, 1, 1)

        self.textLabelLicenseURL = QLabel(self.groupBoxInfo)
        self.textLabelLicenseURL.setObjectName(u"textLabelLicenseURL")
        self.textLabelLicenseURL.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelLicenseURL, 11, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEditLicenseURL = QLineEdit(self.groupBoxInfo)
        self.lineEditLicenseURL.setObjectName(u"lineEditLicenseURL")

        self.horizontalLayout_2.addWidget(self.lineEditLicenseURL)

        self.pushButtonOpenURL = QPushButton(self.groupBoxInfo)
        self.pushButtonOpenURL.setObjectName(u"pushButtonOpenURL")

        self.horizontalLayout_2.addWidget(self.pushButtonOpenURL)


        self.gridLayout1.addLayout(self.horizontalLayout_2, 11, 1, 1, 1)

        self.textLabelComment = QLabel(self.groupBoxInfo)
        self.textLabelComment.setObjectName(u"textLabelComment")
        self.textLabelComment.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout1.addWidget(self.textLabelComment, 12, 0, 1, 1)

        self.textEditComment = QTextEdit(self.groupBoxInfo)
        self.textEditComment.setObjectName(u"textEditComment")

        self.gridLayout1.addWidget(self.textEditComment, 12, 1, 2, 1)

        self.spacerItem = QSpacerItem(91, 240, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout1.addItem(self.spacerItem, 13, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBoxInfo, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Gui__Dialog__DlgProjectInformation)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.textLabelName.setBuddy(self.lineEditName)
        self.textLabelCreator.setBuddy(self.lineEditCreator)
        self.textLabelCreateDate.setBuddy(self.lineEditDate)
        self.textLabelLastMod.setBuddy(self.lineEditLastMod)
        self.textLabelLastModDate.setBuddy(self.lineEditLastModDate)
        self.textLabelCompany.setBuddy(self.lineEditCompany)
        self.textLabelComment.setBuddy(self.textEditComment)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Gui__Dialog__DlgProjectInformation)
        self.buttonBox.accepted.connect(Gui__Dialog__DlgProjectInformation.accept)
        self.buttonBox.rejected.connect(Gui__Dialog__DlgProjectInformation.reject)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgProjectInformation)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgProjectInformation):
        Gui__Dialog__DlgProjectInformation.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Document information", None))
        self.groupBoxInfo.setTitle(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Information", None))
        self.textLabelName.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"&Name:", None))
        self.textLabelPath.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Path:", None))
        self.textLabelUuid.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"UUID:", None))
        self.textLabelProgramVersion.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Program version:", None))
        self.textLabelUnitSystem.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Unit System:", None))
#if QT_CONFIG(tooltip)
        self.comboBox_unitSystem.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Unit system for this file", None))
#endif // QT_CONFIG(tooltip)
        self.textLabelCreator.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Created &by:", None))
        self.textLabelCreateDate.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Creation &date:", None))
        self.textLabelLastMod.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"&Last modified by:", None))
        self.textLabelLastModDate.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Last &modification date:", None))
        self.textLabelCompany.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Com&pany:", None))
        self.textLabelLicense.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"License information:", None))
        self.textLabelLicenseURL.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"License URL", None))
        self.pushButtonOpenURL.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"Open in browser", None))
        self.textLabelComment.setText(QCoreApplication.translate("Gui::Dialog::DlgProjectInformation", u"&Comment:", None))
    # retranslateUi

