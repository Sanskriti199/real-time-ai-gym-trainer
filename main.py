import streamlit as st
import os
from services.auth.login_wall import render_login_wall
from services.state.session_default import initial_session_default  # type: ignore
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import load_css, inject_local_font, inject_webrtc_styles
from services.persistence.exercise_repository import init_db
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from services.vision.exercise_video_processor import VideoProcessorClass


def main():


    st.set_page_config(
        page_icon="⚡",
        page_title="AI Real-time GYM Coach",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    load_css(os.path.join(os.getcwd(),"static","style.css"))
    inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")

    init_db()
    

    if not render_login_wall():
        return

    initial_session_default()

    workout_started=st.session_state.get("workout_started", False)


    with st.sidebar:
        st.title("My AI Coach")

        if st.session_state.username:
            st.caption(f"👤 Logged in as {st.session_state.username}")
 
        st.divider()

        st.subheader("Workout Plan")

        if not workout_started:
            with st.form("workout_config_form"):
                st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")
                st.number_input("Sets", min_value=0, max_value=150, key="plan_sets", step=1)
                st.number_input("Reps per Set", min_value=0, max_value=150, key="plan_reps", step=1)

                start_session_button = st.form_submit_button("Start Workout", width="stretch")

            if start_session_button:
                st.session_state["workout_started"] = True
                st.rerun()

        else:
            exercise=st.session_state.get("plan_exercise")
            sets=st.session_state.get("plan_sets")
            reps=st.session_state.get("plan_reps")

            st.info(f"**{exercise}**-- {sets} Sets/ {reps} Reps")

            end_session_button=st.button("End Workout", key="end_session_button",width="stretch")

            if end_session_button:
                st.session_state["workout_started"]=False
                st.rerun()


        if workout_started:
            st.divider()

            exercise=st.session_state.get("plan_exercise")
            total_reps=st.session_state.get("reps")
            current_set_reps=st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets=st.session_state.get("plan_sets")

            st.subheader("Progress")

            st.markdown(f"""
            <div class="progress-card">
                <span class="progress-title">Total Reps</span>
                <span class="progress-value">{total_reps}</span>
            </div>

            <div class="progress-card">
                <span class="progress-title">Current Set Reps</span>
                <span class="progress-value">{current_set_reps}/{reps_per_set}</span>
            </div>

            <div class="progress-card">
                <span class="progress-title">Sets Completed</span>
                <span class="progress-value">{sets_completed}/{target_sets}</span>
            </div>
            """, unsafe_allow_html=True)

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")

                st.markdown(f"""
                <div class="progress-card">
                    <span class="progress-title">Knee Angle</span>
                    <span class="progress-value">{st.session_state.knee_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Back Angle</span>
                    <span class="progress-value">{st.session_state.back_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Depth Status</span>
                    <span class="progress-value">{st.session_state.depth_status}</span>
                </div>
                """, unsafe_allow_html=True)

            elif exercise == "Push-ups":
                st.subheader("Push-up Metrics")

                st.markdown(f"""
                <div class="progress-card">
                    <span class="progress-title">Elbow Angle</span>
                    <span class="progress-value">{st.session_state.elbow_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Body Alignment</span>
                    <span class="progress-value">{st.session_state.body_alignment}</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Hip Position</span>
                    <span class="progress-value">{st.session_state.hip_status}</span>
                </div>
                """, unsafe_allow_html=True)

            elif exercise == "Bicep Curls (Dumbbell)":
                st.subheader("Curl Metrics")

                st.markdown(f"""
                <div class="progress-card">
                    <span class="progress-title">Elbow Angle</span>
                    <span class="progress-value">{st.session_state.elbow_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Shoulder Stability</span>
                    <span class="progress-value">{st.session_state.shoulder_status}</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Swing Detection</span>
                    <span class="progress-value">{st.session_state.swing_status}</span>
                </div>
                """, unsafe_allow_html=True)

            elif exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")

                st.markdown(f"""
                <div class="progress-card">
                    <span class="progress-title">Elbow Angle</span>
                    <span class="progress-value">{st.session_state.elbow_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Arm Extension</span>
                    <span class="progress-value">{st.session_state.extension_status}</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Back Arch</span>
                    <span class="progress-value">{st.session_state.back_arch_status}</span>
                </div>
                """, unsafe_allow_html=True)

            elif exercise == "Lunges":
                st.subheader("Lunge Metrics")

                st.markdown(f"""
                <div class="progress-card">
                    <span class="progress-title">Front Knee Angle</span>
                    <span class="progress-value">{st.session_state.front_knee_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Torso Angle</span>
                    <span class="progress-value">{st.session_state.torso_angle}°</span>
                </div>

                <div class="progress-card">
                    <span class="progress-title">Balance Status</span>
                    <span class="progress-value">{st.session_state.balance_status}</span>
                </div>
                """, unsafe_allow_html=True)

    st.title("AI Real-time GYM Coach")
    st.markdown("#### Real-time pose detection with proactive AI voice coaching")

    if not workout_started:
        st.markdown("""
<div class="workout-box">
    <div class="workout-title">👉 Set your workout plan</div>
    <div class="workout-subtitle">
        Choose your exercise, sets and reps in the sidebar.<br>
        Then click <strong>Start Workout</strong> to activate the camera and AI coach.
    </div>
</div>
""", unsafe_allow_html=True)


    else :
        context= webrtc_streamer(
            key="exercise-analysis",  
            mode=WebRtcMode.SENDRECV,
            video_processor_factory=VideoProcessorClass,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            media_stream_constraints={
            "video": True,
            "audio": False,
            },
            async_processing=True
        )
        inject_webrtc_styles()

    st.markdown("#### Workout History")

    
        
if __name__ == "__main__":
    main()