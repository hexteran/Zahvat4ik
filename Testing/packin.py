import os
import cv2

def compress(image):
    height = image.shape[0]
    width = image.shape[1]
    N = 0
    lister = []
    output = []
    for y in range(0, height):
        for x in range(0,width):
            if N>=height:
                r = 0
                for i in range(0, N):
                    if lister[i]==0:
                        r+=pow(2,i)
                N=0
                lister = []
                output.append(r)  
            lister.append(image[y,x])
            N+=1 
    r = 0
    for i in range(0, N):
        if lister[i]==0:
            r+=pow(2,i)
    output.append(r)  
    return output

def decompress(r, height, width):
    out = []
    #print (len(r))
    for i in r:
        column = []
        for digit in range(0, height):
            if int(i/(pow(2, digit)))%2 == 1:
                column.append(0)
            else:
                column.append(255)
        out.append(column)
    return out

def unpack(file):
    f = open(file,"r")
    string = f.read()
    split = string.split()
    split = [int(i) for i in split]
    height = split[0]
    width = split[1]
    f.close()
    file = []
    for i in range(0, int((len(split)-2)/width)):
        #for x in range(0, width):
        picture = (decompress(split[2+i*width:2+i*width+width], height, width))
        file.append(picture)
    return file

def check(a,b):
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            return False
    return True

def checkmatrix(a,b):
    for i in range(0,16):
        for j in range(0,16):
            if a[i][j] != b[i,j]:
                return False
    return True

def pack(path, file, height,width):
    fe = open(file,"w")
    fe.write(str(height)+" "+str(width)+" ")
    out = []
    gro = []
    for r,d,f in os.walk(path):
        for file in f:
            image = cv2.imread(path+"\\"+file)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gro.append(gray)
            out.append(compress(gray))
          #  m = decompress(out[-1],height,width)
    for i in out:
        for g in i:
            fe.write(str(g)+" ")
    fe.close()

