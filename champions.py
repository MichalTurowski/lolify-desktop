import requests
import os
from PySide6.QtWidgets import QTableWidgetItem
from dotenv import load_dotenv

load_dotenv()


def fetch_champions():
    API_URL = os.getenv("API_URL")
    try:
        response = requests.get(f"{API_URL}/champion")
        response.raise_for_status()
        champions = response.json()
        return champions
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas pobierania danych:", e)
        return None


def fetch_top_champions():
    API_URL = os.getenv("API_URL")
    try:
        response = requests.get(f"{API_URL}/top3/champion")
        response.raise_for_status()
        champions = response.json()
        return champions
    except requests.exceptions.RequestException as e:
        print("Wystąpił błąd podczas pobierania danych:", e)
        return None
