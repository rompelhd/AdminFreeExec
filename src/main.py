import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

class DragDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AdminFreeExec')
        self.setGeometry(100, 100, 500, 250)

        self.label = QLabel('Arrastra un archivo aquí', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 20px;')

        self.button = QPushButton('Abrir archivo', self)
        self.button.clicked.connect(self.open_file)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Seleccionar un archivo')
        if file_path:
            self.label.setText(f"Archivo seleccionado: {file_path}")
            self.run_as_invoker(file_path)

    def run_as_invoker(self, exe_path):
        exe_path = f'"{exe_path}"'
        os.system(f'cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" {exe_path}"')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.label.setText(f"Archivo arrastrado: {file_path}")
        self.run_as_invoker(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.setAcceptDrops(True)
    window.show()
    sys.exit(app.exec_())
