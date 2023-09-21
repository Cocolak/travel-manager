import sys
from PyQt5 import QtWidgets
from SelectTravel import Ui_selectTravelWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_selectTravelWindow()
    ui.setupUi(window)

    screen = QtWidgets.QDesktopWidget().screenGeometry()
    x = (screen.width() - window.width()) // 2
    y = (screen.height() - window.height()) // 2
    window.move(x,y)

    window.show()
    sys.exit(app.exec_())
