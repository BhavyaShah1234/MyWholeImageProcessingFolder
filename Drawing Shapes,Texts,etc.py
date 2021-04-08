import cv2
import numpy as np

image1 = np.zeros((512, 512, 3), np.uint8)
image2 = np.zeros((512, 512, 3), np.uint8)
image3 = np.zeros((512, 512, 3), np.uint8)
image4 = np.zeros((512, 512, 3), np.uint8)
print(image1.shape)
print(image2.shape)
print(image3.shape)
print(image4.shape)
image1[:] = 255, 0, 0
image2[:] = 0, 255, 0
image3[:] = 0, 0, 255

'''IN PYTHON/OPENCV THE [X:Y, A:B] THE X:Y REPRESENTS FROM HEIGHT X TO HEIGHT Y AND THE A:B REPRESENTS FROM WIDTH A TO 
WIDTH B'''
image4[200:300, 300:500] = 0, 255, 0
cv2.imshow('Image Blue', image1)
cv2.imshow('Image Green', image2)
cv2.imshow('Image Red', image3)
cv2.imshow('Image Partially Green', image4)
cv2.waitKey(0)
