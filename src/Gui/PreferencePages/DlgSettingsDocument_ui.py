# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DlgSettingsDocument.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Gui_Dialog_DlgSettingsDocument(object):
    def setupUi(self, Gui__Dialog__DlgSettingsDocument):
        if not Gui__Dialog__DlgSettingsDocument.objectName():
            Gui__Dialog__DlgSettingsDocument.setObjectName(u"Gui__Dialog__DlgSettingsDocument")
        Gui__Dialog__DlgSettingsDocument.resize(607, 859)
        self.gridLayout_3 = QGridLayout(Gui__Dialog__DlgSettingsDocument)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.GroupBox5 = QGroupBox(Gui__Dialog__DlgSettingsDocument)
        self.GroupBox5.setObjectName(u"GroupBox5")
        self.gridLayout_4 = QGridLayout(self.GroupBox5)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.prefCheckNewDoc = Gui_PrefCheckBox(self.GroupBox5)
        self.prefCheckNewDoc.setObjectName(u"prefCheckNewDoc")
        self.prefCheckNewDoc.setChecked(False)
        self.prefCheckNewDoc.setProperty(u"prefEntry", u"CreateNewDoc")
        self.prefCheckNewDoc.setProperty(u"prefPath", u"Document")

        self.gridLayout_4.addWidget(self.prefCheckNewDoc, 0, 0, 1, 1)

        self.line1 = QFrame(self.GroupBox5)
        self.line1.setObjectName(u"line1")
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)
        self.line1.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line1, 1, 0, 1, 1)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setSpacing(6)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)
        self.textLabel1 = QLabel(self.GroupBox5)
        self.textLabel1.setObjectName(u"textLabel1")

        self.hboxLayout.addWidget(self.textLabel1)

        self.prefCompression = Gui_PrefSpinBox(self.GroupBox5)
        self.prefCompression.setObjectName(u"prefCompression")
        self.prefCompression.setValue(7)
        self.prefCompression.setProperty(u"prefEntry", u"CompressionLevel")
        self.prefCompression.setProperty(u"prefPath", u"Document")

        self.hboxLayout.addWidget(self.prefCompression)


        self.gridLayout_4.addLayout(self.hboxLayout, 2, 0, 1, 1)

        self.line1_2 = QFrame(self.GroupBox5)
        self.line1_2.setObjectName(u"line1_2")
        self.line1_2.setFrameShape(QFrame.HLine)
        self.line1_2.setFrameShadow(QFrame.Sunken)
        self.line1_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_4.addWidget(self.line1_2, 3, 0, 1, 1)

        self.prefUndoRedo = Gui_PrefCheckBox(self.GroupBox5)
        self.prefUndoRedo.setObjectName(u"prefUndoRedo")
        self.prefUndoRedo.setChecked(True)
        self.prefUndoRedo.setProperty(u"prefEntry", u"UsingUndo")
        self.prefUndoRedo.setProperty(u"prefPath", u"Document")

        self.gridLayout_4.addWidget(self.prefUndoRedo, 4, 0, 1, 1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setSpacing(6)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)
        self.textLabel1_2 = QLabel(self.GroupBox5)
        self.textLabel1_2.setObjectName(u"textLabel1_2")

        self.hboxLayout1.addWidget(self.textLabel1_2)

        self.prefUndoRedoSize = Gui_PrefSpinBox(self.GroupBox5)
        self.prefUndoRedoSize.setObjectName(u"prefUndoRedoSize")
        self.prefUndoRedoSize.setValue(20)
        self.prefUndoRedoSize.setProperty(u"prefEntry", u"MaxUndoSize")
        self.prefUndoRedoSize.setProperty(u"prefPath", u"Document")

        self.hboxLayout1.addWidget(self.prefUndoRedoSize)


        self.gridLayout_4.addLayout(self.hboxLayout1, 5, 0, 1, 1)

        self.line = QFrame(self.GroupBox5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 6, 0, 1, 1)

        self.prefCanAbortRecompute = Gui_PrefCheckBox(self.GroupBox5)
        self.prefCanAbortRecompute.setObjectName(u"prefCanAbortRecompute")
        self.prefCanAbortRecompute.setProperty(u"prefEntry", u"CanAbortRecompute")
        self.prefCanAbortRecompute.setProperty(u"prefPath", u"Document")

        self.gridLayout_4.addWidget(self.prefCanAbortRecompute, 7, 0, 1, 1)


        self.gridLayout_3.addWidget(self.GroupBox5, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Gui__Dialog__DlgSettingsDocument)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.FormatTimeDocsLabel = QLabel(self.groupBox)
        self.FormatTimeDocsLabel.setObjectName(u"FormatTimeDocsLabel")
        font = QFont()
        font.setItalic(True)
        self.FormatTimeDocsLabel.setFont(font)
        self.FormatTimeDocsLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.FormatTimeDocsLabel.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.FormatTimeDocsLabel, 9, 0, 1, 1)

        self.prefDiscardTransaction = Gui_PrefCheckBox(self.groupBox)
        self.prefDiscardTransaction.setObjectName(u"prefDiscardTransaction")
        self.prefDiscardTransaction.setEnabled(False)
        self.prefDiscardTransaction.setProperty(u"prefEntry", u"TransactionsDiscard")
        self.prefDiscardTransaction.setProperty(u"prefPath", u"Document")

        self.gridLayout_2.addWidget(self.prefDiscardTransaction, 1, 0, 1, 1)

        self.line1_2_3 = QFrame(self.groupBox)
        self.line1_2_3.setObjectName(u"line1_2_3")
        self.line1_2_3.setFrameShape(QFrame.HLine)
        self.line1_2_3.setFrameShadow(QFrame.Sunken)
        self.line1_2_3.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_2.addWidget(self.line1_2_3, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.prefSaveThumbnail = Gui_PrefCheckBox(self.groupBox)
        self.prefSaveThumbnail.setObjectName(u"prefSaveThumbnail")
        self.prefSaveThumbnail.setChecked(True)
        self.prefSaveThumbnail.setProperty(u"prefEntry", u"SaveThumbnail")
        self.prefSaveThumbnail.setProperty(u"prefPath", u"Document")

        self.horizontalLayout_3.addWidget(self.prefSaveThumbnail)

        self.spacerItem = QSpacerItem(91, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.spacerItem)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.prefThumbnailSize = Gui_PrefSpinBox(self.groupBox)
        self.prefThumbnailSize.setObjectName(u"prefThumbnailSize")
        self.prefThumbnailSize.setMinimum(64)
        self.prefThumbnailSize.setMaximum(512)
        self.prefThumbnailSize.setValue(256)
        self.prefThumbnailSize.setProperty(u"prefEntry", u"ThumbnailSize")
        self.prefThumbnailSize.setProperty(u"prefPath", u"Document")

        self.horizontalLayout_3.addWidget(self.prefThumbnailSize)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setSpacing(6)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
        self.prefSaveBackupFiles = Gui_PrefCheckBox(self.groupBox)
        self.prefSaveBackupFiles.setObjectName(u"prefSaveBackupFiles")
        self.prefSaveBackupFiles.setChecked(True)
        self.prefSaveBackupFiles.setProperty(u"prefEntry", u"CreateBackupFiles")
        self.prefSaveBackupFiles.setProperty(u"prefPath", u"Document")

        self.hboxLayout2.addWidget(self.prefSaveBackupFiles)

        self.spacerItem1 = QSpacerItem(91, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem1)

        self.prefCountBackupFiles = Gui_PrefSpinBox(self.groupBox)
        self.prefCountBackupFiles.setObjectName(u"prefCountBackupFiles")
        self.prefCountBackupFiles.setMinimum(1)
        self.prefCountBackupFiles.setProperty(u"prefEntry", u"CountBackupFiles")
        self.prefCountBackupFiles.setProperty(u"prefPath", u"Document")

        self.hboxLayout2.addWidget(self.prefCountBackupFiles)


        self.gridLayout_2.addLayout(self.hboxLayout2, 7, 0, 1, 1)

        self.prefRecovery = Gui_PrefCheckBox(self.groupBox)
        self.prefRecovery.setObjectName(u"prefRecovery")
        self.prefRecovery.setChecked(True)
        self.prefRecovery.setProperty(u"prefEntry", u"RecoveryEnabled")
        self.prefRecovery.setProperty(u"prefPath", u"Document")

        self.gridLayout_2.addWidget(self.prefRecovery, 2, 0, 1, 1)

        self.prefSaveTransaction = Gui_PrefCheckBox(self.groupBox)
        self.prefSaveTransaction.setObjectName(u"prefSaveTransaction")
        self.prefSaveTransaction.setEnabled(False)
        self.prefSaveTransaction.setProperty(u"prefEntry", u"SaveTransactions")
        self.prefSaveTransaction.setProperty(u"prefPath", u"Document")

        self.gridLayout_2.addWidget(self.prefSaveTransaction, 0, 0, 1, 1)

        self.prefAddLogo = Gui_PrefCheckBox(self.groupBox)
        self.prefAddLogo.setObjectName(u"prefAddLogo")
        self.prefAddLogo.setChecked(False)
        self.prefAddLogo.setProperty(u"prefEntry", u"AddThumbnailLogo")
        self.prefAddLogo.setProperty(u"prefPath", u"Document")

        self.gridLayout_2.addWidget(self.prefAddLogo, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prefAutoSaveEnabled = Gui_PrefCheckBox(self.groupBox)
        self.prefAutoSaveEnabled.setObjectName(u"prefAutoSaveEnabled")
        self.prefAutoSaveEnabled.setChecked(True)
        self.prefAutoSaveEnabled.setProperty(u"prefEntry", u"AutoSaveEnabled")
        self.prefAutoSaveEnabled.setProperty(u"prefPath", u"Document")

        self.horizontalLayout.addWidget(self.prefAutoSaveEnabled)

        self.prefAutoSaveTimeout = Gui_PrefSpinBox(self.groupBox)
        self.prefAutoSaveTimeout.setObjectName(u"prefAutoSaveTimeout")
        self.prefAutoSaveTimeout.setSuffix(u" min")
        self.prefAutoSaveTimeout.setMinimum(1)
        self.prefAutoSaveTimeout.setMaximum(60)
        self.prefAutoSaveTimeout.setValue(15)
        self.prefAutoSaveTimeout.setProperty(u"prefEntry", u"AutoSaveTimeout")
        self.prefAutoSaveTimeout.setProperty(u"prefPath", u"Document")

        self.horizontalLayout.addWidget(self.prefAutoSaveTimeout)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setSpacing(6)
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.hboxLayout3.setContentsMargins(0, 0, 0, 0)
        self.prefSaveBackupExtension = Gui_PrefCheckBox(self.groupBox)
        self.prefSaveBackupExtension.setObjectName(u"prefSaveBackupExtension")
        self.prefSaveBackupExtension.setChecked(True)
        self.prefSaveBackupExtension.setProperty(u"prefEntry", u"UseFCBakExtension")
        self.prefSaveBackupExtension.setProperty(u"prefPath", u"Document")

        self.hboxLayout3.addWidget(self.prefSaveBackupExtension)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.hboxLayout3.addWidget(self.label_5)

        self.prefSaveBackupDateFormat = Gui_PrefLineEdit(self.groupBox)
        self.prefSaveBackupDateFormat.setObjectName(u"prefSaveBackupDateFormat")
        self.prefSaveBackupDateFormat.setText(u"%Y%m%d-%H%M%S")
        self.prefSaveBackupDateFormat.setProperty(u"prefEntry", u"SaveBackupDateFormat")
        self.prefSaveBackupDateFormat.setProperty(u"prefPath", u"Document")

        self.hboxLayout3.addWidget(self.prefSaveBackupDateFormat)


        self.gridLayout_2.addLayout(self.hboxLayout3, 8, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Gui__Dialog__DlgSettingsDocument)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.prefDuplicateLabel = Gui_PrefCheckBox(self.groupBox_2)
        self.prefDuplicateLabel.setObjectName(u"prefDuplicateLabel")
        self.prefDuplicateLabel.setProperty(u"prefEntry", u"DuplicateLabels")
        self.prefDuplicateLabel.setProperty(u"prefPath", u"Document")

        self.gridLayout.addWidget(self.prefDuplicateLabel, 0, 0, 1, 1)

        self.prefPartialLoading = Gui_PrefCheckBox(self.groupBox_2)
        self.prefPartialLoading.setObjectName(u"prefPartialLoading")
        self.prefPartialLoading.setProperty(u"prefEntry", u"NoPartialLoading")
        self.prefPartialLoading.setProperty(u"prefPath", u"Document")

        self.gridLayout.addWidget(self.prefPartialLoading, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Gui__Dialog__DlgSettingsDocument)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.prefAuthor = Gui_PrefLineEdit(self.groupBox_3)
        self.prefAuthor.setObjectName(u"prefAuthor")
        self.prefAuthor.setProperty(u"prefEntry", u"prefAuthor")
        self.prefAuthor.setProperty(u"prefPath", u"Document")

        self.gridLayout_5.addWidget(self.prefAuthor, 0, 1, 1, 1)

        self.prefSetAuthorOnSave = Gui_PrefCheckBox(self.groupBox_3)
        self.prefSetAuthorOnSave.setObjectName(u"prefSetAuthorOnSave")
        self.prefSetAuthorOnSave.setProperty(u"prefEntry", u"prefSetAuthorOnSave")
        self.prefSetAuthorOnSave.setProperty(u"prefPath", u"Document")

        self.gridLayout_5.addWidget(self.prefSetAuthorOnSave, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.prefCompany = Gui_PrefLineEdit(self.groupBox_3)
        self.prefCompany.setObjectName(u"prefCompany")
        self.prefCompany.setProperty(u"prefEntry", u"prefCompany")
        self.prefCompany.setProperty(u"prefPath", u"Document")

        self.gridLayout_5.addWidget(self.prefCompany, 1, 1, 1, 2)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 1)

        self.prefLicenseType = Gui_PrefComboBox(self.groupBox_3)
        self.prefLicenseType.setObjectName(u"prefLicenseType")
        self.prefLicenseType.setEnabled(True)
        self.prefLicenseType.setEditable(False)
        self.prefLicenseType.setProperty(u"prefEntry", u"prefLicenseType")
        self.prefLicenseType.setProperty(u"prefPath", u"Document")

        self.gridLayout_5.addWidget(self.prefLicenseType, 2, 1, 1, 2)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 3, 0, 1, 1)

        self.prefLicenseUrl = Gui_PrefLineEdit(self.groupBox_3)
        self.prefLicenseUrl.setObjectName(u"prefLicenseUrl")
        self.prefLicenseUrl.setText(u"https://en.wikipedia.org/wiki/All_rights_reserved")
        self.prefLicenseUrl.setReadOnly(False)
        self.prefLicenseUrl.setProperty(u"prefEntry", u"prefLicenseUrl")
        self.prefLicenseUrl.setProperty(u"prefPath", u"Document")

        self.gridLayout_5.addWidget(self.prefLicenseUrl, 3, 1, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.spacerItem2 = QSpacerItem(429, 37, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.spacerItem2, 4, 0, 1, 1)


        self.retranslateUi(Gui__Dialog__DlgSettingsDocument)
        self.prefSaveBackupFiles.toggled.connect(self.prefCountBackupFiles.setEnabled)
        self.prefAutoSaveEnabled.toggled.connect(self.prefAutoSaveTimeout.setEnabled)
        self.prefSaveBackupFiles.toggled.connect(self.prefSaveBackupExtension.setEnabled)
        self.prefSaveBackupFiles.toggled.connect(self.prefSaveBackupDateFormat.setEnabled)
        self.prefSaveThumbnail.toggled.connect(self.prefThumbnailSize.setEnabled)

        QMetaObject.connectSlotsByName(Gui__Dialog__DlgSettingsDocument)
    # setupUi

    def retranslateUi(self, Gui__Dialog__DlgSettingsDocument):
        Gui__Dialog__DlgSettingsDocument.setWindowTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Document", None))
        self.GroupBox5.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"General", None))
#if QT_CONFIG(tooltip)
        self.prefCheckNewDoc.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"The application will create a new document when started", None))
#endif // QT_CONFIG(tooltip)
        self.prefCheckNewDoc.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Create new document at start up", None))
        self.textLabel1.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Document save compression level\n"
"(0 = none, 9 = highest, 7 = default)", None))
#if QT_CONFIG(tooltip)
        self.prefCompression.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Compression level for FCStd files", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prefUndoRedo.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"All changes in documents are stored so that they can be undone/redone", None))
#endif // QT_CONFIG(tooltip)
        self.prefUndoRedo.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Using Undo/Redo on documents", None))
        self.textLabel1_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Maximum Undo/Redo steps", None))
#if QT_CONFIG(tooltip)
        self.prefUndoRedoSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"How many Undo/Redo steps should be recorded", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prefCanAbortRecompute.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Allow user aborting document recomputation by pressing ESC.\n"
"This feature may slightly increase recomputation time.", None))
#endif // QT_CONFIG(tooltip)
        self.prefCanAbortRecompute.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Allow aborting recomputation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Storage", None))
        self.FormatTimeDocsLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Show format documentation", None))
        self.prefDiscardTransaction.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Discard saved transaction after saving document", None))
#if QT_CONFIG(tooltip)
        self.prefSaveThumbnail.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"A thumbnail will be stored when document is saved", None))
#endif // QT_CONFIG(tooltip)
        self.prefSaveThumbnail.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Save thumbnail into project file when saving document", None))
        self.label_6.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Size", None))
#if QT_CONFIG(tooltip)
        self.prefThumbnailSize.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Sets the size of the thumbnail that is stored in the document.\n"
"Common sizes are 128, 256 and 512", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prefSaveBackupFiles.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"How many backup files will be kept when saving document", None))
#endif // QT_CONFIG(tooltip)
        self.prefSaveBackupFiles.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Maximum number of backup files to keep when resaving document", None))
#if QT_CONFIG(tooltip)
        self.prefRecovery.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"If there is a recovery file available the application will\n"
"automatically run a file recovery when it is started.", None))
#endif // QT_CONFIG(tooltip)
        self.prefRecovery.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Run AutoRecovery at startup", None))
        self.prefSaveTransaction.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Saving transactions (Auto-save)", None))
#if QT_CONFIG(tooltip)
        self.prefAddLogo.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"The program logo will be added to the thumbnail", None))
#endif // QT_CONFIG(tooltip)
        self.prefAddLogo.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Add the program logo to the generated thumbnail", None))
#if QT_CONFIG(tooltip)
        self.prefAutoSaveEnabled.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"How often a recovery file is written", None))
#endif // QT_CONFIG(tooltip)
        self.prefAutoSaveEnabled.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Save AutoRecovery information every", None))
#if QT_CONFIG(tooltip)
        self.prefSaveBackupExtension.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Backup files will get extension '.FCbak' and file names\n"
"get date suffix according to the specified format", None))
#endif // QT_CONFIG(tooltip)
        self.prefSaveBackupExtension.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Use date and FCBak extension", None))
        self.label_5.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Date format", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Document objects", None))
#if QT_CONFIG(tooltip)
        self.prefDuplicateLabel.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Allow objects to have same label", None))
#endif // QT_CONFIG(tooltip)
        self.prefDuplicateLabel.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Allow duplicate object labels in one document", None))
#if QT_CONFIG(tooltip)
        self.prefPartialLoading.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Enable partial loading of external linked documents.\n"
"Then only referenced objects and their dependencies will be loaded\n"
"when a linked document is auto-opened together with the main document.\n"
"A partially loaded document cannot be edited. Double click the document\n"
"icon in the tree view to fully reload it.", None))
#endif // QT_CONFIG(tooltip)
        self.prefPartialLoading.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Disable partial loading of external linked objects", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Authoring and License", None))
        self.label_3.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Author name", None))
#if QT_CONFIG(tooltip)
        self.prefAuthor.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"All documents that will be created will get the specified author name.\n"
"Keep blank for anonymous.\n"
"You can also use the form: John Doe <john@doe.com>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.prefSetAuthorOnSave.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"The field 'Last modified by' will be set to specified author when saving the file", None))
#endif // QT_CONFIG(tooltip)
        self.prefSetAuthorOnSave.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Set on save", None))
        self.label_4.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Company", None))
#if QT_CONFIG(tooltip)
        self.prefCompany.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Default company name to use for new files", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Default license", None))
#if QT_CONFIG(tooltip)
        self.prefLicenseType.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"Default license for new documents", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"License URL", None))
#if QT_CONFIG(tooltip)
        self.prefLicenseUrl.setToolTip(QCoreApplication.translate("Gui::Dialog::DlgSettingsDocument", u"URL describing more about the license", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

