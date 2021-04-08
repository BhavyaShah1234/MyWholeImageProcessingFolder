import cv2
import numpy as np

frame_width = 800
frame_height = 600
brightness = 150
web_cam = cv2.VideoCapture(0)
web_cam.set(3, frame_width)
web_cam.set(4, frame_height)
web_cam.set(10, brightness)

my_colors = [[5, 107, 0, 19, 255, 255],
             [133, 56, 0, 159, 156, 255],
             [57, 76, 0, 100, 255, 255],
             [90, 48, 0, 118, 255, 255]]

my_color_values = [[51, 153, 255],
                   [255, 0, 255],
                   [0, 255, 0],
                   [255, 0, 0]]

my_points = []


def find_color(img, colors, color_value):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_point = []
    for k in colors:
        lower = np.array(k[0:3])
        upper = np.array(k[3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        x, y = get_contours(mask)
        cv2.circle(image_result, (x, y), 10, color_value[count], cv2.FILLED)
        if x != 0 and y != 0:
            new_point.append([x, y, count])
        count = count + 1
        cv2.imshow(f'{k[0]}', mask)
    return new_point


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x = 0
    y = 0
    w = 0
    for j in contours:
        area = cv2.contourArea(j)
        if area > 500:
            cv2.drawContours(image_result, j, -1, (0, 255, 0), 4)
            perimeter = cv2.arcLength(j, True)
            approx = cv2.approxPolyDP(j, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def draw(points, color_values):
    for point in points:
        cv2.circle(image_result, (point[0], point[1]), 10, color_values[point[2]], cv2.FILLED)


while True:
    success, image = web_cam.read()
    image_result = image.copy()
    new_points = find_color(image, my_colors, my_color_values)
    for i in new_points:
        if len(new_points) != 0:
            my_points.append(i)
        if len(my_points) != 0:
            draw(my_points, my_color_values)
    cv2.imshow('Air Brush', image_result)
    cv2.waitKey(1)
