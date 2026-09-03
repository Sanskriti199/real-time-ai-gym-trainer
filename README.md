# 🏋️ AI Real-Time Gym Coach

> An AI-powered fitness coach that uses Computer Vision and Large Language Models to analyze exercises in real time, track performance, and provide intelligent coaching feedback.

🚀 **[Try AI Real-Time Gym Coach](https://ai-apna-coach.netlify.app/)**

---

## 📌 Overview

**AI Real-Time Gym Coach** is an intelligent fitness application that combines **Computer Vision, Pose Estimation, and Large Language Models** to provide real-time workout assistance.

The application uses a webcam to analyze body posture, count repetitions, evaluate exercise form, provide AI-generated coaching feedback, and maintain workout progress and history.

---

## ✨ Features

- 🎥 Real-time pose detection
- 🔢 Automatic repetition counting
- 🧍 Exercise form correction
- 🤖 AI-powered workout coaching
- 🔊 AI-generated voice feedback
- 📊 Workout progress tracking
- 🔐 User authentication
- 📜 Workout history
- 🏋️ Multi-exercise support
- ⚡ Real-time webcam processing

---

## 🏋️ Supported Exercises

- Squats
- Push-ups
- Biceps Curls
- Shoulder Press
- Lunges

---

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – Interactive web application
- **Streamlit WebRTC** – Real-time camera streaming
- **MediaPipe** – Human pose detection
- **OpenCV** – Computer vision and image processing
- **SQLite** – User authentication and workout history
- **Groq LLM API** – AI coaching and workout feedback
- **gTTS** – Voice feedback generation
- **NumPy** – Numerical computations
- **python-dotenv** – Environment variable management

---

## ⚙️ How It Works

1. User logs into the application.
2. Selects an exercise, sets, and repetitions.
3. Webcam starts through WebRTC.
4. MediaPipe detects body landmarks.
5. The application counts repetitions and evaluates form.
6. Groq LLM generates personalized coaching feedback.
7. Voice feedback is generated using gTTS.
8. Workout progress and history are stored in SQLite.

---

## 🚀 Live Application

### 🌐 Main Application

**[https://ai-apna-coach.netlify.app/](https://ai-apna-coach.netlify.app/)**

The main web interface for **AI Real-Time Gym Coach**.

### 🤖 AI Coach

**[https://real-time-ai-coach.streamlit.app/](https://real-time-ai-coach.streamlit.app/)**

Launch the real-time AI workout coaching environment.

---

## 🧩 Application Architecture

```text
                    AI REAL-TIME GYM COACH
                             │
                             ▼
                    Main Web Application
                          Netlify
                             │
                             ▼
                    AI Coaching Application
                         Streamlit
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
             WebRTC Camera          User Input
                 │
                 ▼
             OpenCV + MediaPipe
                 │
                 ▼
          Pose & Exercise Analysis
                 │
        ┌────────┴─────────┐
        ▼                  ▼
  Rep Counting        Form Analysis
        │                  │
        └────────┬─────────┘
                 ▼
              Groq LLM
                 │
                 ▼
          AI Coaching Feedback
                 │
                 ▼
              gTTS Voice
                 │
                 ▼
          Workout Progress
                 │
                 ▼
               SQLite
