import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

#dado uma imagem de um dado, retorna o valor dele
def valorDado(img):
    detector = cv2.SimpleBlobDetector_create()
    keypoints = detector.detect(img)
    return len(keypoints)


font = cv2.FONT_HERSHEY_SIMPLEX
valores = [] 

img = cv2.imread('dados.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY_INV)

medianFiltered = cv2.medianBlur(thresh, 5)

contours, hierarchy = cv2.findContours(
    medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        contour_list.append(contour)

cv2.drawContours(img, contour_list, -1, (255, 255, 255), 2)
#cv2.imshow('Objects detected', img)

idx=0
for contour in contour_list:
    idx += 1
    x, y, w, h = cv2.boundingRect(contour)
    roi = img[y:y+h, x:x+w]
    
    #escreve o valor retornados da função valorDado na imagem
    cv2.putText(img, str(valorDado(roi)), (x+w, y+h), font, 1, (0,0,255), thickness=3)    
    
    #desenha retangulo
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

#exibe a imagem com os valores
cv2.imshow('img', img)

#tentanto exibir colorido
img_cor = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
cv2.imshow('img_cor', img_cor)

cv2.waitKey(0)
