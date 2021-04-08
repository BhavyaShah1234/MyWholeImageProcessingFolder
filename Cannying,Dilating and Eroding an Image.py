import cv2
import numpy as np

# Loading Image
image = cv2.imread('lena.jpg')
# Defining a Kernel (the (4, 4) in kernel is the thickness of lines required when dilating the image)
kernel = np.ones((4, 4), np.uint8)
# Converting Image to Canny Image
image_canny1 = cv2.Canny(image, 100, 100)
image_canny2 = cv2.Canny(image, 10, 200)
image_canny3 = cv2.Canny(image, 200, 10)
# Dilating a Canny Image(iterations = thickness)
image_dilated1 = cv2.dilate(image_canny1, kernel, iterations=1)
image_dilated2 = cv2.dilate(image_canny1, kernel, iterations=4)
# Eroding a Canny Image
image_eroded1 = cv2.erode(image_dilated1, kernel, iterations=1)
image_eroded2 = cv2.erode(image_dilated1, kernel, iterations=3)
# Displaying Image
cv2.imshow('Original Coloured Image', image)
cv2.imshow('Canny Image1', image_canny1)
cv2.imshow('Canny Image2', image_canny2)
cv2.imshow('Canny Image3', image_canny3)
cv2.imshow('Dilated Image1', image_dilated1)
cv2.imshow('Dilated Image2', image_dilated2)
cv2.imshow('Eroded Image1', image_eroded1)
cv2.imshow('Eroded Image2', image_eroded2)
cv2.waitKey(0)
