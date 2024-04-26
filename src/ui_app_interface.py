# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_app_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(800, 469)
        MenuWindow.setStyleSheet(u"QPushButton{\n"
"	text-align: left;\n"
"}")
        self.centralwidget = QWidget(MenuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(52, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(10)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.topBtn = QPushButton(self.frame_2)
        self.topBtn.setObjectName(u"topBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topBtn.sizePolicy().hasHeightForWidth())
        self.topBtn.setSizePolicy(sizePolicy1)
        self.topBtn.setFont(font)
        self.topBtn.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/crown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.topBtn.setIcon(icon1)
        self.topBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.topBtn)

        self.championsBtn = QPushButton(self.frame_2)
        self.championsBtn.setObjectName(u"championsBtn")
        self.championsBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.championsBtn.setIcon(icon2)
        self.championsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.championsBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.searchBtn = QPushButton(self.frame_3)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon3)
        self.searchBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.searchBtn)

        self.profileBtn = QPushButton(self.frame_3)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon4)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.profileBtn)

        self.checkBox1 = QCustomCheckBox(self.frame_3)
        self.checkBox1.setObjectName(u"checkBox1")
        self.checkBox1.setMinimumSize(QSize(50, 0))
        self.checkBox1.setMaximumSize(QSize(16777201, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/mode_night.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox1.setIcon(icon5)
        self.checkBox1.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.checkBox1)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.closeMoreMenu = QPushButton(self.frame_4)
        self.closeMoreMenu.setObjectName(u"closeMoreMenu")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeMoreMenu.setIcon(icon6)
        self.closeMoreMenu.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.closeMoreMenu, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.mainBodyContainer)
        self.header.setObjectName(u"header")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.frame_6)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMaximumSize(QSize(40, 40))
        self.label_logo.setPixmap(QPixmap(u":/images/League of Legends.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_logo)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.notificationShow = QPushButton(self.frame_5)
        self.notificationShow.setObjectName(u"notificationShow")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationShow.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.notificationShow)

        self.minimize_window = QPushButton(self.frame_5)
        self.minimize_window.setObjectName(u"minimize_window")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.minimize_window)

        self.restore_window = QPushButton(self.frame_5)
        self.restore_window.setObjectName(u"restore_window")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.restore_window)

        self.close_window = QPushButton(self.frame_5)
        self.close_window.setObjectName(u"close_window")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.close_window)


        self.horizontalLayout_3.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.horizontalLayout_6 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.verticalLayout_11 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.stackedWidget_2 = QCustomQStackedWidget(self.mainContentContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 475, 299))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.paginationButtons = QWidget(self.scrollAreaWidgetContents)
        self.paginationButtons.setObjectName(u"paginationButtons")
        self.paginationButtons.setMaximumSize(QSize(494, 215))
        self.paginationButtons.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.paginationButtons)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.paginationButtons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 40))
        font3 = QFont()
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.pushButton.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.paginationButtons)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.paginationButtons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(60, 40))

        self.horizontalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.paginationButtons)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.paginationButtons)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.paginationButtons)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(60, 40))

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.paginationButtons, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.champions = QWidget(self.scrollAreaWidgetContents)
        self.champions.setObjectName(u"champions")
        self.champions.setMinimumSize(QSize(0, 233))
        self.gridLayout_2 = QGridLayout(self.champions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addWidget(self.champions, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_7)

        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)


        self.horizontalLayout_6.addWidget(self.mainContentContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.footer = QWidget(self.mainBodyContainer)
        self.footer.setObjectName(u"footer")
        self.verticalLayout_14 = QVBoxLayout(self.footer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.notificationSlide = QCustomSlideMenu(self.footer)
        self.notificationSlide.setObjectName(u"notificationSlide")
        self.verticalLayout_15 = QVBoxLayout(self.notificationSlide)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_7 = QFrame(self.notificationSlide)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.closeNotification = QPushButton(self.frame_7)
        self.closeNotification.setObjectName(u"closeNotification")
        self.closeNotification.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.closeNotification, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.frame_7)


        self.verticalLayout_14.addWidget(self.notificationSlide)


        self.verticalLayout_10.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MenuWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.topBtn.setToolTip(QCoreApplication.translate("MenuWindow", u"TopChampions", None))
#endif // QT_CONFIG(tooltip)
        self.topBtn.setText(QCoreApplication.translate("MenuWindow", u"  Top Champions", None))
#if QT_CONFIG(tooltip)
        self.championsBtn.setToolTip(QCoreApplication.translate("MenuWindow", u"ChampionsList", None))
#endif // QT_CONFIG(tooltip)
        self.championsBtn.setText(QCoreApplication.translate("MenuWindow", u"  Champions List", None))
#if QT_CONFIG(tooltip)
        self.searchBtn.setToolTip(QCoreApplication.translate("MenuWindow", u"SearchFriend", None))
#endif // QT_CONFIG(tooltip)
        self.searchBtn.setText(QCoreApplication.translate("MenuWindow", u"  Search friend", None))
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MenuWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText(QCoreApplication.translate("MenuWindow", u"  Profile", None))
        self.checkBox1.setText(QCoreApplication.translate("MenuWindow", u"Dark Mode", None))
        self.label.setText(QCoreApplication.translate("MenuWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeMoreMenu.setToolTip(QCoreApplication.translate("MenuWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeMoreMenu.setText("")
        self.label_2.setText(QCoreApplication.translate("MenuWindow", u"Search friend", None))
        self.label_3.setText(QCoreApplication.translate("MenuWindow", u"Profile", None))
        self.label_logo.setText("")
        self.label_5.setText(QCoreApplication.translate("MenuWindow", u"Lolify", None))
        self.notificationShow.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_window.setToolTip(QCoreApplication.translate("MenuWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_window.setText("")
#if QT_CONFIG(tooltip)
        self.restore_window.setToolTip(QCoreApplication.translate("MenuWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restore_window.setText("")
#if QT_CONFIG(tooltip)
        self.close_window.setToolTip(QCoreApplication.translate("MenuWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.close_window.setText("")
        self.pushButton.setText(QCoreApplication.translate("MenuWindow", u"ALL", None))
        self.pushButton_2.setText(QCoreApplication.translate("MenuWindow", u"TOP", None))
        self.pushButton_3.setText(QCoreApplication.translate("MenuWindow", u"JUNGLE", None))
        self.pushButton_4.setText(QCoreApplication.translate("MenuWindow", u"MID", None))
        self.pushButton_5.setText(QCoreApplication.translate("MenuWindow", u"ADC", None))
        self.pushButton_6.setText(QCoreApplication.translate("MenuWindow", u"SUPPORT", None))
        self.label_7.setText(QCoreApplication.translate("MenuWindow", u"Champions List", None))
        self.label_8.setText(QCoreApplication.translate("MenuWindow", u"Notification message", None))
#if QT_CONFIG(tooltip)
        self.closeNotification.setToolTip(QCoreApplication.translate("MenuWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotification.setText("")
    # retranslateUi

