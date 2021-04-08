import cv2
import numpy as np


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        area = cv2.contourArea(i)
        print(area)
        if area > 500:
            cv2.drawContours(image_cont, i, -1, (0, 255, 0), 4)
            perimeter = cv2.arcLength(i, True)
            print(perimeter)
            approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
            obj_corner = len(approx)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(image_cont, (x, y), (x + w, y + h), (0, 0, 255), 2)
            if obj_corner == 3:
                obj_type = 'Triangle'
            elif obj_corner == 4:
                obj_type = 'Rectangle'
            elif obj_corner > 4:
                obj_type = 'Circle'
            else:
                pass
            cv2.putText(image_cont, obj_type, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 2)


image = cv2.imread('shapes.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_gray_image = cv2.GaussianBlur(gray_image, (7, 7), 1)
image_blur_canny = cv2.Canny(blur_gray_image, 50, 50)
image_canny = cv2.Canny(gray_image, 50, 50)
blank_image = np.zeros_like(image)
image_cont = image.copy()

get_contours(image_blur_canny)

image_stack = stack_images(0.6, ([image, gray_image, blur_gray_image], [image_blur_canny, image_cont, blank_image]))
cv2.imshow('Image', image_stack)
cv2.waitKey(0)
