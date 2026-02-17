import cv2
import os
from ultralytics import YOLO

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Video path
video_path = "videos/demo1.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output writer
out = cv2.VideoWriter(
    "outputs/predicted_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    out.write(annotated_frame)
    cv2.imshow("Pothole Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Video saved in outputs/predicted_video.mp4")
