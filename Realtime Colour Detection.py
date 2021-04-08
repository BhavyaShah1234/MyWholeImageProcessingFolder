import cv2
import numpy as np


def empty(a):
    print(a)


# OPENING WEBCAM
video = cv2.VideoCapture(0)
# CREATING TRACKBAR WINDOW
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
# CREATING TRACKBAR OPTIONS
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 84, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)
while True:
    # CAPTURING VIDEO
    success, image = video.read()
    # CONVERTING TO HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # GETTING TRACKBAR POSITION ON IMAGE
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
    # CREATING MASK
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(image_hsv, lower, upper)
    # CREATING NEW IMAGE FROM HSV IMAGE AND MASK
    output = cv2.bitwise_and(image, image, mask=mask)
    # DISPLAYING OUTPUT
    # cv2.imshow('Video', image)
    # cv2.imshow('HSV Video', image_hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Output', output)
    cv2.waitKey(1)
