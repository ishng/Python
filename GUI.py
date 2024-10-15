import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Main_Window (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(400,300)
        self.Label1=QLabel()
        self.Label1.setText("Hello World")
        self.Button=QPushButton("Press Me")
        self.Button.clicked.connect(self.ButtonMethod)
        self.setCentralWidget(self.Button)
    def ButtonMethod(self):
        self.Label1.setText("HI!")

if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    main.show()
    app.exec()
