import pytesseract
import cv2
import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

video = cv2.VideoCapture(1)

while True:
    success, frame = video.read()
    speak(pytesseract.image_to_string(frame))
    cv2.imshow('Video', frame)
    cv2.waitKey(1)

# image = cv2.imread('sample.png')
# img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# speak(pytesseract.image_to_string(img))
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
