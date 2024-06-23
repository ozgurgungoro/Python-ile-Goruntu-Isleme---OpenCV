import cv2
import numpy as np 


# Resmi yükleme
resim = cv2.imread("kus.jpg")


# resimden bölge kesme

kesit = resim[50:150,300:400]    #  [50:150   bu iki alan y kordinatı  ,300:400     bu iki alan x kordinatı]


resim[100:200,100:200]=kesit           


# resim[ : ,: ,2]=255        # 0 mavi   # 2 kırmızı



resim[400:450,300:350]=(0,150,255)



# y parametresi    soldan aşşağa in 



# cv2.imshow("Kesit Alani",kesit)



# Resmi görüntüleme (isteğe bağlı)
cv2.imshow("Resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()