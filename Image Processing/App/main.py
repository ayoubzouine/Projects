################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import numpy as np 
import  matplotlib.pyplot as plt
import cv2
import scipy
import base64
from ImageClass import ImageClass

import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from ui_binarisation import Ui_Dialog

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
from ui_resize import Ui_ResizeDialog

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path=""
        self.mainImg=np.array([])
        self.pixmap=QtGui.QPixmap()
        self.resultPixmap=QtGui.QPixmap()
        self.imageClass=ImageClass(self.pixmap)
        self.rotationAngle=0
        self.resultImg=[[]];

        self.dialog = QDialog(self)
        self.resizeDialog = QDialog(self)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 170, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_basic))

        # PAGE 2
        self.ui.btn_basic.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_basic), self.ui.label_image_menu_basic.setPixmap(QtGui.QPixmap(self.pixmap))))

        # PAGE 3
        self.ui.btn_filtre.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_fltr_median),self.ui.label_img_med.setPixmap(QtGui.QPixmap(self.getPixmap(self.mainImg,self.ui.label_img_med.width(),self.ui.label_img_med.height())))))
        
        # PAGE 5
        self.ui.btn_morpho.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_morpho), self.ui.label_img_morpho.setPixmap(QtGui.QPixmap(self.pixmap))))
        
        # PAGE 6
        self.ui.btn_seg.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_segmentation),self.ui.label_img_segmentation.setPixmap(QtGui.QPixmap(self.getPixmap(self.mainImg,self.ui.label_img_segmentation.width(),self.ui.label_img_segmentation.height())))))
        
        # PAGE 6
        self.ui.btn_contour.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_contour), self.ui.label_img_contour.setPixmap(QtGui.QPixmap(self.getPixmap(self.mainImg,self.ui.label_img_contour.width(),self.ui.label_img_contour.height())))))
        
        # PAGE 6
        self.ui.btn_compression.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_compression), self.ui.label_img_compress.setPixmap(QtGui.QPixmap(self.getPixmap(self.mainImg,self.ui.label_img_compress.width(),self.ui.label_img_compress.height())))))

        #PAGE 
        self.ui.btn_interet.clicked.connect(lambda: (self.ui.pages_widget.setCurrentWidget(self.ui.page_pnts_interet), self.ui.label_img_interet.setPixmap(QtGui.QPixmap(self.getPixmap(self.mainImg,self.ui.label_img_interet.width(),self.ui.label_img_interet.height())))))
        #/////////////////// BASIC MENU BUTTONS ///////////////////#
        ui = self.ui

        ui.btn_negatif.clicked.connect(lambda: self.handleNegatif(self.mainImg))
        ui.btn_etirer.clicked.connect(lambda: self.handleEtirement(self.mainImg))
        ui.btn_rotation.clicked.connect(lambda: self.handleRotation(self.mainImg))
        ui.btn_egaliser.clicked.connect(lambda: self.handleEgalisation(self.mainImg))
        ui.btn_histogramme.clicked.connect(lambda: self.handleHist(self.mainImg))
        ui.btn_binarisation.clicked.connect(lambda: self.handleBinarisationDialog(self.mainImg))
        ui.btn_redimensionner.clicked.connect(lambda: self.handleResiseDialog(self.mainImg))
        ui.btn_selectioner.clicked.connect(lambda: self.handleSelect(self.mainImg))
        #//////////////////////////////////////////////////////////#

        #////////////////// MORPHOLOGY MENU ///////////////////////#
        ui.btn_calculer_morpho.clicked.connect(lambda: self.handleMorpho(self.mainImg))
        ui.btn_calculer_contour.clicked.connect(lambda: self.handleContour(self.mainImg))
        ui.btn_calculer_seg.clicked.connect(lambda: self.handleSegmentation(self.mainImg))
        ui.btn_fltr_med.clicked.connect(lambda: self.handleFiltrage(self.mainImg))
        ui.btn_compress.clicked.connect(lambda: self.handleCompresse(self.mainImg))
        ui.btn_calculer_interet.clicked.connect(lambda: self.handleInteret(self.mainImg))
        #//////////////////////////////////////////////////////////#

        self.ui.file_comboBox.model().item(0).setEnabled(False)
        # OPEN FILE
        self.ui.file_comboBox.currentIndexChanged.connect(self.on_combobox_changed)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    def on_combobox_changed(self,index):
        if index==1: self.openFile()
        elif index==2:
            1;
        elif index==3:
            1;
        elif index==4:
            1

    def openFile(self):
        fileName = QFileDialog.getOpenFileName()
        self.path = fileName[0]
        self.mainImg = cv2.imread(self.path)

        pixmap = QPixmap(self.path)
        pixmap = pixmap.scaled(self.ui.label_image_menu_basic.width(),self.ui.label_image_menu_basic.height())
        self.pixmap = pixmap
        
        self.ui.label_image_menu_basic.setPixmap(QtGui.QPixmap(self.pixmap))
        self.ui.file_comboBox.setCurrentIndex(0)


    def handleHist(self,img):
        """
            Affiche l'histogramme d'une image donnée(img).
        """
        hist = cv2.calcHist(img, [0], None, [256], [0, 256])
        plt.plot(hist)
        plt.title("histogrmme")
        plt.show()
    
    def handleNegatif(self, img):
        """
            Applique une inversion de couleurs (négatif) à une image donnée (`255-img pour les images RGB`).
            (`255 - (r, g ou b) pour les différents spectres des images RVB, puis reconstruit l'image résultante`).
        """
        self.imageClass = ImageClass(img)
        result = self.imageClass.negatif(img)
        self.resultImg = result
        
        image = self.getQImage(result)
            
        pixmap = QtGui.QPixmap(image)
        pixmap = pixmap.scaled(self.ui.label_image_menu_basic.width(),self.ui.label_image_menu_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))


    def handleEtirement(self,img):
        """
            Applique une opération d'étirement de contraste à une image donnée.
        """
        self.imageClass = ImageClass(img)

        img = self.imageClass.etire()
        
        result = QtGui.QImage(
            img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(result)
        pixmap = pixmap.scaled(self.ui.label_image_menu_basic.width(),self.ui.label_image_menu_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))


    def handleRotation(self, img):
        """
            Effectue une rotation de l'image donnée par defaut(angle de rotation=-45deg).
        """

        self.imageClass = ImageClass(img)

        self.rotationAngle-=45
        result = self.imageClass.rotate_image(self.rotationAngle)
        image = self.getQImage(result)

        pixmap = QtGui.QPixmap(image)
        pixmap = pixmap.scaled(self.ui.label_image_menu_basic.width(),self.ui.label_image_menu_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))



    def getQImage(self, img):
        height, width, byteValue = img.shape
        if byteValue:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue *
                                width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(
                img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            
        return imag
    

    def getPixmap(self,img,width,height):
        result = self.getQImage(img)
        pixmap = QPixmap(result)
        pixmap = pixmap.scaled(width,height)

        return pixmap


    def handleBinarisationDialog(self, img):
        """
            Afficher le dialog box pour la binarisation.
        """
        
        self.dialog = QDialog(self)
        
        self.dialog.ui = Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        ui = self.dialog.ui
        ui.comboBox.currentIndexChanged.connect(lambda: self.handleBinarisationType())
        ui.pushButton_2.clicked.connect(lambda: self.handleBinarisation(self.mainImg))
        self.dialog.exec_()


    def handleBinarisationType(self):
        """
            Changer le comportement de dialog box en fonction du type de binarisation selectionné.
        """
        ui = self.dialog.ui
        type = ui.comboBox.currentText()

        if type=='OTSU':
            ui.spinBox.setDisabled(True)
        else:
            ui.spinBox.setDisabled(False)

    
    def handleBinarisation(self, img):
        """
            Effectue une binarisation de l'image donnée selon le seuil donné ou automatiquement(OTSU).
        """
        ui = self.dialog.ui
        type = ui.comboBox.currentText()
        thresh = int(ui.spinBox.text())

        # Convert the image to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        if type=='Par seuil':
            # Apply thresholding
            ret, result = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
        elif type=='OTSU':
            ui.spinBox.setDisabled(True)

            # Apply Otsu's method
            _, result = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        result = cv2.cvtColor(result, cv2.COLOR_GRAY2RGB)
        pixmap = self.getPixmap(result,self.ui.label_result_basic.width(),self.ui.label_result_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))
        # Close the dialog
        self.dialog.reject()


    def handleSelect(self, img):
        """
            Permet à l'utilisateur de sélectionner une région d'intérêt (ROI) dans l'image et affiche la région sélectionnée.
        """
        # Select ROI
        r = cv2.selectROI(img)

        # Crop image
        imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

        pixmap = self.getPixmap(imCrop,self.ui.label_result_basic.width(),self.ui.label_result_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))


    def handleResiseDialog(self, img):
        """
        Ouvre une boîte de dialogue pour redimensionner l'image donnée.
        """

        self.resizeDialog = QDialog(self)
        
        self.resizeDialog.ui = Ui_ResizeDialog()
        self.resizeDialog.ui.setupUi(self.resizeDialog)
        ui = self.resizeDialog.ui
        
        ui.enter.clicked.connect(lambda: self.handleresize(img))
        self.resizeDialog.exec_()

    def handleresize(self, img):
        """
        Redimensionne l'image donnée en fonction des dimensions spécifiées dans la boîte de dialogue.
        """
        ui = self.resizeDialog.ui
        img_width = int(ui.width.text())
        img_height = int(ui.height.text())

        # Get the original image size
        # h, w = img.shape[:2]
        # new_h = int(h * (new_w / float(w)))

        resized_img = cv2.resize(img, (img_width, img_height))
        pixmap = self.getPixmap(resized_img,self.ui.label_result_basic.width(),self.ui.label_result_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))
        self.resizeDialog.reject()

    def handleEgalisation(self,img):
        """
        Applique une opération d'égalisation d'histogramme à l'image donnée.
        """
        self.imageClass = ImageClass(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(gray)
        imag = QtGui.QImage(
            img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        
        pixmap = QtGui.QPixmap(imag)
        pixmap = pixmap.scaled(self.ui.label_image_menu_basic.width(),self.ui.label_image_menu_basic.height())
        self.ui.label_result_basic.setPixmap(QtGui.QPixmap(pixmap))



    def handleMorpho(self,img):
        structrantElements = {"3x3":np.ones((3,3),int),"4x4":np.ones((4,4),int),
                              "5x5":np.ones((5,5),int),"7x7":np.ones((7,7),int),
                              "11x11":np.ones((11,11),int),"45x45":np.ones((45,45),int)}
        typeMorpho = self.ui.comboBox_morpho.currentText()

        element = structrantElements[self.ui.comboBox_morpho_elem.currentText()]

        if typeMorpho=="Erosion":
            result = cv2.erode(img,element)
        elif typeMorpho=="Dilatation":
            result = cv2.dilate(img,element)
        elif typeMorpho=="Fermeture":
            result = cv2.morphologyEx(img,cv2.MORPH_CLOSE,element)
        elif typeMorpho=="Ouverture":
            result = cv2.morphologyEx(img,cv2.MORPH_OPEN,element)
        elif typeMorpho=="Filtrage morpho":
            ouverture = cv2.morphologyEx(img,cv2.MORPH_OPEN,element)
            result = cv2.morphologyEx(ouverture,cv2.MORPH_CLOSE,element)

        # result = self.getQImage(result)
        # pixmap = QtGui.QPixmap(result)
        # pixmap = pixmap.scaled(self.ui.label_rslt_morpho.width(),self.ui.label_rslt_morpho.height())
        pixmap = self.getPixmap(result,self.ui.label_rslt_morpho.width(),self.ui.label_rslt_morpho.height())
        self.ui.label_rslt_morpho.setPixmap(QtGui.QPixmap(pixmap))


    def handleContour(self,img):
        typeContour = self.ui.comboBox_contour.currentText()
        img2 = img.copy()
        if typeContour=="Sobel":
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply Sobel filters
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

            # Calculate the gradient magnitude
            mag = np.sqrt(sobelx**2 + sobely**2)
            mag = cv2.convertScaleAbs(mag)
            # gray = cv2.cvtColor(mag, cv2.COLOR_BGR2GRAY)
            # Apply threshold to create a binary mask
            _, mask = cv2.threshold(mag, 50, 255, cv2.THRESH_BINARY)

            # Find the contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw the contours on the original image
            cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)


        elif typeContour=="Robert":
            kernelx = np.array([[-1,0],[0,1]], dtype=np.float32)
            kernely = np.array([[0,-1],[1,0]], dtype=np.float32)

            gx = cv2.filter2D(img, -1, kernelx)
            gy = cv2.filter2D(img, -1, kernely)

            mag = np.sqrt(gx**2 + gy**2).astype(np.uint8)
            gray = cv2.cvtColor(mag, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)


        elif typeContour=="Laplacien":
            img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Appliquer un filtre Laplacien à l'image
            laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
            laplacian = cv2.convertScaleAbs(laplacian)
            # Seuiller l'image
            _, binary = cv2.threshold(laplacian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Trouver les contours dans l'image binaire
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Dessiner les contours sur l'image originale
            cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)


        elif typeContour=="Gradient":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Kernel for horizontal gradient (Prewitt)
            kx = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])

            # Kernel for vertical gradient (Prewitt)
            ky = np.array([[-1, -1, -1],
                        [0, 0, 0],
                        [1, 1, 1]])
            # Calculer les gradients en utilisant le filtre de Prewitt
            dx = cv2.filter2D(gray, -1, kx)
            dy = cv2.filter2D(gray, -1, ky)

            dx = cv2.convertScaleAbs(dx)
            dy = cv2.convertScaleAbs(dy)

            # Calculer la magnitude du gradient
            mag = np.sqrt(dx**2 + dy**2).astype(np.uint8)

            # Appliquer un seuillage adaptatif pour obtenir l'image binaire des contours
            _, binary = cv2.threshold(mag, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Trouver les contours dans l'image binaire
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Dessiner les contours sur l'image originale
            cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)


        pixmap = self.getPixmap(img2,self.ui.label_img_contour.width(),self.ui.label_img_contour.height())
        self.ui.label_rslt_contour.setPixmap(pixmap)


    def handleSegmentation(self,img):
        typeSegmantation = self.ui.comboBox_seg.currentText()

        if typeSegmantation==" Croissance de régions D":
            result = self.regionGrowing(img)
        elif typeSegmantation==" Partition de régions D":
            result = self.imageClass.split_merge(img,min_size=100, max_stddev=20.0)
        elif typeSegmantation==" Méthode des k-means":
            result = self.segmentationKmeans(img)

        pixmap = self.getPixmap(result,self.ui.label_rslt_segmentation.width(),self.ui.label_rslt_segmentation.height())
        self.ui.label_rslt_segmentation.setPixmap(pixmap)


    def regionGrowing(self,img):
        # définir la graine
        seed = (100, 100)

        # définir les paramètres de seuillage et de croissance de région
        thresh = 10
        min_size = 10
        max_size = 1000

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Initialiser la région de départ avec le point de départ
        region = np.zeros_like(gray)
        region[seed[1], seed[0]] = 255
        
        # Parcourir les pixels voisins et les ajouter à la région si ils répondent aux critères de similarité
        while True:
            old_region = np.copy(region)
            
            for y in range(1, img.shape[0]-1):
                for x in range(1, img.shape[1]-1):
                    if region[y, x] == 255:
                        if abs(int(gray[y, x]) - int(gray[y-1, x])) < thresh:
                            region[y-1, x] = 255
                        if abs(int(gray[y, x]) - int(gray[y+1, x])) < thresh:
                            region[y+1, x] = 255
                        if abs(int(gray[y, x]) - int(gray[y, x-1])) < thresh:
                            region[y, x-1] = 255
                        if abs(int(gray[y, x]) - int(gray[y, x+1])) < thresh:
                            region[y, x+1] = 255
            
            # Si la région n'a pas été agrandie, arrêter la boucle
            if np.array_equal(region, old_region):
                break
            
        region = cv2.cvtColor(region, cv2.COLOR_GRAY2BGR)
        return region


    def segmentationKmeans(self,img):
        # Redimensionner l'image si nécessaire
        img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

        # Transformer l'image en un tableau de pixels
        Z = img.reshape((-1,3))
        Z = np.float32(Z)

        # Spécifier les critères d'arrêt pour l'algorithme K-means
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        # Spécifier le nombre de clusters (k)
        k = 3

        # Appliquer l'algorithme K-means
        ret,label,center=cv2.kmeans(Z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # Convertir les centres des clusters en entiers
        center = np.uint8(center)

        # Convertir chaque pixel de l'image en la couleur de son cluster correspondant
        res = center[label.flatten()]
        res2 = res.reshape((img.shape))    

        return res2


    def handleFiltrage(self, img):
        typeFiltre = self.ui.comboBox_filtre.currentText()
        structrantElements = {"3x3":(3,3),"4x4":(4,4),
                              "5x5":(5,5),"7x7":(7,7),
                              "11x11":(11,11),"45x45":(45,45)}
        
        element = structrantElements[self.ui.comboBox2_filtre.currentText()]
        if typeFiltre=="Gaussien":
            result = cv2.GaussianBlur(img, element, 0)
        if typeFiltre=="Median":
            result = cv2.medianBlur(img, element[0])
        if typeFiltre=="Moyenneur":
            result = cv2.blur(img, element)

        pixmap = self.getPixmap(result, self.ui.label_rslt_med.width(), self.ui.label_rslt_med.height())
        self.ui.label_rslt_med.setPixmap(pixmap)



    def handleCompresse(self, img):
        typeCompression = self.ui.comboBox_compress.currentText()

        if typeCompression=="Huffman":
            encoded, codes = self.imageClass.huffman_encode(img)
            filepath = "./results/result_huffman"
        elif typeCompression=="LZW":
            encoded, codes = self.imageClass.lzw_encode(img)
            filepath = "./results/result_lzw"
        elif typeCompression=="Ondelette":
            encoded, codes = self.imageClass.ondelette_encode(img)
            filepath = "./results/result_ondelette"
        else:
            print("Compression type not recognized.")
            return
        
        # Convert the encoded data to a byte array
        byte_array = bytearray(base64.b64decode(encoded))

        # Convert the byte array to a numpy array
        np_array = np.asarray(byte_array, dtype=np.uint8)

        with open(filepath+".bin", "wb") as f:
            f.write(encoded)

        with open(filepath+'.bin', 'rb') as f:
            encoded_data = f.read()

        # Convert the encoded data to a numpy array
        encoded_array = np.frombuffer(encoded_data, dtype=np.uint8)
        print('encoded : ',encoded_array)
        # Decode the array as an image
        # decoded = self.imageClass.huffman_decode(encoded, codes)
        # print('decoded')
        
        result = cv2.imdecode(encoded_array, cv2.IMWRITE_JPEG_QUALITY)
        # cv2.imwrite(filepath, result)



    def handleInteret(self,img):
        typeInteret = self.ui.comboBox_interet.currentText()
        img2 = img.copy()
        if typeInteret=="Hough":
            # Convertir l'image en niveaux de gris
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Appliquer un flou gaussien pour réduire les bruits
            blur = cv2.GaussianBlur(gray, (5,5), 0)

            # Détecter les cercles dans l'image
            circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, minDist=20,
                                    param1=50, param2=30, minRadius=0, maxRadius=0)

            # Convertir les coordonnées des cercles (x,y,r) en entiers
            circles = np.uint16(np.around(circles))

            # Dessiner les cercles détectés sur l'image
            for i in circles[0,:]:
                # Dessiner le cercle
                cv2.circle(img2, (i[0],i[1]), i[2], (0,255,0), 2)
                # Dessiner le centre du cercle
                cv2.circle(img2, (i[0],i[1]), 2, (0,0,255), 3)

        elif typeInteret=="Gabor":
            # Créer le filtre de Gabor
            ksize = 31
            sigma = 5
            theta = 0
            lamda = 10
            gamma = 0.5
            psi = 0
            kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, psi, ktype=cv2.CV_32F)

            # Appliquer le filtre de Gabor
            filtered = cv2.filter2D(img, cv2.CV_8UC3, kernel)

            # Détecter les points d'intérêt avec la méthode Gabor
            detector = cv2.SimpleBlobDetector_create()
            keypoints = detector.detect(filtered)

            # Dessiner les cercles autour des points d'intérêt trouvés
            img2 = cv2.drawKeypoints(img2, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


        elif typeInteret=="Shi-Tomasi":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Define parameters for Shi-Tomasi algorithm
            max_corners = 100
            quality_level = 0.3
            min_distance = 7

            # Apply Shi-Tomasi corner detection
            corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level, min_distance)

            # Draw detected corners on image
            corners = np.int0(corners)
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(img2, (x, y), 5, (0, 255, 0), -1)

        pixmap = self.getPixmap(img2, self.ui.label_rslt_interet.width(), self.ui.label_rslt_interet.height())
        self.ui.label_rslt_interet.setPixmap(pixmap)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())