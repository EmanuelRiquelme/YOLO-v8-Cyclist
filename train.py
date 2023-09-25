from ultralytics import YOLO
import torch
from torchvision import transforms 
from PIL import Image

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='dataset.yaml', epochs=10, imgsz=640)
