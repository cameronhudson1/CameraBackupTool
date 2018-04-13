import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class CameraBackup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): #lmao love you

        #################################################################
        # Initialize layouts
        #################################################################
        mainLayout = QHBoxLayout()
        leftSide = QVBoxLayout()
        rightSide = QVBoxLayout()




        #################################################################
        # Add to Left Side
        #################################################################
        cloudIntegrationCheck = QtWidgets.QCheckBox("Cloud Integration")
        visionAIIntegrationCheck = QtWidgets.QCheckBox("Sort Photos")
        leftSide.addWidget(cloudIntegrationCheck)
        leftSide.addWidget(visionAIIntegrationCheck)



        #################################################################
        # Add to right side
        #################################################################
        testButton = QPushButton("Test")
        criticalButtons = QGroupBox()
        applySettingsButton = QtWidgets.QPushButton("Apply Settings")
        backupCameraButton = QtWidgets.QPushButton("Backup")
        rightSide.addWidget(testButton)
        applyRunButtons = QHBoxLayout()
        applyRunButtons.addWidget(applySettingsButton)
        applyRunButtons.addWidget(backupCameraButton)
        criticalButtons.setLayout(applyRunButtons)



        #################################################################
        # Add sub layouts to parents
        #################################################################
        rightSide.addWidget(criticalButtons)
        mainLayout.addLayout(leftSide)
        mainLayout.addLayout(rightSide)



        #################################################################
        # Display main layout
        #################################################################
        self.setLayout(mainLayout)
        self.setWindowTitle("Camera Backup Tool")
        self.setGeometry(400, 400, 1000, 300)          # setGeometry(xOffset, yOffset, Width, Height)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CameraBackup()
    sys.exit(app.exec_())
