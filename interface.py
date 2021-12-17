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
from filters.watershedWithCount import watershedWithCountCv
from filters.zeroCross import laplace_of_gaussian


class MyWidget(QtWidgets.QWidget):
    """
    Classe responssavel por gerenciar a interface.
    """

    def __init__(self):
        """
        Construtor da classe.
        """
        super().__init__()
        self.listImages = []
        self.title = "Trabalho PDI"
        self.initUI()
        self.pathImage = ""

    def initUI(self):
        """
        Inicializa a interface.
        """
        self.setWindowTitle(self.title)

        self.threshholdButton = self.newButton(
            "Limiarização", 10, 45, 150, 25, self.threshholdButtonEventOnClick)
        self.greyScaleButton = self.newButton(
            "Escala de cinza", 10, 80, 150, 25, self.greyScaleButtonEventOnClick)
        self.highPassBasicButton = self.newButton(
            "Passa alta (básica)", 10, 115, 150, 25, self.highPassBasicButtonEventOnClick)
        self.highPassButton = self.newButton(
            "Passa alta (alto reforço)", 10, 150, 150, 25, self.highPassButtonEventOnClick)
        self.averagingButton = self.newButton(
            "Passa baixa (média)", 10, 185, 150, 25, self.averagingButtonEventOnClick)
        self.medianButton = self.newButton(
            "Passa baixa (mediana)", 10, 220, 150, 25, self.medianButtonEventOnClick)
        self.robertsButton = self.newButton(
            "Roberts", 10, 255, 150, 25, self.robertsButtonEventOnClick)
        self.prewittButton = self.newButton(
            "Prewitt", 10, 290, 150, 25, self.prewittButtonEventOnClick)
        self.sobelButton = self.newButton(
            "Sobel", 10, 325, 150, 25, self.sobelButtonEventOnClick)
        self.logButton = self.newButton(
            "Log", 10, 360, 150, 25, self.logButtonEventOnClick)
        self.cannyButton = self.newButton(
            "Canny", 10, 395, 150, 25, self.cannyButtonEventOnClick)
        self.saltPepperButton = self.newButton(
            "Salt & Pepper", 10, 430, 150, 25, self.saltPepperButtonEventOnClick)
        self.watershedButton = self.newButton(
            "Watershed", 10, 465, 150, 25, self.watershedButtonEventOnClick)
        self.histogramButton = self.newButton(
            "Histograma", 10, 500, 150, 25, self.histogramButtonEventOnClick)
        self.countObjectsButton = self.newButton(
            "Contagem de objetos", 10, 535, 150, 25, self.countObjectsButtonEventOnClick)
        self.zerocrossButton = self.newButton(
            "Zerocross", 10, 570, 150, 25, self.zerocrossButtonEventOnClick)
        self.eqHist = self.newButton(
            "Equalizar imagem", 10, 605, 150, 25, self.equalizehistogramButtonEventOnClick)

        self.dialogButton = self.newButton(
            "Arquivo", 170, 45, 150, 25, self.openDialog)
        self.undo = self.newButton(
            "Desfazer", 330, 45, 150, 25, self.undoImage)

        self.originalImageLabel = QtWidgets.QLabel(self)
        self.originalImageLabel.setGeometry(780, 315, 400, 200)
        self.titleOriginalImage = QtWidgets.QLabel(self)
        self.titleOriginalImage.setGeometry(780, 315, 200, 17)
        self.titleOriginalImage.setText("Imagem original")

        self.lastImageLabel = QtWidgets.QLabel(self)
        self.lastImageLabel.setGeometry(170, 80, 600, 400)
        self.titleLastImage = QtWidgets.QLabel(self)
        self.titleLastImage.setGeometry(170, 80, 200, 17)
        self.titleLastImage.setText("Imagem modificada")

    def showDialogInt(self, title, instruction, value=0):
        dlg = QtWidgets.QInputDialog(self)
        dlg.setInputMode(QtWidgets.QInputDialog.IntInput)
        dlg.setLabelText(instruction)
        dlg.setWindowTitle(title)
        dlg.setIntMaximum(1024)
        dlg.setIntValue(value)
        dlg.resize(500, 100)
        ok = dlg.exec()
        return dlg.intValue()

    def showDialogDouble(self, title, instruction, value=0.0):
        dlg = QtWidgets.QInputDialog(self)
        dlg.setInputMode(QtWidgets.QInputDialog.DoubleInput)
        dlg.setLabelText(instruction)
        dlg.setWindowTitle(title)
        dlg.setDoubleMaximum(1024)
        dlg.setDoubleDecimals(5)
        dlg.setDoubleValue(value)
        dlg.resize(500, 100)
        ok = dlg.exec()
        return dlg.doubleValue()

    def newButton(self, name, x, y, w, h, event):
        """
        Cria um botão e retorna a instancia do mesmo.
        """
        temp = QtWidgets.QPushButton(name, self)
        temp.clicked.connect(event)
        temp.setGeometry(x, y, w, h)
        return temp

    def openFileNameDialog(self):
        """
        Cria um dialog para a leitura de arquivo.
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

    def setLastImageLabel(self, path):
        """
        setter do atributo LastImageLabel
        """
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.lastImageLabel.setPixmap(pixmap)

    def setOriginalImageLabel(self):
        """
        setter do atributo OriginalImageLabel
        """
        pixmap = QtGui.QPixmap(self.pathImage)
        pixmap = pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio)
        self.originalImageLabel.setPixmap(pixmap)

    @QtCore.Slot()
    def openDialog(self):
        """
        Evento do botão que inicia o dialog
        """
        self.pathImage = self.openFileNameDialog()
        self.setOriginalImageLabel()
        self.setLastImageLabel(self.pathImage)
        self.listImages.clear()
        self.listImages.append(imageReadCv(self.pathImage))
        self.saveLastImage()

    @QtCore.Slot()
    def undoImage(self):
        """
        Evento do botão q retrocede a imagem
        """
        if(len(self.listImages) > 1):
            try:
                self.listImages.pop()
                self.saveLastImage()
            except:
                print("Erro ao voltar imagem.'undoImage'")

    @QtCore.Slot()
    def threshholdButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro Threshhold.
        """
        varT = self.showDialogInt(
            "Valor do limiarização", "valor de 0 a 255:", 150)
        varV = self.showDialogInt("Tipo de limiarização", "valor de 0 a 4:", 0)
        try:
            image = thresholdingCv(imageReadCv(
                "lastImage.jpg"), int(varT), int(varV))
            self.listImages.append(image)
            self.saveLastImage()
        except Exception as e:
            print("Erro ao executar a Limiarização.")

    @QtCore.Slot()
    def greyScaleButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro escala de cinza.
        """
        try:
            image = greyScaleCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao converter imagem para escala de cinza.")

    @QtCore.Slot()
    def highPassBasicButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro passa alta basica.
        """
        var = self.showDialogInt("Tamanho da matriz", "valor de 1 a 12:", 3)
        try:
            image = highpassBasicCv(imageReadCv("lastImage.jpg"), int(var))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar passa alta basica.")

    @QtCore.Slot()
    def highPassButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro passa alta de alto contraste.
        """
        varM = self.showDialogInt("Tamanho da matriz", "valor de 1 a 12:", 3)
        varP = self.showDialogInt("Valor de sigma", "valor < 1:", 1)
        try:
            image = highpassCv(imageReadCv("lastImage.jpg"),
                               int(varM), int(varP))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar passa alta básica")

    @QtCore.Slot()
    def averagingButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro de média.
        """
        var = self.showDialogInt("Tamanho da matriz", "valor de 1 a 12:", 3)
        try:
            image = averagingCv(imageReadCv("lastImage.jpg"), int(var))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar passa baixa media")

    @QtCore.Slot()
    def medianButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro de mediana.
        """
        var = self.showDialogInt("Tamanho da matriz", "valor de 1 a 12:", 3)
        try:
            image = medianCv(imageReadCv("lastImage.jpg"), int(var))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicas passa baixa mediana")

    @QtCore.Slot()
    def robertsButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro roberts.
        """
        try:
            image = robertsCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Roberts.")

    @QtCore.Slot()
    def prewittButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro prewitt.
        """
        try:
            image = prewittCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Prewitt.")

    @QtCore.Slot()
    def sobelButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro sobel.
        """
        try:
            image = sobelCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image[0])
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro Sobel.")

    @QtCore.Slot()
    def logButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro de log.
        """
        try:
            image = logCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar o filtro log.")

    @QtCore.Slot()
    def cannyButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro canny.
        """
        try:
            image = cannyCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
        except:
            print("Erro ao aplicar o filtro canny.")
        self.saveLastImage()

    @QtCore.Slot()
    def saltPepperButtonEventOnClick(self):
        """
        Evento do botão que aplica o ruido salt & pepper.
        """
        var = self.showDialogDouble(
            "Frequencia do ruido", "valor de 0 a 1:", 0.004)
        try:
            image = SaltPepperCv(imageReadCv("lastImage.jpg"), float(var))
            self.listImages.append(image)
            self.saveLastImage()
        except:
            print("Erro ao aplicar ruido de salt and pepper")

    @QtCore.Slot()
    def watershedButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro watershed.
        """
        try:
            image = watershedWithCountCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image[0])
            self.saveLastImage()
        except Exception as e:
            print("Erro ao aplicar o filtro watershed."+str(e))

    @QtCore.Slot()
    def countObjectsButtonEventOnClick(self):
        """
        Evento do botão que faz a contagem de objetos.
        """
        try:
            image = watershedWithCountCv(imageReadCv("lastImage.jpg"))
            self.listImages.append(image[1])
            self.saveLastImage()
        except:
            print("Erro fazer contagem dos objetos.")

    @QtCore.Slot()
    def histogramButtonEventOnClick(self):
        """
        Evento do botão que gera o histograma.
        """
        try:
            histCv(imageReadCv("lastImage.jpg"))
            self.setLastImageLabel("histogram.jpg")
        except:
            print("Erro ao gerar histograma")

    @QtCore.Slot()
    def equalizehistogramButtonEventOnClick(self):
        """
        Evento do botão que aplica a equalização no histograma.
        """
        try:

            image = eqHist(imageReadCv("lastImage.jpg"))
            self.listImages.append(image)
            self.saveLastImage()
        except Exception as e:
            print("Erro equalizar imagem."+str(e))

    @QtCore.Slot()
    def zerocrossButtonEventOnClick(self):
        """
        Evento do botão que aplica o filtro zerocross.
        """
        varS = self.showDialogDouble("Valor de sigma", "valor de 1 a 12:", 1)
        varK = self.showDialogDouble("Valor de kappa", "valor de 0 a 1:", 0.75)
        try:
            image = laplace_of_gaussian(imageReadCv(
                "lastImage.jpg"), sigma=float(varS), kappa=float(varK))
            self.listImages.append(image)
            self.saveLastImage()
        except Exception as e:
            print("Erro ao aplicar zero cross."+str(e))

    def saveLastImage(self):
        """
        Método que salva a ultima versão da imagem.
        """
        cv2.imwrite("lastImage.jpg", self.listImages[len(self.listImages)-1])
        self.setLastImageLabel("lastImage.jpg")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1200, 800)
    widget.show()
    sys.exit(app.exec())
