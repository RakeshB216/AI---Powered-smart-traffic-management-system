# AI-Powered Vehicle Detection and Traffic Analysis

This project is an **AI-driven** computer vision application that uses the YOLOv8 deep learning model to detect vehicles in video feeds, track their movement, and analyze traffic conditions in real-time. It identifies and classifies vehicles (e.g., cars, buses, trucks, motorbikes) and emergency vehicles (e.g., ambulances, fire trucks), counts them, and categorizes traffic as smooth, moderate, or heavy.

## Project Overview
The system leverages **YOLOv8**, a state-of-the-art deep learning model for object detection, combined with **OpenCV** for video processing and visualization. It tracks vehicle movement by analyzing bounding box positions and provides real-time insights into traffic conditions, making it suitable for applications like traffic monitoring, smart city infrastructure, or autonomous vehicle perception.

## Features
- **Vehicle Detection**: Uses YOLOv8 (`yolov8n.pt`) to detect and classify vehicles in video frames with high accuracy.
- **Movement Tracking**: Determines vehicle direction (forward ⬆️ or backward ⬇️) by comparing bounding box center positions across frames.
- **Traffic Analysis**: Counts vehicles and classifies traffic conditions:
  - **Heavy**: >15 vehicles
  - **Moderate**: 9–15 vehicles
  - **Smooth**: ≤8 vehicles
- **Emergency Vehicle Detection**: Highlights ambulances and fire trucks with distinct red bounding boxes and "Emergency 🚨" labels.
- **Real-Time Visualization**: Displays vehicle count, traffic status, and movement direction on the video feed.

## AI Components
- **Deep Learning**: YOLOv8, a convolutional neural network (CNN), powers object detection and classification.
- **Computer Vision**: OpenCV processes video frames and overlays annotations (bounding boxes, labels, and text).
- **Intelligent Decision-Making**: Custom logic analyzes vehicle counts and movement to provide traffic insights.

## Requirements
- Python 3.8 or higher
- Libraries:
  - `opencv-python`: For video processing and visualization
  - `ultralytics`: For YOLOv8 model inference
- A video file (e.g., MP4 format) for processing
- YOLOv8 model weights (`yolov8n.pt`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Vehicle-Detection.git
   cd Vehicle-Detection
