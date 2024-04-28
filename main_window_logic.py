import sys
import requests
import keyring

from dotenv import load_dotenv

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from app_window_logic import AppWindowLogic
from User import User

load_dotenv()
API_URL = "https://lolify.fly.dev/api"


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
            # lambda: self.showNotification("Sign up button clicked!")
            lambda: self.register()
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
        email = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not email or not password:
            self.showNotification("Please enter email and password")
            return
        user = User(email, password)

        payload = {
            "email": user.email,
            "password": user.password,
        }

        response = requests.post(f"{API_URL}/login", json=payload)

        if response.status_code == 200:
            token = response.json()["access_token"]
            keyring.set_password("lolify", "token", token)
            print("Logged in successfully.")
            self.close()
            app_logic = AppWindowLogic()
        elif response.status_code == 401:
            self.showNotification("These credentials don't match our records.")
        else:
            print("Failed to login. Status code:", response.status_code)
            self.showNotification("Something went wrong.")

    def register(self):
        email = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        confirm_password = self.ui.lineEdit_5.text()
        if not email or not password:
            self.showNotification("Please enter email and password")
            return
        if password != confirm_password:
            self.showNotification("Passwords do not match.")
            return

        user = User(email, password)

        payload = {
            "email": user.email,
            "password": user.password,
            "password_confirmation": user.password,
        }

        response = requests.post(f"{API_URL}/register", json=payload)

        if response.status_code == 200:
            token = response.json()["access_token"]
            keyring.set_password("lolify", "token", token)
            print("Registered and logged in successfully.")
            self.close()
            app_logic = AppWindowLogic()
        else:
            print("Failed to register. Status code:", response.status_code)
            self.showNotification("Something went wrong.")
