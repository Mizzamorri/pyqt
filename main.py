from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from name import Ui_Dialog  # импорт нашего сгенерированного файла
import sys, pyowm


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setText("Не погода")
        self.ui.pushButton.clicked.connect(self.get_city)
        #hook
    def get_city(self):
        text = self.ui.textEdit.toPlainText()
        self.ui.label.setText(text)

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_F12:
            self.close


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())