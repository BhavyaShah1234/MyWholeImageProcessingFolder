import cv2

# Loading/Reading an Image
image = cv2.imread('car.jpg')
# Printing Dimensions of Image
print(image.shape)
# Resizing Image
image_resized1 = cv2.resize(image, (500, 500))
image_resized2 = cv2.resize(image, (1000, 1000))
# Printing Dimensions of Resized Image
print(image_resized1.shape)
print(image_resized2.shape)
# Displaying Original and Resized Image
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image1', image_resized1)
cv2.imshow('Resized Image2', image_resized2)
cv2.waitKey(0)
