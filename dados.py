import cv2 
from matplotlib import pyplot as plt

img = cv2.imread('dados.jpg',cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img,245,255,cv2.THRESH_BINARY_INV)

medianFiltered = cv2.medianBlur(thresh,5)
cv2.imshow("Median Filtered Image", medianFiltered)

contours, hierarchy = cv2.findContours(medianFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        contour_list.append(contour)

cv2.drawContours(img, contour_list, -1, (0,0,0), 2)
cv2.imshow('Objects detected', img)

for contour in contour_list:
    x,y,w,h = cv2.boundingRect(contour)
    rect = img[y:y+h, x:x+w]

print(rect)

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
