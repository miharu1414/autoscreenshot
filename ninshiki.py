
import imgsim
import cv2

def judge(path1, path2):
    img0 = cv2.imread(path1)
    img1 = cv2.imread(path2)

    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)

    dist = imgsim.distance(vec0, vec1)
    if dist > 5:
        print(dist)
        return 1
    else:
        return 0
  
a = judge("img2.png", "img1.png")

