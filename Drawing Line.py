import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
# ARGUMENTS OF LINE ARE IMAGE,(STARTING COORDINATES), (ENDING COORDINATES), (COLOR), THICKNESS
cv2.line(image, (0, 0), (300, 250), (0, 255, 0), 7)
cv2.line(image, (512, 0), (300, 250), (0, 0, 255), 10)
cv2.line(image, (300, 512), (300, 250), (255, 0, 0), 5)
cv2.imshow('Lined Image', image)
cv2.waitKey(0)
