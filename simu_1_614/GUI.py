import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLayout,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QPainter,QBrush,QPen,QColor,QPalette
from PyQt5.QtCore import Qt,QRect

class simuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.setMinimumSize(400,400)
        self.pen = QPen()
        self.brush = QBrush() 
        
    def draw(self):
        self.setGeometry(40,70,750,500)
        self.show()
        
    def setPen(self,p):
        self.pen = p
        self.update()
    
    def setBrush(self,b):
        self.brush = b
        self.update()
    
    def paintEvent(self,QPaintEvent):
        p = QPainter(self)
        p.setPen(self.pen)
        p.setBrush(self.brush)
        
        rect = QRect(40,70,100,100) 

        p.drawLine(rect.topLeft(),rect.bottomRight())

        
      
class simulation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        main_layout = QVBoxLayout()
        compare_layout = QVBoxLayout()
        up_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        
        start_but = QPushButton('start')
        exit_but = QPushButton('exit')
        simu_widget = simuWidget()
        '''compare_widget_origin = create_campare_widget()
        compare_widget_new = create_campare_widget()
        
        compare_layout.addWidget(compare_widget_origin)
        compare_layout.addWidget(compare_widget_new)
        up_layout.addWidget(simu_widget)
        up_layout.addLayout(compare_layout)'''
        up_layout.addWidget(simu_widget)
        #bottom_layout.addStretch(1)
        bottom_layout.addWidget(start_but)
        bottom_layout.addWidget(exit_but)
        #main_layout.addLayout(up_layout)
        #main_layout.addStretch(1)
        main_layout.addLayout(bottom_layout)
        
        self.setLayout(main_layout)
        self.setGeometry(30,60,1500,1000)
        self.setWindowTitle('simulation')
        self.show()
        
    #def create_simu_widget(self):
        
    #def create_campare_widget(self):
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    simu = simulation()
    sys.exit(app.exec_())
    