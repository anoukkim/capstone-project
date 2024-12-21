# Real-Time Depth Camera Software

This project is a software application for real-time depth estimation, image segmentation, and object detection using advanced AI models. The program provides a user-friendly interface and robust performance for capturing images and analyzing depth maps.

---

## Features

### Input
- **Video Feed**: Live video feed from an external camera.
- **Captured Images**: Still images captured from the external camera.

### Output
- **Instance Segmentation and Object Detection**: Annotated images with detected objects and their boundaries.
- **Grasp Pose Visualization**: Images showing the grasp poses for detected objects.
- **Depth Image**: High-quality depth maps of detected objects and background.

---

## Key Components

### 1. **YOLOv8 Image Segmentation**
- **Model**: YOLOv8 (2023), trained on the COCO Dataset.
- **Features**:
  - Real-time detection with excellent speed and accuracy.
  - Lightweight model optimized for performance.
- **Advantages**:
  - Outstanding real-time object detection capabilities.
  - Compact deep learning model suitable for limited hardware resources.

To download and set up YOLOv8 for this project, run the following commands:

```bash
git clone https://github.com/ultralytics/yolov8
cd yolov8
pip install -r requirements.txt
```
Ensure the `yolov8n-seg.pt` model file is placed in the `models` directory after setup.

### 2. **MiDaS Depth Estimation**
- **Model**: MiDaS by IntelLab for Monocular Depth Estimation.
- **Features**:
  - Predicts depth maps with high accuracy from single images.
  - Trained on diverse datasets for robust performance.
  - Multiple versions available (`small`, `large`, `hybrid`); this project uses the `small` version for RAM efficiency.

---

## Conclusion

This project demonstrates the creation of a versatile camera software application capable of:
- Extracting depth information from images.
- Performing real-time segmentation and grasp pose visualization.
- Combining these features with robotics for real-world applications, such as detecting and interacting with objects.

By leveraging cutting-edge AI networks, this software offers an affordable alternative to high-cost depth cameras. The program is designed for real-time feedback, ease of use, and a convenient user interface.

---

## Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/anoukkim/capstone-project.git
cd real-time-depth-camera-software
```

### 2. Set Up the Environment
Install the required dependencies using the provided requirements.yml file.

```bash
conda env create -f requirements.yml
conda activate depth_camera_env
```

3. Run the Application
Start the application by running the following command:

```bash
python main.py
```
