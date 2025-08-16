import os
import webbrowser
import subprocess
import platform
from document_writer import create_word_file, write_to_file, add_bullet_point, close_file
def open_folder(path):
    system = platform.system()
    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", path])
    else:  # Linux
        subprocess.run(["xdg-open", path])

def handle_command(text):
    text = text.lower()

    # 🌐 Browser commands
    if "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open google" in text:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "search for" in text:
        query = text.split("search for")[-1].strip()
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        return f"Searching Google for {query}."

    elif "open drive" in text:
        webbrowser.open("https://drive.google.com")
        return "Opening Google Drive."

    # 📁 Folder commands
    elif "open downloads" in text:
        open_folder(os.path.expanduser("~/Downloads"))
        return "Opening Downloads folder."

    elif "open desktop" in text:
        open_folder(os.path.expanduser("~/Desktop"))
        return "Opening Desktop folder."

    elif "open documents" in text:
        open_folder(os.path.expanduser("~/Documents"))
        return "Opening Documents folder."

    elif "open demon project" in text:
        demon_path = os.path.expanduser("C:/Users/bajpa/Downloads/demon-assistant-v0.1")
        open_folder(demon_path)
        return "Opening your demon project folder."
        # 📝 Word File Commands
    elif "create a word file called" in text:
        filename = text.split("called")[-1].strip().replace(" ", "_")
        return create_word_file(filename)

    elif "write" in text:
        content = text.split("write", 1)[-1].strip(": ").capitalize()
        return write_to_file(content)

    elif "add a bullet" in text:
        bullet = text.split("add a bullet")[-1].strip(": ").capitalize()
        return add_bullet_point(bullet)

    elif "close the file" in text or "save and close" in text:
        return close_file()


    return None
