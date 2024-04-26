import sys

from src.ui_login_interface import *
from src.ui_app_interface import *

from champions import fetch_champions
from ChampionCard import ChampionCard

from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from main_window_logic import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
