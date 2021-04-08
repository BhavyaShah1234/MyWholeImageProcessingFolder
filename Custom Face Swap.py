import cv2
import dlib
import numpy as np

frontal_face_detector = dlib.get_frontal_face_detector()
frontal_face_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

src_img = cv2.imread('jason.jpg')
src_copy1 = src_img.copy()
src_gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
src_canvas = np.zeros_like(src_gray)

src_faces = frontal_face_detector(src_gray)

for src_face in src_faces:
    src_face_landmark = frontal_face_predictor(src_gray, src_face)
    src_face_landmark_points = []

    for landmark_no in range(0, 68, 1):
        x_src = src_face_landmark.part(landmark_no).x
        y_src = src_face_landmark.part(landmark_no).y
        src_face_landmark_points.append((x_src, y_src))
    src_face_landmark_points_array = np.array(src_face_landmark_points, np.int32)

    src_face_convexhull = cv2.convexHull(src_face_landmark_points_array)

    cv2.fillConvexPoly(src_canvas, src_face_convexhull, 255)

    cv2.bitwise_and(src_img, src_img, mask=src_canvas)
