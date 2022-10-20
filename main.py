from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui 
import os
from glob import glob
from collections import defaultdict
import numpy as np
import cv2
import matplotlib.pyplot as plt

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("keras-vs-yolo.ui",self)
        self.show()
        self.current_file = "Keras_vs_Yolo.png"
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1,1)
        self.file_list = None
        self.file_counter = None
        self.actionKlasorden_Ac_2.triggered.connect(self.open_directory)
        self.pushButton_3.clicked.connect(self.previous_image)
        self.pushButton.clicked.connect(self.next_image)
        self.pushButton_2.clicked.connect(self.log)
        self.pushButton_4.clicked.connect(self.keras)
        self.kerasBool = False
        self.yoloBool = False
        self.readData(1)
        self.readData(0)
         

    def openCvImage(self,cvImg):
        
        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
       
        
        pixmap =  QtGui.QPixmap.fromImage(QtGui.QImage(cvImg.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888))
        return pixmap

    def resizeEvent(self,event):
        cvImg = cv2.imread("Keras_vs_Yolo.png")
        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
       
        
        pixmap =  QtGui.QPixmap.fromImage(QtGui.QImage(cvImg.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888))
        pixmap = pixmap.scaled(self.width(), self.height())

        self.label.setPixmap(pixmap)
        self.label.resize(self.width(), self.height())


    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file_list = [directory + "/" + f for f in os.listdir(directory) if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg")]
        self.file_counter = 0
        self.current_file = self.file_list[self.file_counter]
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)

    def next_image(self):
        if self.file_counter is not None:
            self.file_counter +=1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            self.imageRead()
            

    def previous_image(self):
        if self.file_counter is not None:
            self.file_counter -=1
            self.file_counter %= len(self.file_list)
            self.current_file = self.file_list[self.file_counter]
            self.imageRead()

    def imageRead(self):
        cvImg = cv2.imread(self.current_file)
        cvImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        if self.kerasBool:
            data = self.kerasData[os.path.basename(self.current_file)]
            for i in data:
                i[1:] = list(map(int,i[1:]))
                cvImg = cv2.rectangle(cvImg,(i[1], i[2]), (i[3], i[4]), (0, 255, 0), 3) # !!!!
                cvImg = cv2.putText(cvImg,f"{i[0]}",(i[1],i[2]),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),1,cv2.LINE_AA)

        if self.yoloBool:
            data = self.yoloData[os.path.basename(self.current_file)]
            for i in data:
                i[1:] = list(map(float,i[1:]))
                i[1:] = list(map(int,i[1:]))
                cvImg = cv2.rectangle(cvImg,(i[1], i[2]), (i[3], i[4]), (255, 255, 0), 3) # !!!!
                cvImg = cv2.putText(cvImg,f"{i[0]}",(i[1],i[2]),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),1,cv2.LINE_AA)


        pixmap = QtGui.QPixmap(self.openCvImage(cvImg))
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)

    def keras(self):
        self.kerasBool = not self.kerasBool 
    
    def log(self):
        self.yoloBool = not self.yoloBool

    def readData(self,type):
        if type:
            with open("YOLO.txt") as f:
                lines = f.readlines()
                yoloList = defaultdict(list)
                for line in lines:
                    lineData = line.split(",")
                    yoloList[lineData[0].strip()].append(lineData[1:-1])
            self.yoloData = yoloList
        else:
            with open("KERAS.txt") as f:
                lines = f.readlines()
                yoloList = defaultdict(list)
                for line in lines:
                    lineData = line.split(",")
                    if lineData[-1] != '\n':
                        yoloList[lineData[0].strip()].append(lineData[1:])
                    else:
                        yoloList[lineData[0].strip()].append(lineData[1:-1])
            self.kerasData = yoloList


def main():
    app=QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()