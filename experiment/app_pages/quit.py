import streamlit as st # type: ignore

def quit_page():
    st.info("You have withdrawn from the study.")
    st.write("Thank you for your time.")
    st.stop()