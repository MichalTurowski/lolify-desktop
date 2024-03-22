# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_login_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 338)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 5, 0)
        self.notificationSlide = QCustomSlideMenu(self.header)
        self.notificationSlide.setObjectName(u"notificationSlide")
        self.notificationSlide.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.notificationSlide)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.notificationSlide)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(466, 36))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.notificationTxt = QLabel(self.frame_7)
        self.notificationTxt.setObjectName(u"notificationTxt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notificationTxt.sizePolicy().hasHeightForWidth())
        self.notificationTxt.setSizePolicy(sizePolicy)
        self.notificationTxt.setAlignment(Qt.AlignCenter)
        self.notificationTxt.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.notificationTxt)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.closeNotification = QPushButton(self.notificationSlide)
        self.closeNotification.setObjectName(u"closeNotification")
        self.closeNotification.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotification.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.closeNotification, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.notificationSlide)

        self.close_window_button = QPushButton(self.header)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(24, 24))
        self.close_window_button.setMaximumSize(QSize(24, 24))
        self.close_window_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.close_window_button, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QCustomQStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.welcome_login_pg = QWidget()
        self.welcome_login_pg.setObjectName(u"welcome_login_pg")
        self.welcome_login_pg.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_login_pg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.welcome_login_pg)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.to_signup = QPushButton(self.frame)
        self.to_signup.setObjectName(u"to_signup")
        self.to_signup.setMinimumSize(QSize(100, 0))
        self.to_signup.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.to_signup, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_login_pg)
        self.welcome_signup_pg = QWidget()
        self.welcome_signup_pg.setObjectName(u"welcome_signup_pg")
        self.verticalLayout_8 = QVBoxLayout(self.welcome_signup_pg)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.welcome_signup_pg)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.to_login = QPushButton(self.frame_4)
        self.to_login.setObjectName(u"to_login")
        self.to_login.setMinimumSize(QSize(100, 0))
        self.to_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_7.addWidget(self.to_login, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.welcome_signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.stackedWidget_2 = QCustomQStackedWidget(self.main_body)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.login_pg = QWidget()
        self.login_pg.setObjectName(u"login_pg")
        self.verticalLayout_4 = QVBoxLayout(self.login_pg)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.login_pg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.signInBtn = QPushButton(self.frame_3)
        self.signInBtn.setObjectName(u"signInBtn")
        self.signInBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.signInBtn)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.login_pg)
        self.signup_pg = QWidget()
        self.signup_pg.setObjectName(u"signup_pg")
        self.verticalLayout_11 = QVBoxLayout(self.signup_pg)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.signup_pg)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lineEdit_3 = QLineEdit(self.frame_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_10.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)

        self.verticalLayout_10.addWidget(self.lineEdit_5)

        self.signUpBtn = QPushButton(self.frame_6)
        self.signUpBtn.setObjectName(u"signUpBtn")
        self.signUpBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.signUpBtn)


        self.verticalLayout_9.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.frame_5, 0, Qt.AlignVCenter)

        self.stackedWidget_2.addWidget(self.signup_pg)

        self.horizontalLayout.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.footer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 10, 5)
        self.checkBox = QCustomCheckBox(self.footer)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(50, 0))
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/mode_night.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon2)
        self.checkBox.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.checkBox, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.notificationTxt.setText(QCoreApplication.translate("MainWindow", u"Notification message. Click \"x\" to hide.", None))
        self.closeNotification.setText("")
        self.close_window_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Hi, Welcome!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter your details to login.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Not registered? Click below to register", None))
        self.to_signup.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Hi, Welcome!</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enter your details to register.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Already registered? Click below to login", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Sing In</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signInBtn.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Sing Up</span></p></body></html>", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.signUpBtn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
    # retranslateUi

