# Real-Time Object Detection with YOLOv8

<p align="center">
  <b>Computer Vision Project for Real-Time Object Detection</b>
</p>

---

## 📌 Overview

This project implements a **real-time object detection system using YOLOv8 and OpenCV**.

The application captures live video from a webcam and uses the **YOLOv8s pretrained model** to identify objects in each frame.

Detected objects are displayed in real time with bounding boxes and labels.

The project demonstrates how deep learning and computer vision can be combined to build a simple real-time object detection application.

---

## ✨ Key Features

* 🎥 Real-time webcam video capture
* 🤖 YOLOv8s pretrained object detection model
* 🔍 Automatic object detection
* 📦 Bounding boxes and object labels
* 🖥️ Real-time annotated video output
* ⚡ Continuous frame-by-frame inference
* 📐 640 × 480 webcam resolution
* ⌨️ `Q` key to exit the application

---

## 🧠 Object Detection Workflow

```text
                    ┌──────────────────┐
                    │     Webcam       │
                    │   Live Video     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Capture Video    │
                    │     Frame        │
                    └────────┬─────────┘
                             │
                             ▼
                  ┌───────────────────────┐
                  │      YOLOv8s Model    │
                  │   Object Detection    │
                  └──────────┬────────────┘
                             │
                             ▼
                  ┌───────────────────────┐
                  │ Detection Results     │
                  │ Objects + Confidence  │
                  └──────────┬────────────┘
                             │
                             ▼
                  ┌───────────────────────┐
                  │ Bounding Boxes &      │
                  │ Object Labels         │
                  └──────────┬────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Real-Time Display│
                    │   Video Output   │
                    └──────────────────┘
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| 🐍 Python      | Programming language                |
| 👁️ OpenCV     | Webcam capture and image processing |
| 🤖 YOLOv8      | Object detection                    |
| 🧠 Ultralytics | YOLO model implementation           |
| 🎥 Webcam      | Real-time video input               |

---

## 📂 Project Structure

```text
Real-Time-Object-Detection/
│
├── 📄 main.py
├── 🤖 yolov8s.pt
└── 📖 README.md
```

### File Description

**`main.py`**

Contains the complete real-time object detection workflow, including webcam initialization, frame capture, YOLOv8 inference, result visualization, and application control.

**`yolov8s.pt`**

Pretrained YOLOv8 Small model used for object detection. Ultralytics can automatically download the model when it is loaded for the first time.

---

## ⚙️ Detection Pipeline

The application follows a continuous frame-processing pipeline:

```text
Webcam Frame
     ↓
YOLOv8 Inference
     ↓
Object Detection
     ↓
Detection Results
     ↓
Bounding Boxes
     ↓
Annotated Frame
     ↓
Display
```

---

## 🤖 YOLOv8 Model

The project uses:

```text
YOLOv8s
```

The pretrained model is loaded using:

```python
model = YOLO('yolov8s.pt')
```

YOLOv8 performs object detection on every frame captured from the webcam and returns the detected objects and their corresponding bounding boxes.

---

## 🎥 Webcam Configuration

The webcam is initialized using OpenCV:

```python
cap = cv2.VideoCapture(0)
```

The video resolution is configured to:

```text
Width  → 640 pixels
Height → 480 pixels
```

This provides a standard resolution suitable for real-time processing.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Real-Time-Object-Detection.git
cd Real-Time-Object-Detection
```

### 2. Install Dependencies

```bash
pip install opencv-python ultralytics
```

### 3. Run the Project

```bash
python main.py
```

Make sure your webcam is connected and accessible by your computer.

---

## 🔄 How the Program Works

### Step 1 — Load YOLOv8

The pretrained YOLOv8s model is loaded into the application.

### Step 2 — Initialize Webcam

OpenCV connects to the default webcam and starts capturing live video.

### Step 3 — Capture Frames

The program continuously reads frames from the webcam.

### Step 4 — Detect Objects

Each frame is passed to the YOLOv8 model for object detection.

### Step 5 — Visualize Results

YOLOv8 generates an annotated frame containing bounding boxes and detected object labels.

### Step 6 — Display Results

The processed frame is displayed in a window named:

```text
Real-Time Object Detection
```

### Step 7 — Exit

Press:

```text
Q
```

to stop the application and release the webcam.

---

## 📊 Output

The project produces a **real-time annotated video stream**.

Detected objects are displayed with:

```text
Object Label
     +
Bounding Box
```

The output is displayed directly in the OpenCV window rather than being saved to a separate file.

---

## ⌨️ Controls

| Key | Action               |
| --- | -------------------- |
| `Q` | Exit the application |

---

## 💡 Example Workflow

```text
Live Webcam
     ↓
Person / Car / Phone / Other Object
     ↓
YOLOv8 Detection
     ↓
Bounding Box + Label
     ↓
Real-Time Display
```

---

## 🎯 Project Goal

The goal of this project is to demonstrate a practical implementation of **real-time object detection using deep learning and computer vision**.

It provides a simple end-to-end workflow:

```text
Webcam Processing
        ↓
Computer Vision
        ↓
Deep Learning
        ↓
YOLOv8 Inference
        ↓
Object Detection
        ↓
Real-Time Visualization
```

---

<p align="center">
  <b>👁️ Seeing the World Through AI 🤖</b>
</p>