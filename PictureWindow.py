from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class PictureWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PictureWindow, self).__init__(parent)
        self.setFixedSize(1065, 695)
        self.setWindowTitle("Test")

        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(-6, -5, 1071, 701))
        pixmap = QtGui.QPixmap('Placeholder.png')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        self.resize(pixmap.width(), pixmap.height())

def start():
    app = QtWidgets.QApplication(sys.argv)
    newWindow = PictureWindow()
    newWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()