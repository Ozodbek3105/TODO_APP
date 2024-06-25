from PySide6.QtWidgets import QApplication

from backend_code import  MyTODO

app = QApplication()
window = MyTODO()
window.show()
app.exec()