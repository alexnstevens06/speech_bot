# In your terminal, first run:
# pip install xai-sdk

import os
import access_config
from xai_sdk import Client
from xai_sdk.chat import user, system

env_id = access_config.get_api_env_key()
model_name = access_config.get_model_name()
client = Client(
    
    api_key=os.getenv(env_id),
    timeout=3600, # Override default timeout with longer timeout for reasoning models
)

chat = client.chat.create(model=model_name)
chat.append(system("You are Grok, a highly intelligent, helpful AI assistant."))
chat.append(user("What is the meaning of life, the universe, and everything?"))



response = chat.sample()
print(response.content)