from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys


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

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
app.setStyleSheet(dark_stylesheet)

app.exec()