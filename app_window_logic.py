import sys
import requests
import keyring
import os

from src.ui_login_interface import *
from src.ui_app_interface import *

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from ChampionCard import ChampionCard
from TopChampionCard import TopChampionCard
from champions import fetch_champions, fetch_top_champions
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_URL = os.getenv("API_URL")


class AppWindowLogic(QMainWindow, Ui_MenuWindow):
    champions_data = []
    top_champions_data = []

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/app_style.json"})

        QAppSettings.updateAppSettings(self)
        self.ui.notificationSlide.collapseMenu()
        self.show()
        self.ui.championsBtn.clicked.connect(lambda: self.switch_to_app_ui())
        self.ui.topBtn.clicked.connect(lambda: self.update_top_champions_ui())
        self.ui.checkBox_app.stateChanged.connect(lambda: self.darkMode())
        self.ui.notificationShow.clicked.connect(
            lambda: self.showNotification("Notification show button clicked!")
        )
        self.ui.logoutBtn.clicked.connect(lambda: self.logout())
        self.ui.profileBtn.clicked.connect(lambda: self.profile())
        if not AppWindowLogic.champions_data:
            AppWindowLogic.champions_data = fetch_champions()
        if not AppWindowLogic.top_champions_data:
            AppWindowLogic.top_champions_data = fetch_top_champions()
        self.ui.allBtn.clicked.connect(lambda: self.filter_champions(None))
        self.ui.topBtn_2.clicked.connect(lambda: self.filter_champions(1))
        self.ui.jungleBtn.clicked.connect(lambda: self.filter_champions(2))
        self.ui.midBtn.clicked.connect(lambda: self.filter_champions(3))
        self.ui.adcBtn.clicked.connect(lambda: self.filter_champions(4))
        self.ui.supportBtn.clicked.connect(lambda: self.filter_champions(5))
        self.ui.searchBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu()
        )
        self.ui.search.clicked.connect(lambda: self.search_and_display_profile())
        self.ui.closeMoreMenu.clicked.connect(
            lambda: self.ui.centerMenuContainer.collapseMenu()
        )

    def showNotification(self, msg):
        self.ui.label_8.setText(msg)
        self.ui.notificationSlide.expandMenu()

    def darkMode(self):
        settings = QSettings()

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
                self.showNotification("Failed to log out.")
                print("Failed to log out.")
        else:
            self.showNotification("No token found. You are not logged in.")
            print("No token found. You are not logged in.")

    def createNewWidgets(self, rowNumber, columNumber, champion_data):
        champion_card = ChampionCard(champion_data, self.ui.champions)
        champion_card.champion_clicked.connect(self.handle_champion_clicked)
        self.ui.gridLayout_2.addWidget(champion_card, rowNumber, columNumber, 1, 1)

    def handle_champion_clicked(self, champion_id):
        champion_data = self.fetch_champion_details(champion_id)
        if champion_data:
            self.display_champion_details(champion_data)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        else:
            self.showNotification("Failed to fetch champion details.")

    def switch_to_app_ui(self):
        self.filter_champions(None)

    def filter_champions(self, role_id):
        if role_id is None:
            champions_data = AppWindowLogic.champions_data
        else:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.get(
                f"{API_URL}/champion/role/{role_id}", headers=headers
            )
            if response.status_code == 200:
                champions_data = response.json()
            else:
                print("Failed to fetch champions by role.")
                self.showNotification("Failed to fetch champions by role.")
                return

        self.update_champions_ui(champions_data)

    def update_champions_ui(self, champions_data):
        while self.ui.gridLayout_2.count():
            item = self.ui.gridLayout_2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        total_champions = len(champions_data)

        num_rows = (total_champions + 4) // 5
        num_columns = 5

        for x in range(num_rows):
            for y in range(num_columns):
                champion_index = x * num_columns + y
                if champion_index < total_champions:
                    champion_data = champions_data[champion_index]
                    self.createNewWidgets(x, y, champion_data)

    def update_top_champions_ui(self):
        top_champions_data = AppWindowLogic.top_champions_data

        total_top_champions = len(top_champions_data)

        num_rows = 1
        num_columns = 3

        for x in range(num_rows):
            for y in range(num_columns):
                champion_index = x * num_columns + y
                if champion_index < total_top_champions:
                    champion_data = top_champions_data[champion_index]
                    self.createNewTopWidgets(x, y, champion_data)

    def createNewTopWidgets(self, rowNumber, columNumber, champion_data):
        champion_card = TopChampionCard(champion_data, self.ui.champions_2)
        champion_card.champion_clicked.connect(self.handle_champion_clicked)
        self.ui.gridLayout_4.addWidget(champion_card, rowNumber, columNumber, 1, 1)

    def search_and_display_profile(self):
        username = self.ui.friendName.text()
        if not username:
            self.showNotification("Enter friend name.")
            return

        access_token = keyring.get_password("lolify", "token")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        response = requests.get(f"{API_URL}/profile/{username}", headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            self.profile(user_data)
        else:
            self.showNotification("User not found.")

    def profile(self, user_data=None):
        if user_data is None:
            access_token = keyring.get_password("lolify", "token")
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.get(f"{API_URL}/me", headers=headers)
            if response.status_code == 200:
                user_data = response.json()
            else:
                print("Failed to get user data. Status code:", response.status_code)
                return

        summoner_name = user_data.get("name", "Unknown")
        summoner_email = user_data.get("email", "Unknown")
        self.ui.summonerName.setText(summoner_name)
        self.ui.summonerEmail.setText(summoner_email)

        logs = user_data.get("logs", [])
        likes = user_data.get("likes", [])

        self.create_favorite_champion_widgets(likes)
        self.ui.tableWidget.setColumnWidth(0, 300)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setRowCount(len(logs))
        row = 0
        for log in logs:
            text = log.get("text")
            timestamp = log.get("timestamp")
            parsed_timestamp = datetime.fromisoformat(timestamp[:-1])
            item_text = QTableWidgetItem(text)
            item_timestamp = parsed_timestamp.strftime("%d-%m-%Y, %H:%M:%S")
            self.ui.tableWidget.setItem(row, 0, item_text)
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item_timestamp))
            row += 1

        self.ui.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 956, 441))
        self.ui.gridLayout_6.setGeometry(QRect(10, 10, 931, 421))

    def create_favorite_champion_widgets(self, likes):
        while self.ui.gridLayout_6.count():
            item = self.ui.gridLayout_6.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        num_columns = 5
        num_rows = (len(likes) + num_columns - 1) // num_columns

        for i, like in enumerate(likes):
            champion_data = {
                "id": like["id"],
                "name": like["name"],
                "description": like["description"],
                "image_link": like["image_link"],
                "title": like["title"],
            }
            row_number = i // num_columns
            column_number = i % num_columns
            self.create_favorite_champion_widget(
                row_number, column_number, champion_data
            )

    def create_favorite_champion_widget(self, row_number, column_number, champion_data):
        favorite_champion_widget = ChampionCard(champion_data, self.ui.champions_3)
        favorite_champion_widget.champion_clicked.connect(self.handle_champion_clicked)
        self.ui.gridLayout_6.addWidget(
            favorite_champion_widget, row_number, column_number
        )

    def display_champion_details(self, champion_data):
        while self.ui.verticalLayout_24.count():
            item = self.ui.verticalLayout_24.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        while self.ui.verticalLayout_23.count():
            item = self.ui.verticalLayout_23.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.ui.championName.setText(champion_data["name"])
        self.ui.championName.setStyleSheet(
            "font-size: 18pt; font-weight: bold; text-align: left;"
        )

        self.ui.championTitle.setText(champion_data["title"])
        self.ui.championTitle.setStyleSheet(
            "font-size: 18pt; font-weight: bold; text-align: left;"
        )

        roles_text = ", ".join([role["name"] for role in champion_data["roles"]])
        self.ui.championRole.setText(f"Role: {roles_text}")
        self.ui.championRole.setStyleSheet("font-size: 14pt; text-align: left;")

        description_text = champion_data["description"]
        self.ui.championDescription.setText(description_text)
        self.ui.championDescription.setStyleSheet("font-size: 9pt; text-align: left;")

        self.ui.championLikes.setText(f"Likes: {champion_data['likes_count']}")
        self.ui.championLikes.setStyleSheet("font-size: 16pt;")

        image_url = champion_data["image_link"]
        image_data = requests.get(image_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)
        scaled_pixmap = pixmap.scaled(575, 339)
        self.ui.championImage.setPixmap(scaled_pixmap)
        self.ui.championImage.setScaledContents(True)

        self.ui.likeBtn.setEnabled(False)
        self.ui.likeBtn.clicked.connect(
            lambda: self.handle_like_button_clicked(champion_data["id"])
        )

        self.set_champion_skills(champion_data["skills"])

        self.set_champion_skins(champion_data["skins"])

        self.ui.likeBtn.setEnabled(True)

    def set_champion_skins(self, skins):
        for i, skin in enumerate(skins):
            skin_image_url = skin["image_link"]
            skin_image_data = requests.get(skin_image_url).content
            skin_pixmap = QPixmap()
            skin_pixmap.loadFromData(skin_image_data)
            skin_label = QLabel(self.ui.frame_17)
            skin_label.setPixmap(skin_pixmap)
            skin_label.setObjectName(f"skinChampion_{i}")
            self.ui.verticalLayout_23.addWidget(skin_label)

    def set_champion_skills(self, skills):
        skill_keys = ["Q", "W", "E", "R", "Passive"]
        for i, skill in enumerate(skills):
            skill_name = skill["name"]
            skill_key = skill_keys[i]

            skill_label = QLabel(
                f"<b>{skill_key}</b><br>{skill_name}", self.ui.frame_18
            )
            skill_label.setObjectName(f"skillLabel_{i}")
            skill_label.setStyleSheet("font-size: 12pt;")
            skill_label.setWordWrap(True)

            skill_image_url = skill["image_link"]
            skill_image_data = requests.get(skill_image_url).content
            skill_pixmap = QPixmap()
            skill_pixmap.loadFromData(skill_image_data)
            skill_image_label = QLabel(self.ui.frame_18)
            skill_image_label.setPixmap(skill_pixmap)

            self.ui.verticalLayout_24.addWidget(skill_label)
            self.ui.verticalLayout_24.addWidget(skill_image_label)

    def fetch_champion_details(self, champion_id):
        url = f"{API_URL}/champion/{champion_id}"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            self.showNotification("Failed to fetcg cgampion data.")
            return None

    def handle_like_button_clicked(self, champion_id):
        liked = self.check_if_champion_liked(champion_id)
        if liked:
            self.dislike_champion(champion_id)
        else:
            self.like_champion(champion_id)

    def like_champion(self, champion_id):
        access_token = keyring.get_password("lolify", "token")
        if access_token:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.post(
                f"{API_URL}/champion/like/{champion_id}", headers=headers
            )
            if response.status_code == 200:
                self.showNotification(
                    "Champion has been added to the liked champions list."
                )
                champion_data = self.fetch_champion_details(champion_id)
                if champion_data:
                    self.display_champion_details(champion_data)
            elif response.status_code == 404:
                self.showNotification("Champion not found.")
            else:
                self.showNotification(
                    "There was a problem adding the champion to the liked champions list."
                )
        else:
            self.showNotification("User is not logged in.")

    def dislike_champion(self, champion_id):
        access_token = keyring.get_password("lolify", "token")
        if access_token:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
            response = requests.post(
                f"{API_URL}/champion/dislike/{champion_id}", headers=headers
            )
            if response.status_code == 200:
                self.showNotification(
                    "Champion has been removed from the liked champions list."
                )
                champion_data = self.fetch_champion_details(champion_id)
                if champion_data:
                    self.display_champion_details(champion_data)
            elif response.status_code == 404:
                self.showNotification("Champion not found.")
            else:
                self.showNotification(
                    "There was a problem removing the champion from the liked champions list."
                )
        else:
            self.showNotification("User is not logged in.")

    def check_if_champion_liked(self, champion_id):
        access_token = keyring.get_password("lolify", "token")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        response = requests.get(f"{API_URL}/me", headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            likes = user_data.get("likes", [])
            champion_ids = [like["id"] for like in likes]
            if champion_id in champion_ids:
                return True
            else:
                return False
        else:
            self.showNotification("Failed to get user data.")
            print("Failed to get user data. Status code:", response.status_code)
            return False
