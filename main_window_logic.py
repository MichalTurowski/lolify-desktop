import sys

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from app_window_logic import AppWindowLogic


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/login_style.json"})

        QAppSettings.updateAppSettings(self)

        self.ui.notificationSlide.collapseMenu()
        self.show()

        self.ui.signInBtn.clicked.connect(
            # lambda: self.showNotification("Sign in button clicked!")
            lambda: self.login()
        )
        self.ui.signUpBtn.clicked.connect(
            lambda: self.showNotification("Sign up button clicked!")
        )

        self.ui.checkBox.stateChanged.connect(lambda: self.darkMode())

    def showNotification(self, msg):
        self.ui.notificationTxt.setText(msg)
        self.ui.notificationSlide.expandMenu()

    def darkMode(self):
        settings = QSettings()
        print("Current theme", settings.value("THEME"))
        print("Current Icons color", settings.value("ICONS-COLOR"))

        if settings.value("THEME") == "Dark-Blue":
            settings.setValue("THEME", "Light-Blue")

        else:
            settings.setValue("THEME", "Dark-Blue")

        CompileStyleSheet.applyCompiledSass(self)

    def login(self):
        self.hide()
        app_logic = AppWindowLogic()
