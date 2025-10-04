# PyQt5 GUI intro
# PyQt5 labels 🏷️
# PyQt5 images 📷
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets.QWidget import setStyleSheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(300, 300, 400, 400)
        self.setWindowIcon(QIcon('warehouse.png'))
        self.initUI()

        def initUI(self):
            self.button1 = QPushButton("Click Me!", self)
            self.button.setGeometry(150, 200, 200, 100)
            self.button = setStyleSheet("font-size: 30px;")
            self.button.clicked.connect(self.on_click)

        def on_click(self):
            print("clicked")
            self.button.setText("Click Me!")



        label = QLabel("Hello", self)
        label.setFont(QFont('Arial', 30))
        label.setGeometry(20, 20, 200, 200)
        label.setStyleSheet("color : #EBEB03;"
                            "background-color: #03EBDC;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignBottom)
        label.setAlignment(Qt.AlignCenter)

        label = QLabel(self)
        label.setGeometry(20, 80, 200, 200)

        pixmap = QPixmap("warehouse.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        label.setGeometry(self.width(),0, label.width(), label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
