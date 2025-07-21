# controllers/ai_controller.py
from services.ai_service import AIService

ai_service = AIService()

def handle_prompt_execution(prompt, category):
    if "Prompt Engineering" in category:
        if "analyze" in prompt.lower():
            return ai_service.analyze_prompt(
                st.session_state.details.get('prompt', ''),
                st.session_state.details.get('context', '')
            )
        elif "optimize" in prompt.lower():
            return ai_service.optimize_prompt(
                st.session_state.details.get('prompt', ''),
                "Issues would be identified here",
                "Optimization goal"
            )
    return ai_service.process_prompt(prompt, category)