import cv2
import numpy as np

for i in range(6):
    image1 = cv2.imread('camera4_{0}_temps_2000.jpg'.format(i))
    # img_ = cv2.resize(img_, (0,0), fx=1, fy=1)
    img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    image2 = cv2.imread('camera5_{0}_temps_2000.jpg'.format(i))
    # img = cv2.resize(img, (0,0), fx=1, fy=1)
    img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    image3 = cv2.imread('camera6_{0}_temps_2000.jpg'.format(i))
    # img = cv2.resize(img, (0,0), fx=1, fy=1)
    img3 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
# trouve les points comumn entre les images pour les detections
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

kp3, des3 = sift.detectAndCompute(img2, None)
kp4, des4 = sift.detectAndCompute(img3, None)

cv2.imwrite("detectionGauchePoint_1_2.jpg", cv2.drawKeypoints(image1, kp1, None))
cv2.imwrite("detectionDroitePoint_1_2.jpg", cv2.drawKeypoints(image2, kp2, None))

cv2.imwrite("detectionDroitePoint_2_3.jpg", cv2.drawKeypoints(image2, kp3, None))
cv2.imwrite("detectionDroitePoint_2_3.jpg", cv2.drawKeypoints(image3, kp4, None))

cv2.imshow('original_image_points_gauche', cv2.drawKeypoints(image1, kp1, None))
cv2.waitKey(0)

cv2.imshow('original_image_points_droit', cv2.drawKeypoints(image2, kp2, None))
cv2.waitKey(0)

cv2.imshow('original_image_points_gauche', cv2.drawKeypoints(image1, kp3, None))
cv2.waitKey(0)

cv2.imshow('original_image_points_droit', cv2.drawKeypoints(image2, kp4, None))
cv2.waitKey(0)

cv2.destroyAllWindows()

# FLANN_INDEX_KDTREE = 0
# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# search_params = dict(checks = 50)
# match = cv2.FlannBasedMatcher(index_params, search_params)
match = cv2.BFMatcher()
matches = match.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.03 * n.distance:
        good.append(m)

draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                   singlePointColor=None,
                   flags=2)

img3 = cv2.drawMatches(image1, kp1, image2, kp2, good, None, **draw_params)
cv2.imwrite("combinasisonImages.jpg", img3)
cv2.imshow("original_image_drawMatches.jpg", img3)
