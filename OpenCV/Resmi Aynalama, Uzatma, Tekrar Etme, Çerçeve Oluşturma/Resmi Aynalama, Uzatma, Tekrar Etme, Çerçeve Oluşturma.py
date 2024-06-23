import cv2
import numpy as pn

resim = cv2.imread("insan.png")



aynanalanResim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)   # resim aynalama
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarlananResim=cv2.copyMakeBorder(resim,300,300,300,300,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                                value=(75,150,255))




cv2.imshow("aynalama Fotosu", aynanalanResim)
cv2.imshow("uzatian resim", uzatilanResim)
cv2.imshow("Tekrarlanan Resim", tekrarlananResim)
cv2.imshow("Sarilan Resim", sarilanResim)


cv2.waitKey(0)
cv2.destroyAllWindows()