import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to output image")
args = vars(ap.parse_args())

mtx = np.array([[2.94734305e+03, 0.00000000e+00, 1.26990532e+03],
       [0.00000000e+00, 2.95330846e+03, 9.88590328e+02],
       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist = np.array([[-0.48941621,  0.2512973 , -0.00142362, -0.00482556, -0.26849009]])

def left_calib(imgPath, renderPath):
    
    img = cv2.imread(imgPath)

    h,  w = img.shape[:2]
	
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, (w,h))
	
    mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)

    dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
	
    x,y,w,h = roi
	
    dst = dst[y:y+h, x:x+w]
    
    cv2.imwrite(renderPath, dst)

left_calib(args["input"], args["output"])
