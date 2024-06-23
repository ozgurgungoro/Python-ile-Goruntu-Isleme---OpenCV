# https://www.w3schools.com/colors/colors_rgb.asp       renk seçimi rgb 


import cv2
import numpy as np



kemalsunal=cv2.imread("resim.jpg")



kemalsunal[150:200,350:500,0]=255    # istenilen alana mavi efekti uygulama     kemalsunal[50:yukarıdan aşşağa boyanacak alan,kaçla kaç arası boyaacak,0]=250

kemalsunal[150:200,350:500,1]=200 


#  kemalsunal[:,:,2]=255    # rgb değerleri buradan oynanır öğrneğin; 0 mavi     1 yeşil     2 kırmızı yapar örneğin
#   kemalsunal[:,:,1]=150     # karışım yaptık kırmızı oldu 


# kemalsunal[:,:,0]=50
# kemalsunal[:,:,1]=200




cv2.imshow("Kemal Sunal",kemalsunal)



cv2.waitKey(0)
cv2.destroyAllWindows()