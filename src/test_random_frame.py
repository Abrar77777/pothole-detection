import cv2
import random
import os
from ultralytics import YOLO

# Create debug folder
os.makedirs("debug", exist_ok=True)

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

video_path = "videos/demo1.mp4"

cap = cv2.VideoCapture(video_path)

# Total frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total Frames:", total_frames)

# Pick random frame number
random_frame_number = random.randint(0, total_frames - 1)
print("Selected Frame:", random_frame_number)

# Set frame position
cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)

ret, frame = cap.read()

if ret:
    results = model(frame)
    annotated_frame = results[0].plot()

    # Save image
    cv2.imwrite("debug/random_frame_detection.jpg", annotated_frame)

    # Show image
    cv2.imshow("Random Frame Detection", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("✅ Saved in debug/random_frame_detection.jpg")

else:
    print("❌ Failed to read frame")

cap.release()
