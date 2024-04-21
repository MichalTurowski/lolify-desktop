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

    def fetch_and_display_champions(self):
        # Pobranie i wyświetlenie danych bohaterów
        champions_data = fetch_champions()
        if champions_data:
            print("Pobrane dane bohaterów:")
            for champion in champions_data:
                print(champion)
            # Jeśli pobranie danych powiodło się, przełącz na interfejs aplikacji
            self.switch_to_app_ui()
        else:
            print("Nie udało się pobrać danych bohaterów.")

    def switch_to_app_ui(self):
        # Przełączenie na interfejs aplikacji po udanym zalogowaniu
        self.hide()
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/app_style.json"})
        QAppSettings.updateAppSettings(self)
        self.show()
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
