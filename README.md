# 😊 Real-Time Emotion Detection using CNN

This project detects human emotions (like Happy, Sad, Angry, etc.) in **real-time using your webcam**, powered by **Convolutional Neural Networks (CNN)** and OpenCV.

---

## 📁 Project Structure

```
real-time-emotion-detection/
│
├── emotion_detector.py         # Main Python script to run the model
├── emotion_model.h5            # Trained CNN model file
├── haarcascade_frontalface.xml # Haar Cascade for face detection
├── README.md                   # Project documentation
```

---

## 🧠 Emotion Classes Detected

- Angry  
- Disgust  
- Fear  
- Happy  
- Sad  
- Surprise  
- Neutral  

---

## 📦 Step-by-Step Setup Instructions

### ✅ 1. Prerequisites

- Python 3.7 or higher
- Webcam (built-in or external)

---

### 📁 2. Clone the Repository

```bash
git clone https://github.com/samrat0033/Emotion_Detection.git
cd Emotion-Detection
```

---

### 🧪 3. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

---

### 📚 4. Install Required Libraries

```bash
pip install keras tensorflow numpy opencv-python
```

---

### 🎯 5. Run the Application

Make sure the files `emotion_model.h5` and `haarcascade_frontalface.xml` are in the same directory as your Python script.

```bash
python emotion_detector.py
```

This will activate your webcam and start detecting emotions in real time.

---

## 🧠 Libraries Used

- `Keras` – For loading the pre-trained CNN model
- `TensorFlow` – Backend for Keras
- `OpenCV` – For webcam access and face detection
- `NumPy` – For image array manipulation

---

## ⚙️ How It Works

1. The webcam feed is captured using `cv2.VideoCapture()`.
2. Faces are detected in each frame using Haar Cascades.
3. The face region is preprocessed and passed through a CNN model.
4. The model outputs an emotion class which is displayed on the screen.

---

## 🖼️ Sample Output

Emotion label is overlaid on the detected face in real-time video feed.

---

## 📞 Contact

For questions, suggestions, or collaboration:

**Samrat Ghorui**  
Email: [sg.samratghorui@gmail.com](mailto:sg.samratghorui@gmail.com)  
GitHub: [samrat0033](https://github.com/samrat0033)  
LinkedIn: [samrat-ghorui-859144296](https://linkedin.com/in/samrat-ghorui-859144296)
