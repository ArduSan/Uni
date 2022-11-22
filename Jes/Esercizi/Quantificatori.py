pic1=makePicture(pickAFile())
pic2=makePicture(pickAFile())

def lum(p):
#@param p: list of pixel
#@return int: lum = R+G+B
    return getRed(p)+getBlue(p)+getGreen(p)

def equilum(pic1,pic2):
#@param pic1:picture
#@param pic2:picture
#@return bool
    px1=getPixels(pic1)
    for i in range(0, len(px1)):
        if lumpic2(lum(px1[i]))==False:
            return False
     return True


def lumpic2(lumn):
#@param lumn:luminosity of pixels
#@return bool
    px2=getPixels(pic2)
    for j in range(0, len(px2)):
        if lumn==lum(px2[j]):
            return True
    return False
