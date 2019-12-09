from MyFunctions import getImg, callYolo
import sys
import requests
import os
import shutil
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QLineEdit, QLabel, QLCDNumber

class WinForm(QWidget):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Find Utility Pole')
        self.Run = QPushButton('Run', self)
        self.Run.setGeometry(250, 100, 80, 40)
        self.Run.setStyleSheet("background-color: green")
        self.Run.clicked.connect(self.run)

        self.Inf = QLabel(self)
        self.Inf.move(40, 40)
        self.Inf.resize(200, 40)
        self.Inf.setText('Please type in the location')


        self.Inline = QLineEdit(self)
        self.Inline.move(40,100)
        self.Inline.resize(200,40)

#        self.Outline = QLCDNumber(self)
#        self.Outline.move(90,170)
#        self.Outline.resize(150,80)
#        self.Outline.setDigitCount(2)
#        self.Outline.display(00)

        self.Run.setDisabled(True)
        self.Inline.textChanged.connect(self.disableRun)

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
        
        	a = float(intxt[0])
        	b = float(intxt[1])
        	find([a,b])

        	
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