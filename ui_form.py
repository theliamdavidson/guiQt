# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import vessel_math
import capture_ocr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1049, 722)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.confirmButton = QPushButton(self.centralwidget)
        self.confirmButton.setObjectName(u"confirmButton")
        self.confirmButton.setGeometry(QRect(330, 360, 141, 91))

        self.skipButton = QPushButton(self.centralwidget)
        self.skipButton.setObjectName(u"skipButton")
        self.skipButton.setGeometry(QRect(480, 360, 141, 91))

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(844, 20, 141, 81))

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(844, 120, 141, 81))

        self.dataShowLabel = QLabel(self.centralwidget)
        self.dataShowLabel.setObjectName(u"dataShowLabel")
        self.dataShowLabel.setGeometry(QRect(330, 280, 141, 71))
        font = QFont()
        font.setPointSize(28)
        self.dataShowLabel.setFont(font)
        self.dataShowLabel.setAlignment(Qt.AlignCenter)

        self.vesselNameLabel = QLabel(self.centralwidget)
        self.vesselNameLabel.setObjectName(u"vesselNameLabel")
        self.vesselNameLabel.setGeometry(QRect(480, 280, 141, 71))
        font1 = QFont()
        font1.setPointSize(12)
        self.vesselNameLabel.setFont(font1)
        self.vesselNameLabel.setAlignment(Qt.AlignCenter)
        
        self.vesselProgressBar = QProgressBar(self.centralwidget)
        self.vesselProgressBar.setObjectName(u"vesselProgressBar")
        self.vesselProgressBar.setGeometry(QRect(10, 10, 151, 31))
        self.vesselProgressBar.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1049, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)
        self.quitButton.clicked.connect(MainWindow.close)
        self.quitButton.clicked.connect(MainWindow.close)
        self.quitButton.clicked.connect(MainWindow.close)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.confirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.skipButton.setText(QCoreApplication.translate("MainWindow", u"Skip Vessel", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.dataShowLabel.setText("")
        self.vesselNameLabel.setText(QCoreApplication.translate("MainWindow", u"Press Skip to Begin", None))
    # retranslateUi

