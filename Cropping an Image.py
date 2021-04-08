import cv2

# Loading image
image = cv2.imread('car.jpg')
# Printing dimensions of Original Image
print(image.shape)
# Cropping Image
image_cropped = image[200:500, 0:800]
# Displaying Image
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', image_cropped)
cv2.waitKey(0)
