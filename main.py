import sys
from PyQt5 import QtWidgets
import product_table
import mysql.connector

# подключение БД
connect = mysql.connector.connect(user="root", password="Anastasiia!27", host="127.0.0.1", database="vista")
cursor = connect.cursor(buffered=True)

add_value = ("INSERT INTO services VALUES (%(0)s, %(1)s, %(2)s, %(3)s)")

# вытаскиваем данные из БД
cursor.execute("SELECT * FROM services")
rows = cursor.fetchall()


class ExampleApp(QtWidgets.QMainWindow, product_table.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # клдичество строк и столбцов
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(50)

        # подгонка размера ширины колонок в таблице
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


        # привязка кнопки к вызову функции очистить
        self.button2.clicked.connect(self.clear)

        # привязка кнопки к функции записать все данные в ДБ
        self.button1.clicked.connect(self.save_data)

        self.tableWidget.setHorizontalHeaderLabels(
            ('Название', 'Цена', 'Ссылка', 'Примечание')
        )
        row = 0
        for dict in rows:
            col = 0
            for item in dict:
                cellinfo = QtWidgets.QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    def clear(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            ('Название', 'Цена', 'Ссылка', 'Примечание')
        )

    def save_data(self):
        # удаляем всё из БД
        cursor.execute("DELETE FROM services")

        # записываем всё
        cash = {}
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                try:
                    cash[str(j)] = self.tableWidget.item(i, j).text()
                    if j == 3:
                        cursor.execute(add_value, cash)
                except:
                    break

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

connect.commit()