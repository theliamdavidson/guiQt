# This Python file uses the following encoding: utf-8
import sys
import threading
import queue
import concurrent.futures
import logging
import vessel_math as vm
import capture_ocr
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThread,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#from ui_form import Ui_MainWindow
artery_num = 0
message_list = []
len_list = []

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
        self.skipButton.clicked.connect(self.thread_4_cm)
        self.quitButton.clicked.connect(MainWindow.close)
        self.quitButton.clicked.connect(MainWindow.close)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def cam_listener(self, queue, event):
        """
            Creates a watchdog thread that captures data from the ultrasound,
            and sends it to the algorithm thread via the queue
        """
        while not event.is_set():
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                ocr_thread = executor.submit(capture_ocr.capture_decoder)
                return_value = ocr_thread.result()
            thread_return = str(return_value).split(",")
            #logging.info("cam_listener is active")
            return_string = ""
            #logging.info("recieved from thread: %s",thread_return)
            for i in range(len(thread_return)):
                try:
                    return_float = float(thread_return[i])
                    logging.info("recieved from thread: %f",return_float)
                    found = True

                except:
                    if thread_return[i] == ".":
                        return_string += thread_return[i]

            if found == True:
                queue.put( return_float, "Camera")
    def thread_4_cm(self):
        self.thread = QThread()
        #self.worker = Worker()
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                executor.submit(self.cam_listener, pipeline, event)

    def alg_store(queue, event):
        """
            takes the information captured by the ocr thread,
            and runs it through Dr. Busell's algorithm
        """
        while not event.is_set() or not queue.empty():
            message = queue.get()
            update_label(message)

            #if len(message_list) < 5:
            #    message_list.append(message)
                #logging.info("alg_store is active: %f", message)
            #else:
                #logging.info("alg_store is active")
            #    if len(len_list) == 51:
            #        event.set()
            #    logging.info("run through the algorithm: %s",message_list)
            #    algThread = threading.Thread(target=patient_instance.converter, args=(message_list,))
            #    algThread.start()
            #    algThread.join()
            #    message_list.clear()
            #    len_list.append("i")
            #    message_list.append(len(len_list))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.confirmButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.skipButton.setText(QCoreApplication.translate("MainWindow", u"Skip Vessel", None))
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.dataShowLabel.setText("")
        self.vesselNameLabel.setText(QCoreApplication.translate("MainWindow", u"Press Skip to Begin", None))
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
   

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = MainWindow()
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    patient_instance = vm.Vessel_math("DavidsonLiam")


    def update_label(message):
        value_2_show = str(message)
        ui.dataShowLabel.setText(value_2_show)
    ui.show()
    sys.exit(app.exec())
