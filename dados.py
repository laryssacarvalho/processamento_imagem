import cv2 
import numpy as np
from matplotlib import pyplot as plt
import glob

img = cv2.imread('dados.jpg',cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img,245,255,cv2.THRESH_BINARY_INV)

medianFiltered = cv2.medianBlur(thresh,5)

contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        contour_list.append(contour)

cv2.drawContours(img, contour_list, -1, (255,255,255), 2)
cv2.imshow('Objects detected', img)

idx = 0
for contour in contour_list:
    idx += 1
    x,y,w,h = cv2.boundingRect(contour)
    roi=img[y:y+h,x:x+w]
    cv2.imwrite('dados_recortados/'+ str(idx) + '.jpg', roi)
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)

i = 0
for file in glob.glob('dados_recortados/*.jpg'):
	img_dado = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
	ret,thresh_dado = cv2.threshold(img_dado,127,255,cv2.THRESH_BINARY_INV)	
	i+=1

	detector = cv2.SimpleBlobDetector_create()
	keypoints = detector.detect(img_dado)
	
	height_dado, width_dado = img_dado.shape[:2]
	print("Altura do dado: " + str(height_dado) + " Largura do dado: " + str(width_dado))
	posicao = (width_dado-30, height_dado-5)

	height, width = img.shape[:2]

	cv2.putText(img_dado, str(len(keypoints)), (posicao), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0))
	# cv2.putText(img, str(len(keypoints)), (width-posicao[0], height-posicao[1]), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0))
	cv2.imshow("Blobs = "+ str(i), img_dado)
# print("Altura da imagem: " + str(height) + " Largura da imagem: " + str(width))
# cv2.imshow("Original ", img)

cv2.waitKey(0)
