from __future__ import unicode_literals

import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # self.fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)
        #
        # self.compute_initial_figure()
        #
        # self.setParent(parent)
        #
        # # FigureCanvas.setSizePolicy(self,
        # #                            QtWidgets.QSizePolicy.Expanding,
        # #                            QtWidgets.QSizePolicy.Expanding)
        # # FigureCanvas.updateGeometry(self)

        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.compute_initial_figure)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.toolbar)
        self.setLayout(layout)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        # data = 10 * np.random.rand(100, 100)
        #
        # ax = self.fig.add_subplot(111)
        # ax.imshow(data)
        #
        # def format_coord(x, y):
        #     col = int(x + 0.5)
        #     row = int(y + 0.5)
        #     return 'x={}, y={}'.format(col, row)
        #
        # ax.format_coord = format_coord
        # self.canvas.draw()
        pass


class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(sc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        # QtWidgets.QMessageBox.about(self, "About")
        pass

# qApp = QtWidgets.QApplication(sys.argv)
# aw = ApplicationWindow()
# aw.show()
# sys.exit(qApp.exec_())
