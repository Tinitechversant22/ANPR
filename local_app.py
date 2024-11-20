import os
import requests
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory for storing uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['IMAGE_UPLOADS'] = UPLOAD_FOLDER

# Replace this with your Colab ngrok URL
COLAB_API_URL = 'https://7aaa-34-29-122-143.ngrok-free.app/upload'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve the uploaded file."""
    return send_from_directory(app.config['IMAGE_UPLOADS'], filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error="No file uploaded"), 400

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error="No selected file"), 400

    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["IMAGE_UPLOADS"], filename)
    file.save(file_path)

    # Prepare the file for the Colab API request
    with open(file_path, 'rb') as file_stream:
        files = {'file': (filename, file_stream, file.mimetype)}

        try:
            # Send the file to the Colab server
            response = requests.post(COLAB_API_URL, files=files)

            if response.status_code == 200:
                result = response.json()
                return render_template(
                    'result.html',
                    plate_text=result.get('plate_text', 'No result'),
                    uploaded_image=f'/uploads/{filename}'
                )
            else:
                error_message = response.text or "Unknown error occurred"
                return render_template('index.html', error=error_message), response.status_code
        except Exception as e:
            return render_template('index.html', error=f"Error communicating with Colab API: {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
