import sys
from PyQt5.QtWidgets import QApplication

from Kuis import *

if __name__ == '__main__':
   a = QApplication(sys.argv)
   
   form = Kuis()
   form.show()
   
   a.exec_()