import sys

from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self.delete_clicked)

        self.toRightButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.toRightButton.setObjectName("toRightButton")
        self.horizontalLayout.addWidget(self.toRightButton)
        self.toRightButton.clicked.connect(self.toRight_clicked)

        self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.clearButton.clicked.connect(self.clear_clicked)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.editButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editButton.setObjectName("pushButton")
        self.editButton.clicked.connect(self.edit_clicked)

        self.horizontalLayout.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.leftList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.leftList.setObjectName("leftList")
        self.horizontalLayout_3.addWidget(self.leftList)

        self.rightList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.rightList.setObjectName("rightList")
        self.horizontalLayout_3.addWidget(self.rightList)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.leftList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.rightList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.deleteButton.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.toRightButton.setText(QtWidgets.QApplication.translate("MainWindow", "To right", None, -1))
        self.clearButton.setText(QtWidgets.QApplication.translate("MainWindow", "Clear", None, -1))
        self.editButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))

    def toRight_clicked(self):
        lst = []
        for item in self.leftList.selectedItems():
            lst.append(item.text())
        for item in lst:
            self.rightList.addItem(QtWidgets.QListWidgetItem(item))

    def clear_clicked(self):
        self.leftList.clear()
        self.rightList.clear()

    def delete_clicked(self):
        left = []
        for item in self.leftList.selectedItems():
            left.append(item.text())

        right = []
        for item in self.rightList.selectedItems():
            right.append(item.text())

        delete_strings = list(set(left).union(set(right)))

        ind = 0
        while ind != self.leftList.count():
            item = self.leftList.item(ind)
            if item and item.text() in delete_strings:
                self.leftList.takeItem(ind)
            else:
                ind += 1

        ind = 0
        while ind != self.rightList.count():
            item = self.rightList.item(ind)
            if item and item.text() in delete_strings:
                self.rightList.takeItem(ind)

            else:
                ind += 1


    def edit_clicked(self):
        string = self.lineEdit.text()
        self.lineEdit.setText('')

        lst = []
        for ind in range(self.leftList.count()):
            lst.append(self.leftList.item(ind).text())

        if not (string in lst):
            self.leftList.addItem(QtWidgets.QListWidgetItem(string))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())