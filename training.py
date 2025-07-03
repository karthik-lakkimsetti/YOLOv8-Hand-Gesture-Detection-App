from ultralytics import YOLO

def train_model():
    model = YOLO("runs/detect/gesture_detection/weights/last.pt")  # Resume from last checkpoint
    model.train(
        data="D:/Multi-Detection/data/data.yaml",
        epochs=33,
        imgsz=512,             # Reduced Image Size ✅
        batch=4,               # Reduced Batch Size ✅
        patience=20,
        optimizer='SGD',
        device='0',            # GPU
        workers=0,             # To avoid DataLoader multiprocessing issues ✅
        project="runs/detect",
        name="gesture_detection",
        exist_ok=True,
        resume=True            # ✅ Correct comma and placement
    )

if __name__ == "__main__":
    train_model()
