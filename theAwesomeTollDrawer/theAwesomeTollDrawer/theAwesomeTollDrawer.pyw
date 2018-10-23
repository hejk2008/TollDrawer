# coding:utf-8
import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from theAwesomeTollDrawer_form import Ui_Form

def loadList(klassNumber):
    global fp
    fp=[]
    with open('Class'+str(klassNumber)+'.txt') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            if len(line) == 3:
                line = line[0] + ' ' + line[1]
            fp.append(line.strip())
        f.close()


class mywindow(QtWidgets.QWidget,Ui_Form):    
    def __init__(self):
        global stdNumber
        super(mywindow,self).__init__()    
        self.setupUi(self)
        self.student.setText('')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.draw)

    def draw(self):
        global stdList
        try:
            self.student.setText(str(random.choice(stdList)))
        except(IndexError):
            self.statusLabel.setText('<font color=black>已停止</font>')

    def drawStart(self):
        global stdList, fp
        stdList = []
        if self.klass1.isChecked() or self.klass2.isChecked() or self.klass3.isChecked():
            if self.klass1.isChecked():
                loadList(1)
                stdList += fp
            if self.klass2.isChecked():
                loadList(2)
                stdList += fp
            if self.klass3.isChecked():
                loadList(3)
                stdList += fp
            #print(stdList)
            self.statusLabel.setText('<font color=green>运行中</font>')
            self.timer.start(10)

    def drawStop(self):
        self.timer.stop()
        self.statusLabel.setText('<font color=black>已停止</font>')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

