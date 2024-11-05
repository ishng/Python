# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:21:47 2024

@author: Administrator
"""

import sys 
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Info():
    def __init__(self):
        self.dictionary = {"Tricia":"05052005"}





class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize (300,150)
        MainWidget = QWidget()
        self.Layout = QFormLayout()
        MainWidget.setLayout(self.Layout)
        self.setCentralWidget(MainWidget)
        self.UserLineEdit = QLineEdit()
        self.PassLineEdit = QLineEdit()
        self.PassLineEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Submit")
        self.CancelButton = QPushButton("Cancel")
        self.Layout.addRow(QLabel("Username: "), self.UserLineEdit)
        self.Layout.addRow(QLabel("Password: "), self.PassLineEdit)
        self.Layout.addRow(self.submitButton, self.CancelButton)
        self.submitButton.clicked.connect(self.LogIn)
        self.label = QLabel()
        self.label.hide()

    def LogIn(self):
        info_item = Info()
        
        username = self.UserLineEdit.text()
        password = self.PassLineEdit.text()

        if username in info_item.dictionary and password == info_item.dictionary[username]:
            if not self.label.isVisible():
                self.label = QLabel("Login Successfully!",self)
                self.label.setAlignment(Qt.AlignCenter)
                self.Layout.addRow(self.label)
               
        else:
            if not self.label.isVisible():
                self.label = QLabel("Incorrect Username or Password. Please Try Again ",self)
                self.label.setStyleSheet("Color: RED")
                self.label.setAlignment(Qt.AlignCenter)
                self.Layout.addRow(self.label)
             
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    app.exec()