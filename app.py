# app.py
import streamlit as st
from models.session_state import init_session_state
from views.category_view import render_category_selection
from views.detail_view import render_detail_collection
from views.prompt_view import render_prompt_generation
from views.result_view import render_result_display

def main():
    st.set_page_config(
        page_title="AI Prompt Engineering Studio",
        page_icon="🤖",
        layout="wide"
    )
    
    # Initialize session state
    init_session_state()
    
    # Setup sidebar
    st.sidebar.title("Navigation")
    app_state = st.sidebar.radio("Go to", [
        "Category Selection",
        "Details Collection",
        "Prompt Generation",
        "Results"
    ], index=st.session_state.current_step)
    
    # Render appropriate view based on state
    if app_state == "Category Selection":
        render_category_selection()
    elif app_state == "Details Collection":
        render_detail_collection()
    elif app_state == "Prompt Generation":
        render_prompt_generation()
    elif app_state == "Results":
        render_result_display()

if __name__ == "__main__":
    main()