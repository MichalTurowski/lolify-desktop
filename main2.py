from PySide6.QtWidgets import QApplication, QLabel

import sys
from test import *

app = QApplication(sys.argv)

label = QLabel(get_all_champions()[0]["name"])

label.show()

app.exec()
