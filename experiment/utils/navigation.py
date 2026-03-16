import streamlit as st # type: ignore

def set_page(page):
    scroll_to_top()
    st.session_state.page = page
    st.rerun()

def scroll_to_top():
    top = st.empty()
    top.markdown(" ")