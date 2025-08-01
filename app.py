from flask import Flask, request, render_template
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename
import cv2
import base64

app = Flask(__name__)

UPLOAD_FOLDER = "F:/AI By Amar/AI/PAdas tips_tricks/Projects/yolov11/Bone_Fracture/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load YOLO model
model = YOLO("F:/AI By Amar/AI/PAdas tips_tricks/Projects/yolov11/Bone_Fracture/Model/best(1).pt")  # Adjust path if needed

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No image uploaded", 400

        file = request.files["image"]
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Run YOLO detection
        results = model(filepath)
        result = results[0]

        detections = []
        for box in result.boxes:
            x1, y1, x2, y2 = map(float, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]
            detections.append({
                "class": label,
                "confidence": round(conf * 100, 2),
                "box": [x1, y1, x2, y2]
            })

        # Annotated image (base64 for embedding in HTML)
        image_with_boxes = result.plot()
        _, buffer = cv2.imencode('.jpg', image_with_boxes)
        image_base64 = base64.b64encode(buffer).decode('utf-8')

        return render_template("result.html", detections=detections, image_base64=image_base64)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
