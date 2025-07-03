✋ YOLOv8 Hand Gesture Detection App 🤖🎥
A real-time Computer Vision project that detects and classifies multiple hand gestures using YOLOv8 (Ultralytics) and a Streamlit Web Interface.

🚀 Built with Python, OpenCV, and Streamlit, this project demonstrates object detection, custom model training, and web app deployment.

📌 Project Highlights
✅ Real-time Webcam Stream Detection
✅ Multi-class Hand Gesture Recognition (Like 👍🏻 Peace ✌🏻 Stop 🛑 Rock 🤘🏻 etc.)
✅ Emoji-based visual representation for each gesture
✅ Streamlit UI for easy interaction
✅ Custom trained YOLOv8 model with 16 gesture classes
✅ Deployable on Streamlit Cloud or Hugging Face Spaces

📊 Problem Statement
In the field of Human-Computer Interaction (HCI), contactless control using gestures is becoming essential for:

AI-controlled interfaces

Sign Language Recognition

Virtual Gaming

Smart Devices

This app enables detection of gestures like:

Gesture	Emoji
Peace	✌🏻
Like	👍🏻
Dislike	👎🏻
Stop	🛑
Rock	🤘🏻
Fist	✊🏻
One	☝🏻
Palm	🫱🏻

(You can add more gesture classes as per your dataset)

🧠 Tech Stack
Domain	Tools Used
Language	Python
Deep Learning Framework	YOLOv8 (Ultralytics)
Libraries	OpenCV, PIL, Streamlit, Ultralytics
UI Framework	Streamlit
Model Format	YOLOv8 .pt weights
Deployment Ready?	✅ Yes

📊 Model Training Summary
Metric	Value
Total Training Images	9,948
Total Validation Images	449
Total Epochs	33
Precision	98.85%
Recall	98.69%
mAP@0.5	99.37%
mAP@0.5:0.95	85.51%

✅ Training performed on a custom hand gesture dataset with 16 classes

🚀 How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/karthik-lakkimsetti/YOLOv8-Hand-Gesture-Detection-App.git
cd YOLOv8-Hand-Gesture-Detection-App
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv yolov8
.\yolov8\Scripts\activate   # On Windows
3. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your YOLOv8 Model Weights
Place your YOLOv8 .pt file (example: best.pt) in the correct directory and update the model path in app.py:

python
Copy
Edit
model = YOLO('path/to/your/best.pt')
5. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
📂 Folder Structure
bash
Copy
Edit
YOLOv8-Hand-Gesture-Detection-App/
├── app.py                  # Streamlit app for real-time hand gesture detection
├── training.py             # YOLOv8 training script (for custom model training)
├── Pretrained yolov8s.py   # YOLOv8 model inference on sample images (optional)
├── requirements.txt        # Python package dependencies
├── .gitignore              # Files and folders to ignore in Git
├── Readme.md               # Project documentation (this file)
├── yolov8/                 # Virtual environment folder (ignored from Git)
├── data/                   # Your custom dataset (images and labels) (ignored from Git)
├── runs/                   # YOLOv8 training output (saved model weights, logs) (ignored from Git)
✅ Skills Demonstrated
🎯 Real-time Computer Vision using YOLOv8

🧠 Custom Object Detection Model Training

💻 Streamlit Web App Development

📦 Python Project Structure & Best Practices

📈 Metrics Tracking during Training

🌐 Git & GitHub Version Control

🏗️ Deployment Readiness for Cloud Hosting

💡 Future Improvements
🌍 Deploy to Streamlit Cloud or Hugging Face Spaces

🎥 Add Video File Detection Mode

📓 Include Jupyter Notebook for Model Training Walkthrough

🖥️ Improve UI/UX with custom Streamlit components

✋ Expand for Full Sign Language Recognition (ASL)

🤝 Let's Connect
📧 Email: karthiksrivardhan45@gmail.com
🔗 LinkedIn: Karthik Sri Vardhan
🌐 GitHub: karthik-lakkimsetti

