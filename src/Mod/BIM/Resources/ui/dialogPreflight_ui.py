# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogPreflight.ui'
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
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(308, 1308)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_7)

        self.testAll = QPushButton(Form)
        self.testAll.setObjectName(u"testAll")

        self.verticalLayout.addWidget(self.testAll)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.getSelection = QRadioButton(self.groupBox)
        self.getSelection.setObjectName(u"getSelection")

        self.verticalLayout_2.addWidget(self.getSelection)

        self.getVisible = QRadioButton(self.groupBox)
        self.getVisible.setObjectName(u"getVisible")
        self.getVisible.setChecked(True)

        self.verticalLayout_2.addWidget(self.getVisible)

        self.getAll = QRadioButton(self.groupBox)
        self.getAll.setObjectName(u"getAll")

        self.verticalLayout_2.addWidget(self.getAll)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_6 = QGroupBox(Form)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_5 = QGridLayout(self.groupBox_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelIFC4 = QLabel(self.groupBox_6)
        self.labelIFC4.setObjectName(u"labelIFC4")
        self.labelIFC4.setWordWrap(True)

        self.gridLayout_5.addWidget(self.labelIFC4, 0, 0, 1, 1)

        self.testIFC4 = QPushButton(self.groupBox_6)
        self.testIFC4.setObjectName(u"testIFC4")

        self.gridLayout_5.addWidget(self.testIFC4, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.testStoreys = QPushButton(self.groupBox_2)
        self.testStoreys.setObjectName(u"testStoreys")

        self.gridLayout.addWidget(self.testStoreys, 3, 1, 1, 1)

        self.labelBuildings = QLabel(self.groupBox_2)
        self.labelBuildings.setObjectName(u"labelBuildings")
        self.labelBuildings.setWordWrap(True)

        self.gridLayout.addWidget(self.labelBuildings, 2, 0, 1, 1)

        self.labelStoreys = QLabel(self.groupBox_2)
        self.labelStoreys.setObjectName(u"labelStoreys")
        self.labelStoreys.setWordWrap(True)

        self.gridLayout.addWidget(self.labelStoreys, 3, 0, 1, 1)

        self.testBuildings = QPushButton(self.groupBox_2)
        self.testBuildings.setObjectName(u"testBuildings")

        self.gridLayout.addWidget(self.testBuildings, 2, 1, 1, 1)

        self.labelSites = QLabel(self.groupBox_2)
        self.labelSites.setObjectName(u"labelSites")
        self.labelSites.setWordWrap(True)

        self.gridLayout.addWidget(self.labelSites, 1, 0, 1, 1)

        self.testSites = QPushButton(self.groupBox_2)
        self.testSites.setObjectName(u"testSites")

        self.gridLayout.addWidget(self.testSites, 1, 1, 1, 1)

        self.labelHierarchy = QLabel(self.groupBox_2)
        self.labelHierarchy.setObjectName(u"labelHierarchy")
        self.labelHierarchy.setWordWrap(True)

        self.gridLayout.addWidget(self.labelHierarchy, 0, 0, 1, 1)

        self.testHierarchy = QPushButton(self.groupBox_2)
        self.testHierarchy.setObjectName(u"testHierarchy")

        self.gridLayout.addWidget(self.testHierarchy, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.testSolid = QPushButton(self.groupBox_3)
        self.testSolid.setObjectName(u"testSolid")

        self.gridLayout_2.addWidget(self.testSolid, 1, 1, 1, 1)

        self.labelSolid = QLabel(self.groupBox_3)
        self.labelSolid.setObjectName(u"labelSolid")
        self.labelSolid.setWordWrap(True)

        self.gridLayout_2.addWidget(self.labelSolid, 1, 0, 1, 1)

        self.labelUndefined = QLabel(self.groupBox_3)
        self.labelUndefined.setObjectName(u"labelUndefined")
        self.labelUndefined.setWordWrap(True)

        self.gridLayout_2.addWidget(self.labelUndefined, 0, 0, 1, 1)

        self.testUndefined = QPushButton(self.groupBox_3)
        self.testUndefined.setObjectName(u"testUndefined")

        self.gridLayout_2.addWidget(self.testUndefined, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelStandards = QLabel(self.groupBox_4)
        self.labelStandards.setObjectName(u"labelStandards")
        self.labelStandards.setWordWrap(True)

        self.gridLayout_3.addWidget(self.labelStandards, 5, 0, 1, 1)

        self.testQuantities = QPushButton(self.groupBox_4)
        self.testQuantities.setObjectName(u"testQuantities")

        self.gridLayout_3.addWidget(self.testQuantities, 0, 1, 1, 1)

        self.testCommonPsets = QPushButton(self.groupBox_4)
        self.testCommonPsets.setObjectName(u"testCommonPsets")

        self.gridLayout_3.addWidget(self.testCommonPsets, 1, 1, 1, 1)

        self.labelCommonPsets = QLabel(self.groupBox_4)
        self.labelCommonPsets.setObjectName(u"labelCommonPsets")
        self.labelCommonPsets.setWordWrap(True)

        self.gridLayout_3.addWidget(self.labelCommonPsets, 1, 0, 1, 1)

        self.labelQuantities = QLabel(self.groupBox_4)
        self.labelQuantities.setObjectName(u"labelQuantities")
        self.labelQuantities.setWordWrap(True)

        self.gridLayout_3.addWidget(self.labelQuantities, 0, 0, 1, 1)

        self.labelMaterials = QLabel(self.groupBox_4)
        self.labelMaterials.setObjectName(u"labelMaterials")
        self.labelMaterials.setWordWrap(True)

        self.gridLayout_3.addWidget(self.labelMaterials, 3, 0, 1, 1)

        self.testMaterials = QPushButton(self.groupBox_4)
        self.testMaterials.setObjectName(u"testMaterials")

        self.gridLayout_3.addWidget(self.testMaterials, 3, 1, 1, 1)

        self.labelPsets = QLabel(self.groupBox_4)
        self.labelPsets.setObjectName(u"labelPsets")
        self.labelPsets.setWordWrap(True)

        self.gridLayout_3.addWidget(self.labelPsets, 2, 0, 1, 1)

        self.testPsets = QPushButton(self.groupBox_4)
        self.testPsets.setObjectName(u"testPsets")

        self.gridLayout_3.addWidget(self.testPsets, 2, 1, 1, 1)

        self.testStandards = QPushButton(self.groupBox_4)
        self.testStandards.setObjectName(u"testStandards")

        self.gridLayout_3.addWidget(self.testStandards, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.testExtrusions = QPushButton(self.groupBox_5)
        self.testExtrusions.setObjectName(u"testExtrusions")

        self.gridLayout_4.addWidget(self.testExtrusions, 0, 1, 1, 1)

        self.labelExtrusions = QLabel(self.groupBox_5)
        self.labelExtrusions.setObjectName(u"labelExtrusions")
        self.labelExtrusions.setWordWrap(True)

        self.gridLayout_4.addWidget(self.labelExtrusions, 0, 0, 1, 1)

        self.labelStandardCases = QLabel(self.groupBox_5)
        self.labelStandardCases.setObjectName(u"labelStandardCases")
        self.labelStandardCases.setWordWrap(True)

        self.gridLayout_4.addWidget(self.labelStandardCases, 1, 0, 1, 1)

        self.testStandardCases = QPushButton(self.groupBox_5)
        self.testStandardCases.setObjectName(u"testStandardCases")

        self.gridLayout_4.addWidget(self.testStandardCases, 1, 1, 1, 1)

        self.labelTinyLines = QLabel(self.groupBox_5)
        self.labelTinyLines.setObjectName(u"labelTinyLines")
        self.labelTinyLines.setWordWrap(True)

        self.gridLayout_4.addWidget(self.labelTinyLines, 2, 0, 1, 1)

        self.testTinyLines = QPushButton(self.groupBox_5)
        self.testTinyLines.setObjectName(u"testTinyLines")

        self.gridLayout_4.addWidget(self.testTinyLines, 2, 1, 1, 1)

        self.labelRectangleProfileDef = QLabel(self.groupBox_5)
        self.labelRectangleProfileDef.setObjectName(u"labelRectangleProfileDef")
        self.labelRectangleProfileDef.setWordWrap(True)

        self.gridLayout_4.addWidget(self.labelRectangleProfileDef, 3, 0, 1, 1)

        self.testRectangleProfileDef = QPushButton(self.groupBox_5)
        self.testRectangleProfileDef.setObjectName(u"testRectangleProfileDef")

        self.gridLayout_4.addWidget(self.testRectangleProfileDef, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"IFC Preflight", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>The following test will check the model or the selected object(s) and their children for conformity to IFC standards.</p><p><span style=\" font-weight:600;\">Important</span>: None of the failed tests below will prevent exporting IFC files, nor do these tests guarantee that the IFC files meets some specific quality or standard requirement. They are there to assess which elements are included or excluded from the exported file. Choose which item is of importance manually. Hovering the mouse over each description will show more information.</p><p>After a test is run, clicking the corresponding button will show more information to help fix the problems.</p><p>The <a href=\"http://www.buildingsmart-tech.org/specifications\"><span style=\" text-decoration: underline; color:#0000ff;\">official IFC website</span></a> contains a lot of useful information about IFC standards.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.testAll.setToolTip(QCoreApplication.translate("Form", u"Warning, this may take a large amount of time!", None))
#endif // QT_CONFIG(tooltip)
        self.testAll.setText(QCoreApplication.translate("Form", u"Run All Tests", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Work on", None))
        self.getSelection.setText(QCoreApplication.translate("Form", u"Selection", None))
        self.getVisible.setText(QCoreApplication.translate("Form", u"All visible objects", None))
        self.getAll.setText(QCoreApplication.translate("Form", u"Whole document", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"IFC Export", None))
#if QT_CONFIG(tooltip)
        self.labelIFC4.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>IFC export in FreeCAD is performed by an open-source third-party library called IfcOpenShell. To be able to export to the newer IFC4 standard, IfcOpenShell must have been compiled with IFC4 support enabled. This test will check if IFC4 support is available in the installed version of IfcOpenShell. If not, FreeCAD will only export IFC files in the older IFC2x3 standard. Note that some applications out there still have incomplete or inexistent IFC4 support, so in some cases IFC2x3 might still work better.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelIFC4.setText(QCoreApplication.translate("Form", u"Is IFC4 support enabled?", None))
        self.testIFC4.setText(QCoreApplication.translate("Form", u"Test", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Project Structure", None))
        self.testStoreys.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelBuildings.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>All IfcBuildingStorey (levels) elements are required to be inside an IfcBuilding element. This is a mandatory requirement of the IFC standard. When exporting the FreeCAD model to IFC, a default IfcBuilding will be created for all level objects (BuildingPart objects with their IFC role set as Building Storey) found that are not inside a Building. However, it is best to manually create that building, to have more control over its name and properties. This test is here to help find those levels without buildings.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelBuildings.setText(QCoreApplication.translate("Form", u"Are all storeys part of a building?", None))
#if QT_CONFIG(tooltip)
        self.labelStoreys.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>All elements derived from IfcProduct (that is, all the BIM elements that compose the model) are required to be inside an IfcBuildingStorey (level) element. This is a mandatory requirement of the IFC standard. When exporting the FreeCAD model to IFC, a default IfcBuildingStorey will be created for all BIM objects found that are not inside one already. However, it is best to check that all elements are correctly located inside a level to have more control over it. This test is here to help find those BIM objects without a level.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelStoreys.setText(QCoreApplication.translate("Form", u"Are all BIM objects part of a level?", None))
        self.testBuildings.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelSites.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>All IfcBuilding elements are required to be inside an IfcSite element. This is a mandatory requirement of the IFC standard. When exporting the FreeCAD model to IFC, a default IfcSite will be created for all Building objects found that are not inside a Site. However, it is best to manually create that site to have more control over its name and properties. This test is here to help find those buildings without sites.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSites.setText(QCoreApplication.translate("Form", u"Are all buildings part of a site?", None))
        self.testSites.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelHierarchy.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The IFC standard requires at least one site, one building and one level or building storey per project. This test will ensure that at least one object of each of these 3 types exists in the model.</p><p>Note that, as this is a mandatory requirement, FreeCAD will automatically add a default site, a default building and/or a default building storey if any of these is missing. So even if this test did not pass, the exported IFC file will meet the requirements.</p><p>However, it is always better to manually create these projects to gain more control over naming and properties.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelHierarchy.setText(QCoreApplication.translate("Form", u"Is there at least one site, one building and one level in the model?", None))
        self.testHierarchy.setText(QCoreApplication.translate("Form", u"Test", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Geometry", None))
        self.testSolid.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelSolid.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Although it is not a requirement for IFC objects to have fully clean and solid geometry, it is better if they do. This will reduce chances of problems with other applications. In real life, all objects have solid shapes.</p><p>FreeCAD has a lot of tools to check for geometry quality, and most parametric objects, including BIM objects, will usually warn the user if their geometry becomes unclean or not solid at some point. This test makes validates the solidity of the geometry.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelSolid.setText(QCoreApplication.translate("Form", u"Are all BIM objects solid and valid?", None))
#if QT_CONFIG(tooltip)
        self.labelUndefined.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The IFC format provides a defined type for most of the objects that compose a building, for example walls, columns, doors, or sinks. But it also supports undefined objects, which are given the generic BuildingElementProxy type. This test will check that all objects have a defined type.</p><p><br/></p><p>Note that failing this test is not necessarily bad, as it may be desirable for some object to not have any defined type. In some cases, this might even give better results, as some applications like Revit might add unwanted additional constraints or transformations to some known types such as structural elements (beams or columns). Exporting them as BuildingElementProxies will prevent that.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelUndefined.setText(QCoreApplication.translate("Form", u"Are all BIM objects of a defined IFC type?", None))
        self.testUndefined.setText(QCoreApplication.translate("Form", u"Test", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Properties", None))
#if QT_CONFIG(tooltip)
        self.labelStandards.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Classification systems, such as UniClass or MasterFormat, or even a custom system, are in some cases an important part of a building project. This test will ensure that all BIM objects and materials found in the model have their standard code property dutifully filled.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelStandards.setText(QCoreApplication.translate("Form", u"Do all BIM objects and materials have a standard classification code defined?", None))
        self.testQuantities.setText(QCoreApplication.translate("Form", u"Test", None))
        self.testCommonPsets.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelCommonPsets.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The IFC standard offers standard, predefined property sets for many object types. For example, the property set Pset_WallCommon contains properties that the IFC standard thinks all walls should have. This test will check that all BIM objects have the right property set, if available.</p><p>Note that this is by no means a formal requirement, and these will inflate the size of the IFC file consequently. It is recommended to add standard property sets only if they are in use.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelCommonPsets.setText(QCoreApplication.translate("Form", u"Do all common IFC types have the corresponding Property Set?", None))
#if QT_CONFIG(tooltip)
        self.labelQuantities.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>IFC objects have a geometry representation, which defines the shape of the object, but can also have some or their dimensions, such as height, width or area, explicitly stated. This is very useful for BIM applications that do not process the geometry, such as spreadsheets. Those applications are still able to get and estimate quantities from IFC objects without the need to analyze the geometry.</p><p>It is also a possibility for errors (or even fraud), as nothing guarantees that those explicitly stated dimensions match what is inside the geometry.</p><p>This test will find any BIM object that has available dimension properties such as width or height, for example walls and structures, but such properties are not marked for explicit export to IFC.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelQuantities.setText(QCoreApplication.translate("Form", u"Do all geometric BIM objects have explicit dimensions set?", None))
#if QT_CONFIG(tooltip)
        self.labelMaterials.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Although there is no requirement for IFC objects to have a material defined, in the real world, it is an important layer of information to be added to the model. This test will find BIM objects without a material defined.</p><p>If a BIM object is exported without a material, it will nevertheless be assigned an IfcSurfaceStyle, which will be created from the object color. Some BIM applications disregard materials, and only consider the surface style of an object. No IfcMaterial will be attributed to that object.</p><p>If a BIM object has a material defined, a surface style will still be created (an IfcMaterial too), but its surface style will take the same name and properties as the material, thus giving more consistency to the file.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelMaterials.setText(QCoreApplication.translate("Form", u"Do all BIM objects have a material?", None))
        self.testMaterials.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelPsets.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Even if a BIM object has a standard property set for its type attributed, there is no guarantee that this property set still contains or only contains all the properties that the IFC standard has defined for that set. They might have been modified after the property set has been added.</p><p>This test will check that all standard property sets found throughout the model contain all and only the properties specified in the standard definition.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelPsets.setText(QCoreApplication.translate("Form", u"Do all standard Property Set contain the correct properties?", None))
        self.testPsets.setText(QCoreApplication.translate("Form", u"Test", None))
        self.testStandards.setText(QCoreApplication.translate("Form", u"Test", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Optional/Compatibility", None))
        self.testExtrusions.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelExtrusions.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The geometry of IFC objects can be defined in a large number of ways, such as extrusions, subtractions, revolutions, or even faceted objects.</p><p>However, extrusions of flat shapes, which is the most basic and common type, often offer advantages over other types in other BIM applications.</p><p>This test will find any object that cannot be exported to IFC as an extrusion, or as a shared extrusion (clone).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelExtrusions.setText(QCoreApplication.translate("Form", u"Are all object exportable as extrusions?", None))
#if QT_CONFIG(tooltip)
        self.labelStandardCases.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Walls, columns and beams in FreeCAD can be constructed in a wide number of ways, but some simpler BIM applications might have difficulties with walls that are not of the most simple type. That is, a single, straight piece of wall (which correspond to the IfcWallStandardCase type) or beams and columns that are not based on a straight extrusion of a flat profile (BeamStandardCase, ColumnStandardCase)</p><p>This test will find any wall which is not such a standard case.</p><p><span style=\" font-weight:600;\">Note</span>: At the moment, BIM objects that meet the requirements to be of a standard case, are still exported as IfcWall, IfcBeam, IfcColumn.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelStandardCases.setText(QCoreApplication.translate("Form", u"Are all walls, beams and columns based on a single line or profile (standard case)?", None))
        self.testStandardCases.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelTinyLines.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Revit discards all objects that contain lines smaller than 1/32 inch (0.8mm). This test will find any object containing lines smaller than that value.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelTinyLines.setText(QCoreApplication.translate("Form", u"Are all lines bigger than 1/32 inches (minimum accepted by Revit)?", None))
        self.testTinyLines.setText(QCoreApplication.translate("Form", u"Test", None))
#if QT_CONFIG(tooltip)
        self.labelRectangleProfileDef.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>When exporting a model to IFC, all BIM objects that are an extrusion of a rectangular profile will use an IfcRectangleProfileDef entity as their extrusion profile. However, Revit will not import these correctly. If using the IFC file in Revit, it is recommended to disable this behavior by checking the option under menu <span style=\" font-weight:600;\">Edit -&gt; Preferences -&gt; BIM -&gt; Native IFC -&gt; Disable IfcRectangularProfileDef</span>.</p><p>When that option is checked, all extrusion profiles will be exported as generic IfcArbitraryProfileDef entities, regardless of if they are rectangular or not, which will contain a little less information, but will open correctly in Revit.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelRectangleProfileDef.setText(QCoreApplication.translate("Form", u"Is IfcRectangleProfileDef export disabled? (Revit only)", None))
        self.testRectangleProfileDef.setText(QCoreApplication.translate("Form", u"Test", None))
    # retranslateUi

