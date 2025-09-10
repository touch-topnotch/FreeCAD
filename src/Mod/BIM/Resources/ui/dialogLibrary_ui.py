# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogLibrary.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(290, 798)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tree = QTreeView(Form)
        self.tree.setObjectName(u"tree")
        self.tree.setDragEnabled(True)

        self.verticalLayout.addWidget(self.tree)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonInsert = QPushButton(Form)
        self.buttonInsert.setObjectName(u"buttonInsert")

        self.horizontalLayout_4.addWidget(self.buttonInsert)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.buttonLink = QPushButton(Form)
        self.buttonLink.setObjectName(u"buttonLink")

        self.horizontalLayout_4.addWidget(self.buttonLink)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.searchBox = QLineEdit(Form)
        self.searchBox.setObjectName(u"searchBox")

        self.horizontalLayout.addWidget(self.searchBox)

        self.comboSearch = QComboBox(Form)
        self.comboSearch.addItem("")
        self.comboSearch.setObjectName(u"comboSearch")
        self.comboSearch.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.comboSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.buttonPreview = QPushButton(Form)
        self.buttonPreview.setObjectName(u"buttonPreview")
        self.buttonPreview.setFlat(True)

        self.horizontalLayout_5.addWidget(self.buttonPreview)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.framePreview = QLabel(Form)
        self.framePreview.setObjectName(u"framePreview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePreview.sizePolicy().hasHeightForWidth())
        self.framePreview.setSizePolicy(sizePolicy)
        self.framePreview.setMinimumSize(QSize(256, 256))
        self.framePreview.setMaximumSize(QSize(256, 256))
        self.framePreview.setScaledContents(True)
        self.framePreview.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.framePreview)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonOptions = QPushButton(Form)
        self.buttonOptions.setObjectName(u"buttonOptions")
        self.buttonOptions.setCheckable(False)
        self.buttonOptions.setFlat(True)

        self.horizontalLayout_3.addWidget(self.buttonOptions)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frameOptions = QFrame(Form)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setFrameShape(QFrame.StyledPanel)
        self.frameOptions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameOptions)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkOnline = QCheckBox(self.frameOptions)
        self.checkOnline.setObjectName(u"checkOnline")
        self.checkOnline.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkOnline)

        self.checkWebSearch = QCheckBox(self.frameOptions)
        self.checkWebSearch.setObjectName(u"checkWebSearch")

        self.verticalLayout_2.addWidget(self.checkWebSearch)

        self.check3DPreview = QCheckBox(self.frameOptions)
        self.check3DPreview.setObjectName(u"check3DPreview")

        self.verticalLayout_2.addWidget(self.check3DPreview)

        self.checkFCStdOnly = QCheckBox(self.frameOptions)
        self.checkFCStdOnly.setObjectName(u"checkFCStdOnly")
        self.checkFCStdOnly.setEnabled(True)

        self.verticalLayout_2.addWidget(self.checkFCStdOnly)

        self.label = QLabel(self.frameOptions)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)
        self.label.setIndent(24)

        self.verticalLayout_2.addWidget(self.label)

        self.checkThumbnail = QCheckBox(self.frameOptions)
        self.checkThumbnail.setObjectName(u"checkThumbnail")

        self.verticalLayout_2.addWidget(self.checkThumbnail)


        self.verticalLayout.addWidget(self.frameOptions)

        self.buttonSave = QPushButton(Form)
        self.buttonSave.setObjectName(u"buttonSave")

        self.verticalLayout.addWidget(self.buttonSave)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Library browser", None))
#if QT_CONFIG(tooltip)
        self.buttonInsert.setToolTip(QCoreApplication.translate("Form", u"Inserts the selected object in the current document", None))
#endif // QT_CONFIG(tooltip)
        self.buttonInsert.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"or", None))
#if QT_CONFIG(tooltip)
        self.buttonLink.setToolTip(QCoreApplication.translate("Form", u"Links the selected object in the current document. Only works in Offline mode", None))
#endif // QT_CONFIG(tooltip)
        self.buttonLink.setText(QCoreApplication.translate("Form", u"Link", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Search:", None))
        self.comboSearch.setItemText(0, QCoreApplication.translate("Form", u"...", None))

#if QT_CONFIG(tooltip)
        self.comboSearch.setToolTip(QCoreApplication.translate("Form", u"Search external websites", None))
#endif // QT_CONFIG(tooltip)
        self.buttonPreview.setText(QCoreApplication.translate("Form", u"Preview", None))
        self.framePreview.setText("")
        self.buttonOptions.setText(QCoreApplication.translate("Form", u"Options", None))
#if QT_CONFIG(tooltip)
        self.frameOptions.setToolTip(QCoreApplication.translate("Form", u"Save thumbnails when saving a file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkOnline.setToolTip(QCoreApplication.translate("Form", u"If this is checked, the library doesn't need to be installed. Contents will be fetched online.", None))
#endif // QT_CONFIG(tooltip)
        self.checkOnline.setText(QCoreApplication.translate("Form", u"Online mode", None))
#if QT_CONFIG(tooltip)
        self.checkWebSearch.setToolTip(QCoreApplication.translate("Form", u"Open the search results inside FreeCAD's web browser instead of the system browser", None))
#endif // QT_CONFIG(tooltip)
        self.checkWebSearch.setText(QCoreApplication.translate("Form", u"Open search in FreeCAD web view", None))
#if QT_CONFIG(tooltip)
        self.check3DPreview.setToolTip(QCoreApplication.translate("Form", u"Opens a 3D preview of the selected file.", None))
#endif // QT_CONFIG(tooltip)
        self.check3DPreview.setText(QCoreApplication.translate("Form", u"Preview model in 3D view", None))
#if QT_CONFIG(tooltip)
        self.checkFCStdOnly.setToolTip(QCoreApplication.translate("Form", u"Show available alternative file formats for library items (STEP, IFC, etc...)", None))
#endif // QT_CONFIG(tooltip)
        self.checkFCStdOnly.setText(QCoreApplication.translate("Form", u"Display alternative formats", None))
        self.label.setText(QCoreApplication.translate("Form", u"Note: STEP and BREP files can be placed at custom location. FCStd and IFC files will be placed where objects are defined in the file.", None))
        self.checkThumbnail.setText(QCoreApplication.translate("Form", u"Save thumbnails", None))
        self.buttonSave.setText(QCoreApplication.translate("Form", u"Save as...", None))
    # retranslateUi

