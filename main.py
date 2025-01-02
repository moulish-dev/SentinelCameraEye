import cv2
import datetime
import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import os
import numpy as np

class SecurityCamera:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Camera")

        # creation of recording and snapshots directory if not found
        if not os.path.exists('snapshots'):
            os.makedirs('snapshots')
        if not os.path.exists('recordings'):
            os.makedirs('recordings')

        #Video Capturing
        self.cap = cv2.VideoCapture(0)
        self.is_recording = False
        self.video_writer = None
        self.last_mean = 0

        #label to display the video feedpip
        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.motion_label = tk.Label(root,text="No Motion Detected", fg="green")
        self.motion_label.pack()

        self.recording_label = tk.Label(root,text="")
        self.recording_label.pack()

        self.btn_recording = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.btn_recording.pack(pady=10)

        self.btn_snapshot = tk.Button(root, text="Take Snapshot", command=self.take_snapshot)
        self.btn_snapshot.pack(pady=10)

        self.btn_exit = tk.Button(root, text="Exit",command=self.exit_app)
        self.btn_exit.pack(pady=10)

        self.update_video_feed()

    def update_video_feed(self):
        #reading frames from the camera
        # capture_Boolean gives boolean value if the video is being captured or not
        # frame is the numpy array of the video
        capture_Boolean, frame = self.cap.read()
        if capture_Boolean:
            # converting frame to RGB
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            #update the video label which is initaited before 
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        #if video recording is on then frames is passed on
        if self.is_recording and self.video_writer is not None:
            self.video_writer.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            self.recording_label.config(text="Recording Video....",fg="blue")

        # Motion Detection
        #converting frame to grayscale as RGB is computation-intensive
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
        motion_value = np.abs(np.mean(gray_frame) - self.last_mean)
        self.last_mean = np.mean(gray_frame)
        #threshold value set to 0.2 based on assesment but 0.3 is also okay
        if motion_value > 0.2:
            print("Motion Detected")
            self.motion_label.config(text="Motion Detected",fg="red")
        else:
            self.motion_label.config(text="No Motion Detected",fg="green")



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




if __name__== "__main__":
    root=tk.Tk()
    app = SecurityCamera(root)
    root.mainloop()