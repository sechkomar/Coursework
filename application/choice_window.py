import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from test import set_style


class App(QDialog):

    def __init__(self):
        super().__init__()

        self.okButton = QPushButton("OK")
        self.title = 'Choose fields types'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox()
        data_layout = QGridLayout()
        data_layout.setColumnStretch(1, 4)
        data_layout.setColumnStretch(10, 10)

        fields = ['time', 'duration', 'source_ip', 'dest_ip', 'source_port', 'dest_port',
                  'protocol', 'tsp_flags', 'tos', 'smth', 'packets_sent', 'bytes_sent', 'verdict']

        boxes = {}

        data_layout.addWidget(QLabel("Choose type of fields and fields to skip:"))
        for i, field in enumerate(fields):
            boxes[i] = QComboBox()
            boxes[i].addItems(['continuous', 'discrete', 'skip'])
            data_layout.addWidget(boxes[i], i + 1, 1)

            label = QLabel()
            label.setText(field)
            data_layout.addWidget(label, i + 1, 0)

        data_layout.addWidget(self.okButton, len(fields) + 2, 2)
        self.horizontalGroupBox.setLayout(data_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    set_style(app)
    ex = App()
    sys.exit(app.exec_())
