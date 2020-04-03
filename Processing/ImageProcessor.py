from PIL import Image, ImageDraw
from sklearn.cluster import KMeans
import networkx
import numpy as np

class String:
    N = 12
    symbols_image = []
    text = []
    def __slice(self,image):
        def isEmptyColumn(x):
            for y in range(0,self.height):
                if self.clustermap[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]] == 1:
                    return False
            return True

        begin = []
        end = []
        cursor = 0
        while cursor < self.width:
            if isEmptyColumn(cursor) == False:
                begin.append(cursor)
                for counter in range(cursor,self.width):
                    if isEmptyColumn(counter) == True:
                        end.append(counter-1)
                        self.symbols_image.append(image.crop((0,begin[-1],self.width,end[-1]))) #не всегда срабатывает
                        cursor = counter
                        break
                if counter == self.width-1:
                    break
            else:
                for counter in range(cursor, self.width):
                    if isEmptyColumn(counter) == False:
                        cursor = counter
                        break
                if counter == self.width-1:
                    break

    def __init__(self, image, clustermap):
        self.pix = image.load()
        self.width = image.size[0]
        self.height = image.size[1]
        self.clustermap = clustermap
        self.__slice(image)
      #  while self.height < self.N:
     #       self.width *= 2
      #      self.height *= 2
      #      image = image.resize((self.width, self.height))
            


class Pic:

    strings_image = []
    text = []
    clusters = [[],[]]
    clustermap = np.zeros((256,256,256))

    width = 0
    height = 0
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
        for i in range(0, len(colorlist)):
            if predictions[i] == 0:
                self.clusters[0].append(colorlist[i])
            else:
                self.clustermap[colorlist[i][0],colorlist[i][1],colorlist[i][2]] = 1
                self.clusters[1].append(colorlist[i])
        print (counter)

    def draw(self,image):
        draw = ImageDraw.Draw(image)        
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.clusters[0].count(((self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2])))!=0:
                    draw.point((x,y),(255,255,255))
                else:
                    draw.point((x,y),(0,0,0))
        image.save("C:\Buffer\\Samples\\result.PNG")

    def __slice(self,image):

        def isEmptyString(y):
            for x in range(0,self.width):
                if self.clustermap[self.pix[x,y][0],self.pix[x,y][1],self.pix[x,y][2]] == 1:
                    return False
            return True

        begin = []
        end = []
        cursor = 0
        while cursor < self.height:
            if isEmptyString(cursor) == False:
                begin.append(cursor)
                for counter in range(cursor,self.height):
                    if isEmptyString(counter) == True:
                        end.append(counter-1)
                        self.strings_image.append(image.crop((0,begin[-1],self.width,end[-1]))) #не всегда срабатывает
                        cursor = counter
                        break
                if counter == self.height-1:
                    break
            else:
                for counter in range(cursor, self.height):
                    if isEmptyString(counter) == False:
                        cursor = counter
                        break
                if counter == self.height-1:
                    break
            

    def __init__(self, image):
        self.width = image.size[0]
        self.height = image.size[1]
        self.__binarize(image)
        self.__slice(image)


image = Image.open("C:\Buffer\\Samples\\4.PNG")
import time
begin = time.time()
pic = Pic(image)
#pic.strings_image[0].save("C:\Buffer\\Samples\\result.PNG")
image = Image.open("C:\Buffer\\Samples\\result1.PNG")
string = String(image,pic.clustermap)
string.symbols_image[0].save("C:\Buffer\\Samples\\symbol.png")
#pic.draw(image)
end = time.time()
print(end-begin)