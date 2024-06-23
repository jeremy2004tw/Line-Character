import os

MSG_LIMIT = int(os.getenv("MSG_LIMIT", default=10))

memory = os.getenv("MEMORY",default="你是一個年輕女性，熱於助人和幫大家回答問題，喜歡唱歌畫畫聊天和說一些笑話")

class Prompt:
    def __init__(self):
        self.message = [{"role": "system", "content": memory}]

    def add_ai_msg(self, text):
        if len(self.message) >= MSG_LIMIT:
            self.remove_msg()
        self.message.append({"role": "assistant", "content": text})

    def add_user_msg(self, text):
        if len(self.message) >= MSG_LIMIT:
            self.remove_msg()
        self.message.append({"role": "user", "content": text})

    def remove_msg(self):
        self.message.pop(1)

    def generate_prompt(self):
        return self.message
