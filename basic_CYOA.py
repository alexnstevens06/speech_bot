import os

from xai_sdk import Client
from xai_sdk.chat import user, assistant, system

import readchar

import access_config


client = Client(
    api_key=os.getenv(access_config.get_api_env_key()),
    timeout = 3600
)

chat = client.chat.create(model = access_config.get_model_name())

persona_prompt = input("Please input the persona you wish your AI roleplay CYOA partner to take")
system_prompt = ""

key = readchar.readkey()

while(key!="0"):
    for chunk,response in chat.stream():
        pass
    pass
