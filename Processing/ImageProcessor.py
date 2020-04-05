from PIL import Image, ImageDraw
from sklearn.cluster import KMeans
import numpy as np

class Symbol:

    def __skeletonize(self, image): #обработчики символов
        pass
    
    def __resize(self,image):
        pass

    def __init__(self, image, clustermap):
        self.width = image.size[0]
        self.height = image.size[1]
        self.clustermap = clustermap
        self.pix = image.load()
        self.image = image #нужно ли?
       
class String:

    def __slice(self,image):
        def isEmptyColumn(x):
            for y in range(0,self.height):
                if self.clustermap[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]] == 1:
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
                    self.symbols_image.append(image.crop((begin-1,0,end+1,self.height))) 
                    break
            cursor+=1

    def __init__(self, image, clustermap):
        self.symbols_image = []
        self.symbols = []
        self.text = []
        self.pix = image.load()
        self.width = image.size[0]
        self.height = image.size[1]
        self.clustermap = clustermap
        self.__slice(image)
        for i in self.symbols_image:
            self.symbols.append(Symbol(i,self.clustermap))
            
class Picture:

    def __binarize(self, image):
        self.pix = image.load()
        colorlist = np.zeros((256,256,256))
        lister = []
        counter = 0
        for x in range(0,self.width):
            for y in range(0,self.height):
                if colorlist[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]]==0:
                    colorlist[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]] = 1
                    lister.append((self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]))
                    counter += 1
        colorlist = lister
        kmeans = KMeans( n_clusters = 2, max_iter = 25)
        kmeans.fit(colorlist)
        predictions = kmeans.predict(colorlist)
        #check{
        if (predictions[0]==1):
            for i in range(0,len(predictions)):
                predictions[i]=1-predictions[i]
        #}
        for i in range(0, len(colorlist)):
            if predictions[i] == 0:
                self.clusters[0].append(colorlist[i])
            else:
                self.clustermap[colorlist[i][0],colorlist[i][1],colorlist[i][2]] = 1
                self.clusters[1].append(colorlist[i])

    def draw(self,image):
        draw = ImageDraw.Draw(image)        
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.clusters[0].count(((self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2])))!=0:
                    draw.point((x,y),(255,255,255))
                else:
                    draw.point((x,y),(0,0,0))

    def __slice(self,image):
        def isEmptyString(y):
            for x in range(0,self.width):
                if self.clustermap[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]] == 1:
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
                    self.strings_image.append(image.crop((0,begin-1,self.width,end+1))) 
                    break
            cursor+=1
    
    def __init__(self, image):
        self.strings_image = []
        self.strings = []
        self.text = []
        self.clusters = [[],[]]
        self.clustermap = np.zeros((256,256,256))
        self.width = 0
        self.height = 0
        self.width = image.size[0]
        self.height = image.size[1]
        self.__binarize(image)
        self.__slice(image)
        for i in self.strings_image: #нужно засунуть в __slice
            self.strings.append(String(i,self.clustermap)) 
