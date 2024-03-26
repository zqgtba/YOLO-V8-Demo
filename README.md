# YOLO-V8-Demo
YOLO V8 Demo，尝试模型量化处理与TensorRT加速
## requirement
    conda activate tmp
(python>=3.7, pytorch>=1.7)

    pip install ultralytics

    conda install lap -c conda-forge

## detect
      yolo detect predict model=yolov8n.pt source='test.mp4' show=true  
      yolo predict source=0 show=true

## track
      yolo detect track model=yolov8n.pt source='test.mp4' show=true  
      yolo track source=0 show=true tracker=botsort.yaml (or bytetrack.yaml)

## segment
      yolo segment predict source='test.mp4' show=true

## pose
      yolo pose predict source='test.mp4' show=true

## classify
  yolo classify predict source='test.mp4' show=true
