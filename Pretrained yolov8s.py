from ultralytics import YOLO

model = YOLO("yolov8s.pt")  
model.predict(source=0, show=True)  # Open webcam and show predictions
