from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
import serial
import pywinstyles

dark_stylesheet = """
    QMainWindow {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QLabel {
        color: #ffffff;
    }
    QWidget {
        background-color: #2b2b2b;
    }
    QMenuBar {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QMenuBar::item {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QMenuBar::item::selected {
        background-color: #3b3b3b;
    }
    QMenu {
        background-color: #2b2b2b;
        color: #ffffff;
    }
    QMenu::item::selected {
        background-color: #3b3b3b;
    }
    QPushButton {
        background-color: #3b3b3b;
        color: #ffffff;
        border: 1px solid #ffffff;
        padding: 5px;
    }
    QPushButton::hover {
        background-color: #4b4b4b;
    }
    QPushButton::pressed {
        background-color: #5b5b5b;
    }
    """

def Serial_Port_Connect():
    try:
        ser = serial.Serial(
        port='COM20',\
        baudrate=460800,\
        parity=serial.PARITY_EVEN,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS)
        if ser.is_open:
            print("connected to: " + ser.portstr)
    except serial.SerialException as e:
        print(f"Error opening or communicating through serial port: {e}")



app = QApplication(sys.argv)

window = QMainWindow()
pywinstyles.apply_style(window,"dark")
window.setWindowTitle("Shahrokh Tester")

Connect_btn = QPushButton()
Connect_btn.setText("Connect")
window.setCentralWidget(Connect_btn) 
Connect_btn.clicked.connect(Serial_Port_Connect)

window.show()
app.setStyleSheet(dark_stylesheet)
app.exec()