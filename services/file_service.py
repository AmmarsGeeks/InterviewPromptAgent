# services/file_service.py
import datetime
import os

OUTPUT_DIR = "outputs"

def save_results(category, prompt, response):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    filename = f"{category.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    with open(filepath, 'w') as f:
        f.write(f"Category: {category}\n")
        f.write(f"Prompt: {prompt}\n")
        f.write("\nResponse:\n")
        
        if isinstance(response, dict):
            for key, value in response.items():
                f.write(f"{key}: {value}\n")
        else:
            f.write(response)
    
    return filepath