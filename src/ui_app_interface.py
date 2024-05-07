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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(800, 493)
        MenuWindow.setMinimumSize(QSize(0, 0))
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

        self.checkBox_app = QCustomCheckBox(self.frame_3)
        self.checkBox_app.setObjectName(u"checkBox_app")
        self.checkBox_app.setMinimumSize(QSize(50, 0))
        self.checkBox_app.setMaximumSize(QSize(16777201, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/mode_night.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox_app.setIcon(icon5)
        self.checkBox_app.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.checkBox_app)


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


        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.stackedWidget_3 = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 200))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.friendName = QLineEdit(self.page_2)
        self.friendName.setObjectName(u"friendName")

        self.verticalLayout_8.addWidget(self.friendName)

        self.search = QPushButton(self.page_2)
        self.search.setObjectName(u"search")
        self.search.setMaximumSize(QSize(90, 16777215))
        self.search.setIcon(icon3)

        self.verticalLayout_8.addWidget(self.search, 0, Qt.AlignHCenter)

        self.stackedWidget_3.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget_3)


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
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logoutBtn = QPushButton(self.frame_5)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/log-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.logoutBtn)

        self.notificationShow = QPushButton(self.frame_5)
        self.notificationShow.setObjectName(u"notificationShow")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationShow.setIcon(icon8)

        self.horizontalLayout_4.addWidget(self.notificationShow)

        self.minimize_window = QPushButton(self.frame_5)
        self.minimize_window.setObjectName(u"minimize_window")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.minimize_window)

        self.restore_window = QPushButton(self.frame_5)
        self.restore_window.setObjectName(u"restore_window")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.restore_window)

        self.close_window = QPushButton(self.frame_5)
        self.close_window.setObjectName(u"close_window")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window.setIcon(icon11)

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
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 492, 315))
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
        self.allBtn = QPushButton(self.paginationButtons)
        self.allBtn.setObjectName(u"allBtn")
        self.allBtn.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.allBtn.setFont(font2)

        self.horizontalLayout_9.addWidget(self.allBtn)

        self.topBtn_2 = QPushButton(self.paginationButtons)
        self.topBtn_2.setObjectName(u"topBtn_2")
        self.topBtn_2.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.topBtn_2)

        self.jungleBtn = QPushButton(self.paginationButtons)
        self.jungleBtn.setObjectName(u"jungleBtn")
        self.jungleBtn.setMaximumSize(QSize(60, 40))

        self.horizontalLayout_9.addWidget(self.jungleBtn)

        self.midBtn = QPushButton(self.paginationButtons)
        self.midBtn.setObjectName(u"midBtn")
        self.midBtn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_9.addWidget(self.midBtn)

        self.adcBtn = QPushButton(self.paginationButtons)
        self.adcBtn.setObjectName(u"adcBtn")
        self.adcBtn.setMaximumSize(QSize(40, 40))
        self.adcBtn.setStyleSheet(u"QPushButton {\n"
"    text-align: center;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.adcBtn)

        self.supportBtn = QPushButton(self.paginationButtons)
        self.supportBtn.setObjectName(u"supportBtn")
        self.supportBtn.setMaximumSize(QSize(60, 40))

        self.horizontalLayout_9.addWidget(self.supportBtn)


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
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_3 = QVBoxLayout(self.page_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_3 = QScrollArea(self.page_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -175, 532, 477))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_8 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 180))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_4)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_6)

        self.summonerName = QLabel(self.frame_8)
        self.summonerName.setObjectName(u"summonerName")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(200)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.summonerName.sizePolicy().hasHeightForWidth())
        self.summonerName.setSizePolicy(sizePolicy4)
        self.summonerName.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.summonerName)

        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_10)

        self.summonerEmail = QLabel(self.frame_8)
        self.summonerEmail.setObjectName(u"summonerEmail")
        sizePolicy4.setHeightForWidth(self.summonerEmail.sizePolicy().hasHeightForWidth())
        self.summonerEmail.setSizePolicy(sizePolicy4)
        self.summonerEmail.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.summonerEmail)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 16777210))
        self.label_11.setFont(font1)
        self.label_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_11)


        self.verticalLayout_18.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_4 = QScrollArea(self.frame_9)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 492, 251))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.champions_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.champions_3.setObjectName(u"champions_3")
        self.champions_3.setMinimumSize(QSize(474, 233))
        self.gridLayout_6 = QGridLayout(self.champions_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_11 = QFrame(self.champions_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.champions_3, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_19.addWidget(self.scrollArea_4)


        self.verticalLayout_18.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setMaximumSize(QSize(16777215, 180))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.line = QFrame(self.frame_10)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(494, 0))
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line)

        self.tableWidget = QTableWidget(self.frame_10)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(494, 176))
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.tableWidget)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.scrollArea_3)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 492, 315))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.champions_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.champions_2.setObjectName(u"champions_2")
        self.champions_2.setMinimumSize(QSize(0, 233))
        self.gridLayout_4 = QGridLayout(self.champions_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout_3.addWidget(self.champions_2, 1, 0, 1, 1)

        self.topChampions = QWidget(self.scrollAreaWidgetContents_2)
        self.topChampions.setObjectName(u"topChampions")
        self.topChampions.setMinimumSize(QSize(0, 0))
        self.topChampions.setMaximumSize(QSize(494, 215))
        self.topChampions.setFont(font1)
        self.horizontalLayout_10 = QHBoxLayout(self.topChampions)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.topChampions)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.label_9 = QLabel(self.topChampions)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(38, 38))
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setStyleSheet(u"")
        self.label_9.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/medal.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_9)


        self.gridLayout_3.addWidget(self.topChampions, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

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

        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)


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
        self.checkBox_app.setText(QCoreApplication.translate("MenuWindow", u"Dark Mode", None))
        self.label.setText(QCoreApplication.translate("MenuWindow", u"Search friend", None))
#if QT_CONFIG(tooltip)
        self.closeMoreMenu.setToolTip(QCoreApplication.translate("MenuWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeMoreMenu.setText("")
        self.friendName.setPlaceholderText(QCoreApplication.translate("MenuWindow", u"Name", None))
        self.search.setText(QCoreApplication.translate("MenuWindow", u"Search", None))
        self.label_logo.setText("")
        self.label_5.setText(QCoreApplication.translate("MenuWindow", u"Lolify", None))
        self.logoutBtn.setText("")
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
        self.allBtn.setText(QCoreApplication.translate("MenuWindow", u"ALL", None))
        self.topBtn_2.setText(QCoreApplication.translate("MenuWindow", u"TOP", None))
        self.jungleBtn.setText(QCoreApplication.translate("MenuWindow", u"JUNGLE", None))
        self.midBtn.setText(QCoreApplication.translate("MenuWindow", u"MID", None))
        self.adcBtn.setText(QCoreApplication.translate("MenuWindow", u"ADC", None))
        self.supportBtn.setText(QCoreApplication.translate("MenuWindow", u"SUPPORT", None))
        self.label_4.setText(QCoreApplication.translate("MenuWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MenuWindow", u"Summoner:", None))
        self.summonerName.setText(QCoreApplication.translate("MenuWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MenuWindow", u"E-mail: ", None))
        self.summonerEmail.setText(QCoreApplication.translate("MenuWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MenuWindow", u"Favorites", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MenuWindow", u"Logs", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MenuWindow", u"Date", None));
        self.label_7.setText(QCoreApplication.translate("MenuWindow", u"Top Champions", None))
        self.label_9.setText("")
        self.label_8.setText(QCoreApplication.translate("MenuWindow", u"Notification message", None))
#if QT_CONFIG(tooltip)
        self.closeNotification.setToolTip(QCoreApplication.translate("MenuWindow", u"Close notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotification.setText("")
    # retranslateUi

