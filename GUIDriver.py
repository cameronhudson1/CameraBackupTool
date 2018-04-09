import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout


class CameraBackup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout()

        btop = QtWidgets.QPushButton("Button1")
        cmid = QtWidgets.QCheckBox("Check Me Out!")

        mainLayout.addWidget(btop)
        mainLayout.addWidget(cmid)

        self.setLayout(mainLayout)
        self.setWindowTitle("Camera Backup Tool")
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CameraBackup()
    sys.exit(app.exec_())
