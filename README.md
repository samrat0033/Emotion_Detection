# 😄 Emotion Detection System

An advanced **real-time emotion detection system** using **CNN**, **TensorFlow**, **OpenCV**, and **Streamlit**. This application can identify emotions from human facial expressions using webcam input or uploaded images. Whether you're building an AI assistant or analyzing sentiment, this tool offers a versatile interface with both GUI and web access.

---

## 🧠 Features

- 📷 Real-time emotion detection via webcam
- 🌐 Web-based image analysis using Streamlit
- 🧪 CNN model trained on facial expression data
- 👁️ Face detection using Haar Cascade
- 💾 Easy-to-run with minimal setup

---

## 📁 Project Structure


```
Pre-trained Model: Ready-to-use emotion classification model
📁 Project Structure
emotion-classification/
├── test/                          # Test datasets and files
├── tfenv/                         # TensorFlow environment files
├── train/                         # Training datasets and scripts
├── app.py                         # Streamlit web application
├── emotion-classification...      # Main emotion classification module
├── haarcascade_frontalface...     # Haar cascade for face detection
├── main.py                        # Desktop GUI application with webcam
├── model.h5                       # Pre-trained CNN model
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```


---

## 🔧 Technologies Used

- 🐍 Python 3.x
- 🧠 TensorFlow / Keras
- 👁️ OpenCV
- 🌐 Streamlit
- 📊 CNN (Convolutional Neural Network)
- 📂 Haar Cascade Classifier

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emotion-detection-cnn.git
   cd emotion-detection-cnn


## Create and activate a virtual environment (recommended)

bash
```
python -m venv myenv
source myenv/bin/activate     # On Windows: tfenv\Scripts\activate
```
## Install required packages

```
pip install -r requirements.txt
```

## 🖥️ How to Run
### 💻 Desktop GUI App (main.py)
This application uses your webcam and shows live emotion predictions.
```
python main.py 
```

Make sure your webcam is enabled.

Detected emotions are displayed in real-time.

## 🌍 Web App (app.py)
A user-friendly web interface built with Streamlit for uploading and analyzing images.
```
streamlit run app.py
```
Opened in your browser.

Give permission to open your webcam and get emotion prediction with visualization.

## 🧠 Model Details
- Built using Convolutional Neural Networks (CNN).

- Trained on datasets like FER-2013 or similar emotion datasets.

- Supports emotion classes like: 😄 Happy, 😢 Sad, 😠 Angry, 😲 Surprised, 😐 Neutral.

- The model (model.h5) is loaded for prediction in both the GUI and Streamlit apps.

## 🖼️ Demo
<img width="1486" height="985" alt="image" src="https://github.com/user-attachments/assets/1b977c9e-345d-4ba8-8bcb-eb8fbb45c8eb" />
<img width="1567" height="1361" alt="image" src="https://github.com/user-attachments/assets/b0667df8-3449-48f7-9f88-9c35154e3ef5" />


[LIVE](https://emotion-detection-3wfz.onrender.com)


### ⚙️ Requirements
- Python 3.7 - 3.12

- TensorFlow

- OpenCV

- Streamlit

- Numpy, Matplotlib, etc.

All dependencies are listed in requirements.txt.

## 📝 Acknowledgments
- FER-2013 Dataset — Public dataset used for facial expression recognition.

- OpenCV — Computer vision library for real-time face detection.

- TensorFlow — Deep learning framework.

- Streamlit — Simple framework for creating web apps in Python.
- Kaggle for the Dataset [Data Set Link](https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset)

### 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

🙋‍♂️ Author
Samrat Ghorui
📫 sg.samratghorui@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/samrat-ghorui/) | [GitHub](https://github.com/samrat0033/)


