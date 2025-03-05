from ultralytics import YOLO
import cv2
import numpy as np
from norfair import Tracker, Detection  

model = YOLO("models/yolov8n.pt") 

def detect_objects(frame, lines_boolean):
    results = model(frame)
    annotated_frame = frame
    if lines_boolean:
        #frame with results labeled
        annotated_frame = results[0].plot() 
    
    return annotated_frame

tracker = Tracker(distance_function="euclidean", distance_threshold=30)

def track_objects(frame, lines_boolean):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = [Detection(np.array([x+w // 2, y+h // 2])) for x, y, w, h in [cv2.boundingRect(cnt) for cnt in contours]]
    
    #update tracker
    tracked_objects = tracker.update(detections)
    
    # drawing tracking circles
    for obj in tracked_objects:
        if isinstance(obj.estimate, np.ndarray) and obj.estimate.shape  == (2,):
            if lines_boolean:
                x, y = obj.estimate
                cv2.circle(frame, tuple(obj.estimate), 10, (0, 255, 0), -1)
        
    return frame