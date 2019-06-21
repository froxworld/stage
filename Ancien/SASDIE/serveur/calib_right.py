import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to output image")
args = vars(ap.parse_args())

mtx = np.array([[2.96100575e+03, 0.00000000e+00, 1.43152610e+03],
       [0.00000000e+00, 2.95898299e+03, 1.05768515e+03],
       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist = np.array([[-5.44637689e-01,  5.43881218e-01, -4.71314891e-05, -7.46244419e-03, -5.32311722e-01]])

def right_calib(imgPath, renderPath):

    img = cv2.imread(imgPath)

    h,  w = img.shape[:2]

    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, (w,h))

    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
    dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)

    x, y, w, h = roi

    dst = dst[y:y+h, x:x+w]

    cv2.imwrite(renderPath, dst)

right_calib(args["input"], args["output"])
