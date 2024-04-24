########################################################################
## IMPORTS
########################################################################
import sys

########################################################################
# IMPORT GUI FILE
from src.ui_login_interface import *
from src.ui_app_interface import *

########################################################################
from champions import fetch_champions
from ChampionCard import ChampionCard

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/login_style.json"})
        ########################################################################
        QAppSettings.updateAppSettings(self)
        ########################################################################
        self.ui.notificationSlide.collapseMenu()
        self.show()

        # Event listeners
        self.ui.signInBtn.clicked.connect(
            # lambda: self.showNotification("Sign in button clicked!")
            lambda: self.login()
        )
        self.ui.signUpBtn.clicked.connect(
            lambda: self.showNotification("Sign up button clicked!")
        )

        # Change theme
        self.ui.checkBox.stateChanged.connect(lambda: self.darkMode())

    # Function to display notification
    def showNotification(self, msg):
        self.ui.notificationTxt.setText(msg)
        self.ui.notificationSlide.expandMenu()

    # Function to switch theme
    def darkMode(self):
        #######################################################################
        # CHECK THE CURRENT THEME SETTINGS
        #######################################################################
        settings = QSettings()
        # CURRENT ICONS
        # CURRENT THEME NAME
        print("Current theme", settings.value("THEME"))
        print("Current Icons color", settings.value("ICONS-COLOR"))

        if settings.value("THEME") == "Dark-Blue":
            # CHANGE THE THEME NAME IN SETTINGS
            # Use one of the app themes from your JSON file
            settings.setValue("THEME", "Light-Blue")

        else:
            settings.setValue("THEME", "Dark-Blue")

        # RE APPLY THE NEW SETINGS
        # CompileStyleSheet might also work
        CompileStyleSheet.applyCompiledSass(self)
        # QAppSettings.updateAppSettings(self)

    def login(self):
        # Logowanie użytkownika
        self.fetch_and_display_champions()
        # self.switch_to_app_ui()

    def fetch_and_display_champions(self):
        # Pobranie i wyświetlenie danych bohaterów
        champions_data = fetch_champions()
        if champions_data:
            total_champions = len(champions_data)  # Zlicz liczbę wszystkich bohaterów
            total_champions_label = QLabel(f"Total champions: {total_champions}")
            print("Pobrane dane bohaterów:")
            for champion in champions_data:
                print(champion)
            # Jeśli pobranie danych powiodło się, przełącz na interfejs aplikacji
            self.switch_to_app_ui()
        else:
            print("Nie udało się pobrać danych bohaterów.")

    def createNewWidgets(self, rowNumber, columNumber, champion_data):
        newName = "frame" + str(rowNumber) + "_" + str(columNumber)
        print(newName)
        champion_card = ChampionCard(champion_data, self.ui.champions)
        champion_card.champion_clicked.connect(self.handle_champion_clicked)
        self.ui.gridLayout_2.addWidget(champion_card, rowNumber, columNumber, 1, 1)

    def handle_champion_clicked(self, champion_id):
        print(f"Champion clicked! Champion ID: {champion_id}")

    def switch_to_app_ui(self):
        # Przełączenie na interfejs aplikacji po udanym zalogowaniu
        self.hide()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/app_style.json"})
        QAppSettings.updateAppSettings(self)
        self.show()
        champions_data = fetch_champions()
        if champions_data:
            # Zlicz liczbę bohaterów
            total_champions = len(champions_data)

            # Oblicz liczbę wierszy i kolumn
            num_rows = (total_champions + 4) // 5  # 5 kolumn na wiersz
            num_columns = 5

            # Pętla do tworzenia kontenerów na bohaterów
            for x in range(num_rows):
                for y in range(num_columns):
                    champion_index = x * num_columns + y
                    if champion_index < total_champions:
                        champion_data = champions_data[champion_index]
                        self.createNewWidgets(x, y, champion_data)
        self.ui.searchBtn.clicked.connect(
            lambda: self.ui.centerMenuContainer.expandMenu()
        )
        self.ui.closeMoreMenu.clicked.connect(
            lambda: self.ui.centerMenuContainer.collapseMenu()
        )
        self.ui.notificationShow.clicked.connect(
            lambda: self.ui.notificationSlide.expandMenu()
        )
        self.ui.closeNotification.clicked.connect(
            lambda: self.ui.notificationSlide.collapseMenu()
        )


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################
