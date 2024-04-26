import sys

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings


class AppWindowLogic(QMainWindow, Ui_MenuWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)
        self.champions_data = None

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/app_style.json"})

        QAppSettings.updateAppSettings(self)

        self.ui.notificationSlide.collapseMenu()
        self.show()
        self.ui.checkBox1.stateChanged.connect(lambda: self.darkMode())

    def darkMode(self):
        settings = QSettings()

        print("Current theme", settings.value("THEME"))
        print("Current Icons color", settings.value("ICONS-COLOR"))

        if settings.value("THEME") == "Dark-Blue":

            settings.setValue("THEME", "Light-Blue")

        else:
            settings.setValue("THEME", "Dark-Blue")

        CompileStyleSheet.applyCompiledSass(self)
