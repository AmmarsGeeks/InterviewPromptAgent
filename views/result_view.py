# views/result_view.py
import streamlit as st
from controllers.ai_controller import handle_prompt_execution
from services.file_service import save_results

def render_result_display():
    st.title("🚀 Results")
    
    if not st.session_state.final_prompt:
        st.warning("No prompt to execute")
        st.session_state.current_step = 2
        st.experimental_rerun()
    
    # Execute prompt if not already done
    if not st.session_state.ai_response:
        with st.spinner("Processing prompt..."):
            st.session_state.ai_response = handle_prompt_execution(
                st.session_state.final_prompt,
                st.session_state.category
            )
    
    # Display results
    st.subheader("Final Prompt")
    st.code(st.session_state.final_prompt, language="text")
    
    st.subheader("AI Response")
    
    if isinstance(st.session_state.ai_response, dict):
        # For structured responses like analysis
        st.metric("Clarity Score", f"{st.session_state.ai_response['clarity_score']}/10")
        st.metric("Specificity Score", f"{st.session_state.ai_response['specificity_score']}/10")
        st.write("**Suggestions:**")
        for suggestion in st.session_state.ai_response['suggestions']:
            st.write(f"- {suggestion}")
        st.divider()
        st.write("**Detailed Analysis:**")
        st.write(st.session_state.ai_response['analysis'])
    else:
        # For text responses
        st.write(st.session_state.ai_response)
    
    # Save results
    if not st.session_state.filename:
        st.session_state.filename = save_results(
            st.session_state.category,
            st.session_state.final_prompt,
            st.session_state.ai_response
        )
    
    st.success(f"Results saved to: {st.session_state.filename}")
    
    if st.button("Start New Session"):
        # Reset session state
        keys_to_keep = ['current_step']
        for key in list(st.session_state.keys()):
            if key not in keys_to_keep:
                del st.session_state[key]
        st.session_state.current_step = 0
        st.experimental_rerun()