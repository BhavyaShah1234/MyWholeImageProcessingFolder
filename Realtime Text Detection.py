import cv2
import pytesseract

# LOCATING FILE
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# OPENING WEBCAM
web_cam = cv2.VideoCapture(0)
while True:
    # CAPTURING IMAGES
    suc, image = web_cam.read()
    # CONVERTING BGR TO RGB
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # GETTING HEIGHT AND WIDTH OF IMAGE
    image_height, image_width, _ = image.shape
    # CONVERTING IMAGE TO DATA
    boxes = pytesseract.image_to_data(img)
    for a, b in enumerate(boxes.splitlines()):
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(img, b[11], (x, y-5), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
    cv2.imshow('Result', img)
    cv2.waitKey(1)
