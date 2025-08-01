![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-orange.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-red.svg)

# Bone Fracture Detection using YOLOv8

A Flask web application that detects bone fractures in X-ray images using YOLOv8 object detection model.

## Features

- Upload X-ray images for fracture detection
- Real-time object detection with bounding boxes
- Confidence percentage display for each detection
- Clean web interface with results visualization

## Technologies Used

- Python
- Flask (web framework)
- YOLOv8 (object detection)
- OpenCV (image processing)
- HTML/CSS (frontend)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bone-fracture-detection.git
   cd bone-fracture-detection
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3.Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4.Download the YOLOv8 model weights and place in the Model/ directory.

5.Run the application:
 ```bash
 python app.py
```
6.Open your browser and navigate to **http://localhost:5000**

**Project Structure:**
  - **app.py** - Main Flask application

- **templates/** - HTML templates

- **index.html** - Upload page

- **result.html** - Results page

- **uploads/** - Directory for uploaded images

- **Model/** - Contains YOLOv8 model weights

**Usage:**

    1.Upload an X-ray image using the web interface

    2.View the detection results with bounding boxes

    3.See confidence percentages for each detected fracture

**Contributing:**

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
