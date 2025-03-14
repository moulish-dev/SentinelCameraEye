# Sentinel Camera Eye: AI-Assistant

## 📌 Overview
**Sentinel Camera Eye** is an **AI-Assistant** built with **Python**.  
It provides **real-time surveillance, motion detection, object tracking, and video recording** capabilities.  
Designed to be **lightweight and efficient**, this application is perfect for **home or office use**.

## Features
- **Real-time Video Feed**: Displays live video from a connected webcam.
- **Motion Detection**: Detects movement and highlights moving objects.
- **Object Recognition & Tracking**: Uses **YOLOv8** to detect and track objects (humans, vehicles, etc.).
- **Snapshot Capture**: Allows users to take screenshots of the video feed.
- **Video Recording**: Saves video recordings locally.
- **Toggle Tracking Lines**: Users can toggle on/off bounding boxes and tracking markers.
- **User-Friendly GUI**: Built with **Tkinter** for a simple and intuitive interface.

---

## 🖥️ System Requirements
### **🔹 Hardware**
- A computer with a built-in **webcam** or an **external USB camera**.

### **🔹 Software**
- **Python 3.x**
- Required Python libraries:
  - **OpenCV (`cv2`)**
  - **Tkinter** (included with Python standard library)
  - **NumPy (`numpy`)**
  - **Pillow (`Pillow`)**
  - **Ultralytics YOLO (`ultralytics`)** _(for object detection)_
  - **Norfair (`norfair`)** _(for object tracking)_

---

## 🔧 Installation & Setup
### ** 1️. Clone the Repository**
```bash
git clone https://github.com/moulish-dev/SentinelCameraEye.git
cd SentinelCameraEye
```

### ** 2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### ** 3. Run the Application**
```bash
python main.py
```

---

## Usage Instructions
1. **Launch the application** (`python main.py`).
2. The **live video feed** starts automatically.
3. **Enable/Disable Tracking Lines** using the **"Show Lines" toggle button**.
4. **Click "Snapshot"** to capture an image.
5. **Click "Start Recording"** to begin recording video.
6. **Motion detection runs automatically** and will highlight detected motion.
7. **Click "Exit"** to close the application.

---

## 📂 Project Structure
```
SentinelCameraEye/
├── main.py                 # Main application script
├── README.md               # Project documentation
├── requirements.txt        # List of required Python libraries
├── snapshots/              # Stores captured snapshots
├── recordings/             # Stores video recordings
├── motion_detection_pkg/             # AI Processing Modules
│   ├── motion_detection.py   # Motion detection logic
│   ├── object_detection.py   # YOLO object detection  # Norfair object tracking
```

---

## 📜 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## Roadmap
View the project [ROADMAP](ROADMAP) here.
---

## 🙌 Acknowledgments
- **[OpenCV](https://opencv.org/)** for computer vision functionalities.
- **[YOLO (Ultralytics)](https://github.com/ultralytics/ultralytics)** for real-time object detection.
- **[Norfair](https://github.com/tryolabs/norfair)** for object tracking.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** for GUI development.

---

## 🤝 Contributing & Support
💡 **Suggestions or Issues?**  
- Feel free to **open an issue** or **submit a pull request** in the repository.  
- Contributions are always welcome!  
