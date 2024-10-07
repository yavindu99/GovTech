import openai

from config.config import config as conf


class OpenAIClient:

    def __init__(self):
        self.client = openai.OpenAI(
            api_key=f'{conf.config["open-ai"]["api-key"]}',
            organization=f'{conf.config["open-ai"]["org-id"]}',
            project=f'{conf.config["open-ai"]["project-id"]}',
        )

    def ask(self, message):
        stream = self.client.chat.completions.create(
            model="gpt-4",  # Specify the model you want to use (e.g., "gpt-3.5-turbo")
            messages=[{"role": 'user', "content": message}],
            stream=True
        )

        return stream
