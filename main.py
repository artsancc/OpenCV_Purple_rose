import cv2
import numpy as np

img = cv2.imread("rose.jpeg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Kırmızı maske
lower_red1 = np.array([0, 80, 80])
upper_red1 = np.array([10, 255, 255])
# HSV'de kırmızının iki değeri olduğu için red2 değeri de eklendi.
lower_red2 = np.array([120, 30, 20])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

rose_mask = cv2.bitwise_or(mask1, mask2)

# Gürültü temizleme
kernel = np.ones((9,7), np.uint8)
rose_mask = cv2.morphologyEx(rose_mask, cv2.MORPH_CLOSE, kernel)
rose_mask = cv2.GaussianBlur(rose_mask, (9,7), 0)

# Gülü ayır
rose_only = cv2.bitwise_and(img, img, mask=rose_mask)

# HSV'ye çevir
hsv_rose = cv2.cvtColor(rose_only, cv2.COLOR_BGR2HSV)

# Mor renk
hsv_rose[:,:,0] = 145

# Geri BGR
mor_rose = cv2.cvtColor(hsv_rose, cv2.COLOR_HSV2BGR)

# Siyah arka plan
sonuc = cv2.bitwise_and(mor_rose, mor_rose, mask=rose_mask)

cv2.imwrite("output/maske.png", rose_mask)
cv2.imwrite("output/sonuc.png", sonuc)

cv2.imshow("maske", rose_mask)
cv2.imshow("Purple Rose", sonuc)

cv2.waitKey(0)
cv2.destroyAllWindows()