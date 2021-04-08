import cv2

video = cv2.VideoCapture(0)
# Setting Width
video.set(3, 640)
# Setting Height
video.set(4, 480)
# Setting Brightness
video.set(10, 100)
while True:
    # Capturing Video frame by frame
    success, img = video.read()
    # Displaying image/frame
    cv2.imshow('Video', img)
    cv2.waitKey(1)
