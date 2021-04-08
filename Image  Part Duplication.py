import cv2

img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('messi.jpg')
img1 = cv2.resize(img1, (600, 512))
img2 = cv2.resize(img2, (600, 512))

ball = img1[410:500, 360:450]
img2[410:500, 200:290] = ball

cv2.imshow('Original', img1)
cv2.imshow('Result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
