import cv2

img1 = cv2.imread('car.jpg')
img2 = cv2.imread('messi.jpg')
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.resize(img2, (600, 600))
result1 = cv2.add(img2, img1)
result2 = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)
cv2.imshow('Result', result1)
cv2.waitKey(0)
cv2.destroyAllWindows()
