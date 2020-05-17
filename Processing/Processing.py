import cv2
from ImageProcessor_Otsu import Picture
from tensorflow.keras.models import load_model
import time

class Model:#Processor поменял на Model
    def __init__(self):
        self.Data_query = []
        self.Meta_query = []
        self.model = load_model("convolutional_4.h5")
    def put_new_data(self, Data, Metadata):
        self.Data_query.append(Data)
        self.Meta_query.append(Metadata)
    def isEmpty_query(self):
        pass 
    def process_image(self, image):
        begin = time.time()
        pic = Picture(image,self.model)
        print(time.time()-begin)
        print(pic.text)

#begin = time.time()
proc = Model()
for i in range(0,29):
    image = cv2.imread("testing\\pics\\"+str(i)+".bmp")
    cv2.imshow("1",image)
    cv2.waitKey(0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    proc.process_image(gray)
#resized = cv2.resize(image,(image.shape[1]*2,image.shape[0]*2))
#cv2.imshow("1",resized)
#cv2.waitKey(0)

proc = Model()

