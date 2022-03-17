import sys

from PyQt5.QtWidgets import QApplication,QDesktopWidget
from PyQt5.QtWidgets import QLabel,QPushButton,QComboBox,QScrollArea,QDialog
from PyQt5.QtWidgets import QWidget,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout,QMessageBox
from PyQt5.QtGui import QIntValidator,QDoubleValidator
from PyQt5 import QtCore
from generate import Generate_data
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
##################### GUI ######################################
row,col = 1,0 #control row numbers
columns = {} #all columns
def col_message(error, error_type,info):
    column_name_error = QMessageBox()
    column_name_error.setIcon(QMessageBox.Information)
    column_name_error.setWindowTitle(error_type)
    column_name_error.setText(error)
    column_name_error.exec()

def addColumn(label,data_length,option,layout_3):
    global row,col,columns
    column = QLabel(label.text())
    if label.text() in columns.keys() or not label.text() or not data_length.text():
        if not label.text():
            col_message("Column name empty !",'Column Error','Critical')
            return None
        if not data_length.text():
            col_message("Column length empty !",'Column Error','Critical')
            return None
        col_message("Column name already exists !",'Column Error','Critical')
        return None
    data_type = QLabel(option.currentText())
    length = QLabel(data_length.text())
    layout_3.addWidget(column,row,col)
    layout_3.addWidget(data_type,row,col+1)
    layout_3.addWidget(length,row,col+2)
    row+=1
    columns[label.text()]=[option.currentText(),data_length.text()]

def genCsv(columns,number_rows):
    if not columns:
        col_message("Column List empty !",'Column Error','Critical')
        return None
    with ProcessPoolExecutor() as exe:
        exe.submit(Generate_data.data_generate(columns,int(number_rows.text())))
        col_message('Completed','Done','Information')
    return None

def main_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Dummy Data Generator')
    screen = app.primaryScreen()
    size = screen.size()

    window.setFixedSize(int(size.width()/2), int(size.height()/2))
    window.move(int(size.width()/4),200)

    layout_1 = QVBoxLayout()
    window.setLayout(layout_1)


    layout_1.setSpacing(4)
    label = QLineEdit()
    option = QComboBox()
    option.addItems(["String", "Integer", "Float","Boolean"])
    data_length = QLineEdit()
    data_length.setValidator(QIntValidator())

    btn = QPushButton('Add')
    btn.clicked.connect(lambda:addColumn(label,data_length,option,layout_3))  

    btn_gen = QPushButton('Generate (CSV)')
    btn_gen.clicked.connect(lambda:genCsv(columns,number_rows))

    scrollArea = QScrollArea()
    scrollArea.setWidgetResizable(True)
    scrollAreaWidgetContents = QWidget()
    layout_3 = QGridLayout(scrollAreaWidgetContents)
    scrollArea.setWidget(scrollAreaWidgetContents)
    layout_1.addWidget(scrollArea)
    scrollArea.setStyleSheet('background-color: white;')


    main_row = QWidget()
    layout_2 = QGridLayout(main_row)

    layout_2.addWidget(QLabel("Column Name"),0,1)
    layout_2.addWidget(label,1,1)
    layout_2.addWidget(QLabel("Data Type"),0,2)
    layout_2.addWidget(option,1,2)
    layout_2.addWidget(QLabel("Length"),0,3)
    layout_2.addWidget(data_length,1,3)
    layout_2.addWidget(btn,1,4)
    layout_2.addWidget(QLabel("Number Of Rows"),2,1)
    number_rows=QLineEdit('20')
    layout_2.addWidget(number_rows,3,1)
    layout_2.addWidget(btn_gen,3,2,1,4)
    layout_1.addWidget(main_row)


    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    multiprocessing.freeze_support()
    main_window()
#pyinstaller.exe --onefile --windowed app.py