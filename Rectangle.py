import cv2
import numpy as np

image1 = np.zeros((512, 512, 3), np.uint8)
image2 = np.zeros((512, 512, 3), np.uint8)
'''ARGUMENTS OF RECTANGLE ARE IMAGE, (STARTING POINTS OF DIAGONAL), (END POINTS OF DIAGONAL), (COLOR), THICKNESS,
FILL/HOLLOR'''
cv2.rectangle(image1, (100, 100), (300, 500), (0, 255, 0), 4)
cv2.rectangle(image2, (100, 100), (300, 500), (0, 255, 0), cv2.FILLED)
cv2.imshow('Rectangle Empty', image1)
cv2.imshow('rectangle Filled', image2)
cv2.waitKey(0)
