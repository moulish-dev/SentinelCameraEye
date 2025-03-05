import cv2
import numpy as np
import matplotlib.pyplot as plt

backSub = cv2.createBackgroundSubtractorMOG2()

def detect_frameMotion(frame, lines_boolean):
    
    
    # Background Subtraction
    fg_mask = backSub.apply(frame) 
    # detect contours  --- this will show the regions of interests or motion
    contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # improve contour detection
        # apply thresholding to remove shadows
    retval, mask_thresh = cv2.threshold(fg_mask, 180, 255, cv2.THRESH_BINARY)
        #erosion and dilation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)
        # filter contours
    min_contour_area = 1000
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
    
    # draw red boxes around the objects in motion 
    frame_out = frame.copy()
    motion_detected = False
    
    for cnt in large_contours:
        if lines_boolean:
            x, y, w, h = cv2.boundingRect(cnt)
            frame_out = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 200), 3)
        motion_detected = True
    
    return motion_detected, frame_out

