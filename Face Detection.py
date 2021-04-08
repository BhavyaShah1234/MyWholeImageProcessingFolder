import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread('people2.jpg')
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image_grayscale, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow('Result', image)
cv2.waitKey(0)
