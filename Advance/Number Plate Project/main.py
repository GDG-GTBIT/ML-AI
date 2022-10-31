
'''MUST READ'''
#####AIM- REAL TIME DETECTION OF
##########NUMBER PLATES AND STORING
##########THE PLATE NUMBER IN A TEXT FILE

import cv2
import os

from pytesseract import pytesseract

'''copy the path of tesseract.exe from your PC
                        ^                           |
                     library                    here|
                                                    V'''
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
from PIL import Image
import pickle
fwidth = 640
fheight = 480
nPlateCascade= cv2.CascadeClassifier("number_plate_scanning_model.xml")
minArea = 500
color = (255,0,255)
cap = cv2.VideoCapture(0)
cap.set(3, fwidth)
cap.set(4, fheight)
cap.set(10,150)

count = 0

while True:
    success, img = cap.read()
    grayimage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(grayimage,1.1,4)
 
    for (x,y,w,h) in numberPlates:
        #w*h=Area
        if (w*h)>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(img, "Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            
            newimg = img[y:y+h,x:x+w]
            cv2.imshow("Scan",newimg)
        

        cv2.imshow("Result", img)
        #REMEMBER to create a folder named scanned_images in the same directory in which your code is saved.
        cv2.imwrite("scanned_images/PlateNo_" + str(count) + ".jpg", newimg)
        path12="C:\\Users\\LENOVO\\Desktop\\Number Plate Project\\scanned_images\\PlateNo_"+str(count)+".jpg"
        if os.path.exists(path12)==True:
            Image1 = Image.open("C:\\Users\\LENOVO\\Desktop\\Number Plate Project\\scanned_images\\PlateNo_%d.jpg"%count)
            pytesseract.tesseract_cmd=path_to_tesseract
            text = pytesseract.image_to_string(Image1)
            print(text[:-1])
            d=str(text[:-1])
            f=open('NUMBER_PLATE_TEXT.txt','a+')
            f.write(d)
            f.close()
        else:
            continue
        cv2.rectangle(img , (0,200), (640,300) , (0,255,0) , cv2.FILLED )
        cv2.putText(img, "scan saved" , (150,255) , cv2.FONT_HERSHEY_DUPLEX , 
                        2,(0,0,255),2)

        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1   
        cv2.imshow("Scanned",newimg)

