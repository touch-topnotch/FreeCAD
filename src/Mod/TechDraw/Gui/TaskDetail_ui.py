# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TaskDetail.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import TechDraw_rc

class Ui_TechDrawGui_TaskDetail(object):
    def setupUi(self, TechDrawGui__TaskDetail):
        if not TechDrawGui__TaskDetail.objectName():
            TechDrawGui__TaskDetail.setObjectName(u"TechDrawGui__TaskDetail")
        TechDrawGui__TaskDetail.resize(497, 367)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TechDrawGui__TaskDetail.sizePolicy().hasHeightForWidth())
        TechDrawGui__TaskDetail.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/actions/TechDraw_DetailView.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TechDrawGui__TaskDetail.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(TechDrawGui__TaskDetail)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(TechDrawGui__TaskDetail)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.leBaseView = QLineEdit(TechDrawGui__TaskDetail)
        self.leBaseView.setObjectName(u"leBaseView")
        self.leBaseView.setEnabled(False)
        self.leBaseView.setMouseTracking(False)
        self.leBaseView.setFocusPolicy(Qt.NoFocus)
        self.leBaseView.setAcceptDrops(False)

        self.gridLayout.addWidget(self.leBaseView, 0, 1, 1, 1)

        self.label = QLabel(TechDrawGui__TaskDetail)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.leDetailView = QLineEdit(TechDrawGui__TaskDetail)
        self.leDetailView.setObjectName(u"leDetailView")
        self.leDetailView.setEnabled(False)

        self.gridLayout.addWidget(self.leDetailView, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pbDragger = QPushButton(TechDrawGui__TaskDetail)
        self.pbDragger.setObjectName(u"pbDragger")

        self.horizontalLayout.addWidget(self.pbDragger)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(TechDrawGui__TaskDetail)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(TechDrawGui__TaskDetail)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.leReference = QLineEdit(TechDrawGui__TaskDetail)
        self.leReference.setObjectName(u"leReference")
        self.leReference.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.leReference, 5, 2, 1, 1)

        self.qsbScale = Gui_QuantitySpinBox(TechDrawGui__TaskDetail)
        self.qsbScale.setObjectName(u"qsbScale")
        self.qsbScale.setEnabled(False)
        self.qsbScale.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbScale.setKeyboardTracking(False)
        self.qsbScale.setProperty(u"unit", u"")
        self.qsbScale.setSingleStep(1.000000000000000)
        self.qsbScale.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.qsbScale, 4, 2, 1, 1)

        self.qsbY = Gui_QuantitySpinBox(TechDrawGui__TaskDetail)
        self.qsbY.setObjectName(u"qsbY")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.qsbY.sizePolicy().hasHeightForWidth())
        self.qsbY.setSizePolicy(sizePolicy1)
        self.qsbY.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbY.setKeyboardTracking(False)
        self.qsbY.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.qsbY, 1, 2, 1, 1)

        self.label_8 = QLabel(TechDrawGui__TaskDetail)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.qsbRadius = Gui_QuantitySpinBox(TechDrawGui__TaskDetail)
        self.qsbRadius.setObjectName(u"qsbRadius")
        sizePolicy1.setHeightForWidth(self.qsbRadius.sizePolicy().hasHeightForWidth())
        self.qsbRadius.setSizePolicy(sizePolicy1)
        self.qsbRadius.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbRadius.setKeyboardTracking(False)
        self.qsbRadius.setProperty(u"unit", u"")
        self.qsbRadius.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.qsbRadius, 2, 2, 1, 1)

        self.label_7 = QLabel(TechDrawGui__TaskDetail)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)

        self.qsbX = Gui_QuantitySpinBox(TechDrawGui__TaskDetail)
        self.qsbX.setObjectName(u"qsbX")
        sizePolicy1.setHeightForWidth(self.qsbX.sizePolicy().hasHeightForWidth())
        self.qsbX.setSizePolicy(sizePolicy1)
        self.qsbX.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.qsbX.setProperty(u"unit", u"")

        self.gridLayout_2.addWidget(self.qsbX, 0, 2, 1, 1)

        self.label_6 = QLabel(TechDrawGui__TaskDetail)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_2 = QLabel(TechDrawGui__TaskDetail)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"X")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.cbScaleType = QComboBox(TechDrawGui__TaskDetail)
        self.cbScaleType.addItem("")
        self.cbScaleType.addItem("")
        self.cbScaleType.addItem("")
        self.cbScaleType.setObjectName(u"cbScaleType")

        self.gridLayout_2.addWidget(self.cbScaleType, 3, 2, 1, 1)

        self.label_3 = QLabel(TechDrawGui__TaskDetail)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Y")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 2)

        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(TechDrawGui__TaskDetail)

        QMetaObject.connectSlotsByName(TechDrawGui__TaskDetail)
    # setupUi

    def retranslateUi(self, TechDrawGui__TaskDetail):
        TechDrawGui__TaskDetail.setWindowTitle(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Detail Anchor", None))
        self.label_4.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Base View", None))
        self.label.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Detail view", None))
#if QT_CONFIG(tooltip)
        self.pbDragger.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Enables dragging of the detail highlight to a new position", None))
#endif // QT_CONFIG(tooltip)
        self.pbDragger.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Drag Highlight", None))
        self.label_9.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Scale type", None))
#if QT_CONFIG(tooltip)
        self.leReference.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Reference label", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.qsbScale.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Scale factor for detail view", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.qsbY.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Y-position of detail highlight within view", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Scale factor", None))
#if QT_CONFIG(tooltip)
        self.qsbRadius.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Size of detail view", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Reference", None))
#if QT_CONFIG(tooltip)
        self.qsbX.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"X position of detail highlight within view", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Radius", None))
        self.cbScaleType.setItemText(0, QCoreApplication.translate("TechDrawGui::TaskDetail", u"Page", None))
        self.cbScaleType.setItemText(1, QCoreApplication.translate("TechDrawGui::TaskDetail", u"Automatic", None))
        self.cbScaleType.setItemText(2, QCoreApplication.translate("TechDrawGui::TaskDetail", u"Custom", None))

#if QT_CONFIG(tooltip)
        self.cbScaleType.setToolTip(QCoreApplication.translate("TechDrawGui::TaskDetail", u"Page: scale factor of page is used\n"
"Automatic: if the detail view is larger than the page,\n"
"                   it will be scaled down to fit into the page\n"
"Custom: custom scale factor is used", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

