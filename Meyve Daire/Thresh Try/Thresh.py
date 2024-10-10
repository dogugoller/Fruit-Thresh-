import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#thresh denemelerim

#görseli oku
image = cv.imread('meyve.jpg.',0)

#thresh işlemleri
ret,thresh1 = cv.threshold(image,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(image,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(image,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(image,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(image,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [image, thresh1, thresh2, thresh3, thresh4, thresh5]


#görüntüyü görselleştir
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray') # bir sütun oluşturur ve görseli gri yapar
    plt.title(titles[i]) # görsellerin üstüne yazı yazar
    plt.xticks([]),plt.yticks([]) # x, y koordinatlarını gizler

# başlık ekle
plt.suptitle('Thresh Görüntüleri', fontsize=16)
plt.show()


#thresh hallerini kaydet
cv2.imwrite("original_image.jpg", image)        # Orijinal görüntü
cv2.imwrite("binary.jpg", thresh1)            # BINARY
cv2.imwrite("binary_inv.jpg", thresh2)        # BINARY_INV
cv2.imwrite("trunc.jpg", thresh3)             # TRUNC
cv2.imwrite("tozero.jpg", thresh4)            # TOZERO
cv2.imwrite("tozero_inv.jpg", thresh5)        # TOZERO_INV