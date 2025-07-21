# views/category_view.py
import streamlit as st

def render_category_selection():
    st.title("🏢 AI Prompt Engineering Studio")
    st.subheader("What would you like me to help you with today?")
    
    categories = {
        "1": "Prompt Engineering & Analysis",
        "2": "Technical Specifications & Architecture", 
        "3": "Project Proposals & Client Communication", 
        "4": "Code Documentation & Testing",
        "5": "Development Estimates & Project Management",
        "6": "Deployment Guides & DevOps",
        "7": "Technical Interview Questions & Hiring",
        "8": "Custom Task"
    }
    
    cols = st.columns(2)
    for i, (key, value) in enumerate(categories.items()):
        with cols[i % 2]:
            if st.button(value, key=f"cat_{key}", use_container_width=True):
                st.session_state.category = value
                st.session_state.current_step = 1
                st.experimental_rerun()
