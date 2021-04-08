import cv2
import numpy as np

img1 = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (256, 0), (512, 512), (255, 255, 255), -1)
img2 = np.zeros((512, 512, 3), np.uint8)
img2 = cv2.rectangle(img2, (0, 256), (512, 512), (255, 255, 255), -1)

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('AND', bit_and)
cv2.imshow('OR', bit_or)
cv2.imshow('NOT', bit_not)
cv2.imshow('XOR', bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
