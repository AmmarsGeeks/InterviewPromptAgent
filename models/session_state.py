
import streamlit as st

# models/session_state.py
def init_session_state():
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    
    if 'category' not in st.session_state:
        st.session_state.category = ""
    
    if 'details' not in st.session_state:
        st.session_state.details = {}
    
    if 'prompts' not in st.session_state:
        st.session_state.prompts = []
    
    if 'selected_prompt' not in st.session_state:
        st.session_state.selected_prompt = ""
    
    if 'final_prompt' not in st.session_state:
        st.session_state.final_prompt = ""
    
    if 'ai_response' not in st.session_state:
        st.session_state.ai_response = ""
    
    if 'filename' not in st.session_state:
        st.session_state.filename = ""