🖼️ Edge Detection Web App
A simple web-based application for edge detection using Sobel, Prewitt, and Canny operators. Built with Flask and OpenCV, it lets users upload an image and view processed outputs with a stylish interface.

🔍 Features
📤 Upload an image (PNG, JPG, etc.)

⚙️ Apply:

Sobel

Prewitt

Canny

🖥️ See original and edge-detected results

🎨 Modern UI with clean visuals

🚀 Getting Started
Prerequisites
Python 3.x

pip

Installation
Clone the repository and install the dependencies:

bash
Copy
Edit
git clone https://github.com/yourusername/edge-detection-app.git
cd edge-detection-app

pip install flask opencv-python
Run the App
bash
Copy
Edit
python app.py
Then open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
📁 Project Structure
php
Copy
Edit
├── app.py                 # Main Flask app
├── templates/
│   ├── index.html         # Upload page
│   └── results.html       # Edge detection result display
└── static/
    └── uploads/           # Subfolders created for:
        ├── original/
        ├── sobel/
        ├── prewitt/
        └── canny/
✨ Author
Tooba Zak+++
