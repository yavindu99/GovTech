from openai import OpenAI
from config.config import config as conf

client = OpenAI(
    organization=f'{conf.config["open-ai"]["org-id"]}',
    project=f'{conf.config["open-ai"]["project-id"]}',
)

resp = client.post('https://api.openai.com/v1/chat/completions',
                   headers={'Authorization': f'Bearer {conf.config["open-ai"]["api-key"]}'},
                   data={'model': 'gpt-3.5-turbo',
                         'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}]})

print(resp.json())
