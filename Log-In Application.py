import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Data():
    def __init__(self):
        self.mydict = {"Patricia":"2005"}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.Fixedsize(350, 50)
        self.MainWidget = QWidget()
        self.Layout = QFormLayout()
        self.MainWidget.setLayout(self.Layout)
        self.setCentralWidget(self.MainWidget)
        self.UserLineEdit = QLineEdit()
        self.PassLineEdit = QLineEdit()

        self.PassLineEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Submit")
        self.CancelButton = QPushButton("Cancel")
        self.Layout.addRow(QLabel("USERNAME: "), self.UserLineEdit)
        self.Layout.addRow(QLabel("PASSWORD: "), self.PassLineEdit)
        self.Layout.addRow(self.submitButton, self.CancelButton)
        self.submitButton.clicked.connect(self.LogIn)
        
    def LogIn(self):
        username = self.UserLineEdit.text()
        password = self.PassLineEdit.text()
        if username in data_item.mydict and password == dataitem.dict[username]:

            if not self.Label.isVisible():
                self.Label = QLabel("Log In Successfully!!",self)
                self.Label.setAlignment(Qt.AlignCenter)
                self.Layout.addRow(self.Label)
            else :
                if not self.Label.isVisible():
                    self.Label = QLabel("Incorrect Username or Password. Please Try Again.", self)
                     self.Label.setAlignment(Qt.AlignCenter)
                    self.Layout.addRow(self.Label)

        if __name__ == '__main__':
            app = QApplication(sys.argv)
            main = MainWindow()
            app.exec()
