import sys
import requests
import keyring
import time
import os

from dotenv import load_dotenv

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from app_window_logic import AppWindowLogic
from User import User

load_dotenv()
API_URL = os.getenv("API_URL")


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
            lambda: self.login_or_refresh()
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

    def login_or_refresh(self):
        access_token = keyring.get_password("lolify", "token")
        if access_token:
            print("Access token:", access_token)
            self.check_token_expiration()
            self.close()
            app_logic = AppWindowLogic()
        else:
            self.login()

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
        name = self.ui.lineEdit_6.text()
        email = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        confirm_password = self.ui.lineEdit_5.text()
        if not email or not password:
            self.showNotification("Please enter email and password")
            return
        if password != confirm_password:
            self.showNotification("Passwords do not match.")
            return

        user = User(email, password, name)

        payload = {
            "email": user.email,
            "password": user.password,
            "password_confirmation": user.password,
            "name": user.name,
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

    def check_token_expiration(self):
        token_expiration_time = keyring.get_password("lolify", "token_expiration")
        if token_expiration_time:
            current_time = int(time.time())
            if current_time >= int(token_expiration_time):
                self.refresh_token()

    def refresh_token(self):
        access_token = keyring.get_password("lolify", "token")
        refresh_token = keyring.get_password("lolify", "refresh_token")
        if access_token and refresh_token:
            headers = {
                "Authorization": f"Bearer {refresh_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.post(f"{API_URL}/refresh", headers=headers)
            if response.status_code == 200:
                new_token = response.json()["access_token"]
                keyring.set_password("lolify", "token", new_token)
                print("Token refreshed successfully.")
            else:
                print("Failed to refresh token.")
        else:
            print("No token found or refresh token found. You are not logged in.")
