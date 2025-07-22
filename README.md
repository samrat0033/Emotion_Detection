# Emotion Detection System using CNN, TensorFlow, OpenCV, and Streamlit

This project is an **Emotion Detection System** that uses a **Convolutional Neural Network (CNN)** model built with **TensorFlow** to detect human emotions from webcam input in real-time. It includes two main interfaces:

- `main.py`: A **GUI-based desktop application** using OpenCV that captures video from the webcam and displays real-time emotion classification.
- `app.py`: A **Streamlit web application** that allows users to upload images and see the detected emotion.

## Project Structure

📁 test/ # Directory for testing data
📁 train/ # Directory for training data
📁 tfenv/ # Virtual environment (not included in repo)
📄 app.py # Streamlit web app
📄 main.py # GUI app using OpenCV and webcam
📄 emotion-classification... # Possibly a notebook or script for training
📄 haarcascade_frontalface... # XML file for face detection
📄 model.h5 # Pre-trained CNN model
📄 requirements.txt # Python dependencies
📄 README.md # Project documentation (this file)

markdown
Copy
Edit

## Features

- Real-time emotion detection using your webcam
- Streamlit web interface for uploading and analyzing images
- Trained on a CNN using TensorFlow/Keras
- Uses OpenCV's Haar cascade for face detection

## Technologies Used

- Python  
- TensorFlow / Keras  
- OpenCV  
- Streamlit  
- Haar Cascade Classifier  
- CNN (Convolutional Neural Network)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/emotion-detection-cnn.git
   cd emotion-detection-cnn
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv tfenv
source tfenv/bin/activate  # On Windows: tfenv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
How to Run
1. Desktop GUI with Webcam (main.py)
bash
Copy
Edit
python main.py
Launches a window showing real-time webcam video and predicted emotion.

2. Web App (app.py)
bash
Copy
Edit
streamlit run app.py
Opens a browser-based interface where you can upload an image for emotion detection.

Model Details
Trained on a facial emotion dataset (e.g., FER-2013 or custom).

CNN architecture includes multiple convolutional, pooling, and dense layers.

model.h5 contains the pre-trained model used by both the GUI and web app.

Notes
Make sure your webcam is enabled when running main.py.

haarcascade_frontalface_default.xml is required for detecting faces.

Ensure your Python version is compatible (recommendation: Python 3.7–3.10).

Screenshots
Add screenshots of the desktop and web app interfaces here.
