import requests
import os
from dotenv import load_dotenv


class SendTelegramMessage:
    def __init__(self, message_text, bot_name='crazypythonbot'):
        self.message_text = message_text
        self.bot_name = bot_name

    def credentials(self):
        load_dotenv()
        token = os.environ.get(self.bot_name)
        channel_id = os.environ.get('channel_id')
        return token, channel_id

    def send_message(self):
        url = "https://api.telegram.org/bot"
        token, channel_id = self.credentials()
        url += token
        method = url + "/sendMessage"

        data = {
            "chat_id": channel_id,
            "text": f"Message from local machine\n {self.message_text}"
        }

        r = requests.post(method, data=data)

        if r.status_code != 200:
            raise Exception("post_text error")


if __name__ == '__main__':
    SendTelegramMessage('oop style 222').send_message()
