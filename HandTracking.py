import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

current_time = 0
prev_time = 0

while True:
	success, img = cap.read()
	img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
	results = hands.process(img_rgb)

	if results.multi_hand_landmarks:
		for hand_landmarks in results.multi_hand_landmarks:
			for i, landmarks in enumerate(hand_landmarks.landmark):
				h, w, c = img.shape
				center_x, center_y = int(landmarks.x * w), int(landmarks.y * h)
				if i == 0:
					cv.putText(img, '0', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 1:
					cv.putText(img, '1', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 2:
					cv.putText(img, '2', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 3:
					cv.putText(img, '3', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 4:
					cv.putText(img, '4', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 5:
					cv.putText(img, '5', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 6:
					cv.putText(img, '6', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 7:
					cv.putText(img, '7', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 8:
					cv.putText(img, '8', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 9:
					cv.putText(img, '9', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 10:
					cv.putText(img, '10', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 11:
					cv.putText(img, '11', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 12:
					cv.putText(img, '12', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 13:
					cv.putText(img, '13', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 14:
					cv.putText(img, '14', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 15:
					cv.putText(img, '15', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 16:
					cv.putText(img, '16', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 17:
					cv.putText(img, '17', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 18:
					cv.putText(img, '18', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 19:
					cv.putText(img, '19', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
				if i == 20:
					cv.putText(img, '20', (center_x+5, center_y+5), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
					cv.circle(img, (center_x, center_y), 5, (255, 0, 0), cv.FILLED)
			mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

	current_time = time.time()
	fps = 1 / (current_time - prev_time)
	prev_time = current_time
	cv.putText(img, str(fps), (20, 20), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

	cv.imshow('Image', img)
	cv.waitKey(1)
