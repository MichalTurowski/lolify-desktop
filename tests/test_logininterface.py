import sys

sys.path.insert(0, "D:/ZADANIA/Semestr6/Zmp")
import pytest
import time
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from src.ui_login_interface import Ui_MainWindow
from main_window_logic import MainWindow
from app_window_logic import AppWindowLogic
from unittest.mock import patch, MagicMock

app = QApplication([])


@pytest.fixture
def ui():
    ui = Ui_MainWindow()
    window = QMainWindow()
    ui.setupUi(window)
    return ui, window


def test_login_with_valid_credentials(ui):
    ui, window = ui
    with patch("main_window_logic.keyring.get_password", return_value="valid_token"):
        ui.lineEdit.setText("valid_email@example.com")
        ui.lineEdit_2.setText("valid_password")
        QTest.mouseClick(ui.signInBtn, Qt.LeftButton)
        assert not window.isVisible()


def test_registration_with_valid_data(ui):
    ui, window = ui
    with patch("main_window_logic.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        ui.lineEdit_6.setText("John")
        ui.lineEdit_3.setText("john@example.com")
        ui.lineEdit_4.setText("password123")
        ui.lineEdit_5.setText("password123")
        QTest.mouseClick(ui.signUpBtn, Qt.LeftButton)
        assert not window.isVisible()


def test_dark_mode_switch(ui):
    ui, _ = ui
    assert ui.checkBox.isChecked() == False

    QTest.mouseClick(ui.checkBox, Qt.LeftButton)

    assert ui.checkBox.isChecked() == True

    QTest.mouseClick(ui.checkBox, Qt.LeftButton)

    assert ui.checkBox.isChecked() == False


def test_show_notification(ui):
    window = MainWindow()

    window.ui.notificationTxt = MagicMock()
    window.ui.notificationSlide = MagicMock()

    window.showNotification("Test message")

    window.ui.notificationTxt.setText.assert_called_once_with("Test message")

    window.ui.notificationSlide.expandMenu.assert_called_once()
