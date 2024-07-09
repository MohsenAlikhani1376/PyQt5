from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QToolBar,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QSplitter , QSpacerItem, QSizePolicy,  QComboBox
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QRect
from PyQt5.QtCore import Qt
import serial.tools.list_ports

import pywinstyles

def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

class MainWindow(QMainWindow):
    def __init__(self, app): 
        super().__init__()
        self.app = app
        self.setWindowTitle("Shahrokh FOG Test")
        pywinstyles.apply_style(self,"dark")
        
        self.setGeometry(100, 100, 700, 500)

        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        # Create a top-level splitter
        top_splitter = QSplitter(Qt.Horizontal)

         # Create a top panel
        top_panel = QWidget()
        top_layout = QVBoxLayout()  # Use QVBoxLayout to add vertical spacing
        top_panel.setLayout(top_layout)

         # Create a container widget for horizontal buttons
        top_button_container = QWidget()
        top_button_layout = QHBoxLayout()
        top_button_container.setLayout(top_button_layout)

        # Create a combo box for serial ports
        combo_box = QComboBox(self)
        serial_ports = list_serial_ports()
        combo_box.addItems(serial_ports)
        # Style the combo box
        combo_box.setStyleSheet("""
            QComboBox {
                border: 1px solid gray;
                border-radius: 3px;
                padding: 7px 18px 6px 3px;
                min-width: 10em;
                background-color: #2d2d30;
                color: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: darkgray;
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }
            QComboBox::drop-down {
                width: 15px;  /* Adjust width to fit your icon */
                background-image: url(C:/Users/m.alikhani/Desktop/images.png);  /* Path to your arrow icon */
                background-repeat: no-repeat;
                background-position: center right;  /* Adjust position if needed */
                border-left: 1px solid darkgray;  /* Optional: Add a border for visual separation */
            }
            QComboBox QAbstractItemView {
                border: 1px solid gray;
                selection-background-color: #3d3d40;
                background-color: #2d2d30;
                color: white;
            }
        """)
        
        # Create three buttons
        connect_btn = QPushButton('Connect', self)
        Horizon_spacer = QSpacerItem(0, 0,QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Set fixed sizes for the combo box and connect button
        button_width = 100
        button_height = 30
        connect_btn.setFixedSize(button_width, button_height)
        combo_box.setFixedSize(button_width, button_height)

        # Add buttons to the top panel layout
        top_button_layout.addWidget(combo_box)
        top_button_layout.addItem(Horizon_spacer)
        top_button_layout.addWidget(connect_btn)

        # Add a vertical spacer to push the buttons up
        vertical_spacer = QSpacerItem(100, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        top_layout.addWidget(top_button_container)
        top_layout.addItem(vertical_spacer)

        # Add bottom panel to the splitter
        top_splitter.addWidget(top_panel)

        # Create a bottom-level splitter
        bottom_splitter  = QSplitter(Qt.Vertical)
        bottom_splitter.addWidget(top_splitter)

        # Create a bottom panel
        bottom_panel = QWidget()
        bottom_layout = QHBoxLayout()
        bottom_panel.setLayout(bottom_layout)

        # Create three buttons for the bottom panel
        bottom_btn1 = QPushButton('Bottom Button 1', self)
        bottom_btn2 = QPushButton('Bottom Button 2', self)
        bottom_btn3 = QPushButton('Bottom Button 3', self)

        # Add buttons to the bottom panel layout
        bottom_layout.addWidget(bottom_btn1)
        bottom_layout.addWidget(bottom_btn2)
        bottom_layout.addWidget(bottom_btn3)

        # Add bottom panel to the splitter
        bottom_splitter.addWidget(bottom_panel)

       # Add splitter to the main layout
        main_layout.addWidget(bottom_splitter)
        # Set the main widget layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
