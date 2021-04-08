import cv2

# LoadingReading Image
img = cv2.imread('lena.jpg')
# Convert RGB(BRG in python) to Gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Display Gray Image
cv2.imshow('Gray Image', img_gray)
# Delay Image
cv2.waitKey(0)
