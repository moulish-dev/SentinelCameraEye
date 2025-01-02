# Sentinel Camera Eye: Security Camera Project

## Overview
This project is a Python-based security camera system that captures, processes, and displays real-time video feeds. The application is designed using the Tkinter library for the GUI and incorporates various features such as motion detection, video recording, and snapshot capabilities.
The main aim of this project is to provide easy, less-resource-intensive security camera suitable for daily use. 

## Features
- **Real-time Video Feed**: Displays live video feed from a connected camera.
- **Motion Detection**: Detects motion in the video feed and highlights the moving objects.
- **Snapshot Capture**: Allows users to take snapshots of the video feed.
- **Video Recording**: Enables recording of the live video feed to the local storage.
- **User-Friendly GUI**: Built using Tkinter for an intuitive user-friendly GUI.

## Requirements
### Hardware
- A computer with a webcam or an external USB camera.

### Software
- Python 3.x
- Required Python libraries:
  - OpenCV (`cv2`)
  - Tkinter (included with Python standard library)
  - NumPy (`numpy`)
  - Pillow (`Pillow`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/moulish-dev/SentinelCameraEye.git
   cd SentinelCameraEye
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Launch the application.
2. Upon launch video feed will start.
3. Click on the **Snapshot** button to capture a still image.
4. Use the **Start Recording** button to start/stop video recording.
5. Motion detection is enabled automatically and highlights motion in the feed.

## File Structure
```
SentinelCameraEye/
├── main.py            # Main application script
├── README.md         # Project documentation
├── snapshots/        # Folder to store all captured snapshots
├── recordings/       # Folder to store all video recordings
├── requirements.txt  # List of required Python libraries
```
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgments
- [OpenCV](https://opencv.org/) for computer vision functionality.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.

---
Feel free to suggest improvements or report issues on the project.
