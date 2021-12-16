import sys
from PySide6 import QtCore, QtWidgets, QtGui
import cv2
from filters.averaging import averagingCv
from filters.canny import cannyCv
from filters.eqHist import eqHist
from filters.grayScale import greyScaleCv
from filters.highpassBasic import highpassBasicCv
from filters.highpass import highpassCv
from filters.histogram import histCv
from filters.imageRead import imageReadCv
from filters.log import logCv
from filters.median import medianCv
from filters.prewitt import prewittCv
from filters.roberts import robertsCv
from filters.saltPepper import SaltPepperCv
from filters.sobel import sobelCv
from filters.thresholding import thresholdingCv
from filters.watershedWithCount import countObjects, watershedWithCountCv
from filters.zeroCross import laplace_of_gaussian


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
        self.averagingButton = self.newButton("Passa baixa (média)",10,185,150,25,self.averagingButtonEventOnClick)
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
        self.eqHist = self.newButton("Equalizar imagem",10,605,150,25,self.equalizehistogramButtonEventOnClick)

        self.dialogButton = self.newButton("Arquivo",170,45,150,25,self.openDialog)
        self.undo = self.newButton("Desfazer",330,45,150,25,self.undoImage)

        self.parameters = QtWidgets.QLineEdit(self)
        self.parameters.setPlaceholderText("Parametro")
        self.parameters.setGeometry(490,45,150,25)
        self.matrixScale = QtWidgets.QLineEdit(self)
        self.matrixScale.setPlaceholderText("Tamanho da matriz")
        self.matrixScale.setGeometry(650,45,150,25)


        self.originalImageLabel = QtWidgets.QLabel(self)
        self.originalImageLabel.setGeometry(780,315,400,200)
        self.titleOriginalImage = QtWidgets.QLabel(self)
        self.titleOriginalImage.setGeometry(780,315,200,17)
        self.titleOriginalImage.setText("Imagem original")

        self.lastImageLabel = QtWidgets.QLabel(self)
        self.lastImageLabel.setGeometry(170,80,600,400)
        self.titleLastImage = QtWidgets.QLabel(self)
        self.titleLastImage.setGeometry(170,80,200,17)
        self.titleLastImage.setText("Imagem modificada")

        self.instructions = QtWidgets.QLabel(self)
        self.instructions.setGeometry(780,45,400,270)
        self.instructions.setText("\n \
        Passa alta de alto contraste recebe um valor de 3 a 12.\n \
        Passa alta básica recebe um valor de 3 a 12.\n \
        Mediana recebe um valor de 3 a 12.\n \
        Média recebe um valor de 3 a 12.\n \
        Salt & Pepper recebe um valor de 0.00 a 1.00\n \
        Limiarização recebe os seguintes valores:\n \
            0 binary\n \
            1 binary_inv\n \
            2 trunc\n \
            3 tozero\n \
            4 tozero_inv\n")


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
        pixmap = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.lastImageLabel.setPixmap(pixmap)

    def setOriginalImageLabel(self):
        pixmap = QtGui.QPixmap(self.pathImage)
        pixmap = pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
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
            try:
                self.listImages.pop()
                self.saveLastImage()
            except:
                print("Erro ao voltar imagem.'undoImage'")

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
        self.matrixScale.setText("")


    @QtCore.Slot()
    def greyScaleButtonEventOnClick(self):
        try:
            image = greyScaleCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao converter imagem para escala de cinza.")
        self.parameters.setText("")
        

    @QtCore.Slot()
    def highPassBasicButtonEventOnClick(self):
        var = self.matrixScale.text()
        try:
            image = highpassBasicCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = highpassBasicCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def highPassButtonEventOnClick(self):
        varP = self.parameters.text()
        varM = self.matrixScale.text()
        try:
            image = highpassCv(self.listImages[len(self.listImages)-1],int(varM),int(varP))
        except:
            image = highpassCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def averagingButtonEventOnClick(self):
        var = self.matrixScale.text()
        try:
            image = averagingCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = averagingCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def medianButtonEventOnClick(self):
        var = self.matrixScale.text()
        try:
            image = medianCv(self.listImages[len(self.listImages)-1],int(var))
        except:
            image = medianCv(self.listImages[len(self.listImages)-1])
        self.listImages.append(image)
        self.saveLastImage()
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def robertsButtonEventOnClick(self):
        try:
            image = robertsCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Roberts.")
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def prewittButtonEventOnClick(self):
        try:
            image = prewittCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Prewitt.")
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def sobelButtonEventOnClick(self):
        try:
            image = sobelCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image[0])
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Sobel.")
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def logButtonEventOnClick(self):
        try:
            image = logCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro log.")
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def cannyButtonEventOnClick(self):
        try:
            image = cannyCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
        except:
            print("Erro ao aplicar o filtro canny.")
        self.saveLastImage()
        self.parameters.setText("")
        self.matrixScale.setText("")


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
        self.matrixScale.setText("")


    @QtCore.Slot()
    def watershedButtonEventOnClick(self):
        try:
            image = watershedWithCountCv(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except Exception as e:
            print("Erro ao aplicar o filtro watershed."+str(e))
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def countObjectsButtonEventOnClick(self):
        try:
            countObjects
            image = countObjects(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro fazer contagem dos objetos.")
        self.parameters.setText("")
        self.matrixScale.setText("")

    @QtCore.Slot()
    def histogramButtonEventOnClick(self):
        histCv(self.listImages[len(self.listImages)-1])
        self.setLastImageLabel("histogram.jpg")
        self.parameters.setText("")
        self.matrixScale.setText("")

    @QtCore.Slot()
    def equalizehistogramButtonEventOnClick(self):
        try:
            image = eqHist(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro equalizar imagem.")
        self.parameters.setText("")
        self.matrixScale.setText("")


    @QtCore.Slot()
    def zerocrossButtonEventOnClick(self):
        try:
            image = laplace_of_gaussian(self.listImages[len(self.listImages)-1])
            self.listImages.append(image)
            self.saveLastImage()
        except Exception as e:
            print("Erro ao aplicar zero cross.",str(e))
        self.parameters.setText("")

    def saveLastImage(self):
        cv2.imwrite("lastImage.jpg",self.listImages[len(self.listImages)-1])
        self.setLastImageLabel("lastImage.jpg")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1200, 800)
    widget.show()

    sys.exit(app.exec())
