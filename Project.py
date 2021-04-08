import cv2
import numpy as np


def nothing(x):
    print(x)


def empty_slots(path):
    img = cv2.imread(path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 21, 160])
    upper = np.array([35, 100, 255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    return mask, result


def joint(a, b):
    black = cv2.bitwise_or(a, b)
    return black


while True:
    mask1, result1 = empty_slots(r'C:\Users\user\Downloads\1.png')
    mask2, result2 = empty_slots(r'C:\Users\user\Downloads\2.png')
    mask3, result3 = empty_slots(r'C:\Users\user\Downloads\3.png')

    mask1 = cv2.resize(mask1, (1188, 581))
    mask2 = cv2.resize(mask2, (1180, 587))
    mask3 = cv2.resize(mask3, (1180, 587))
    join = joint(mask2, mask3)

    cv2.imshow('Mask1', mask2)
    cv2.imshow('Mask2', mask3)
    cv2.imshow('Joint', join)
    cv2.waitKey(1)
