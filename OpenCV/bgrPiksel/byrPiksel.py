import cv2
import numpy as np

kopek = cv2.imread("kopek.jpg")  # degisken atama 


cv2.imshow("Kopek Resmi", kopek)  # resim gösterme


print(kopek[(230,80)])     # 230 resimde aşşaya 80 sağa demek 


print("Resmin Boyutu: "+str(kopek.size))         # resim boyutunu getir
print("Resim Özellikleri: "+str(kopek.shape))    # özelliğini getir
print("Resmin Veri Tipi: "+str(kopek.dtype))     # veri tipini getir


cv2.waitKey(0)
cv2.destroyAllWindows()