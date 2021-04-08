import cv2
import numpy as np


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ', ' + str(y)
        cv2.circle(img, (x, y), 2, (0, 255, 0), 2)
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 255), 2)
        cv2.imshow('Clickable Image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ', ' + str(green) + ', ' + str(red)
        print(text)
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 255), 2)
        cv2.imshow('Clickable Image', img)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 2, (0, 255, 255), 2)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 255, 0), 2)
        cv2.imshow('Clickable Image', img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 2, (255, 0, 255), 2)
        img_color = np.zeros((512, 512, 3), np.uint8)
        img_color[:] = [blue, green, red]
        cv2.imshow('Color', img_color)


img = cv2.imread('messi.jpg')
img = cv2.resize(img, (600, 512))
# img = np.zeros([512, 512, 3], np.uint8)
cv2.imshow('Clickable Image', img)
points = []
cv2.setMouseCallback('Clickable Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
