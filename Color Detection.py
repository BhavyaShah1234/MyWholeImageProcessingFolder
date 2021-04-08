import cv2
import numpy as np


def empty(a):
    print(a)


# CREATING TRACKBAR WINDOW
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
# CREATING TRACKBAR OPTIONS
cv2.createTrackbar('Hue Min', 'TrackBars', 6, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Saturation Min', 'TrackBars', 111, 255, empty)
cv2.createTrackbar('Saturation Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Value Min', 'TrackBars', 154, 255, empty)
cv2.createTrackbar('Value Max', 'TrackBars', 255, 255, empty)

while True:
    # LOADING IMAGE
    image = cv2.imread('lambo.png')
    # CONVERTING IMAGE FROM BGR TO HSV
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # GETTING TRACKBAR POSITION ON IMAGE
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Saturation Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Saturation Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Value Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Value Max', 'TrackBars')
    # CREATING MASK
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(image_hsv, lower, upper)
    # CREATING NEW IMAGE FROM HSV IMAGE AND MASK
    output = cv2.bitwise_and(image, image, mask=mask)
    # DISPLAYING ORIGINAL,HSV,MASK AND RESULT IMAGE
    cv2.imshow('Original Image', image)
    cv2.imshow('HSV Image', image_hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Final Output', output)
    cv2.waitKey(1)
