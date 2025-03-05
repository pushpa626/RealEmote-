# RealEmote-
Real-time Facial Emotion Recognition using Machine Learning Techniques
# RealEmote - Realtime Facial Emotion Detection

## Overview
RealEmote is a real-time facial emotion detection system using Python, OpenCV, and DeepFace/FER. It detects emotions from live video feed or images and displays results in real-time.

## Features
- Real-time emotion detection using OpenCV and FER
- Supports multiple emotions: Happy, Sad, Angry, Surprised, Neutral, etc.
- Works with live webcam feed and image input
- Uses Deep Learning models for high accuracy

## Installation
### 1. Clone the Repository
```sh
 git clone https://github.com/akshanshthakur2/RealEmote.git
 cd RealEmote
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
 python -m venv .venv
 source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 📝 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 🚀 4. Run the Application
```sh
 python emotion_detection.py
```
To test on a video file:
```bash
python emotion_detection.py --video path/to/video.mp4
```

## 🔥 Troubleshooting
### Module Not Found Errors
If you encounter missing modules, try reinstalling them manually:
```sh
 pip install opencv-contrib-python moviepy tensorflow numpy
```
If `cv2` is not found, ensure OpenCV is installed correctly.

### DeepFace or FER Issues
If `DeepFace` or `FER` fails, reinstall with:
```sh
 pip install deepface fer
```
### OpenCV Import Error (`ModuleNotFoundError: No module named 'cv2'`)
```bash
pip install opencv-contrib-python
```
### MoviePy Import Error (`ModuleNotFoundError: No module named 'moviepy.editor'`)
Fix: Use `from moviepy import ...` instead of `from moviepy.editor import ...`

### NumPy Version Conflict
```bash
pip install numpy==1.26.4 --force-reinstall
```


## 📌 Contribution
Feel free to open issues or pull requests for improvements.

## 📜 License
MIT License
