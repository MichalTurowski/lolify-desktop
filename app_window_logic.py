import sys
import requests
import keyring
import os

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")


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
        self.ui.checkBox_app.stateChanged.connect(lambda: self.darkMode())
        self.ui.notificationShow.clicked.connect(
            lambda: self.showNotification("Notification show button clicked!")
        )
        self.ui.logoutBtn.clicked.connect(lambda: self.logout())

    def showNotification(self, msg):
        self.ui.label_8.setText(msg)
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

    def logout(self):
        access_token = keyring.get_password("lolify", "token")
        if access_token:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.post(f"{API_URL}/logout", headers=headers)
            if response.status_code == 200:
                keyring.delete_password("lolify", "token")
                print("Successfully logged out and token deleted.")
                self.close()
            else:
                print("Failed to log out.")
        else:
            print("No token found. You are not logged in.")
