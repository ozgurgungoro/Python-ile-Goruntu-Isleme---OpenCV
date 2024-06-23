# Kaynak :    https://www.youtube.com/watch?v=IAVjMKTyQg4&list=PLzcys7whQ6eSJdSHJh-xdOLvWPP24J76x&index=2

import cv2
import numpy as np


# resim = cv2.imread("Logo.png",0)

resim1 = cv2.imread("kus.png",0)    # ,0 işlemi resmi grileştirir   bu işlem boyutta düşme sağlar
resim2 = cv2.imread("Logo.png")



cv2.imshow("Logo Baslik",resim1)

#  cv2.imwrite("yeniresim.png",resim)


# print(resim)  # matris görme kod parcacigi

# print(resim1.size)  # boyut ögrenme kodu

# print(resim1.dtype)


print(resim1.size)
print(resim1.dtype)
print(resim1.shape)  #genişlik yükseklik ve kaç kanaldan oluştuğunu gösterir



cv2.waitKey(0)
cv2.destroyAllWindows()