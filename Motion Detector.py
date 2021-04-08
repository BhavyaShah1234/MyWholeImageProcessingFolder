import cv2
import datetime

first_frame = None
video = cv2.VideoCapture(1)

while True:
    success, img = video.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 50)
    if first_frame is None:
        first_frame = img_blur
    frame_diff = cv2.absdiff(first_frame, img_blur)
    threshold_diff = cv2.threshold(frame_diff, 20, 255, cv2.THRESH_BINARY)[1]
    threshold_diff_dilate = cv2.dilate(threshold_diff, None, iterations=0)
    copy = threshold_diff_dilate.copy()
    contours, hierarchy = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            continue
        (x, y, width, height) = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
    dt = str(datetime.datetime.now())
    img = cv2.putText(img, dt, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Original', img)
    #cv2.imshow('GrayScale Blur', img_blur)
    #cv2.imshow('Difference', frame_diff)
    # cv2.imshow('First Frame', first_frame)
    cv2.waitKey(1)
