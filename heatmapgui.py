from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
import sys
import PictureWindow


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 589)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ruimte = QtWidgets.QComboBox(self.centralwidget)
        self.ruimte.setGeometry(QtCore.QRect(110, 20, 171, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.ruimte.setFont(font)
        self.ruimte.setObjectName("ruimte")
        self.ruimte.addItem("")
        self.ruimte.addItem("")
        self.ruimte.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 30, 41, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 30, 31, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.start_date = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.start_date.setGeometry(QtCore.QRect(380, 20, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_date.setFont(font)
        self.start_date.setObjectName("start_date")
        self.end_date = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.end_date.setGeometry(QtCore.QRect(600, 20, 151, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.end_date.setFont(font)
        self.end_date.setObjectName("end_date")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 61, 16))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.new_window = QtWidgets.QRadioButton(self.centralwidget)
        self.new_window.setGeometry(QtCore.QRect(480, 60, 161, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.new_window.setFont(font)
        self.new_window.setObjectName("new_window")
        self.ruimte_foto = QtWidgets.QLabel(self.centralwidget)
        self.ruimte_foto.setGeometry(QtCore.QRect(10, 100, 781, 451))
        self.ruimte_foto.setText("")
        self.ruimte_foto.setPixmap(QtGui.QPixmap("Placeholder.png"))
        self.ruimte_foto.setScaledContents(True)
        self.ruimte_foto.setObjectName("ruimte_foto")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(650, 62, 101, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.submitPressed)
        self.dialogs = list()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ruimte.setItemText(0, _translate("MainWindow", "Huiskamer"))
        self.ruimte.setItemText(1, _translate("MainWindow", "Slaapkamer"))
        self.ruimte.setItemText(2, _translate("MainWindow", "Badkamer"))
        self.label.setText(_translate("MainWindow", "Vanaf:"))
        self.label_2.setText(_translate("MainWindow", "Tot:"))
        self.label_3.setText(_translate("MainWindow", "Ruimte:"))
        self.new_window.setText(_translate("MainWindow", "Open in New window"))
        self.submit.setText(_translate("MainWindow", "Submit"))

    def submitPressed(self):
        selected_room = self.ruimte.currentText()

        if self.new_window.isChecked():
            self.newWindow()
        else:
            self.ruimte_foto.setPixmap(QtGui.QPixmap(selected_room + ".png"))

    def newWindow(self):
        dialog = PictureWindow.PictureWindow(self)
        self.dialogs.append(dialog)
        dialog.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()