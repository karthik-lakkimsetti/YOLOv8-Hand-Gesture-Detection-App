
<h1 align="center">✋ YOLOv8 Hand Gesture Detection App 🤖🎥</h1>

<p align="center">
A <strong>real-time Computer Vision project</strong> that detects and classifies <strong>multiple hand gestures</strong> using <code>YOLOv8 (Ultralytics)</code> and a <code>Streamlit Web Interface</code>.
</p>

---

🚀 <strong>Built with Python, OpenCV, and Streamlit</strong>, this project demonstrates <em>object detection</em>, <em>custom model training</em>, and <em>web app deployment</em>.

---

## 📌 Key Features

- ✅ Real-time <strong>Webcam Stream Detection</strong>
- ✅ <strong>Multi-class Hand Gesture Recognition</strong> (Like 👍🏻 Peace ✌🏻 Stop 🛑 Rock 🤘🏻 etc.)
- ✅ Emoji-based <strong>visual representation</strong> for each gesture
- ✅ <strong>Streamlit UI</strong> for easy interaction
- ✅ <strong>Custom trained YOLOv8 model</strong> with 16 gesture classes
- ✅ Deployable on <strong>Streamlit Cloud</strong> or <strong>Hugging Face Spaces</strong>

---

## 📊 Problem Statement

In the field of <strong>Human-Computer Interaction (HCI)</strong>, <strong>contactless control</strong> using gestures is becoming essential for:

- 🤖 AI-controlled interfaces  
- ✋ Sign Language Recognition  
- 🎮 Virtual Gaming  
- 📱 Smart Devices  

This app enables detection of gestures like:

| Gesture | Emoji |
|--------|-------|
| Peace  | ✌🏻   |
| Like   | 👍🏻  |
| Dislike| 👎🏻  |
| Stop   | 🛑    |
| Rock   | 🤘🏻  |
| Fist   | ✊🏻   |
| One    | ☝🏻   |
| Palm   | 🫱🏻  |

_(You can add more gesture classes based on your dataset)_

---

## 🧠 Tech Stack

| Domain                  | Tools Used                          |
|------------------------|-------------------------------------|
| Language                | Python                              |
| Deep Learning Framework | YOLOv8 (Ultralytics)                |
| Libraries               | OpenCV, PIL, Streamlit, Ultralytics |
| UI Framework            | Streamlit                           |
| Model Format            | YOLOv8 `.pt` weights                |
| Deployment Ready?       | ✅ Yes                               |

---

## 📈 Model Training Summary

| Metric                  | Value  |
|-------------------------|--------|
| Total Training Images   | 9,948  |
| Total Validation Images | 449    |
| Total Epochs            | 33     |
| Precision               | 98.85% |
| Recall                  | 98.69% |
| mAP@0.5                 | 99.37% |
| mAP@0.5:0.95            | 85.51% |

✅ Training performed on a <strong>custom hand gesture dataset with 16 classes</strong>

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/karthik-lakkimsetti/YOLOv8-Hand-Gesture-Detection-App.git
cd YOLOv8-Hand-Gesture-Detection-App
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv yolov8
.\yolov8\Scriptsctivate   # On Windows
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your YOLOv8 Model Weights

Place your YOLOv8 `.pt` file (e.g., `best.pt`) in the project directory.  
Then update the path in `app.py`:

```python
model = YOLO('path/to/your/best.pt')
```

### 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```bash
YOLOv8-Hand-Gesture-Detection-App/
├── app.py                  # Streamlit app
├── training.py             # YOLOv8 training script
├── Pretrained yolov8s.py   # Sample inference (optional)
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files/folders
├── README.md               # Project documentation
├── yolov8/                 # Virtual environment (ignored)
├── data/                   # Custom dataset (ignored)
└── runs/                   # YOLO training outputs (ignored)
```

---

## ✅ Skills Showcased

- 🎯 Real-time Computer Vision using YOLOv8  
- 🔍 Custom Object Detection Model Training  
- 🌐 Streamlit Web App Development  
- 🧱 Clean Python Project Structuring  
- 🧠 Model Training and Metrics Tracking  
- ☁️ Ready for Deployment  
- 💻 Version Control with Git & GitHub  

---

## 💡 Future Improvements

- ☁️ Deploy on **Streamlit Cloud** or **Hugging Face Spaces**
- 📹 Support for **video file gesture detection**
- 🧪 Add **Jupyter Notebook** walkthrough for training
- ✨ Enhance UI with Streamlit custom components
- 🤟 Extend to full **ASL gesture recognition**

---

## 🤝 Let's Connect

📧 Email: [karthiksrivardhan45@gmail.com](mailto:karthiksrivardhan45@gmail.com)  
🔗 LinkedIn: [Karthik Sri Vardhan](https://www.linkedin.com/in/karthik-sri-vardhan/)  
🌐 GitHub: [@karthik-lakkimsetti](https://github.com/karthik-lakkimsetti)
