import sys
from PyQt5 import QtWidgets
import product_table

data = [(''),(),]

class ExampleApp(QtWidgets.QMainWindow, product_table.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(50)

        self.button2.clicked.connect(self.clear)

        self.tableWidget.setHorizontalHeaderLabels(
            ('Название', 'Цена', 'Ссылка', 'Примечание')
        )

    def clear(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ('Название', 'Цена', 'Ссылка', 'Примечание')
        )

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
