import cv2
import numpy as np


resim = cv2.imread("resim.jpg",0)   # anında 0 ekleyerek grileştirilir


cv2.imshow("gri resim",resim)



# resimGri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)    # resim grileştirme

# yukseklik,genislik,kanalSayisi=resim.shape

# print("Orjinal",yukseklik,genislik,kanalSayisi)


# yukseklik,genislik=resimGri.shape

# print("Gri resim",yukseklik,genislik)


# cv2.imshow("Orjinal Resim",resim)
# cv2.imshow("grilestirilmis resim",resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()