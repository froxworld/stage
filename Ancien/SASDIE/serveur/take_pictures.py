import numpy as np
import RPi.GPIO as gp
import os
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--img1", required=True, help="path to first image")
ap.add_argument("-i2", "--img2", required=True, help="path to second image")
ap.add_argument("-i3", "--img3", required=True, help="path to depth image")
args = vars(ap.parse_args())

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.output(11, True)
gp.output(12, True)


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype = "float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect

def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped

def main():
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(3)

    image1 = cv2.imread(args['img1'])
    image2 = cv2.imread(args['img2'])
    oh = 156
    ov = 107
    t1 = 2592 - oh
    t2 = 1944 - ov
    pts1 = np.float32([[0,ov],[oh,1944],[2592,t2],[t1,0]])

    warped1 = four_point_transform(image1, pts1)

    mtx = np.array([[2.750053719e+03, 0.00000000e+00, 1.48815392e+03],
       [0.00000000e+00, 2.75152615e+03, 1.07830939e+03],
       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    dist = np.array([[-4.05510606e-01, -5.50383175e-01, -8.70307074e-04,
         -9.05091476e-03,  1.74894345e+00]])

    newcam  = np.array([[2.57673486e+03, 0.00000000e+00, 1.46372537e+03],
       [0.00000000e+00, 2.56617578e+03, 1.09056348e+03],
       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

    img1undist = cv2.undistort(warped1, mtx, dist, None, newcam)

    new1 = img1undist[75:1800, 10:2400]
    
    oh = 0
    ov = 42
    t1 = 2592 - oh
    t2 = 1944 - ov
    pts2 = np.float32([[0,ov],[oh,1944],[2592,t2],[t1,0]])

    warped2 = four_point_transform(image2, pts2)

    img2undist = cv2.undistort(warped2, mtx, dist, None, newcam)

    new2 = img2undist[75:1800, 10:2400]

    cv2.imwrite(args['img2'], new2)
    cv2.imwrite(args['img1'], new1)
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=25)


    frame2=cv2.cvtColor(new2, cv2.COLOR_BGR2GRAY)
    frame1=cv2.cvtColor(new1, cv2.COLOR_BGR2GRAY)

    disparity = stereo.compute(frame2, frame1)
    cv2.imwrite(args['img3'], disparity)

def capture(cam):
    if cam == 1:
       cmd = "raspistill -vf -hf  -o %s" % args['img1']
    if cam == 3:
       cmd = "raspistill -vf -hf  -o %s" % args['img2']       
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)

