import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt_themes import fusion_dark

from browse_window import Ui_browseWindow


def set_style(app):
    # theme_palet = fusion_dark.FusionBlue()
    # theme_palet.set_app(app)

    app.setFont(QtGui.QFont("Noto Sans CJK TC Light", 11))
    pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    set_style(app)

    browseWindow = QtWidgets.QMainWindow()
    ui = Ui_browseWindow()
    ui.setupUi(browseWindow)
    browseWindow.show()
    sys.exit(app.exec_())