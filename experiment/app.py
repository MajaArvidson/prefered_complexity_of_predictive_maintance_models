import streamlit as st # type: ignore
from app_pages import consent, instructions, case, survey, quit

ROUTES = {
    "consent": consent.consent_page,
    "instructions": instructions.instructions_page,
    "cases": case.case_page,
    "survey": survey.post_survey_page,
    "quit": quit.quit_page
}

st.set_page_config(
    page_title="User Perceptions of AI",
    page_icon="🤖",
    initial_sidebar_state="collapsed"
)

if st.sidebar.button("Quit study"):
    st.session_state.page = "quit"

if "page" not in st.session_state:
    st.session_state.page = "consent"

ROUTES[st.session_state.page]()