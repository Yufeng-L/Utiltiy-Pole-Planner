from MyFunctions import getImg, callYolo, setMap
import sys
import requests
import os
import time
import shutil
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Find Utility Pole')
        self.Run = QPushButton('Run', self)
        self.Run.setGeometry(240, 300, 50, 40)
        self.Run.setStyleSheet("background-color: green")
        self.Run.clicked.connect(self.run)

        self.Inf = QLabel(self)
        self.Inf.move(20, 240)
        self.Inf.resize(200, 40)
        self.Inf.setText('Please type in the location')



        self.Inline = QLineEdit(self)
        self.Inline.move(20,300)
        self.Inline.resize(200,40)
        self.Inline.setText('42.393885, -71.123333') 
#        self.Outline = QLCDNumber(self)
#        self.Outline.move(90,170)
#        self.Outline.resize(150,80)
#        self.Outline.setDigitCount(2)
#        self.Outline.display(00)

        self.Run.setDisabled(False)
        self.Inline.textChanged.connect(self.disableRun)


        self.label = QLabel(self)
        self.pixmap = QPixmap('initial.png')
        self.label.setPixmap(self.pixmap)







    def disableRun(self):

        self.Run.setDisabled(True)

        for ele in self.Inline.text():
            if ele != ' ':
                self.Run.setDisabled(False)

        



    def run(self):
        intxt = self.Inline.text()
        intxt = intxt.split(',')
        print(intxt)
        if len(intxt) == 2:    
            try: 
                a = float(intxt[0])
                b = float(intxt[1])
                self.Inf.setText('Please waiting')
                setMap([a,b])

                pixmap = QPixmap('data/streetview/local_image.png')
                self.label.setPixmap(pixmap)
                find([a,b])
                print('picture changed')
                self.Inf.setText('Please type in the location')
            except:
                self.Inf.setText('location is like: 42.393885, -71.123333')
       	else:
       		self.Inf.setText('location is like: 42.393885, -71.123333')




def find(location):
    getImg(location)
    callYolo()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())