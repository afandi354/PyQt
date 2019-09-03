import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from OtherForm import *

class UAS(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(300, 300)
      self.setWindowTitle('UAS Pemograman GUI')
      self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

      self.label1 = QLabel('Nama')
      self.lineEdit = QLineEdit()
      
      self.label2 = QLabel('Alamat')
      self.textEdit = QTextEdit()
      
      self.label3 = QLabel('Umur')
      self.spinBox = QSpinBox()

      self.button1 = QPushButton('Submit')
      self.button2 = QPushButton('Clear')

      tombol = QHBoxLayout()
      tombol.addWidget(self.button1)
      tombol.addWidget(self.button2)

      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.lineEdit, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.textEdit, 1, 1)
      layout.addWidget(self.label3, 2, 0)
      layout.addWidget(self.spinBox, 2, 1)
      layout.addLayout(tombol, 3,1)
      self.setLayout(layout)


if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = UAS()
   form.show()
   
   a.exec_()