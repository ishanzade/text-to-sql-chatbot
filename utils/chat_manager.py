import json
import os

class ChatManager:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def get_history(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def add_to_history(self, message):
        history = self.get_history()
        history.append(message)
        with open(self.file_path, 'w') as f:
            json.dump(history[-20:], f)  
