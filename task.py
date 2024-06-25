import psycopg2
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from task_widget_ui import Ui_Form


class Task(QWidget, Ui_Form):
    delete_btn_click = Signal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.index = None
        self.delete_btn.clicked.connect(self.delete_btn_clicked)
        self.btn_is_checked.clicked.connect(self.change_style)

    def delete_btn_clicked(self):
        self.delete_btn_click.emit(self.index)

    def create_connection(self):
        database = 'TODO'
        user = 'postgres'
        password = 'Ozodbek04@'
        host = 'localhost'
        port = '5432'

        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

        return conn

    def change_style(self, event):
        connection = self.create_connection()
        cursor = connection.cursor()

        query = '''update todo_app set is_done=%s where (task=%s)'''

        cursor.execute(query, (event, self.lineEdit.text()))
        connection.commit()
        connection.close()