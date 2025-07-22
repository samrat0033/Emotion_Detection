Emotion Classification Project
This project provides a robust solution for real-time emotion classification using Convolutional Neural Networks (CNNs) with TensorFlow and OpenCV. It features both a desktop GUI application that utilizes a webcam and a web-based application built with Streamlit for broader accessibility.

Features
Real-time Emotion Detection: Classify emotions from live webcam feed.

GUI Application: A desktop interface (main.py) for direct interaction with the webcam.

Web Application: A user-friendly web interface (app.py) powered by Streamlit.

CNN Model: Utilizes a pre-trained or custom-trained CNN model (model.h5) for accurate emotion prediction.

Face Detection: Employs OpenCV's Haar Cascades for efficient face detection.

Folder Structure
The project is organized as follows:

.
├── test/                       # Contains test scripts or data (if any)
├── tfvenv/                     # Virtual environment for TensorFlow (or similar)
├── train/                      # Scripts and data related to model training
├── app.py                      # Streamlit web application
├── emotion-classification...   # (Potentially a dataset or config file)
├── haarcascade_frontalface_default.xml # OpenCV Haar Cascade for face detection
├── main.py                     # GUI application using webcam
├── model.h5                    # Pre-trained CNN model for emotion classification
├── README.md                   # This README file
└── requirements.txt            # Python dependencies

Installation
To set up the project locally, follow these steps:

Clone the repository:

git clone <your-repository-url>
cd <your-project-directory>

Create a virtual environment (recommended):

python -m venv tfvenv
source tfvenv/bin/activate  # On Windows: `tfvenv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Ensure you have tensorflow, opencv-python, streamlit, and Pillow (or Pillow-SIMD for better performance) listed in your requirements.txt.

Usage
1. Running the GUI Application (Webcam)
To launch the desktop application that uses your webcam for real-time emotion detection:

python main.py

This will open a new window displaying your webcam feed with detected faces and their classified emotions.

2. Running the Web Application (Streamlit)
To start the web application:

streamlit run app.py

After running this command, a new tab will automatically open in your web browser, displaying the Streamlit application. You can then interact with the web interface for emotion classification.

Model
The project uses model.h5 as the pre-trained CNN model for emotion classification. The haarcascade_frontalface_default.xml file is crucial for detecting faces in the input frames before feeding them to the CNN model.

Technologies Used
Python

TensorFlow / Keras: For building and training the CNN model.

OpenCV: For image processing, video capture, and face detection.

Streamlit: For creating the interactive web application.

Tkinter / PyQt / Kivy: (Implicitly, based on main.py being a GUI file) for the desktop GUI.

Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

License
[Specify your license here, e.g., MIT License, Apache 2.0, etc.]
