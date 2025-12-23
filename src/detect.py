import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


def detect_objects(image_path):
    img = cv2.imread(image_path)
    results = model(img)
    return results.pandas().xyxy[0]
