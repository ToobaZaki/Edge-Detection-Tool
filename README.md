🖼️ Edge Detection Web App

This is a simple yet effective web-based application for edge detection using Sobel, Prewitt, and Canny operators. Built with Flask and OpenCV, the app allows users to upload an image and view edge-detected outputs using different filters—all from a sleek browser interface.

🔍 Features
📤 Upload any image (JPG, PNG, etc.)

⚙️ Automatically apply:

Sobel Operator

Prewitt Operator

Canny Edge Detection

🖥️ Display original and processed images side-by-side

🎨 Clean, modern UI with responsive design

📸 Live Preview
Upload → Detect → Compare Results
Simple and intuitive UI built with HTML/CSS and Flask templates.

🚀 Getting Started
Prerequisites
Python 3.x

pip

Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/edge-detection-app.git
cd edge-detection-app

# Install dependencies
pip install flask opencv-python
Run the App
bash
Copy
Edit
python app.py
Then open your browser and go to:
http://127.0.0.1:5000

📁 Project Structure
php
Copy
Edit
├── app.py                 # Flask application with OpenCV logic
├── templates/
│   ├── index.html         # Upload form UI
│   └── results.html       # Results display UI
└── static/
    └── uploads/           # Automatically generated subfolders for saving results
        ├── original/
        ├── sobel/
        ├── prewitt/
        └── canny/
✨ Author
Tooba Zaki
