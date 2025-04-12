import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from PIL import Image
from sklearn.cluster import KMeans

# Initialize Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to extract color palette
def generate_palette(image_path, num_colors=7):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((100, 100))  # Resize to prevent too many pixels
    image_data = np.array(image)
    pixels = image_data.reshape((-1, 3))

    num_clusters = min(num_colors, len(np.unique(pixels, axis=0)))  # Prevent error

    kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    # Convert colors to hex format
    hex_colors = [(f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}', f'Color {i+1}') for i, color in enumerate(dominant_colors)]
    return hex_colors

# Route for Home
@app.route('/')
def home():
    return render_template('index.html')

# Route for Uploading Image and Extracting Colors
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file uploaded!', 'danger')
            return redirect(request.url)

        file = request.files['image']
        if file.filename == '':
            flash('No file selected!', 'danger')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        image_url = url_for('static', filename=f'uploads/{filename}')  # Correct path

        # Generate color palette
        colors = generate_palette(filepath)

        return render_template('result.html', colors=colors, image_path=image_url)

    return render_template('upload.html')
# Run the App
if __name__ == '__main__':
    app.run(debug=True)
