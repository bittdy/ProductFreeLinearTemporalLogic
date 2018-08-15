# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_626.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_simulation(object):
    def setupUi(self, simulation):
        simulation.setObjectName("simulation")
        simulation.resize(1332, 904)
        
        self.simu_main = QtWidgets.QGraphicsView(simulation)
        self.simu_main.setGeometry(QtCore.QRect(30, 80, 811, 741))
        self.simu_main.setObjectName("simu_main")
        
        self.origin_method = QtWidgets.QGraphicsView(simulation)
        self.origin_method.setGeometry(QtCore.QRect(930, 80, 381, 341))
        self.origin_method.setObjectName("origin_method")
        
        self.new_method = QtWidgets.QGraphicsView(simulation)
        self.new_method.setGeometry(QtCore.QRect(930, 470, 381, 351))
        self.new_method.setObjectName("new_method")
        
        self.start = QtWidgets.QPushButton(simulation)
        self.start.setGeometry(QtCore.QRect(980, 840, 111, 41))
        self.start.setObjectName("start")
        
        self.exit = QtWidgets.QPushButton(simulation)
        self.exit.setGeometry(QtCore.QRect(1160, 840, 111, 41))
        self.exit.setObjectName("exit")
        
        self.label = QtWidgets.QLabel(simulation)
        self.label.setGeometry(QtCore.QRect(420, 50, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(simulation)
        self.label_2.setGeometry(QtCore.QRect(1000, 50, 331, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(simulation)
        self.label_3.setGeometry(QtCore.QRect(1020, 440, 251, 20))
        self.label_3.setObjectName("label_3")
        
        self.line = QtWidgets.QFrame(simulation)
        self.line.setGeometry(QtCore.QRect(30, 160, 811, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(simulation)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 811, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(simulation)
        self.line_3.setGeometry(QtCore.QRect(30, 340, 811, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(simulation)
        self.line_4.setGeometry(QtCore.QRect(30, 430, 811, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(simulation)
        self.line_5.setGeometry(QtCore.QRect(30, 520, 811, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(simulation)
        self.line_6.setGeometry(QtCore.QRect(30, 610, 811, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(simulation)
        self.line_7.setGeometry(QtCore.QRect(30, 710, 811, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(simulation)
        self.line_8.setGeometry(QtCore.QRect(110, 80, 20, 741))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(simulation)
        self.line_9.setGeometry(QtCore.QRect(200, 80, 20, 741))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(simulation)
        self.line_10.setGeometry(QtCore.QRect(290, 80, 20, 741))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(simulation)
        self.line_11.setGeometry(QtCore.QRect(380, 80, 20, 741))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(simulation)
        self.line_12.setGeometry(QtCore.QRect(470, 80, 20, 741))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(simulation)
        self.line_13.setGeometry(QtCore.QRect(560, 80, 20, 741))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(simulation)
        self.line_14.setGeometry(QtCore.QRect(650, 80, 20, 741))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(simulation)
        self.line_15.setGeometry(QtCore.QRect(740, 80, 20, 741))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")

        self.retranslateUi(simulation)
        QtCore.QMetaObject.connectSlotsByName(simulation)
        simulation.show()

    def retranslateUi(self, simulation):
        _translate = QtCore.QCoreApplication.translate
        simulation.setWindowTitle(_translate("simulation", "Simulation"))
        self.start.setText(_translate("simulation", "start"))
        self.exit.setText(_translate("simulation", "exit"))
        self.label.setText(_translate("simulation", "simulation"))
        self.label_2.setText(_translate("simulation", "states number of origin method"))
        self.label_3.setText(_translate("simulation", "states number of new method"))

if __name__ =='__main__':
    # 添加if判断语句可以解决spyder内核重启的问题
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    widget = QWidget(None)
    Ui_simulation().setupUi(widget)
    sys.exit(app.exec_())
    pass  
