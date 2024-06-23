import cv2
import numpy as np

resim =cv2.imread("image.jpg")

resim[50,30]=[255,255,255]     # 50 aşşa 30 sağa   değiştirme güncelleme işlemi, yapıldı  bu değişiklik beyaz yapar




for i in range(100):
    resim[70,i]=[255,255,255]    # 70 aşşa i boyunca beyaz çiz dedik  100 de bitiriyor çikiyor




cv2.imshow("Image",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()