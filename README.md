
# 🎯 VisionPilot: Gesture-Controlled Interaction Suite

VisionPilot is a real-time webcam-based control system that lets you interact with applications and browser-based games using hand gestures — no keyboard or mouse required.

🖐️ Move your cursor, 🎮 shoot in games, or 🏎️ steer cars, all using natural hand movements.

---

## 🚀 Features

- 🎯 **Finger-Based Mouse & Click Control**
- 🏎️ **Steering Control for Driving Games**
- 🎮 **Game-Ready with Real-Time Speed**
- 📷 Built using **OpenCV**, **MediaPipe**, and **Streamlit**
- ✅ Works on most standard webcams and modern browsers

---

## 📁 Project Structure

```plaintext
VisionPilot/
├── main.py                  # Entry point (Streamlit app)
├── shooter.py              # Cursor control + shooting mode
├── steering.py             # Steering wheel hand-tracking
├── keyinput.py             # Virtual key presses
├── util.py                 # Helpers for gesture logic
├── config.toml             # UI + detection config
├── requirements.txt        # Python dependencies
├── about.py                # About section (Streamlit)
├── developers.py           # Developer info section
```

---

## 🛠️ Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/abdulmoyeed28/vision-pilot.git
cd vision-pilot
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the App

```bash
streamlit run main.py
```

## 📦 Tech Stack

🧠 Python 3  
🖼️ OpenCV  
🧍‍♂️ MediaPipe  
🌐 Streamlit  
💻 PyAutoGUI  

## 🧠 How It Works

VisionPilot uses MediaPipe’s real-time hand tracking to:  

Detect fingertips and hand poses  
Control the mouse via single-finger gestures  
Simulate clicks (for games like shooters)  
Track two-hand distances (for steering-like motion)  
Gestures are translated into input commands using PyAutoGUI to control applications and games seamlessly.  

---

🏆 **Awards & Recognition**

🥈 **2nd Prize** – Project Expo 2025  
Lords Institute of Engineering & Technology  
Awarded for *VisionPilot* among 60+ competing teams.

---

🙌 **Acknowledgements**

Thanks to the open-source tools that made this possible:

- [Google MediaPipe](https://github.com/google/mediapipe) – real-time hand tracking  
- [OpenCV](https://opencv.org/) – image processing  
- [PyAutoGUI](https://pyautogui.readthedocs.io/) – simulating input events  
- [Streamlit](https://streamlit.io/) – UI interface  

---
