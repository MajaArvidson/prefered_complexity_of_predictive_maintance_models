import streamlit as st # type: ignore
import os
import json
import time

def post_survey_page():
    st.title("Post-Experiment Survey")

    st.subheader("Overall Perceptions of the AI System")

    overall_trust = st.slider(
        "Overall, how much do you trust the AI system?", 1, 7, key="overall_trust"
    )
    overall_understanding = st.slider(
        "Overall, how well did you understand the AI's recommendations?", 1, 7, key="overall_understanding"
    )
    overall_comfort = st.slider(
        "Overall, how comfortable would you be using this system in real life?", 1, 7, key="overall_comfort"
    )

    st.subheader("Cognitive Load / Task Difficulty")

    task_difficulty = st.slider(
        "How mentally demanding was this task?", 1, 7, key="task_difficulty"
    )

    st.subheader("Attention Check")

    attention_check = st.radio(
        "Which of the following actions was recommended by the AI in the experiment?",
        ["Restart router", "Drink water", "Go for a walk", "Ignore system"],
        key="attention_check"
    )

    st.subheader("Optional Feedback")

    feedback = st.text_area(
        "Any comments on the AI system or suggestions for improvement?", key="feedback"
    )

    # Submit button
    if st.button("Submit"):
        response = {
            "participant_id": st.session_state.participant_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "overall_trust": overall_trust,
            "overall_understanding": overall_understanding,
            "overall_comfort": overall_comfort,
            "task_difficulty": task_difficulty,
            "attention_check": attention_check,
            "feedback": feedback
        }

        # Ensure data folder exists
        os.makedirs("data", exist_ok=True)
        filename = f"data/post_survey_{st.session_state.participant_id}.json"

        with open(filename, "w") as f:
            json.dump(response, f, indent=4)

        st.success("Thank you! Your responses have been saved.")
        st.balloons()