**Vision Assist System for Visually Impaired Users**

An intelligent assistive system that uses computer vision (YOLO-based object detection) and speech synthesis to help visually impaired users understand their surroundings through audio feedback.

**Problem Statement**

Visually impaired individuals face difficulties in perceiving their surroundings, especially identifying objects and obstacles in real time. Existing assistive tools are either expensive or limited in functionality.
This project aims to provide an affordable, extensible, and intelligent vision-based assistive system that detects objects from images and conveys the information through natural speech.

**Objectives**

Detect common objects in the environment using computer vision
Convert detection results into meaningful spoken descriptions
Design a modular and extensible Python-based system
Provide a foundation for real-time assistive applications

**Features**

🔍 Object detection using YOLOv5
🔊 Speech output describing detected objects
🧩 Modular code structure (detect, speech, main)
📂 Simple image-based input (easy to extend to camera feed)
🛠️ Clean and reproducible setup using requirements.txt

**Project Structure**

visionassist/
├── data/
│   └── sample_images/
│       └── room.jpg
├── src/
│   ├── main.py        # Entry point
│   ├── detect.py      # Object detection logic
│   └── speech.py      # Text-to-speech logic
├── .gitignore
├── requirements.txt
└── README.md

**Technologies Used**

Python 3
YOLOv5 (Object Detection)
PyTorch
OpenCV
Speech synthesis (TTS)

**Setup Instructions**

Create and activate a virtual environment - python -m venv venv  
                                            Windows- .\venv\Scripts\activate
                                            Linux / macOS- source venv/bin/activate
Install dependencies - pip install -r requirements.txt

**How to Run**

1.Place an image inside: data/sample_images/
2.Update the image filename in src/main.py if needed.
3.Run the application: python src/main.py
**🎧 The system will speak out the detected objects.**

**Sample Output**

“I see a chair, a table, and a person.”
