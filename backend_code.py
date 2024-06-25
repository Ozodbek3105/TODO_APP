import psycopg2
from PySide6.QtWidgets import QWidget, QListWidgetItem
from todo_widget_ui import Ui_TODO
from task import Task


class MyTODO(QWidget, Ui_TODO):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addTask_btn.clicked.connect(self.create_items)
        self.widget = Task()
        self.widget.delete_btn.clicked.connect(self.delete_clicked)
        self.load_data()

    def create_items(self):
        text = self.addTask_lineEdit.text()
        if text:
            item = QListWidgetItem()
            widget = Task()
            widget.delete_btn_click.connect(self.delete_clicked)
            widget.lineEdit.setText(text)
            item.setSizeHint(widget.sizeHint())
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)
            connection = self.create_connection()
            cursor = connection.cursor()
            query = '''
            insert into todo_app
            values (%s, %s, now())
            '''
            cursor.execute(query, (text, widget.btn_is_checked.isChecked()))
            connection.commit()
            connection.close()
            widget.index = self.tasks_listWidget.count() - 1
            print(widget.index)
            self.addTask_lineEdit.clear()

    def delete_clicked(self, row_index):
        # print(row_index)
        self.reindexing()
        # current_item = self.tasks_listWidget.currentItem()
        widget: Task = self.tasks_listWidget.itemWidget(self.tasks_listWidget.item(row_index))
        # row_index = widget.index
        self.tasks_listWidget.takeItem(row_index)
        connection = self.create_connection()
        cursor = connection.cursor()
        query = '''delete from todo_app where (task=%s)'''
        cursor.execute(query, (widget.lineEdit.text(),))
        connection.commit()
        connection.close()

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

    def reindexing(self):
        for row in range(self.tasks_listWidget.count()):
            item = self.tasks_listWidget.item(row)
            widget = self.tasks_listWidget.itemWidget(item)
            widget.index = row

    def load_data(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        query = '''select * from todo_app
                    order by date desc'''
        cursor.execute(query)

        data = cursor.fetchall()
        for task in data:
            item = QListWidgetItem()
            widget = Task()
            widget.delete_btn_click.connect(self.delete_clicked)
            widget.lineEdit.setText(task[0])
            widget.btn_is_checked.setChecked(task[1])
            item.setSizeHint(widget.sizeHint())
            self.tasks_listWidget.addItem(item)
            self.tasks_listWidget.setItemWidget(item, widget)
        self.reindexing()
