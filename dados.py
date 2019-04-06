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
cv2.imshow('img',img)

i = 0
for file in glob.glob('dados_recortados/*.jpg'):
	img_dado = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
	ret,thresh_dado = cv2.threshold(img_dado,127,255,cv2.THRESH_BINARY_INV)
	cv2.imshow("Dado " + str(i), thresh_dado)
	i+=1


# print(rect)

# Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()

# params.blobColor = 255
# params.filterByColor = True 

# # Change thresholds
# # params.minThreshold = 10
# # params.maxThreshold = 200

# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.785
# params.maxCircularity = 0.785

# ver = (cv2.__version__).split('.')
# if int(ver[0]) < 3 :
#     detector = cv2.SimpleBlobDetector(params)
# else : 
#     detector = cv2.SimpleBlobDetector_create(params)

# Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector_create()
 
# keypoints = detector.detect(thresh)

# print("Blobs = ", len(keypoints))
# for marker in keypoints:
#     #center
#     x,y = np.int(marker.pt[0]),np.int(marker.pt[1])
#     pos = np.int(marker.size / 2)
#     cv2.rectangle(thresh2,(x-pos,y-pos),(x+pos,y+pos),(255,0,0),1)
    
# cv2.imshow("Blobs = "+ str(len(keypoints)), thresh)
# cv2.imshow("Blobs",thresh)


cv2.waitKey(0)
