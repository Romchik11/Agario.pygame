from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout

class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.name = None
        self.port = None
        self.host = None

        self.resize(1000, 1000)
        self.setWindowTitle('Agar.io Launcher')

        v_line = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Введіть ваше ім`я')
        v_line.addWidget(self.name_input)

        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText('Введіть ip сервера')
        v_line.addWidget(self.host_input)

        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText('Введіть port сервера')
        v_line.addWidget(self.port_input)

        self.btn = QPushButton('Приєднатися')
        self.btn.clicked.connect(self.join_server)
        v_line.addWidget(self.btn)

        self.setLayout(v_line)

    def join_server(self):
        self.name = self.name_input.text()
        self.port = self.port_input.text()
        self.host = self.host_input.text()

        self.close()
