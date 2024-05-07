import requests
import os
from PySide6.QtWidgets import QTableWidgetItem
from dotenv import load_dotenv

load_dotenv()


def fetch_champions():
    API_URL = os.getenv("API_URL")
    # url = "https://lolify.wheelwallet.cloud/api/champion"
    try:
        response = requests.get(f"{API_URL}/champion")
        response.raise_for_status()  # Sprawdzenie statusu odpowiedzi
        champions = response.json()  # Pobranie danych w formacie JSON
        print("DANE CHAMPIONOW ZOSTALY POBRANE")
        return champions
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas pobierania danych:", e)
        return None


def fetch_top_champions():
    API_URL = os.getenv("API_URL")
    # url = "https://lolify.wheelwallet.cloud/api/champion"
    try:
        response = requests.get(f"{API_URL}/top3/champion")
        response.raise_for_status()  # Sprawdzenie statusu odpowiedzi
        champions = response.json()  # Pobranie danych w formacie JSON
        print("DANE CHAMPIONOW ZOSTALY POBRANE")
        return champions
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas pobierania danych:", e)
        return None


def display_champions_in_ui(table_widget):
    champions_data = fetch_champions()
    if champions_data:
        for index, champion in enumerate(champions_data):
            if index < 10:  # Wyświetl tylko 10 pierwszych bohaterów
                name_item = QTableWidgetItem(champion["name"])
                # Możesz także dodać inne informacje o bohaterze do odpowiednich komórek
                # Np. image_item = QTableWidgetItem(QIcon(champion['image_url']), '')  # Ikona bohatera
                # i umieścić je w odpowiednich kolumnach
                table_widget.setItem(index, 0, name_item)
                # table_widget.setItem(index, 1, image_item)  # Umieść ikonę w drugiej kolumnie
