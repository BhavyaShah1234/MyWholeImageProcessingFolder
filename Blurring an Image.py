import cv2

# Loading Image
image = cv2.imread('lena.jpg')
# Converting Image to Blurry Image(always use odd numbers in second () of Gaussian Blur)
image_blur1 = cv2.GaussianBlur(image, (9, 9), 0)
image_blur2 = cv2.GaussianBlur(image, (1, 23), 0)
image_blur3 = cv2.GaussianBlur(image, (23, 1), 0)
# Displaying Original and Blurred Image
cv2.imshow('Original Coloured Image', image)
cv2.imshow('Blurred Image1', image_blur1)
cv2.imshow('Blurred Image2', image_blur2)
cv2.imshow('Blurred Image3', image_blur3)
cv2.waitKey(0)
