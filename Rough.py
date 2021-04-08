import keras
import numpy as np
import cv2

model = keras.models.load_model('/content/Cat Dog.h5')

video = cv2.VideoCapture(1)
while True:
    success, img = video.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (60, 60))
    img = np.array(img, dtype='float64')
    img = img.reshape(-1, 60, 60, 1)
    img = img / 255.
    print(model.predict(img))
