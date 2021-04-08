import cv2
import numpy as np

image = cv2.imread('lena.jpg')
'''FOR JOINING IMAGES THEY SHOULD HAVE SAME NUMBER OF CHANNELS'''
horizontal_stack = np.hstack((image, image, image))
vertical_stack = np.vstack((image, image, image))
cv2.imshow('Horizontally Stacked Image', horizontal_stack)
cv2.imshow('Vertically Stacked Image', vertical_stack)
cv2.waitKey(0)
