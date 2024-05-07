import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt, Signal, QUrl


class ChampionCard(QWidget):

    champion_clicked = Signal(int)

    def __init__(self, champion_data, parent=None):
        super().__init__(parent)
        self.champion_data = champion_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        image_label = QLabel()
        pixmap = self.get_image_from_url(self.champion_data["image_link"])
        image_label.setPixmap(pixmap)

        image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)
        image_label.setScaledContents(True)
        name_label = QLabel(self.champion_data["name"])
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(name_label)

        self.setLayout(layout)
        self.setMinimumWidth(150)  # Minimalna szerokość
        self.setMaximumWidth(500)  # Maksymalna szerokość
        self.setMinimumHeight(100)
        self.setMaximumHeight(600)
        self.setStyleSheet(
            """
            QWidget {
                border: 1.5px solid #000000;
                border-radius: 0px 0px 10px 10px;
                background-color: #FFFFFF;
                color: #000000;
            }
            QWidget:hover {
                border: 1.5px solid #FFFFFF;
                background-color: #000000;
                color: #FFFFFF;
            }
            """
        )

    def mousePressEvent(self, event):
        self.emit_clicked()

    def emit_clicked(self):
        champion_id = self.champion_data["id"]
        self.champion_clicked.emit(champion_id)

    def get_image_from_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            return pixmap
        except requests.exceptions.RequestException as e:
            print("Error fetching image:", e)
            return QPixmap()  # Return an empty pixmap on error
