from PyQt5.QtGui import  QIcon, QPixmap,QFont,QImage,QPalette,QBrush
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication,QMainWindow,QLabel,QStackedLayout)
import sys
import numpy as np
from matplotlib import pyplot as plt
import cv2 
from PIL import *
import sklearn
from sklearn.cluster import KMeans 

class Button(QPushButton):
  
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
    


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.edit=QLineEdit('', self)
        
        self.button=Button("", self)
        self.button1=Button("", self)
        self.button2=Button("", self)
        self.button3=Button("", self)
        self.button4=Button("", self)
        self.button5=Button("", self)
        self.button6=Button("", self)
        self.button7=Button("", self)
        self.QMainWindow=QMainWindow(self)
        
        self.label=QLabel(self)
        self.labeltext=QLabel(self)
        self.label2=QLabel(self)
        self.labeltext2=QLabel(self)
        self.initUI()
        
        
    def initUI(self):

        self.edit.setDragEnabled(True)
        self.edit.move(30, 10)
        self.edit.resize(300,30)
        self.edit.setPlaceholderText('Place your image url here')
        
        self.button.move(35, 50)
        self.button.resize(70,70)
        self.button.setStyleSheet('QPushButton {background-image: url(bg.jpeg); color: white;border:0}')
        self.button.clicked.connect(lambda: self.image_processing('bg.jpeg'))

        self.button1.move(35, 130)
        self.button1.resize(70,70)
        self.button1.setStyleSheet('QPushButton {background-image: url(blue.PNG); color: white;border:0}')
        self.button1.clicked.connect(lambda: self.image_processing('blue.PNG'))
        

        self.button2.move(35, 210)
        self.button2.resize(70,70)
        self.button2.setStyleSheet('QPushButton {background-image: url(bluem2lm.PNG); color: white;border:0}')
        self.button2.clicked.connect(lambda: self.image_processing('bluem2lm.PNG'))


        self.button3.move(35, 290)
        self.button3.resize(70,70)
        self.button3.setStyleSheet('QPushButton {background-image: url(brown.PNG); color: white;border:0}')
        self.button3.clicked.connect(lambda: self.image_processing('brown.PNG'))

        self.button4.move(35, 370)
        self.button4.resize(70,70)
        self.button4.setStyleSheet('QPushButton {background-image: url(brown2.PNG); color: white;border:0}')
        self.button4.clicked.connect(lambda: self.image_processing('brown2.PNG'))
        
        self.button5.move(35, 450)
        self.button5.resize(70,70)
        self.button5.setStyleSheet('QPushButton {background-image: url(bui.jpg); color: white;border:0}')
        self.button5.clicked.connect(lambda: self.image_processing('bui.jpg'))

        self.button6.move(35, 530)
        self.button6.resize(70,70)
        self.button6.setStyleSheet('QPushButton {background-image: url(pink.PNG); color: white;border:0}')
        self.button6.clicked.connect(lambda: self.image_processing('pink.PNG'))

        self.button7.move(35, 610)
        self.button7.resize(70,70)
        self.button7.setStyleSheet('QPushButton {background-image: url(shyaka.PNG); color: white;border:0}')
        self.button7.clicked.connect(lambda: self.image_processing('shyaka.PNG'))
        
        self.labeltext.move(350,380)
        self.labeltext.resize(300,30)
        self.label.move(350,60)
        self.label.resize(300,300)
        self.labeltext2.move(660,380)
        self.labeltext2.resize(300,30)
        self.label2.move(660,60)
        self.label2.resize(300,300)
        self.labeltext.setStyleSheet('QLabel{color:darkMagenta;}')
        self.labeltext.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.labeltext.setFont(QFont('italic', 15))
        self.labeltext2.setStyleSheet('QLabel{color:yellow;}')
        self.labeltext2.setFont(QFont('italic', 15))
        self.labeltext2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        
        self.setWindowTitle('Paint it')
        self.setGeometry(100, 100, 1000, 700)
        

        
        oImage = QImage("background2.jpg")
        sImage = oImage.scaled(QSize(1000,700))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                     # 10 = Windowrole
        self.setPalette(palette)
       
    def image_processing(self,image):
        img = cv2.imread(self.edit.text())
        cv2.imwrite('input.png',img)
        y=cv2.imread(image)
        
        pixmap = QPixmap('input.png')
        pixmap = pixmap.scaled(300, 300)
        self.labeltext.setText('Before ')
        self.label.setPixmap(pixmap)
        self.labeltext2.setText('After ')
        self.change(img,y)

        
    def change(self,img1,img2):
        #img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img1=cv2.resize(img1,(700,400))
        #img2 =cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img2=cv2.resize(img2,(700,400))
        h,w = img1.shape[:2]
        im_small_long = img1.reshape((h * w, 3))
        im_small_wide = im_small_long.reshape((h,w,3))
    
        km = KMeans(n_clusters=4)
    
        km.fit(im_small_long)
    
        cc = km.cluster_centers_.astype(np.uint8)
        out = np.asarray([cc[i] for i in km.labels_]).reshape((h,w,3))
        r=out[30,10,0]
        g=out[30,10,1]
        b=out[30,10,2]
        r2=out[40,650,0]
        g2=out[40,650,1]
        b2=out[40,650,2]
        e1=img2[np.where((out == [r,g,b]).all(axis = 2))]
        e2=img2[np.where((out == [r2,g2,b2]).all(axis = 2))]
        img1[np.where((out == [r,g,b]).all(axis = 2))] = e1
        img1[np.where((out == [r2,g2,b2]).all(axis = 2))] = e2
        
        cv2.imwrite('output.png',img1)
        pixmap = QPixmap('output.png')
        pixmap = pixmap.scaled(300, 300)
        self.label2.setPixmap(pixmap)
if __name__ == '__main__':
  
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()  