from pathlib import Path

parent_dir = Path(__file__).parent
root_dir = parent_dir.parent
templates_dir = root_dir / 'templates'
google_ai_studio_html_template = templates_dir / 'google-ai-studio-conversation.html'