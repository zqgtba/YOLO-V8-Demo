from ultralytics import YOLO

model = YOLO('yolov8m.pt')

model.export(half=True, format='tensorrt', device=0)