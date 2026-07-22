# AI Real-Time Gym Coach

An AI-powered fitness coach that uses Computer Vision and Large Language Models to analyze exercises in real time. The application tracks body posture, counts repetitions, monitors workout progress, and provides AI-generated voice feedback for a smarter workout experience.

---

## Features

- Real-time pose detection
- Automatic repetition counting
- Form correction
- AI-powered workout coaching
- Voice feedback
- Workout progress tracking
- User authentication
- Workout history
- Multi-exercise support

---

## Supported Exercises

- Squats
- Push-ups
- Biceps Curls
- Shoulder Press
- Lunges

---

## Tech Stack

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

## How It Works

1. User logs into the application.
2. Selects an exercise, sets, and repetitions.
3. Webcam starts through WebRTC.
4. MediaPipe detects body landmarks.
5. The application counts repetitions and evaluates form.
6. AI generates coaching feedback.
7. Voice feedback is played.
8. Workout progress is tracked and stored.

---

## Future Enhancements

- Workout analytics dashboard
- Calories burned estimation
- Personalized workout plans
- Additional exercise support
- Cloud deployment
