import cv2

# Load/Read image
img1 = cv2.imread('lena.png', 0)
img2 = cv2.imread('lena.png', 1)
img3 = cv2.imread('lena.png', -1)
# Show Image
cv2.imshow('Output1', img1)
cv2.imshow('Output2', img2)
cv2.imshow('Output3', img3)
# Retain/Delay Image
cv2.waitKey(0)
# On clicking close on image window the program stops running
cv2.destroyAllWindows()
