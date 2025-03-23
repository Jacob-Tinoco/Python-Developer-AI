from ultralytics import YOLO

# Load a model
model = YOLO("models\yolo11m.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="data\coco8.yaml", epochs=100, imgsz=640)