import cv2

# Load Video
video = cv2.VideoCapture('video.mp4')
while True:
    # Capturing Video frame by frame
    success, img = video.read()
    # Displaying image/frame
    cv2.imshow('Video', img)
    # Breaking loop of video if 'q' is pressed
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
