import cv2

video = cv2.VideoCapture('vtest.avi')

success1, frame1 = video.read()
success2, frame2 = video.read()

while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    a, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        if area < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame1, 'STATUS:{}'.format('MOVEMENT'), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.drawContours(frame1, contours, -1, (0, 255, 0))

    cv2.imshow('Frame1', frame1)

    frame1 = frame2
    success, frame2 = video.read()
    cv2.waitKey(1)
