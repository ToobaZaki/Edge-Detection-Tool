from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folders
UPLOAD_FOLDER = 'static/uploads'
FOLDERS = ['original', 'sobel', 'prewitt', 'canny']

# Create all necessary directories
for folder in FOLDERS:
    folder_path = os.path.join(UPLOAD_FOLDER, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def apply_sobel(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = np.sqrt(gx**2 + gy**2)
    return np.uint8(cv2.normalize(sobel_magnitude, None, 0, 255, cv2.NORM_MINMAX))

def apply_prewitt(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], dtype=np.float32)
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=np.float32)
    prewittx = cv2.filter2D(gray, cv2.CV_64F, kernelx)
    prewitty = cv2.filter2D(gray, cv2.CV_64F, kernely)
    prewitt_magnitude = np.sqrt(prewittx**2 + prewitty**2)
    return np.uint8(cv2.normalize(prewitt_magnitude, None, 0, 255, cv2.NORM_MINMAX))

def apply_canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/detect_edges', methods=['POST'])
def detect_edges():
    if 'file' not in request.files:
        return 'No file uploaded'
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected'
    
    # Secure the filename and generate paths
    filename = secure_filename(file.filename)
    
    # Save original image
    original_path = os.path.join(UPLOAD_FOLDER, 'original', filename)
    file.save(original_path)
    
    # Read image and apply edge detection
    image = cv2.imread(original_path)
    if image is None:
        return 'Error reading image'

    # Dictionary to store paths for template
    image_paths = {
        'original': f'uploads/original/{filename}'
    }
    
    # Apply each operator and save results
    for operator_name, operator_func in {
        'sobel': apply_sobel,
        'prewitt': apply_prewitt,
        'canny': apply_canny
    }.items():
        # Process image
        result = operator_func(image)
        # Save result
        result_path = os.path.join(UPLOAD_FOLDER, operator_name, filename)
        cv2.imwrite(result_path, result)
        # Store path for template
        image_paths[operator_name] = f'uploads/{operator_name}/{filename}'
    
    return render_template('results.html', 
                         original=image_paths['original'],
                         sobel=image_paths['sobel'],
                         prewitt=image_paths['prewitt'],
                         canny=image_paths['canny'])

if __name__ == '__main__':
    app.run(debug=True)