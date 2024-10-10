import cv2
import numpy as np


#görüntüyü yazdır
image = cv2.imread('meyve.jpg')
task_image = image.copy() # orijinal görselin kopyasını alıp bunun üzerinden işlem yapmak için.

#gri ton
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#threshold işlemi
ret,thresh1 = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

#kontur işlemi
contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #findcontours nesne sınırlarını bulur, retr_external en dıştaki konturları bulur, chain_approx_simple kontur noktalarını sadeleştirir.

#konturu çizme ve numaralardırma
fruit_count = 0
for i, contour in enumerate(contours):
    geo = cv2.moments(contour)
    if geo["m00"] != 0:
        cX = int(geo["m10"] / geo["m00"]) #m00 kontur alanı, m10 x koordinatı, m01 y koordinatı [Ağırlık Merkezi]
        cY = int(geo["m01"] / geo["m00"])

        cv2.drawContours(image, [contour], -1, (300, 0, 0), 2) #drawcontours sayesinde orijinal görüntü üzerinde işlemi yapıp, grileştirdiğimiz görüntü üzerinde görüyoruz
        cv2.putText(image,
                    str(i + 1),  # kontur numarası
                    (cX, cY),  # koordinat
                    cv2.FONT_ITALIC,  # yazı tipi
                    0.6,  # yazı boyutu
                    (255, 0, 0),  # yazı rengi mavi
                    2)  # kalınlık

        fruit_count += 1 # elma sayacını 1den başlatmak için


combined_image = cv2.hconcat([task_image, image]) # iki görseli yanyana getirmek için | hconcat kodu iki görseli yanyana getirmek için uygulanan bir kod.

#textleri yerleştirmek için#

text = "Orijinal"
position = (10,30)
color = (255,0,0)
font_size = 1
thickness = 3
font = cv2.FONT_ITALIC
cv2.putText(combined_image, text, position, font, font_size, color, thickness, cv2.LINE_AA)


text = "Task"
position = (650,30)
color = (255,0,0)
font_size = 1
thickness = 3
font = cv2.FONT_ITALIC
cv2.putText(combined_image, text, position, font, font_size, color, thickness, cv2.LINE_AA)


text = f"Meyve Sayisi {fruit_count}"
position = (500,515)
color = (0,0,255)
font_size = 1
thickness = 3
font = cv2.FONT_ITALIC
cv2.putText(combined_image, text, position, font, font_size, color, thickness, cv2.LINE_AA)


#çıktısını al
cv2.imshow('Orijinal ve Islenmis Goruntu', combined_image)
tus = cv2.waitKey(0)
if tus == 27:
    cv2.destroyAllWindows()
elif tus == ord("d"):
    cv2.imwrite("YeniGoruntu.jpg", combined_image) # klavyede escye basılınca fotoğraf kapanır, d harfine basıldığında fotoğraf YeniGoruntu.jpg şeklinde kaydedilir.
