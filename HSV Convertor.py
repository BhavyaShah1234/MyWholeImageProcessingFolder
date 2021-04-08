import cv2

image = cv2.imread('car.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', image_hsv)
cv2.waitKey(0)
