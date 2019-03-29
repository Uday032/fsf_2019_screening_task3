import sys
import openpyxl
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Details_about_steel import Item_Detail
import sqlite3
from sqlite3 import Error


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Steel table"
        # self.width = 440
        # self.height = 280
        self.initUI()

    @pyqtSlot()
    def select_all_tasks(self,conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT Id,Designation FROM Angles")

        rows = cur.fetchall()
        for i in range(len(rows)):
            k = list(rows[i])
            rows[i]= k

        self.row = rows


    @pyqtSlot()
    def create_connection(self,db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None

    def db(self):
        # create a database connection
        self.conn = self.create_connection("steel_sections.sqlite")
        with self.conn:
            self.select_all_tasks(self.conn)



    def initUI(self):

        self.setWindowTitle(self.title)
        self.showFullScreen()

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.db()

        Main_vertical_layout = QVBoxLayout()
        Main_vertical_layout.setSpacing(20)

        Horizontal_Heading_layout = QHBoxLayout()

        Heading_name = QLabel("Steel Database",self)

        Horizontal_Heading_layout.addWidget(Heading_name)
        Horizontal_Heading_layout.setAlignment(Qt.AlignCenter)

        Table_Layout = QVBoxLayout()

        Horizontal_steel_heading_layout = QHBoxLayout()
        Horizontal_steel_heading_layout.setSpacing(20)

        Select = QLabel("Id",self)
        Designation_heading = QLabel("Designation",self)

        Horizontal_steel_heading_layout.addWidget(Select)
        Horizontal_steel_heading_layout.addWidget(Designation_heading)

        Table_Layout.addLayout(Horizontal_steel_heading_layout)

        # Create a button group for radio buttons
        self.radio_group_box = QGroupBox()
        self.radio_button_group = QButtonGroup()
        self.radio_button_list=[]
        counter=1

        for i in range(len(self.row)):

            Horizontal_layout= QHBoxLayout()
            Horizontal_layout.setSpacing(20)

            self.Radio_Button = QRadioButton(str(self.row[i][0]),self)
            Designation = QLabel(str(self.row[i][1]),self)

            self.radio_button_list.append(self.Radio_Button)
            self.radio_button_group.addButton(self.Radio_Button)
            self.radio_button_group.setId(self.Radio_Button,counter)
            counter = counter+1

            # self.Radio_Button.clicked.connect(self.OnClick,self.Radio_Button.text())
            # # self.mood_button_group.addButton(Radio_Button, i)
            # # Radio_Button.clicked.connect(Radio_Button, self.radio_button_clicked)
            #
            # if(Radio_Button.isChecked()):
            #     print(Radio_Button.text())

            # print(Id.text())
            Horizontal_layout.addWidget(self.Radio_Button)
            Horizontal_layout.addWidget(Designation)

            Table_Layout.addLayout(Horizontal_layout)

        self.radio_button_list[0].setChecked(True)
        Table_Layout.setAlignment(Qt.AlignCenter)

        Change_Page_Button_layout = QHBoxLayout()
        Change_Page_Button_layout.setSpacing(20)

        Home_Button = QPushButton('Go to Home',self)
        Get_more_details  = QPushButton("Get More Details", self)

        Change_Page_Button_layout.addWidget(Home_Button)
        Change_Page_Button_layout.addWidget(Get_more_details)

        Change_Page_Button_layout.setAlignment(Qt.AlignCenter)


        Main_vertical_layout.addLayout(Horizontal_Heading_layout)
        Main_vertical_layout.addLayout(Table_Layout)
        Main_vertical_layout.addLayout(Change_Page_Button_layout)

        self.setLayout(Main_vertical_layout)

        Get_more_details.clicked.connect(self.selected_button)


        self.show()



    @pyqtSlot()
    def selected_button(self):
        self.Details = Item_Detail(self.radio_button_group.checkedId())
        print(self.radio_button_group.checkedId())







def main():
    app = QApplication(sys.argv)
    ex = Table()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
