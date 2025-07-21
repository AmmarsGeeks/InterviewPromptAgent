# controllers/prompt_controller.py
def generate_prompts(category, details):
    prompt_templates = {
        "Prompt Engineering & Analysis": [
            f"Analyze this prompt for effectiveness: {details.get('prompt', '')}",
            f"Optimize this prompt: {details.get('prompt', '')}",
            f"Compare this prompt with alternatives: {details.get('prompt', '')}"
        ],
        "Technical Specifications & Architecture": [
            f"Generate technical spec for {details.get('project_type', '')} with requirements: {details.get('requirements', '')}",
            f"Create system architecture for {details.get('project_type', '')} using {details.get('tech_stack', 'modern technologies')}"
        ],
        # Add templates for other categories...
        "Custom Task": [
            f"Help me with: {details.get('custom_task', '')}",
            f"Provide assistance for: {details.get('custom_task', '')}",
            f"Create solution for: {details.get('custom_task', '')}"
        ]
    }
    return prompt_templates.get(category, [])