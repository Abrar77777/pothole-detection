from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

print("Running validation...\n")

# Run validation
metrics = model.val(data="data/raw/data.yaml", split="val")

print("\n===== MODEL PERFORMANCE =====")

# Safely print metrics
try:
    print("mAP50:", metrics.box.map50)
    print("mAP50-95:", metrics.box.map)
    print("Precision:", metrics.box.mp)
    print("Recall:", metrics.box.mr)
except Exception as e:
    print("Error reading metrics:", e)

print("\nDone.")
