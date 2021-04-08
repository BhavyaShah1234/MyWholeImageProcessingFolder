import cv2

# OPENING WEBCAM
video = cv2.VideoCapture(1)


# GET CONTOURS FUNCTION
def get_cont(image):
    # GETTING CONTOURS
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        # GETTING AREA OF FIGURE BOUNDED BY CONTOURS
        area = cv2.contourArea(contour)
        if area > 500:
            # DRAWING CONTOURS AROUND OUR ORIGINAL IMAGE
            cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
            # FINDING PERIMETER OF FIGURES FOUND BY CLOSED CONTOURS
            perimeter = cv2.arcLength(contour, True)
            # GETTING NUMBER AND COORDINATES OF VERTICES
            vertices = cv2.approxPolyDP(contour, 0.05 * perimeter, True)
            num_of_vertex = len(vertices)
            # GETTING COORDINATES, WIDTH AND HEIGHT OF SHAPE
            x, y, width, height = cv2.boundingRect(vertices)
            # DRAWING RECTANGLE AROUND SHAPE
            cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 3)
            # DETECTING SHAPE AND LABELLING THEM
            if num_of_vertex == 4:
                aspect_ratio = width/float(height)
                if 0.9 < aspect_ratio < 1.1:
                    shape = 'SQUARE'
                    cv2.putText(img, shape, (x + (width // 2) + 10, y + (height // 2) + 10), cv2.FONT_HERSHEY_PLAIN, 1,
                                (0, 0, 0), 3)
                else:
                    shape = 'Rectangle'
                    cv2.putText(img, shape, (x + (width // 2) + 10, y + (height // 2) + 10), cv2.FONT_HERSHEY_PLAIN, 1,
                                (0, 0, 0), 3)
            elif num_of_vertex == 3:
                shape = 'Triangle'
                cv2.putText(img, shape, (x + (width // 2) + 10, y + (height // 2) + 10), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 0, 0), 3)
            else:
                shape = 'Circle'
                cv2.putText(img, shape, (x + (width // 2) + 10, y + (height // 2) + 10), cv2.FONT_HERSHEY_PLAIN, 1,
                            (0, 0, 0), 3)


while True:
    # CAPTURING VIDEO
    success, img = video.read()
    # CONVERTING IMAGE TO GRAYSCALE
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ADDING BLUR TO GRAYSCALE IMAGE
    img_blur = cv2.GaussianBlur(img_gray, (9, 9), 1)
    # ADDING CANNY TO BLUR IMAGE
    img_canny = cv2.Canny(img_blur, 75, 75)
    # CALLING GET CONTOURS FUNCTION
    get_cont(img_canny)
    # DISPLAYING OUTPUT
    # cv2.imshow('Gray', img_gray)
    # cv2.imshow('Blur', img_blur)
    cv2.imshow('Canny', img_canny)
    cv2.imshow('Contours', img)
    cv2.waitKey(1)