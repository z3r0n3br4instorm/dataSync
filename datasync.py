from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime
import threading
def run_adb_background():
    while True:
        os.system("""adb shell "su -c 'content query --uri content://call_log/calls'" > data.zttf&""")

adb_thread = threading.Thread(target=run_adb_background)
adb_thread.start()
# class Worker(QtCore.QObject):
#     data_received = QtCore.pyqtSignal(str)

#     def __init__(self):
#         super().__init__()

#     def get_input_data(self):
#         if True:
#             try:
#                 caller_data = open("data.zttf", "r").read()
#                 number = caller_data.split()[18].replace("number=", "").replace(",", "")
#                 self.data_received.emit(number)
#             except:
#                 print("An error occurred!")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 576)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "font: 10pt \"Noto Sans\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -130, 301, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo_new.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 421, 61))
        self.label_2.setStyleSheet("font: 75 28pt \"Calibri\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 271, 81))
        self.pushButton.setStyleSheet("color: rgb(141, 141, 141);\n"
                                       "font: 75 20pt \"Calibri\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 320, 271, 81))
        self.pushButton_2.setStyleSheet("color: rgb(141, 141, 141);\n"
                                         "font: 75 20pt \"Calibri\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 430, 271, 81))
        self.pushButton_3.setStyleSheet("color: rgb(141, 141, 141);\n"
                                         "font: 75 20pt \"Calibri\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(310, 90, 551, 431))
        self.textBrowser.setStyleSheet("font: 10pt \"Noto Sans\";\n"
                                        "color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(597, 550, 251, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_input_data)
        # self.timer.timeout.connect(self.run_adb_background)
        self.timer.start(0)
        self.pushButton.clicked.connect(self.open_log)
        # self.worker = Worker()
        # self.thread = QtCore.QThread()
        # self.worker.moveToThread(self.thread)
        #self.thread.started.connect(self.worker.get_input_data)
        #self.worker.data_received.connect(self.process_data)
        #elf.thread.start()
    def open_log(self):
        os.system("notepad log.txt&")
    def get_input_data(self):
        if True:
            try:
                caller_data = open("data.zttf", "r").read()
                number =caller_data.split()[18].replace("number=","").replace(",","")
            except:
                print("An error occurred!")
            try:
                check_test = open("log.txt","r").readlines()[-1].split()[0].strip()
                if check_test == number:
                    print("match")
                else:
                    print(number)
                    current_time = datetime.datetime.now()
                    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    test = open("log.txt","a")
                    write_data = "\n"+str(number)+" \t"+str(formatted_time)
                    self.textBrowser.append(write_data)
                    test.write(write_data)
                    print(write_data)
            except:
                print("bugskip")


    # def process_data(self, number):
    #     #print(number)
    #     #self.textBrowser.setText(number)
    #     check_data = open("log.txt","r").readlines()[0].strip()
    #     print(check_data)
    #     if check_data == "456":
    #             print("match_skip")
    #     else:
    #             print("non_match")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Zerone Laboratories - dataSync System"))
        self.label_2.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"right\"><span style=\" font-size:36pt; color:#ffffff;\">dataSync v1.2</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Dump Call Log"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset the connection"))
        self.pushButton_3.setText(_translate("MainWindow", "Check adb"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Waiting for office phone [Galaxy j3]...</p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IF ADB PROMPTED, PRESS YES...</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
