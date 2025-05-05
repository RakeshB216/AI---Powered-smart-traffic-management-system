import cv2
from ultralytics import YOLO
from collections import defaultdict
import os
import urllib.request

# Initialize defaultdict for tracking vehicle positions
vehicle_positions = defaultdict(lambda: None)

# Function to download yolov8n.pt if not present
def download_yolov8n_pt():
    model_path = "yolov8n.pt"
    if not os.path.exists(model_path):
        print("Downloading yolov8n.pt...")
        url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
        try:
            urllib.request.urlretrieve(url, model_path)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading yolov8n.pt: {e}")
            print("Please download it manually from https://github.com/ultralytics/assets/releases and place it in the project directory.")
            exit(1)
    return model_path

# Load model
model_path = download_yolov8n_pt()
model = YOLO(model_path)

# Open video file
cap = cv2.VideoCapture("0505.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    vehicle_count = 0  

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item() 
            cls = int(box.cls[0].item())
            label = model.names[int(box.cls[0].item())]

            # Calculate the center of the bounding box
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2  # BGR color (default)

            # Compare with previous position to detect movement
            if vehicle_positions[label] is not None:
                prev_x, prev_y = vehicle_positions[label]
                if center_y < prev_y:  # If the Y position decreases, moving forward
                    direction = "Moving Forward ⬆️"
                else:
                    direction = "Moving Backward ⬇️"
            else:
                direction = "Tracking..."

            vehicle_positions[label] = (center_x, center_y)

            # Display movement direction
            cv2.putText(frame, direction, (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

            if conf > 0.5:  
                label = model.names[cls]  
                if label in ["car", "bus", "truck", "motorbike"]:
                    vehicle_count += 1
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                if label in ["ambulance", "fire truck"]:
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 4) 
                    cv2.putText(frame, "Emergency 🚨", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                    
    if vehicle_count > 15:
        traffic_status = "Heavy Traffic 🚦"
        color = (0, 0, 255) 
    elif vehicle_count > 8:
        traffic_status = "Moderate Traffic ⚠️"
        color = (0, 165, 255) 
    else:
        traffic_status = "Smooth Traffic ✅"
        color = (0, 255, 0)  

    cv2.putText(frame, f"Vehicles: {vehicle_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, traffic_status, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Traffic Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import time
prev_time = time.time()
...
current_time = time.time()
try:
    fps = 1 / (current_time - prev_time)
except:
    ZeroDivisionError
    fps=1
prev_time = current_time
cv2.putText(frame, f"FPS: {fps:.2f}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 255, 255), 2)

