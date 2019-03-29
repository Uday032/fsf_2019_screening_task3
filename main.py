import sys
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "INTERNSHIP"
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        # self.showFullScreen()
        self.setGeometry(10,10,440,280)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)


        Heading_Box = QVBoxLayout()

        heading = QLabel("FOSSEE INTERNSHIP",self)
        Heading_Box.addWidget(heading)
        Heading_Box.setAlignment(Qt.AlignCenter)

        Image_Box = QHBoxLayout()

        layout_heading = QLabel("FOSSEE INTERNSHIP ",self)

        Image_Box.addWidget(layout_heading)
        Image_Box.setAlignment(Qt.AlignCenter)



        Vbox = QVBoxLayout()
        Vbox.setSpacing(20)
        Vbox.setContentsMargins(100,100,100,100)

        new_font = QFont("Times",20)

        Question_heading = QLabel('What you want to do? ', self)
        Question_heading.setFont(new_font)

        button1 = QRadioButton("Show Data",self)
        button2 = QRadioButton("Add Data",self)
        button1.setFont(new_font)
        button2.setFont(new_font)

        Vbox.addWidget(Question_heading)
        Vbox.addWidget(button1)
        Vbox.addWidget(button2)

        Vbox.setAlignment(Qt.AlignCenter)

        HBox = QHBoxLayout()
        HBox.addStretch(1)
        HBox.setAlignment(Qt.AlignCenter)
        HBox.addLayout(Vbox)
        Heading_Box.addLayout(HBox)
        Image_Box.addLayout(Heading_Box)

        button1.clicked.connect(self.run)
        button2.clicked.connect(self.run2)


        self.setLayout(Image_Box)
        self.show()

    @pyqtSlot()
    def run(self):
        print("button1")
    @pyqtSlot()
    def run2(self):
        print("button2")

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
