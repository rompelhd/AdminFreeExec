import sys
import os
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QCheckBox, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont
from update import check_update_applicationfor_update, result_update, update_application, CURRENT_VERSION, LATEST_VERSION
from debug import debug_print

CONFIG_FILE = 'config.json'

class DragDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AdminFreeExec')
        self.setGeometry(100, 100, 500, 250)

        self.dark_mode = False
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.load_config()
        self.init_main_screen()

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                config = json.load(file)
                self.dark_mode = config.get('dark_mode', False)
    
    def save_config(self):
        config = {
            'dark_mode': self.dark_mode,
        }
        with open(CONFIG_FILE, 'w') as file:
            json.dump(config, file)

    def init_main_screen(self):
        self.clear_layout()

        self.top_layout = QHBoxLayout()
        self.settings_button = QPushButton('⚙', self)
        self.settings_button.setFixedSize(30, 30)
        self.settings_button.setStyleSheet("font-size: 18px; border: none;")
        self.settings_button.clicked.connect(self.show_settings_screen)
        self.top_layout.addWidget(self.settings_button)
        
        if result_update():
            self.update_button = QPushButton('🔄', self)
            self.update_button.setFixedSize(30, 30)
            self.update_button.setStyleSheet("font-size: 18px; border: none;")
            self.update_button.setToolTip("Update available")
            self.update_button.clicked.connect(self.show_update_screen)
            self.top_layout.addWidget(self.update_button)
        
        self.top_layout.addStretch()

        self.layout.addLayout(self.top_layout)

        self.center_layout = QVBoxLayout()

        self.label = QLabel('Arrastra un archivo aquí', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Arial", 14))

        self.center_layout.addWidget(self.label)

        self.layout.addStretch()
        self.layout.addLayout(self.center_layout)
        self.layout.addStretch()

        self.bottom_layout = QVBoxLayout()
        
        self.button = QPushButton('Seleccionar archivo', self)
        self.button.clicked.connect(self.open_file)
        self.bottom_layout.addWidget(self.button)

        self.version_credit_layout = QHBoxLayout()

        self.credit_label = QLabel("AdminFreeExec v" + CURRENT_VERSION + " by Rompelhd", self)
        self.credit_label.setFont(QFont("Arial", 10))
        self.credit_label.setAlignment(Qt.AlignRight)

        self.version_credit_layout.addStretch()
        self.version_credit_layout.addWidget(self.credit_label)

        self.bottom_layout.addLayout(self.version_credit_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        self.layout.addLayout(self.bottom_layout)

        self.apply_theme()

    def show_settings_screen(self):
        self.clear_layout()

        self.dark_mode_checkbox = QCheckBox("Modo Oscuro", self)
        self.dark_mode_checkbox.setFont(QFont("Arial", 12))
        self.dark_mode_checkbox.setChecked(self.dark_mode)

        self.settings_top_layout = QVBoxLayout()
        self.settings_top_layout.addWidget(self.dark_mode_checkbox)

        self.button_layout = QHBoxLayout()

        self.save_button = QPushButton("Guardar", self)
        self.save_button.setFont(QFont("Arial", 12))
        self.save_button.clicked.connect(self.save_settings)

        self.discard_button = QPushButton("Descartar", self)
        self.discard_button.setFont(QFont("Arial", 12))
        self.discard_button.clicked.connect(self.init_main_screen)

        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.discard_button)

        self.version_credit_layout = QHBoxLayout()

        self.credit_label = QLabel("AdminFreeExec v" + CURRENT_VERSION + " by Rompelhd", self)
        self.credit_label.setFont(QFont("Arial", 10))
        self.credit_label.setAlignment(Qt.AlignRight)

        self.version_credit_layout.addStretch()
        self.version_credit_layout.addWidget(self.credit_label)

        self.settings_bottom_layout = QVBoxLayout()
        self.settings_bottom_layout.addLayout(self.button_layout)
        self.settings_bottom_layout.addLayout(self.version_credit_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addLayout(self.settings_top_layout)
        self.layout.addItem(spacer)
        self.layout.addLayout(self.settings_bottom_layout)

        self.apply_theme()

    def show_update_screen(self):
        self.clear_layout()

        self.update_layout = QVBoxLayout()
        self.update_label = QLabel(f"¡Nueva actualización disponible a la versión {LATEST_VERSION}!", self)
        self.update_label.setAlignment(Qt.AlignCenter)
        self.update_label.setFont(QFont("Arial", 14))
        self.update_layout.addWidget(self.update_label)

        self.layout.addStretch()
        self.layout.addLayout(self.update_layout)
        self.layout.addStretch()
        
        self.button_layout = QHBoxLayout()

        self.update_button = QPushButton("Actualizar", self)
        self.update_button.setFont(QFont("Arial", 12))
        self.update_button.clicked.connect(update_application)

        self.discard_button = QPushButton("Atrás", self)
        self.discard_button.setFont(QFont("Arial", 12))
        self.discard_button.clicked.connect(self.init_main_screen)

        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.discard_button)

        self.layout.addLayout(self.button_layout)

        self.bottom_layout = QVBoxLayout()

        self.version_credit_layout = QHBoxLayout()

        self.credit_label = QLabel("AdminFreeExec v" + CURRENT_VERSION + " by Rompelhd", self)
        self.credit_label.setFont(QFont("Arial", 10))
        self.credit_label.setAlignment(Qt.AlignRight)

        self.version_credit_layout.addStretch()
        self.version_credit_layout.addWidget(self.credit_label)

        self.bottom_layout.addLayout(self.version_credit_layout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        self.layout.addLayout(self.bottom_layout)


    def save_settings(self):
        self.dark_mode = self.dark_mode_checkbox.isChecked()
        self.save_config()
        self.init_main_screen()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Seleccionar un archivo', "", "Ejecutables (*.exe)")
        if file_path:
            self.label.setText(f"Archivo seleccionado: {file_path}")
            self.run_as_invoker(file_path)

    def run_as_invoker(self, exe_path):
        exe_path = f'"{exe_path}"'
        os.system(f'cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start \"\" {exe_path}\"')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls and urls[0].isLocalFile():
            file_path = urls[0].toLocalFile()
            self.label.setText(f"Archivo seleccionado: {file_path}")
            self.run_as_invoker(file_path)

    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.layout():
                self.clear_layout_recursive(item.layout())
            elif item.widget():
                item.widget().deleteLater()

    def clear_layout_recursive(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.layout():
                self.clear_layout_recursive(item.layout())
            elif item.widget():
                item.widget().deleteLater()

    def apply_theme(self):
        if self.dark_mode:
            self.setStyleSheet("background-color: #2E2E2E; color: white;")
        else:
            self.setStyleSheet("background-color: white; color: black;")

if __name__ == '__main__':
    check_update_applicationfor_update()

    app = QApplication(sys.argv)
    window = DragDropWindow()
    window.setAcceptDrops(True)
    window.show()
    app.aboutToQuit.connect(window.save_config)
    sys.exit(app.exec_())
