# views/prompt_view.py
import streamlit as st
from controllers.prompt_controller import generate_prompts

def render_prompt_generation():
    st.title("🎯 Prompt Options")
    
    # Generate prompts if not already generated
    if not st.session_state.prompts:
        st.session_state.prompts = generate_prompts(
            st.session_state.category, 
            st.session_state.details
        )
    
    # Display prompt options
    st.write("### Generated Prompt Options:")
    for i, prompt in enumerate(st.session_state.prompts):
        if st.button(prompt, key=f"prompt_{i}", use_container_width=True):
            st.session_state.selected_prompt = prompt
            st.session_state.final_prompt = prompt
    
    # Custom prompt option
    st.write("### Or create your own:")
    custom_prompt = st.text_area("Enter custom prompt", height=150)
    if st.button("Use Custom Prompt", disabled=not custom_prompt):
        st.session_state.selected_prompt = custom_prompt
        st.session_state.final_prompt = custom_prompt
    
    # Refinement section
    if st.session_state.final_prompt:
        st.divider()
        st.write("### Refine Prompt")
        refinement_option = st.radio("Refinement options:", [
            "Use as is",
            "Add specific details",
            "Change tone/style",
            "Add requirements"
        ])
        
        if refinement_option != "Use as is":
            refinement_text = st.text_input("Enter refinement details")
            if refinement_text:
                if refinement_option == "Add specific details":
                    st.session_state.final_prompt += f" Additional details: {refinement_text}"
                elif refinement_option == "Change tone/style":
                    st.session_state.final_prompt += f" Use a {refinement_text} tone/style."
                elif refinement_option == "Add requirements":
                    st.session_state.final_prompt += f" Specific requirements: {refinement_text}"
        
        if st.button("Execute Prompt"):
            st.session_state.current_step = 3
            st.experimental_rerun()