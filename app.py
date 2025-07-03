import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# ✅ Load YOLOv8 Model
model = YOLO('D:/YOLOv8-Hand-Gesture-Detection-App/runs/detect/gesture_detection/weights/best.pt')  # Update path as needed

# ✅ Gesture Class Labels with Emojis
gesture_classes = [
    'Call 🤙🏻', 'Peace ✌🏻', 'Stop 🛑', 'Stop Inverted 🛑', 'Like 👍🏻', 'Dislike 👎🏻',
    'OK 👌🏻', 'Rock 🤘🏻', 'Mute 🤫', 'One ☝🏻', 'Two Up ✌🏻', 'Two Up Inverted ✌🏻',
    'Four 🖖🏻', 'Fist ✊🏻', 'Three 🤟🏻', 'Palm 🖐🏻'
]

# ✅ Streamlit Page Config
st.set_page_config(page_title="YOLOv8 Gesture Detection", layout="centered")
st.title("🤖 Real-Time Gesture Detection using YOLOv8")
st.markdown("**Detectable Gestures:** " + ", ".join(gesture_classes))

# ✅ Mode Selection
mode = st.radio("Choose Mode:", ["📷 Live Webcam Detection", "🖼️ Upload Image for Detection"], horizontal=True)

# ✅ -------- Webcam Detection --------
if mode == "📷 Live Webcam Detection":
    st.markdown("### 📷 Live Webcam Detection")

    # ✅ Session State for Webcam
    if "run" not in st.session_state:
        st.session_state.run = False

    start = st.button("▶️ Start Webcam")
    stop = st.button("⏹️ Stop Webcam")

    FRAME_WINDOW = st.image([])

    if start:
        st.session_state.run = True

    if stop:
        st.session_state.run = False

    cap = cv2.VideoCapture(0)

    while st.session_state.run:
        ret, frame = cap.read()
        if not ret:
            st.error("❌ Failed to capture frame")
            break

        # ✅ YOLOv8 Detection
        results = model.predict(frame, conf=0.5, verbose=False)
        result_frame = results[0].plot()
        result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)

        FRAME_WINDOW.image(result_frame)

    cap.release()

# ✅ -------- Image Upload Detection --------
elif mode == "🖼️ Upload Image for Detection":
    st.markdown("### 🖼️ Upload Image for Detection")
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="📸 Uploaded Image", use_column_width=True)

        if st.button("✅ Run Detection"):
            img_np = np.array(img.convert('RGB'))
            results = model.predict(img_np, conf=0.5, verbose=False)
            result_img = results[0].plot()
            result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

            st.image(result_img, caption="✅ Detection Output", use_column_width=True)
