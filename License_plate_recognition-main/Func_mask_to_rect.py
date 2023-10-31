import cv2
import numpy as np

def mask_to_rect(image):
    # Getting the Thresholds and ret
    ret,thresh = cv2.threshold(image, 0, 1, 0)
    
    # Checking the version of open cv I tried for (version 4)
    #   Getting contours on the bases of thresh
    if (int(cv2.__version__[0]) > 3):
        contours, hierarchy = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    else:
        im2, contours, hierarchy = cv2.findContours(thresh.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Getting the biggest contour
    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(image, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        
    return [x, y, w, h]