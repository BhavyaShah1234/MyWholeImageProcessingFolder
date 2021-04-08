import cv2
import numpy as np

image1 = np.zeros((512, 512, 3), np.uint8)
image2 = np.zeros((512, 512, 3), np.uint8)
'''ARGUMENTS OF CIRCLE ARE IMAGE, (CENTER POINT), RADIUS, (COLOR), THICKNESS, FILLED/HOLLOW'''
cv2.circle(image1, (256, 256), 50, (255, 0, 255), 5)
cv2.circle(image2, (256, 256), 50, (255, 0, 255), cv2.FILLED)
cv2.imshow('Circle Empty', image1)
cv2.imshow('Circle Filled', image2)
cv2.waitKey(0)
