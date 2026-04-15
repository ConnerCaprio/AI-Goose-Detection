# AI-Goose-Detection
# 🦢 Goose Deterrent System

A computer vision–powered automated system that detects geese in real-time and scares them away using a targeted water spray.

## 📌 Overview

This project was built to solve a very real problem: geese constantly invading and leaving a mess on a large lawn.  
The solution combines **computer vision**, **hardware control**, and **real-time decision making** to detect geese and respond automatically.

When a goose is detected:
1. The system calculates its position in the frame  
2. Aims a hose using servo motors  
3. Sprays water to safely scare the goose away  

---

## 🧠 How It Works

### Detection Pipeline
- A camera connected to a Raspberry Pi continuously captures video
- Frames are processed using a **YOLOv11 object detection model**
- When a goose is detected:
  - The bounding box center `(x, y)` is extracted
  - Coordinates are translated into servo motor angles

### Targeting System
- **Servo 1 (Pan):** Left / Right movement  
- **Servo 2 (Tilt):** Up / Down movement  
- The servos adjust to aim the hose toward the detected goose

### Response
- Once aligned, the system activates a **water hose**
- The spray safely deters the goose without harm

---

## 🛠️ Hardware Components

- Raspberry Pi  
- Camera module (Pi Camera or USB camera)  
- 2x Servo motors (pan + tilt)  
- Water hose + valve system  
- Mounting rig (for camera + hose alignment)  

---

## 💻 Software Stack

- Python  
- Computer Vision model: **YOLOv11**  
- OpenCV (video capture & frame processing)  
- GPIO control (servo + valve actuation)  

---

## ⚙️ System Architecture
Camera → Frame Capture → YOLOv11 Detection → Coordinate Mapping → Servo Control → Water Spray
