import sys
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Trabalho PDI"
        self.initUI()
        self.pathImage
        

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

    def setLastImageLabel(self):
        pixmap = QtGui.QPixmap(self.pathImage)
        pixmap = pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.lastImageLabel.setPixmap(pixmap)
        pixmap.wi

    def setOriginalImageLabel(self):
        pixmap = QtGui.QPixmap(self.pathImage)
        pixmap = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.originalImageLabel.setPixmap(pixmap)

    @QtCore.Slot()
    def openDialog(self):
        self.pathImage = self.openFileNameDialog()
        self.setOriginalImageLabel()

    @QtCore.Slot()
    def undoImage(self):
        print("undo")

    @QtCore.Slot()
    def threshholdButtonEventOnClick(self):
        print("threshholdButton")


    @QtCore.Slot()
    def greyScaleButtonEventOnClick(self):
        print("greyScaleButton")


    @QtCore.Slot()
    def highPassBasicButtonEventOnClick(self):
        print("highPassBasicButton")


    @QtCore.Slot()
    def highPassButtonEventOnClick(self):
        print("highPassButton")


    @QtCore.Slot()
    def averagingButtonEventOnClick(self):
        print("averagingButton")


    @QtCore.Slot()
    def medianButtonEventOnClick(self):
        print("medianButton")


    @QtCore.Slot()
    def robertsButtonEventOnClick(self):
        print("robertsButton")


    @QtCore.Slot()
    def prewittButtonEventOnClick(self):
        print("prewittButton")


    @QtCore.Slot()
    def sobelButtonEventOnClick(self):
        print("sobelButton")


    @QtCore.Slot()
    def logButtonEventOnClick(self):
        print("logButton")


    @QtCore.Slot()
    def cannyButtonEventOnClick(self):
        print("cannyButton")


    @QtCore.Slot()
    def saltPepperButtonEventOnClick(self):
        print("saltPepperButton")


    @QtCore.Slot()
    def watershedButtonEventOnClick(self):
        print("watershedButton")


    @QtCore.Slot()
    def histogramButtonEventOnClick(self):
        print("histogramButton")


    @QtCore.Slot()
    def countObjectsButtonEventOnClick(self):
        print("countObjectsButton")


    @QtCore.Slot()
    def zerocrossButtonEventOnClick(self):
        print("zerocrossButton")




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1200, 800)
    widget.show()

    sys.exit(app.exec())
