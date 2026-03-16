import streamlit as st # type: ignore
from utils.navigation import set_page

def consent_page():

    st.title("Informed Consent for Participation in Research Study")

    st.subheader("Study Title: User Perceptions of AI Decision-Making Systems")

    st.header("Purpose of the Study")
    st.write("""
    You are invited to participate in a research study investigating how people perceive and interact with artificial intelligence (AI) decision-support systems. The goal of this study is to understand how different types of AI explanations influence user perceptions and trust in AI recommendations.
    """)

    st.header("What Participation Involves")
    st.write("""
    If you agree to participate, you will be asked to review several short scenarios where an AI system provides a recommendation based on telemetry data. For each scenario, you will be asked to rate your perceptions of the system and answer a few short questions. The study is expected to take approximately 5–10 minutes to complete.
    """)

    st.header("Voluntary Participation")
    st.write("""
    Your participation in this study is completely voluntary. You may stop participating at any time without penalty and without providing a reason.
    """)

    st.header("Confidentiality and Data Handling")
    st.write("""
    No personally identifying information will be collected. Your responses will be stored anonymously and used only for research purposes.
    """)

    st.header("Consent")
    st.write("""
    By selecting the option below and continuing to the study, you confirm that:
    - You have read and understood the information above
    - You are at least 18 years old
    - You voluntarily agree to participate in this study
    """)

    st.divider()

    consent = st.checkbox("I have read the information above and agree to participate :red[*]")

    if st.button("Start Study"):
        if consent:
            set_page("instructions")
        else:
            st.write(":red[You have to consent to participate in the study.]")