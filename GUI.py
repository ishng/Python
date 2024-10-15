import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class Main_Window (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setGeometry(100,60,1000,800)
        self.Label1=QLabel()
        self.Label1.setText("Hello World")
        self.setCentralWidget(self.Label1)
        self.Button=QPushButton("Press Me",self)
        self.Button.setFixedSize(100,20)
        self.Button.clicked.connect(self.ButtonMethod)
      
    def ButtonMethod(self):
        self.Label1.setText("HI!")

if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main_Window()
    main.show()
    app.exec()
