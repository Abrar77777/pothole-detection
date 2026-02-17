🚧 Pothole Detection using YOLOv8
📌 Overview

This project detects potholes on road surfaces using YOLOv8 object detection model.
It can detect potholes in:

Images

Videos

Real-time webcam feed

The goal is to build an intelligent road damage monitoring system.

🧠 Model Details

Framework: Ultralytics YOLOv8

Classes: 1 (pothole)

## Dataset

The dataset is downloaded from Roboflow.

To download:

1. Create a Roboflow account
2. Export in YOLOv8 format
3. Place inside data/raw/


Evaluation Metrics:

mAP@50: 0.79

mAP@50-95: 0.49

Precision: 0.86

Recall: 0.65

📂 Project Structure
pothole-detection/
│
├── data/
│   └── raw/
│
├── src/
│   ├── download_data.py
│   ├── train.py
│   ├── predict_video.py
│   ├── test_random_frame.py
│   └── evaluate_model.py
│
├── videos/
├── outputs/
├── requirements.txt
├── .gitignore
└── README.md

⚙ Installation

Clone repository

git clone https://github.com/your-username/pothole-detection.git
cd pothole-detection


Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows


Install dependencies

pip install -r requirements.txt

🏋 Training
yolo detect train model=yolov8n.pt data=data/raw/data.yaml epochs=50 imgsz=640

🎥 Video Inference
python src/predict_video.py

📊 Model Evaluation
python src/evaluate_model.py

🚀 Future Improvements

Improve recall using larger model (YOLOv8s)

Add pothole severity classification

Add GPS tagging for road monitoring

Deploy using Flask or FastAPI

Convert to TensorRT for edge deployment

📌 Applications

Smart city monitoring

Road maintenance automation

Autonomous vehicle safety

Highway inspection systems

👤 Author

Shaik Abrar
Computer Vision Enthusiast
