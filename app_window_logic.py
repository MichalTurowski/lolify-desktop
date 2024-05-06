import sys
import requests
import keyring
import os

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from ChampionCard import ChampionCard
from champions import fetch_champions
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_URL = os.getenv("API_URL")


class AppWindowLogic(QMainWindow, Ui_MenuWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/app_style.json"})

        QAppSettings.updateAppSettings(self)

        self.ui.notificationSlide.collapseMenu()
        self.show()
        self.ui.checkBox_app.stateChanged.connect(lambda: self.darkMode())
        self.ui.notificationShow.clicked.connect(
            lambda: self.showNotification("Notification show button clicked!")
        )
        self.ui.logoutBtn.clicked.connect(lambda: self.logout())
        self.ui.profileBtn.clicked.connect(lambda: self.profile())

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

    def profile(self):
        access_token = keyring.get_password("lolify", "token")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        response = requests.get(f"{API_URL}/me", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            summoner_name = user_data.get("name", "Unknown")
            summoner_email = user_data.get("email", "Unknown")
            self.ui.summonerName.setText(summoner_name)
            self.ui.summonerEmail.setText(summoner_email)

        logs = user_data.get("logs", [])
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setRowCount(len(logs))
        row = 0
        # Iteruj przez logi i wydrukuj tekst i znacznik czasu
        for log in logs:
            text = log.get("text")
            timestamp = log.get("timestamp")
            parsed_timestamp = datetime.fromisoformat(timestamp[:-1])
            print("Text:", text)
            print("Timestamp:", timestamp)
            item_text = QTableWidgetItem(text)
            item_timestamp = parsed_timestamp.strftime("%d-%m-%Y, %H:%M:%S")
            self.ui.tableWidget.setItem(row, 0, item_text)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item_timestamp))
            row += 1

        else:
            print("Failed to get user data. Status code:", response.status_code)
