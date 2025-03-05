import cv2
import datetime
import tkinter as tk
from PIL import Image, ImageTk
import os
import numpy as np
from motion_detection_pkg.motion_detection import detect_frameMotion
from motion_detection_pkg.object_detection import detect_objects, track_objects

def check_directory():
        # creation of recording and snapshots directory if not found
        if not os.path.exists('snapshots'):
            os.makedirs('snapshots')
        if not os.path.exists('recordings'):
            os.makedirs('recordings')
        if not os.path.exists('faces'):
            os.makedirs('faces')

class SecurityCamera:
    
    def __init__(self, root):
        self.root = root
        self.root.title("AI Assistant")

        self.frame_count = 0

        #Video Capturing
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FPS,30) #setting to 30fps
        #Video Recording variables
        self.is_recording = False
        self.video_writer = None
        self.last_mean = 0
        self.show_lines = tk.IntVar(value=0)  # this is for the bounding lines in the video label 

        #Below 2 values will take in three motion values to save in a list
        #       so that the mean of the values will give a number
        #       done so that the motion detection label doesnt change indefinetly again and again
        self.motion_values_list = [] # to save the motion values 
        self.MOTION_AVERAGE_FRAMES = 5 # average frames to detect the motion
        
        # UI ELEMENTS
        #label to display the video feedpip
        

        # Create a frame for better button arrangement
        button_frame = tk.Frame(root)
        button_frame.grid(row=1, column=0, columnspan=3, pady=10)

        # UI Elements
        self.video_label = tk.Label(root)  # Video Feed Label
        self.video_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.motion_label = tk.Label(root, text="No Motion Detected", fg="green", font=("Arial", 14))
        self.motion_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.toggle_lines_btn = tk.Checkbutton(button_frame, text="Show Lines", variable=self.show_lines, onvalue=1, offvalue=0, font=("Arial", 12))
        self.toggle_lines_btn.grid(row=0, column=0, padx=10, pady=5)

        self.btn_recording = tk.Button(button_frame, text="Start Recording", command=self.start_recording)
        self.btn_recording.grid(row=1, column=0, padx=10, pady=5)

        self.btn_snapshot = tk.Button(button_frame, text="Take Snapshot", command=self.take_snapshot)
        self.btn_snapshot.grid(row=1, column=1, padx=10, pady=5)

        self.btn_exit = tk.Button(button_frame, text="Exit", command=self.exit_app, fg="white", bg="red")
        self.btn_exit.grid(row=1, column=2, padx=10, pady=5)

        self.update_video_feed()

    
    def update_video_feed(self):
        #reading frames from the camera
        # capture_Boolean gives boolean value if the video is being captured or not
        # frame is the numpy array of the video
        
        capture_Boolean, frame = self.cap.read()
        if capture_Boolean:
            lines_boolean = self.show_lines.get()
            motion_detected, frame = detect_frameMotion(frame, lines_boolean)
            if motion_detected:
                self.motion_label.config(text="Motion Detected!", fg="red")
            else:
                self.motion_label.config(text="No Motion Detected", fg="green")
            
            # Detect and track objects
            frame = detect_objects(frame, lines_boolean)
            frame = track_objects(frame, lines_boolean)
            
            
            # converting frame to RGB
            rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgIngui = ImageTk.PhotoImage(image=img)
            #update the video label which is initaited before   
            self.video_label.imgtk = imgIngui
            self.video_label.configure(image=imgIngui)
            
        #if video recording is on then frames is passed on
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.recording_label.config(text="Recording Video....",fg="blue")    
        
        # # Motion detected if most recent frames show movement
        # avg_motion_detected = sum(self.motion_values_list) > (self.MOTION_AVERAGE_FRAMES // 2)

        # # **Update Motion Detection Label**
        # if avg_motion_detected:
        #     self.motion_label.config(text="Motion Detected!", fg="red")
        # else:
        #     self.motion_label.config(text="No Motion Detected", fg="green")

        
        
        # self.motion_values_list.append(motion_value)
        # if len(self.motion_values_list) > self.MOTION_AVERAGE_FRAMES:
        #     self.motion_values_list.pop(0)
        # avg_motion_value = sum(self.motion_values_list) / self.MOTION_AVERAGE_FRAMES
        # #threshold value set to 0.2 based on assesment but 0.3 is also okay
        # if avg_motion_value > 0.2:
        #     self.motion_label.config(text="Motion Detected",fg="red")
        # else:
        #     self.motion_label.config(text="No Motion Detected",fg="green")

        # refresh and repeating - 100ms
        self.root.after(100, self.update_video_feed)

    
    def take_snapshot(self):
        img_Boolean, frame = self.cap.read()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if img_Boolean:
            cv2.imwrite(f"snapshots/snapshot_{timestamp}.jpg",frame)
            print("Snapshot saved as snapshot.jpg")
    
    
    def exit_app(self):
        #release the camera and closing all
        self.cap.release()
        self.root.destroy()

    
    def start_recording(self):
        
        if not self.is_recording:
            self.is_recording = True
            self.btn_recording.config(text="Stop Recording")
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.video_writer = cv2.VideoWriter(f'recordings/recording_{timestamp}.mp4',fourcc,20.0,(640,480))
            self.recording_label.config(text="Recording Video....",fg="blue")
        else:
            self.is_recording = False
            self.btn_recording.config(text="Start Recording")
            if self.video_writer is not None:
                self.video_writer.release()
                self.video_writer = None
                self.recording_label.config(text="")

# for describing each frames in the video
# 
# def describe_frame(rgb_frame):

#     # Loading processers and models
#     blip_preprocessor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
#     blip_model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
    
#     image = Image.fromarray(rgb_frame)

#     inputs = blip_preprocessor(images=image,return_tensors='pt')
#     outputs = blip_model.generate(**inputs)
#     description = blip_preprocessor.decode(outputs[0],skip_special_tokens=True)

#     return description
    

if __name__== "__main__":
    root=tk.Tk()
    app = SecurityCamera(root)
    root.mainloop()