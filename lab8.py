import sys

from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication

from PySide2 import QtCore, QtGui, QtWidgets
import random

MAX_HEIGHT = 200
MAX_WIDTH = 200

MIN_HEIGHT = 50
MIN_WIDTH = 50

ELEMENTS_COUNT = 20

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.drawButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.drawButton.setObjectName("drawButton")
        self.horizontalLayout.addWidget(self.drawButton)
        self.drawButton.clicked.connect(self.draw_event)

        self.eraseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.eraseButton.setObjectName("eraseButton")
        self.horizontalLayout.addWidget(self.eraseButton)
        self.eraseButton.clicked.connect(self.clear_event)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_3.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graphicsScene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.graphicsScene)

        self.isDrawn = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_params(self):
        return (
            random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
            random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT),
            random.randrange(MIN_WIDTH, MAX_WIDTH),
            random.randrange(MIN_HEIGHT, MAX_HEIGHT)
        )

    def draw_event(self):
        rnd = random.Random()
        if not self.isDrawn:

            item = QtWidgets.QGraphicsEllipseItem(*self.get_params())
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsEllipseItem(*self.get_params())
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsEllipseItem(*self.get_params())
            item.setStartAngle(90)
            item.setSpanAngle(random.randrange(10, 100))
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsEllipseItem(*self.get_params())
            item.setStartAngle(90 * 20)
            item.setSpanAngle(random.randrange(10, 100) * 20)
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsRectItem(*self.get_params())
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsRectItem(*self.get_params())
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsLineItem()
            item.setLine(random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                         random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT),
                         random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                         random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT))
            self.graphicsScene.addItem(item)

            item = QtWidgets.QGraphicsLineItem()
            item.setLine(random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                         random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT),
                         random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                         random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT))
            self.graphicsScene.addItem(item)

            self.textItem = QtWidgets.QGraphicsTextItem()
            self.textItem.setPos(random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                                 random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT))
            self.textItem.setPlainText('SomeTextRightHere')
            self.textItem.setTextWidth(200)
            self.graphicsScene.addItem(self.textItem)

            self.textItem = QtWidgets.QGraphicsTextItem()
            self.textItem.setPos(random.randrange(0, self.graphicsView.frameGeometry().width() - MAX_WIDTH),
                                 random.randrange(0, self.graphicsView.frameGeometry().height() - MAX_HEIGHT))
            self.textItem.setPlainText('Another one')
            self.textItem.setTextWidth(100)
            self.graphicsScene.addItem(self.textItem)
            self.isDrawn = True

    def clear_event(self):
        self.isDrawn = False
        self.graphicsScene.clear()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.drawButton.setText(QtWidgets.QApplication.translate("MainWindow", "Draw", None, -1))
        self.eraseButton.setText(QtWidgets.QApplication.translate("MainWindow", "Erase", None, -1))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())