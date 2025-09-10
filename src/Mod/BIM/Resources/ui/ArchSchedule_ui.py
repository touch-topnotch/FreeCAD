# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ArchSchedule.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(725, 529)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEditName = Gui_PrefLineEdit(Dialog)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout_3.addWidget(self.lineEditName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.list = QTableWidget(Dialog)
        if (self.list.columnCount() < 5):
            self.list.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.list.setObjectName(u"list")
        self.list.setCornerButtonEnabled(True)
        self.list.setRowCount(0)
        self.list.setColumnCount(5)
        self.list.horizontalHeader().setDefaultSectionSize(120)
        self.list.horizontalHeader().setStretchLastSection(True)
        self.list.verticalHeader().setVisible(True)
        self.list.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.list)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkSpreadsheet = Gui_PrefCheckBox(Dialog)
        self.checkSpreadsheet.setObjectName(u"checkSpreadsheet")

        self.horizontalLayout_4.addWidget(self.checkSpreadsheet)

        self.checkDetailed = Gui_PrefCheckBox(Dialog)
        self.checkDetailed.setObjectName(u"checkDetailed")

        self.horizontalLayout_4.addWidget(self.checkDetailed)

        self.checkAutoUpdate = Gui_PrefCheckBox(Dialog)
        self.checkAutoUpdate.setObjectName(u"checkAutoUpdate")

        self.horizontalLayout_4.addWidget(self.checkAutoUpdate)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonAdd = QPushButton(Dialog)
        self.buttonAdd.setObjectName(u"buttonAdd")
        icon = QIcon()
        iconThemeName = u"add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonAdd.setIcon(icon)

        self.gridLayout.addWidget(self.buttonAdd, 0, 0, 1, 1)

        self.buttonDel = QPushButton(Dialog)
        self.buttonDel.setObjectName(u"buttonDel")
        icon1 = QIcon()
        iconThemeName = u"remove"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonDel.setIcon(icon1)

        self.gridLayout.addWidget(self.buttonDel, 0, 1, 1, 1)

        self.buttonClear = QPushButton(Dialog)
        self.buttonClear.setObjectName(u"buttonClear")
        icon2 = QIcon()
        iconThemeName = u"cancel"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonClear.setIcon(icon2)

        self.gridLayout.addWidget(self.buttonClear, 0, 2, 1, 1)

        self.buttonSelect = QPushButton(Dialog)
        self.buttonSelect.setObjectName(u"buttonSelect")

        self.gridLayout.addWidget(self.buttonSelect, 1, 0, 1, 1)

        self.buttonImport = QPushButton(Dialog)
        self.buttonImport.setObjectName(u"buttonImport")
        icon3 = QIcon()
        iconThemeName = u"document-import"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonImport.setIcon(icon3)

        self.gridLayout.addWidget(self.buttonImport, 1, 1, 1, 1)

        self.buttonExport = QPushButton(Dialog)
        self.buttonExport.setObjectName(u"buttonExport")
        icon4 = QIcon()
        iconThemeName = u"document-export"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.buttonExport.setIcon(icon4)

        self.gridLayout.addWidget(self.buttonExport, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Schedule definition", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Schedule name:", None))
        self.lineEditName.setText(QCoreApplication.translate("Dialog", u"Unnamed schedule", None))
        ___qtablewidgetitem = self.list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Description", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("Dialog", u"A description for this operation", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Property", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("Dialog", u"The property to retrieve from each object.Can be 'Count'\n"
"to count the objects, or property names like 'Length' or\n"
"'Shape.Volume' to retrieve a certain property.\n"
"\n"
"When used with native IFC objects, this can be used to\n"
"retrieve any attribute or custom properties of the elements\n"
"retrieved.", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Unit", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("Dialog", u"An optional unit to express the resulting value. Ex: m^3 (you can also write m\u00b3 or m3)", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Objects", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("Dialog", u"An optional semicolon (;) separated list of object names\n"
"(internal names, not labels), to be considered by this operation.\n"
"If the list contains groups, children will be added.\n"
"\n"
"Leave blank to use all objects from the document.\n"
"\n"
"If the document is an IFC project, all IFC entities of the\n"
"document will be used, no matter if they are expanded\n"
"in FreeCAD or not.\n"
"\n"
"Use the name of the IFC project to get all the IFC entities\n"
"of that project, no matter if they are expanded or not.", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Filter", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("Dialog", u"An optional semicolon (;) separated list of property:value filters. Prepend ! to a property name to invert the effect of the filter (exclude objects that match the filter). Objects whose property contains the value will be matched.\n"
"\n"
"Examples of valid filters (everything is case-insensitive): Name:Wall - Will only consider objects with 'wall' in their name (internal name); !Name:Wall - Will only consider objects which DON'T have 'wall' in their name (internal name); Description:Win - Will only consider objects with 'win' in their description; !Label:Win - Will only consider objects which DO NOT have 'win' in their label; IfcType:Wall - Will only consider objects which Ifc Type is 'Wall'; !Tag:Wall - Will only consider objects which tag is NOT 'Wall'. If you leave this field empty, no filtering is applied\n"
"\n"
"When dealing with native IFC objects, you can use FreeCAD properties name, ex: 'Class:IfcWall' or any other IFC attribute (ex. 'IsTypedBy:#455'). If the 'Objects' column has been set to an IFC "
                        "project or document, all the IFC entities of that project will be considered.", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.checkSpreadsheet.setToolTip(QCoreApplication.translate("Dialog", u"If this is enabled, an associated spreadsheet containing the results will be maintained together with this schedule object", None))
#endif // QT_CONFIG(tooltip)
        self.checkSpreadsheet.setText(QCoreApplication.translate("Dialog", u"Associate spreadsheet", None))
#if QT_CONFIG(tooltip)
        self.checkDetailed.setToolTip(QCoreApplication.translate("Dialog", u"If this is enabled, additional lines will be filled with each object considered. If not, only the totals.", None))
#endif // QT_CONFIG(tooltip)
        self.checkDetailed.setText(QCoreApplication.translate("Dialog", u"Detailed results", None))
#if QT_CONFIG(tooltip)
        self.checkAutoUpdate.setToolTip(QCoreApplication.translate("Dialog", u"If this is enabled, the schedule and the associated spreadsheet are updated whenever the document is recomputed.", None))
#endif // QT_CONFIG(tooltip)
        self.checkAutoUpdate.setText(QCoreApplication.translate("Dialog", u"Auto update", None))
#if QT_CONFIG(tooltip)
        self.buttonAdd.setToolTip(QCoreApplication.translate("Dialog", u"Adds a line below the selected line/cell", None))
#endif // QT_CONFIG(tooltip)
        self.buttonAdd.setText(QCoreApplication.translate("Dialog", u"Add row", None))
#if QT_CONFIG(tooltip)
        self.buttonDel.setToolTip(QCoreApplication.translate("Dialog", u"Deletes the selected line", None))
#endif // QT_CONFIG(tooltip)
        self.buttonDel.setText(QCoreApplication.translate("Dialog", u"Del row", None))
#if QT_CONFIG(tooltip)
        self.buttonClear.setToolTip(QCoreApplication.translate("Dialog", u"Clears the whole list", None))
#endif // QT_CONFIG(tooltip)
        self.buttonClear.setText(QCoreApplication.translate("Dialog", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.buttonSelect.setToolTip(QCoreApplication.translate("Dialog", u"Put selected objects into the 'Objects' column of the selected row", None))
#endif // QT_CONFIG(tooltip)
        self.buttonSelect.setText(QCoreApplication.translate("Dialog", u"Add selection", None))
#if QT_CONFIG(tooltip)
        self.buttonImport.setToolTip(QCoreApplication.translate("Dialog", u"Imports the contents of a CSV file", None))
#endif // QT_CONFIG(tooltip)
        self.buttonImport.setText(QCoreApplication.translate("Dialog", u"Import", None))
#if QT_CONFIG(tooltip)
        self.buttonExport.setToolTip(QCoreApplication.translate("Dialog", u"This exports the results to a CSV or Markdown file. Note for CSV export: In Libreoffice, you can keep this CSV file linked by right-clicking the Sheets tab bar, New sheet, From file, Link (Note: as of LibreOffice v6.x the correct path now is: Sheet, Insert Sheet..., From file, Browse...)", None))
#endif // QT_CONFIG(tooltip)
        self.buttonExport.setText(QCoreApplication.translate("Dialog", u"Export", None))
    # retranslateUi

