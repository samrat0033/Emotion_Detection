from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import streamlit as st
import time # Import time for the sleep

# --- Caching Models ---
# Use st.cache_resource to load the models only once
@st.cache_resource
def load_face_classifier():
    try:
        return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    except Exception as e:
        st.error(f"Error loading face cascade: {e}. Make sure 'haarcascade_frontalface_default.xml' is available.")
        st.stop()

@st.cache_resource
def load_emotion_classifier():
    try:
        return load_model('model.h5', compile=False)
    except Exception as e:
        st.error(f"Error loading emotion model: {e}. Make sure 'model.h5' is in the correct directory.")
        st.stop()

face_classifier = load_face_classifier()
classifier = load_emotion_classifier()

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

st.title("Real-time Emotion Detector")
st.write("This application uses your webcam to detect emotions in real-time.")

# --- Session State for Webcam Control ---
if 'webcam_started' not in st.session_state:
    st.session_state.webcam_started = False

# Buttons
col1, col2 = st.columns(2)
with col1:
    start_button = st.button("Start Webcam")
with col2:
    stop_button = st.button("Stop Webcam")

if start_button:
    st.session_state.webcam_started = True
    st.write("Webcam started. Looking for faces...")

if stop_button:
    st.session_state.webcam_started = False
    st.write("Webcam stopped.")

# Placeholder for the video feed
video_placeholder = st.empty()
cap = None # Initialize cap outside the conditional blocks

if st.session_state.webcam_started:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam. Please ensure it's not in use by another application.")
        st.session_state.webcam_started = False # Reset state if webcam fails to open
    else:
        while st.session_state.webcam_started: # Loop continues as long as webcam_started is True
            ret, frame = cap.read()
            if not ret:
                st.error("Error: Could not read frame from webcam. Stopping webcam.")
                st.session_state.webcam_started = False # Stop if frame read fails
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                if np.sum(roi_gray) != 0:
                    roi = roi_gray.astype('float') / 255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)

                    prediction = classifier.predict(roi)[0]
                    label = emotion_labels[prediction.argmax()]
                    label_position = (x, y)
                    cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # THIS IS THE CHANGED LINE:
            video_placeholder.image(rgb_frame, channels="RGB", use_container_width=True)

            time.sleep(0.01)

            if not st.session_state.webcam_started:
                break

        if cap and cap.isOpened():
            cap.release()
        st.write("Webcam session ended.")

st.markdown(
    """
    **Instructions:**
    1. Click 'Start Webcam' to begin real-time emotion detection.
    2. Ensure your `haarcascade_frontalface_default.xml` and `model.h5` files are in the same directory as this script.
    3. Click 'Stop Webcam' to end the session.
    """
)