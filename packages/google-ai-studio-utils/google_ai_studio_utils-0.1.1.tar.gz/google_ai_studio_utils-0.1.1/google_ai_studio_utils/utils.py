from os import PathLike
from google_ai_studio_utils.config import google_ai_studio_html_template


def parse_csv_to_conversation(file_path: PathLike) -> list[tuple[str, str]]:
    import csv
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        # next(reader)  # Skip the header
        conversation = [(row[0].replace(':', ''), row[1]) for row in reader]
    return conversation

def format_dunder_keys(s: str, **kwargs):
    for k, v in kwargs.items():
        k_ = f'__{k}__'
        s = s.replace(k_, v)
    return s

def conversation_to_html(conversation: list[tuple[str, str]], font: str = 'sans-serif', title: str = 'Google AI Studio Exported Conversation') -> str:
    import markdown
    html_template = google_ai_studio_html_template.read_text()
    

    content = ""
    for role, message in conversation:
        if role == "Model":
            content += f'<div class="model-content">{markdown.markdown(message)}</div><hr>'
        else:
            content += f'<div class="user-content">{message}</div><hr>'

    # return html_template.format(content=content, font=font, title=title)
    return format_dunder_keys(html_template, content=content, font=font, title=title)