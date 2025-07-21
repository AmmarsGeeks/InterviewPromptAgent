# models/prompt_model.py
def get_detail_fields(category):
    fields_map = {
        "Prompt Engineering & Analysis": [
            {"name": "prompt", "label": "Enter the prompt to analyze", "type": "text_area"},
            {"name": "context", "label": "Context (optional)", "type": "text_input"}
        ],
        "Technical Specifications & Architecture": [
            {"name": "project_type", "label": "Project type (e.g., e-commerce, mobile app)", "type": "text_input"},
            {"name": "requirements", "label": "Main requirements", "type": "text_area"},
            {"name": "tech_stack", "label": "Preferred tech stack (optional)", "type": "text_input"}
        ],
        # Add configurations for other categories...
        "Custom Task": [
            {"name": "custom_task", "label": "Describe what you need", "type": "text_area"}
        ]
    }
    return fields_map.get(category, [])