# TouchFlow

AI-Powered Gesture Controlled Smart Workspace using Machine Learning and IoT

## Overview

TouchFlow is a real-time gesture recognition system that enables touchless control of workspace devices using hand gestures. The system combines Computer Vision, Machine Learning, and IoT to detect user gestures through a webcam and trigger actions on an ESP32 microcontroller.

Using MediaPipe hand tracking and a K-Nearest Neighbors (KNN) classifier, TouchFlow recognizes predefined gestures and controls LEDs and a buzzer to simulate workspace automation.

## Features

- Real-time hand gesture recognition
- MediaPipe-based hand landmark tracking
- Machine Learning gesture classification using KNN
- ESP32-based hardware automation
- Touchless device control
- Interactive dashboard interface
- Low-cost and scalable architecture

## Supported Gestures

| Gesture     | Action         |
| ----------- | -------------- |
| Open Palm   | Focus Mode     |
| Closed Fist | Shutdown Mode  |
| Two Fingers | Break Reminder |
| OK Sign     | Reset System   |

## Tech Stack

### Machine Learning

- Python
- Scikit-Learn
- K-Nearest Neighbors (KNN)

### Computer Vision

- OpenCV
- MediaPipe

### IoT

- ESP32
- Arduino IDE
- Serial Communication

### GUI

- CustomTkinter

## System Workflow

Gesture → Webcam → MediaPipe → Landmark Extraction → KNN Classification → ESP32 → LEDs & Buzzer

## Hardware Setup

- ESP32 Development Board
- 4 LEDs
- Active Buzzer
- Breadboard
- Jumper Wires
- Webcam

## Project Structure

TouchFlow/

├── collect_data.py

├── train_model.py

├── gesture_data.csv

├── gesture_model.pkl

├── project.ino

└── README.md

## Installation

```bash
pip install opencv-python mediapipe numpy pandas scikit-learn pyserial customtkinter pillow
```

## Usage

### Collect Gesture Data

```bash
python collect_data.py
```

### Train Model

```bash
python train_model.py
```

### Upload ESP32 Firmware

Upload `esp32_code.ino` using Arduino IDE.

### Launch System

```bash
python ai_dashboard.py
```

## Machine Learning Approach

The project uses the K-Nearest Neighbors (KNN) algorithm to classify gestures based on MediaPipe hand landmark coordinates. During prediction, the model compares incoming landmark features with previously trained samples and predicts the gesture using majority voting among the nearest neighbors.

## Applications

- Smart Workspaces
- Touchless Control Systems
- Human-Computer Interaction
- IoT Automation
- Accessibility Solutions
- Educational Demonstrations

## Future Improvements

- Smart Home Integration
- Voice Assistant Support
- Mobile Application Control
- Deep Learning-Based Gesture Recognition
- Cloud Connectivity

## Author

Adarsh MB

AI • Machine Learning • IoT • Cybersecurity
