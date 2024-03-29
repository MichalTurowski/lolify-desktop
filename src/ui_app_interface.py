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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(800, 468)
        self.centralwidget = QWidget(MenuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.label = QLabel(self.leftMenuContainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 140, 221, 121))

        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuWindow)

        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MenuWindow", u"Second Window", None))
    # retranslateUi

