import sys

import PySide2.QtWidgets as widgets

from PySide2 import QtCore, QtGui, QtWidgets

SPEED = 0.2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 781, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.startButton.setText('Start')
        self.startButton.clicked.connect(self.start_clicked)

        self.horizontalLayout.addWidget(self.startButton)

        self.stopButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setText('Stop')
        self.stopButton.clicked.connect(self.stop_clicked)

        self.horizontalLayout.addWidget(self.stopButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setProperty("cursor", QtCore.Qt.UpArrowCursor)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_draw)

        self.sceneView = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.sceneView)
        self.textItem = None

        self.speed_flag = 1

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.startButton.setText(QtWidgets.QApplication.translate("MainWindow", "start", None, -1))
        self.stopButton.setText(QtWidgets.QApplication.translate("MainWindow", "stop", None, -1))
        self.actionStart.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
        self.actionStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))

    def update_draw(self):
        global SPEED

        dt = self.timer.interval()
        if not self.textItem:
            return

        x = self.textItem.x()
        y = self.textItem.y()
        dx = dt * self.speed_flag * SPEED

        if x + dx >= self.centralwidget.frameGeometry().width() - self.textItem.textWidth() or x + dx <= 0:
           # SPEED += 0.2
            self.speed_flag *= -1
            dx = dt * self.speed_flag * SPEED

        self.textItem.setPos(x + dx, y)

    def start_clicked(self):
        if not self.textItem:
            self.textItem = QtWidgets.QGraphicsTextItem()
            self.textItem.setPos(0, self.centralwidget.frameGeometry().height() // 2)
            self.textItem.setPlainText('SOME TEXT')
            self.textItem.setTextWidth(120)
            self.sceneView.addItem(self.textItem)

        if not self.timer.isActive():
            self.timer.start(10)

    def stop_clicked(self):
        if self.timer.isActive():
            self.timer.stop()


class MainWindow(widgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = widgets.QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())