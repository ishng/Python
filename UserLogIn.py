import sys 
from PyQt5.QtWidgets import *
class MainWindow (QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize (250,50)
        MainWidget = QWidget()
        Layout = QFormLayout()
        MainWidget.setLayout(Layout)
        self.setCentralWidget(MainWidget)
        self.UserLineEdit = QLineEdit()
        self.PassLineEdit = QLineEdit()
        self.submitButton = QPushButton("Submit")
        self.CancelButton = QPushButton("Cancel")
        Layout.addRow(QLabel("Username: "), self.UserLineEdit)
        Layout.addRow(QLabel("Password: "), self.PassLineEdit)
        Layout.addRow(self.submitButton, self.CancelButton)
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    app.exec()
