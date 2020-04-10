import numpy as np
import cv2 

class Symbol:

    def __skeletonize(self, image): #обработчики символов
        pass
    
    def __resize(self,image):
        pass

    def __init__(self, image, binary_image):
        self.width = image.shape[1]
        self.height = image.shape[0]
        self.binary_image = binary_image
        self.image = image
        cv2.imshow("1", image)
        cv2.waitKey()
       
class String:

    def __slice(self,image):
        def isEmptyColumn(x):
            for y in range(0,self.height):
                if self.binary_image[y,x] != self.binary_image[0,0]:
                    return False
            return True
        cursor = 1
        while cursor < self.width:
            begin = cursor
            while isEmptyColumn(cursor) == False:
                cursor += 1
                if (cursor==self.width):
                    break
                if isEmptyColumn(cursor) == True:
                    end = cursor
                    self.symbols_image.append(image[0:self.height+1, begin:end+1]) 
                    self.symbols.append(Symbol(image[0:self.height+1, begin:end+1],self.binary_image[0:self.height, begin:end]))
                    break
            cursor+=1

    def __init__(self, image, binary_image):
        self.symbols_image = [] #может пригодиться для отладки
        self.symbols = []
        self.text = []
        self.width = image.shape[1]
        self.height = image.shape[0]
        self.binary_image = binary_image
        self.__slice(image)
            
class Picture:

    def __binarize(self, image):
        ret, thresh = cv2.threshold(image,0,255,cv2.THRESH_OTSU)
        return thresh
        
    def __slice(self,image):
        def isEmptyString(y):
            for x in range(0,self.width):
                if self.binary_image[y,x] != self.binary_image[0,0]:
                    return False
            return True
        cursor = 1
        while cursor < self.height:
            begin = cursor
            while isEmptyString(cursor) == False:
                cursor += 1
                if (cursor==self.height):
                    break
                if isEmptyString(cursor) == True:
                    end = cursor
                    self.strings_image.append(image[begin:end+1,0:self.width+1]) 
                    self.strings.append(String(image[begin:end+1,0:self.width+1], self.binary_image[begin:end+1,0:self.width+1])) 
                    break
            cursor+=1
    
    def __init__(self, image):
        self.strings_image = [] #может пригодиться для отладки
        self.strings = []
        self.text = []
        self.width = image.shape[1]
        self.height = image.shape[0]
        self.binary_image = self.__binarize(image)
        self.__slice(image)