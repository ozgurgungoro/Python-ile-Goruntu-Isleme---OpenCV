import cv2
import numpy as np


resim = cv2.imread("hababam.jpg")

cv2.rectangle(resim,(50,100),(150,30),[0,0,255],9)


cv2.imshow("Hababam",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()