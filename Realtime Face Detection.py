import cv2

# OPENING WEBCAM
video = cv2.VideoCapture(0)
# OPENING FACE CASCADE XML FILE
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # CAPTURING VIDEO
    success, img = video.read()
    # CONVERTING ORIGINAL IMAGE TO GRAYSCALE
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECTING FACES
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    # CREATING A BOUNDING BOX AROUND DETECTED FACES
    for x, y, width, height in faces:
        cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
    # DISPLAYING OUTPUT
    cv2.imshow('Video', img)
    cv2.waitKey(1)
