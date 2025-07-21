# views/detail_view.py
import streamlit as st
from models.prompt_model import get_detail_fields

def render_detail_collection():
    if not st.session_state.category:
        st.warning("Please select a category first")
        st.session_state.current_step = 0
        st.experimental_rerun()
    
    st.title(f"📋 {st.session_state.category}")
    st.write("Please provide the following details:")
    
    # Get field configuration based on category
    fields = get_detail_fields(st.session_state.category)
    
    with st.form("details_form"):
        details = {}
        for field in fields:
            if field["type"] == "text_area":
                details[field["name"]] = st.text_area(field["label"], key=field["name"])
            else:
                details[field["name"]] = st.text_input(field["label"], key=field["name"])
        
        submitted = st.form_submit_button("Generate Prompts")
        if submitted:
            st.session_state.details = details
            st.session_state.current_step = 2
            st.experimental_rerun()