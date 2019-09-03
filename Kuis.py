import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from OtherForm import *

class Kuis(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(300, 100)
      self.move(300, 300)
      self.setWindowTitle('Kuis Pemograman GUI')
      self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

      self.label1 = QLabel('Username')
      self.lineEdit1 = QLineEdit()
      
      self.label2 = QLabel('Password')
      self.lineEdit2 = QLineEdit()
      self.lineEdit2.setEchoMode(QLineEdit.Password)
      
      self.button1 = QPushButton('Login')
      self.button2 = QPushButton('Clear')

      tombol = QHBoxLayout()
      tombol.addWidget(self.button1)
      tombol.addWidget(self.button2)

      layout = QGridLayout()
      layout.addWidget(self.label1, 0, 0)
      layout.addWidget(self.lineEdit1, 0, 1)
      layout.addWidget(self.label2, 1, 0)
      layout.addWidget(self.lineEdit2, 1, 1)
      layout.addLayout(tombol, 2,1)
      self.setLayout(layout)

      self.button1.clicked.connect(self.button1Click)
      self.button2.clicked.connect(self.button2Click)

   def button1Click(self):
      a = self.lineEdit1.text()
      b = self.lineEdit2.text()
      self.demoForm = OtherForm()
           
      if a == 'afandi' and b == 'nat':
         self.demoForm.show() 
         form.close()
      else:
         QMessageBox.information(self, 'Informasi', 'Login Salah' )

   def button2Click(self):
      self.lineEdit1.clear()
      self.lineEdit2.clear()

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = Kuis()
   form.show()
   
   a.exec_()