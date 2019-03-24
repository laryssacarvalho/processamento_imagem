import glob
import cv2
import shutil
import os

def transition(img1, img2):
    for IN in range(0,5):
        fadein = IN/float(5)
        dst = cv2.addWeighted(img1, 1-fadein, img2, fadein, 0)
        cv2.imshow('Img', dst)
        key = cv2.waitKey(100)
        if key == 113:
            exit()

def watermark(img,file):
        overlay = img.copy()
        output = img.copy()
        height, width = img.shape[:2]
        alpha = 0.3
        namestamp = "Laryssa"
        cv2.putText(overlay, namestamp.format(alpha), (width-300, height-30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), thickness=2)
        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
        cv2.imwrite("watermark{}".format(file), output)

def format_images():
    for file in glob.glob('images/*.jpg'):            
        img = cv2.imread(file)
        img = cv2.resize(img,(300,300))
        img = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=BLACK)            
        watermark(img,file)

def clean_folder():
    files = glob.glob('/watermarkimages/*')
    for f in files:
        os.remove(f)
        
key = None
bordersize = 20
BLACK = [0,0,0]
previous_img = None
clean_folder()

while True:
    format_images()
    for file in glob.glob('watermarkimages/*.jpg'):
        if key != 113:
            img = cv2.imread(file)
            if previous_img is not None:
                transition(previous_img, img)
            cv2.imshow('Img', img)
            key = cv2.waitKey(2000)
            previous_img = img
        else:
            exit()
    if key == 113:
        exit()
cv2.destroyAllWindows()