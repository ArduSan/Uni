

def colorDivers(pic):
    px=getPixels(pic)
    for i in range (0, len(px)):
        for j in range(0,len(px)):
            colpx=getColor(px[i])
            colpx2=getColor(px[j])
            if colpx!=colpx2:
                count+=1
    return count

def almenoK(pic,k):
    if colorDivers(pic)>=k:
        return True
    return False

def foo(pic1,pic2,k):
    if almenoK(pic1,k) and almenoK(pic2,k):
        return True
    return False
