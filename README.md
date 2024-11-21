*Number Plate Detection & Recognition System*

This project implements a Number Plate Recognition System that allows users to upload a vehicle image via a web interface. The system extracts the number plate from the image using EasyOCR and displays both the uploaded image and the extracted number plate on the frontend.

The backend OCR functionality is implemented in Google Colab, integrated with the Flask application using Pyngrok.

*Features*
   - Upload vehicle images through the Flask web application.
   - Extract vehicle number plates using EasyOCR.
   - Display the uploaded image and the extracted number plate on the frontend.
   

*Requirements*

- Python 3.x
- Flask
- EasyOCR
- Pyngrok
- Google Colab

*Setup and Execution*
Step 1: Clone the Repository

    git clone https://github.com/Tinitechversant22/ANPR.git
    cd number-plate-recognition

Step 2: Set Up EasyOCR in Google Colab
    Open Google Colab and create a new notebook.

    Install EasyOCR:
    !pip install easyocr

Step 3: Set Up the Flask Application
    Install the required Python packages:
    pip install flask pyngrok easyocr

Step 4: Run the Flask Application
    Start the Flask app:

    python local_app.py

Step 5: Upload an Image
    Use the Upload button to select a vehicle image.
    The uploaded image and extracted number plate will be displayed on the frontend.
    *Notes*
    Ensure that the Ngrok URL from the Colab notebook is updated in your Flask application (local_app.py).
    If the Colab runtime disconnects, restart it, get a new Ngrok URL, and update it in your Flask app.
    For production deployment, consider replacing the Colab-Pyngrok setup with a dedicated backend server for OCR.
