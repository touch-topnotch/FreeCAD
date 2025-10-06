import sys

# sys.path.append("")

from PySide import QtWidgets, QtGui
import FreeCADGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        from PySide import QtWidgets, QtNetwork

        QtNetwork.QNetworkConfigurationManager()

    def showEvent(self, event):
        FreeCADGui.showMainWindow()
        self.setCentralWidget(FreeCADGui.getMainWindow())

        # Need version >= 0.16.5949
        class BlankWorkbench(FreeCADGui.Workbench):
            MenuText = "Blank"
            ToolTip = "Blank workbench"

            def Initialize(self):
                self.appendMenu("Menu", ["Std_New", "Part_Box"])
                return

            def GetClassName(self):
                return "Gui::PythonBlankWorkbench"

        FreeCADGui.addWorkbench(BlankWorkbench)
        FreeCADGui.activateWorkbench("BlankWorkbench")


app = QtWidgets.QApplication(sys.argv)
mw = MainWindow()
mw.resize(1200, 800)
mw.show()
app.exec_()
