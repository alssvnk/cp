import sys

from PySide2.QtWidgets import QMainWindow, QPushButton, QApplication

from PySide2 import QtCore, QtGui, QtWidgets
import os.path
import math

DELAY = 100
FRAME_DISTANCE = 20
SPEED = 0.2

PIC_NUMS = 23
FILE = ''
POSTFIX = '.gif'
FOLDER = 'source/'
PATH = os.path.join(FOLDER, FILE)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 990, 790))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graphicsScene = QtWidgets.QGraphicsScene()
        self.graphicsScene.mousePressEvent = self.mouse_clicked
        self.graphicsView.setScene(self.graphicsScene)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.tick_event)

        self.pixmaps = []
        for i in range(PIC_NUMS):
            img = QtGui.QImage(PATH + str(i) + POSTFIX)
            self.pixmaps.append(QtGui.QPixmap.fromImage(img))

        self.pic = QtWidgets.QGraphicsPixmapItem(self.pixmaps[0])
        #self.pic.setPixmap()
        self.pic.setPos(0, 0)
        self.graphicsScene.addItem(self.pic)

        self.frameNum = 0
        self.frameDist = FRAME_DISTANCE

        self.picDest = QtCore.QPointF(0, 0)
        self.curPos = QtCore.QPointF(0, 0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))

    def tick_event(self):
        dt = self.timer.interval()
        speed = SPEED * dt

        angle = math.atan2(self.curPos.y() - self.picDest.y(), self.curPos.x() - self.picDest.x())

        posNext = QtCore.QPointF(speed * math.cos(angle), speed * math.sin(angle))
        passedDist = self.get_distance(self.curPos, self.curPos - posNext)
        self.curPos -= QtCore.QPointF(speed * math.cos(angle), speed * math.sin(angle))

        dist = self.get_distance(self.curPos, self.picDest)
        self.frameDist -= passedDist

        if self.frameDist <= 0:
            self.frameDist = FRAME_DISTANCE
            self.frameNum = (self.frameNum + 1) % PIC_NUMS
            self.pic.setPixmap(self.pixmaps[self.frameNum])

        if dist <= 1.0:
            self.timer.stop()

        self.pic.setPos(self.curPos.x(), self.curPos.y())

    def mouse_clicked(self, e):
        self.picDest = QtCore.QPointF(e.scenePos().x(), e.scenePos().y())
        if not self.timer.isActive():
            self.timer.start(10)

    @staticmethod
    def get_distance(p1, p2):
        nP = p2 - p1
        return (nP.x() ** 2 + nP.y() ** 2) ** 0.5

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())