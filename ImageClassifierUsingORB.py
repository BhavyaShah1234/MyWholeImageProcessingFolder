import cv2 as cv
import numpy as np
import os

path = 'ImagesQuery'
images = []
class_names = []

my_list = os.listdir(path)

# img1 = cv.imread(r'ImagesQuery\XBOX Kinect Sports.jpg', 0)
# # img1 = cv.imread(r'ImagesQuery\PS4 Detroit.jpg', 0)
# # img1 = cv.imread(r'ImagesQuery\PS4 The Last Of Us.jpg', 0)
# img2 = cv.imread(r'ImagesTrain\Kinect.jpg', 0)
# # img2 = cv.imread(r'ImagesTrain\Det.jpg', 0)
# # img2 = cv.imread(r'ImagesTrain\Last.jpg', 0)
#
# orb = cv.ORB_create(nfeatures=1000)
#
# key_points1, descriptors1 = orb.detectAndCompute(img1, None)
# key_points2, descriptors2 = orb.detectAndCompute(img2, None)
# # img_kp1 = cv.drawKeypoints(img1, key_points1, None)
# # img_kp2 = cv.drawKeypoints(img2, key_points2, None)
#
# brute_force_matcher = cv.BFMatcher()
# matches = brute_force_matcher.knnMatch(descriptors1, descriptors2, k=2)
# good = []
# for m, n in  matches:
# 	if m.distance < 0.75 * n.distance:
# 		good.append([m])
# print(len(good))
#
# img3 = cv.drawMatchesKnn(img1, key_points1, img2, key_points2, good, None, flags=2)
#
# # cv.imshow('Image Key Points1', img_kp1)
# # cv.imshow('Image Key Points2', img_kp2)
#
# cv.imshow('Matches', img3)
#
# # cv.imshow('Img1', img1)
# # cv.imshow('Img2', img2)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
