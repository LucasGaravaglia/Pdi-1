import sys
from PySide6 import QtCore, QtWidgets, QtGui
import filters
import cv2
from filters.averagingCv import averagingCv
from filters.cannyCv import cannyCv
from filters.greyScaleCv import greyScaleCv
from filters.highpassBasicCv import highpassBasicCv
from filters.highpassCv import highpassCv
from filters.histogramCv import histCv
from filters.imageReadCv import imageReadCv
from filters.logCv import logCv
from filters.medianCv import medianCv
from filters.prewittCv import prewittCv
from filters.robertsCv import robertsCv
from filters.saltPepperCv import SaltPepperCv
from filters.sobelCv import sobelCv

from filters.thresholdingCv import thresholdingCv
from filters.watershedWithCountCv import watershedWithCountCv





class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.listImages = []
        self.title = "Trabalho PDI"
        self.initUI()
        self.pathImage = ""
        

    def initUI(self):
        self.setWindowTitle(self.title)

        self.threshholdButton = self.newButton("Limiarização",10,45,150,25,self.threshholdButtonEventOnClick)
        self.greyScaleButton = self.newButton("Escala de cinza",10,80,150,25,self.greyScaleButtonEventOnClick)
        self.highPassBasicButton = self.newButton("Passa alta (básica)",10,115,150,25,self.highPassBasicButtonEventOnClick)
        self.highPassButton = self.newButton("Passa alta (alto reforço)",10,150,150,25,self.highPassButtonEventOnClick)
        self.averagingButton = self.newButton("Passa alta (média)",10,185,150,25,self.averagingButtonEventOnClick)
        self.medianButton = self.newButton("Passa baixa (mediana)",10,220,150,25,self.medianButtonEventOnClick)
        self.robertsButton = self.newButton("Roberts",10,255,150,25,self.robertsButtonEventOnClick)
        self.prewittButton = self.newButton("Prewitt",10,290,150,25,self.prewittButtonEventOnClick)
        self.sobelButton = self.newButton("Sobel",10,325,150,25,self.sobelButtonEventOnClick)
        self.logButton = self.newButton("Log",10,360,150,25,self.logButtonEventOnClick)
        self.cannyButton = self.newButton("Canny",10,395,150,25,self.cannyButtonEventOnClick)
        self.saltPepperButton = self.newButton("Salt & Pepper",10,430,150,25,self.saltPepperButtonEventOnClick)
        self.watershedButton = self.newButton("Watershed",10,465,150,25,self.watershedButtonEventOnClick)
        self.histogramButton = self.newButton("Histograma",10,500,150,25,self.histogramButtonEventOnClick)
        self.countObjectsButton = self.newButton("Contagem de objetos",10,535,150,25,self.countObjectsButtonEventOnClick)
        self.zerocrossButton = self.newButton("Zerocross",10,570,150,25,self.zerocrossButtonEventOnClick)

        self.dialogButton = self.newButton("Arquivo",170,45,150,25,self.openDialog)
        self.undo = self.newButton("Desfazer",330,45,150,25,self.undoImage)

        self.parameters = QtWidgets.QLineEdit(self)
        self.parameters.setGeometry(10,605,150,25)
        self.parameters.setWindowTitle("aaaa")

        self.titleOriginalImage = QtWidgets

        self.originalImageLabel = QtWidgets.QLabel(self)
        self.originalImageLabel.setGeometry(170,80,500,300)

        self.lastImageLabel = QtWidgets.QLabel(self)
        self.lastImageLabel.setGeometry(600,300,500,300)

    def newButton(self,name,x,y,w,h,event):
        temp = QtWidgets.QPushButton(name, self)
        temp.clicked.connect(event)
        temp.setGeometry(x,y,w,h)
        return temp

    
    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

    def setLastImageLabel(self,path):
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.lastImageLabel.setPixmap(pixmap)

    def setOriginalImageLabel(self):
        pixmap = QtGui.QPixmap(self.pathImage)
        pixmap = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.originalImageLabel.setPixmap(pixmap)

    @QtCore.Slot()
    def openDialog(self):
        self.pathImage = self.openFileNameDialog()
        self.setOriginalImageLabel()
        self.setLastImageLabel(self.pathImage)
        self.listImages.clear()
        self.listImages.append(imageReadCv(self.pathImage))

    @QtCore.Slot()
    def undoImage(self):
        if(len(self.listImages) > 1):
            self.listImages.pop()
            self.saveLastImage()
        print("undo")

    @QtCore.Slot()
    def threshholdButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = thresholdingCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = thresholdingCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")

        print("threshholdButton")


    @QtCore.Slot()
    def greyScaleButtonEventOnClick(self):
        image = greyScaleCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        print("greyScaleButton")


    @QtCore.Slot()
    def highPassBasicButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = highpassBasicCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = highpassBasicCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("highPassBasicButton")


    @QtCore.Slot()
    def highPassButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = highpassCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = highpassCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("highPassButton")


    @QtCore.Slot()
    def averagingButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = averagingCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = averagingCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("averagingButton")


    @QtCore.Slot()
    def medianButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = medianCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = medianCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("medianButton")


    @QtCore.Slot()
    def robertsButtonEventOnClick(self):
        image = robertsCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("robertsButton")


    @QtCore.Slot()
    def prewittButtonEventOnClick(self):
        image = prewittCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("prewittButton")


    @QtCore.Slot()
    def sobelButtonEventOnClick(self):
        image = sobelCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("sobelButton")


    @QtCore.Slot()
    def logButtonEventOnClick(self):
        image = logCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("logButton")


    @QtCore.Slot()
    def cannyButtonEventOnClick(self):
        image = cannyCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("cannyButton")


    @QtCore.Slot()
    def saltPepperButtonEventOnClick(self):
        var = self.parameters.text()
        try:
            image = SaltPepperCv(self.listImages[len(self.listImages)-1],float(var))
        except:
            image = SaltPepperCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("saltPepperButton")


    @QtCore.Slot()
    def watershedButtonEventOnClick(self):
        image,_ = watershedWithCountCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("watershedButton")


    @QtCore.Slot()
    def countObjectsButtonEventOnClick(self):
        _,image = watershedWithCountCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        print("countObjectsButton")

    @QtCore.Slot()
    def histogramButtonEventOnClick(self):
        histCv(imageReadCv(self.pathImage,True))
        print("histogramButton")

    @QtCore.Slot()
    def zerocrossButtonEventOnClick(self):
        print("zerocrossButton")

    def saveLastImage(self):
        cv2.imwrite("lastImage.jpg",self.listImages[len(self.listImages)-1])
        self.setLastImageLabel("lastImage.jpg")




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1200, 800)
    widget.show()

    sys.exit(app.exec())
