#pip install qrcode pillow yarl
import qrcode
from yarl import URL
import os, sys
from definitions import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtTest, QtCore


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
    
form = resource_path('qr_generator.ui')
form_class = uic.loadUiType(form)[0]


dir = '.'


def timer(n):
    QtTest.QTest.qWait(n*1000)


#main window
class mainWindow(QMainWindow, form_class):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.initUI()
        self.button_generate.clicked.connect(self.button_generate_clicked)                      #button_ok를 눌렀을 때 동작할 함수 연결
        self.button_directory.clicked.connect(self.directory)
        

    def initUI(self):
        self.setupUi(self)
        self.setGeometry(0, 0, 400, 200)
        self.setFixedSize(400, 200)

        flags = self.windowFlags()
        flags |= Qt.CustomizeWindowHint
        flags |= Qt.WindowTitleHint
        flags |= Qt.WindowSystemMenuHint
        flags |= Qt.WindowCloseButtonHint
        flags |= Qt.WindowStaysOnTopHint
        flags |= Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)


    def directory(self):
        global dir
        dialog = QFileDialog()
        dir = dialog.getExistingDirectory(self, "저장 경로 선택")
        print(dir)


    def button_generate_clicked(self):
        
        url = self.line_url.text()
        yarl_url = URL(url)
        host = yarl_url.host.split('.')[0]

        img_url = qrcode.make(url)
        img_url.save(f"{dir}/{host}.png")


        timer(1)
        self.label_finishtext.setText(f"QR코드를 \"{dir.split('/')[-1]}\" 에 \"{host}.png\" 로 저장했습니다.")

        timer(3)
        qApp.quit()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainWindow = mainWindow()
    widget.addWidget(mainWindow)
    widget.setFixedSize(400, 200)
    widget.show()
    app.exec_()