import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
                             QColorDialog, QApplication, QVBoxLayout)


class ColorDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.colorFrom = ''
        self.colorTo = ''
        self.initUI()

    def initUI(self):
        self.colorFromBtn = QPushButton('Color from', self)
        self.colorToBtn = QPushButton('Color to', self)

        self.colorFromBtn.clicked.connect(self.showFromDialog)
        self.colorToBtn.clicked.connect(self.showToDialog)

        self.fromFrame = QFrame(self)
        self.toFrame = QFrame(self)

        self.setGeometry(500, 300, 250, 350)

        self.okBtn = QPushButton('OK', self)
        self.okBtn.clicked.connect(self.setGradColors)

        layout = QVBoxLayout()
        layout.addWidget(self.colorFromBtn)
        layout.addWidget(self.fromFrame)
        layout.addWidget(self.colorToBtn)
        layout.addWidget(self.toFrame)
        layout.addWidget(self.okBtn)
        self.setLayout(layout)

        self.setWindowTitle('Colors dialog')
        self.show()

    def showFromDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.fromFrame.setStyleSheet("QWidget { background-color: %s }"
                                         % col.name())
            self.colorFrom = col.name()
        pass

    def showToDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.toFrame.setStyleSheet("QWidget { background-color: %s }"
                                       % col.name())
            self.colorTo = col.name()
        pass

    def setGradColors(self):
        with open('color.txt', 'w') as out:
            out.write('{} {}'.format(self.colorFrom, self.colorTo))

        self.close()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorDialog()
    sys.exit(app.exec_())
