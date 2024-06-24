import cv2
import numpy as np


resim1=cv2.imread("resim1.jpg")
resim2=cv2.imread("resim2.jpg")          #   BU PROJE ÇALIŞMAZ ÇÜNKÜ 2 RESMİN AYNI BOYUTTA OLMASI GEREKÇİYOR ONA GÖRE RESİM İNDİRİN


cv2.imshow("resim1",resim1)
cv2.imshow("resim2",resim2)


toplam=cv2.add(resim1,resim2)


toplam=cv2.add(resim1,resim2)
agirlikliToplama=cv2.addWeighted(resim1,0.7,resim2,0.3,0)

cv2.imshow("Toplanmis Resimler",toplam)
cv2.imshow("Agirlik Toplama",agirlikliToplama)

cv2.waitKey(0)
cv2.destroyAllWindows()