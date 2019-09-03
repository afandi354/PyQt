from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class OtherForm(QWidget):
   def __init__(self):
      super().__init__()
      self.setupUi()
      
   def setupUi(self):
      self.resize(400, 300)
      self.move(500, 100)
      self.setWindowTitle('Form Pendaftaran')
      self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
      
      self.judul = QLabel()
      self.judul.setText('<p align=center><b>Pendaftaran Calon Anggota Avengers</b></p>')

      self.namaLabel = QLabel('Nama')
      self.namaText = QLineEdit()

      self.kelaminLabel = QLabel('Jenis Kelamin')
      self.laki2Button = QRadioButton()
      self.laki2Button.setText('Laki-Laki')
      self.perempuanButton = QRadioButton()
      self.perempuanButton.setText('Perempuan')

      self.tglLabel = QLabel('Tanggal Lahir')
      self.tglLahir = QDateEdit()
      self.tglLahir.setDisplayFormat('dd/MM/yyyy')
      self.tglLahir.setDate(QDate.currentDate())

      self.hobiLabel = QLabel('Hobi')
      self.hobiCombo = QComboBox()
      self.hobiCombo.setEditable(False)
      self.hobiCombo.addItems(['basket', 'sepak bola', 'voli', 'catur', 'lainnya'])

      self.alamatLabel = QLabel('Alamat')
      self.alamatText = QTextEdit()
      self.alamatText.insertPlainText('Masukan alamat anda')

      self.submit = QPushButton('Submit')
      self.cancel = QPushButton('Cancel')

      layout1 = QHBoxLayout()
      layout1.addWidget(self.submit)
      layout1.addWidget(self.cancel)
      #self.setLayout(layout1)

      layout = QGridLayout()
      layout.addWidget(self.judul, 0, 0, 1, 2)
      layout.addWidget(self.namaLabel, 2,0)
      layout.addWidget(self.namaText, 2,1)
      layout.addWidget(self.kelaminLabel, 3,0)
      layout.addWidget(self.laki2Button, 3,1)
      layout.addWidget(self.perempuanButton, 4,1)
      layout.addWidget(self.tglLabel, 5,0)
      layout.addWidget(self.tglLahir, 5,1)
      layout.addWidget(self.hobiLabel, 6,0)
      layout.addWidget(self.hobiCombo, 6,1)
      layout.addWidget(self.alamatLabel, 7,0)
      layout.addWidget(self.alamatText, 7,1)
      layout.addLayout(layout1, 8,1)
      self.setLayout(layout)
      
      self.submit.clicked.connect(self.submitClicked)
      self.cancel.clicked.connect(self.close)

   def kelamin(self):
      if self.laki2Button.isChecked():
         return "Laki-Laki"
      else:
         return "Perempuan"

   def submitClicked(self):
      QMessageBox.information(self, 'Pendaftaran Berhasil', 
         'Nama : ' + self.namaText.text() + '\n' +
         'Jenis Kelamin : ' + self.kelamin() + '\n' +
         'Tanggal Lahir : ' + self.tglLahir.dateTime().toString() + '\n' +
         'Hobi : ' + self.hobiCombo.currentText() + '\n' +
         'Alamat : ' + self.alamatText.toPlainText())
